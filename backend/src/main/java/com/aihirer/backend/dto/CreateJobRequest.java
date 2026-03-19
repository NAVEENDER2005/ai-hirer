package com.aihirer.backend.dto;

import lombok.Data;
import java.util.List;
import java.util.Map;

/**
 * DTO for the job creation form submitted from the HR dashboard.
 * Only requires the fields the HR user fills in.
 * All AI pipeline fields (cutoffs, skills, weightage) default to
 * sensible values that can be updated later.
 */
@Data
public class CreateJobRequest {
    private String title;
    private String department;
    private String location;
    private String description;

    // Optional extended fields — HR can supply them; defaults applied in controller
    // if absent
    private List<String> requiredSkills;
    private Map<String, Double> skillWeightage;
    private Double cutoffRound1;
    private Double cutoffRound2;
    private Double cutoffRound3;
    private Double cutoffRound4;
    private Double cutoffRound5;
    private Integer maxAttempts;
}
