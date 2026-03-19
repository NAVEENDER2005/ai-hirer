package com.aihirer.backend.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import com.aihirer.backend.model.Role;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class SignupRequest {
    private String name;
    private String email;
    private String password;
    private Role role;
    private String experienceLevel;
    private String githubProfile;
    private String linkedinProfile;
    private String interestedRole;
}
