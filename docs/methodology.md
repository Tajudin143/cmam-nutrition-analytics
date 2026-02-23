# Methodology

**2.1 Data Source Description**

Data Source: CMAM program monitoring data (2019–2023)

Programs Included:

• OTP (Outpatient Therapeutic Program)

• SC (Stabilization Center)

• TSFP (if applicable)

Variables:

• Admissions

• Discharges (Cured, Death, Default, Non-response)

• Caseload

• Reporting rate

• MUAC categories

• Age group

**2.2 Data Cleaning Methodology**

Cleaning Steps:

1. Standardized date formats to YYYY-MM-DD
2. Removed duplicate facility records
3. Handled missing values:
   - Admissions missing → replaced with 0
   - Caseload missing → forward-filled
4. Validated caseload balance equation:
End Caseload =
Opening Caseload + Admissions − Discharges

5. Removed impossible values:
   - Cure rate > 100%
   - Negative admissions
  
**2.3 KPI Selection Based on SPHERE Standards**

Key Performance Indicators:

Cure Rate = Cured / Total Discharges

SPHERE Standard: > 75%

Death Rate = Death / Total Discharges

SPHERE Standard: < 10%

Default Rate = Default / Total Discharges

SPHERE Standard: < 15%

Non-response Rate

Caseload Trend

Admission Trend

Average Length of Stay  

**2.4 Analytical Framework**

Analysis Types:

• Time-series trend analysis

• Cohort proxy analysis using caseload balance

• SPHERE compliance monitoring

• Seasonal trend analysis

• Facility-level performance comparison
