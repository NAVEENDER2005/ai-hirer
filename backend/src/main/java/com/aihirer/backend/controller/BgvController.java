package com.aihirer.backend.controller;

import com.aihirer.backend.model.*;
import com.aihirer.backend.security.UserDetailsImpl;
import com.aihirer.backend.service.BgvService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.util.*;

@RestController
@RequestMapping("/api/bgv")
public class BgvController {

    @Autowired
    private BgvService bgvService;

    private UUID getCurrentUserId() {
        UserDetailsImpl userDetails = (UserDetailsImpl) SecurityContextHolder.getContext().getAuthentication()
                .getPrincipal();
        return userDetails.getId();
    }

    @PostMapping("/upload")
    @PreAuthorize("hasRole('CANDIDATE')")
    public ResponseEntity<CandidateDocument> uploadDocument(
            @RequestParam("type") DocumentType type,
            @RequestParam("file") MultipartFile file) throws IOException {
        return ResponseEntity.ok(bgvService.uploadDocument(getCurrentUserId(), type, file));
    }

    @GetMapping("/my-documents")
    @PreAuthorize("hasRole('CANDIDATE')")
    public ResponseEntity<List<CandidateDocument>> getMyDocuments() {
        return ResponseEntity.ok(bgvService.getCandidateDocuments(getCurrentUserId()));
    }

    @PostMapping("/send-documents")
    @PreAuthorize("hasRole('HR')")
    public ResponseEntity<Map<String, Object>> sendDocuments(@RequestParam("applicationId") UUID applicationId)
            throws IOException {
        return ResponseEntity.ok(bgvService.sendToThirdParty(applicationId));
    }

    @PostMapping("/update-status")
    @PreAuthorize("hasRole('HR')") // In reality, this might be a webhook from Third Party
    public ResponseEntity<Map<String, Object>> updateStatus(
            @RequestParam("applicationId") UUID applicationId,
            @RequestParam("status") BgvStatus status) {
        return ResponseEntity.ok(bgvService.updateBgvStatus(applicationId, status));
    }
}
