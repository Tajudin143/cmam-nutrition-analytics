# Methodology

## 1. Data Source

Four years of CMAM program monitoring data (2019–2023).

Programs Included:
- OTP (Outpatient Therapeutic Program)
- SC (Stabilization Center)
- TSFP (if applicable)

Variables:
- Admissions
- Discharges (Cured, Death, Default, Non-response)
- Opening caseload
- End-of-month caseload
- Reporting rate

---

## 2. Data Cleaning

Steps performed:

1. Standardized date format (YYYY-MM)
2. Removed duplicate facility-month entries
3. Replaced missing admissions with 0
4. Validated caseload balance:

End Caseload =
Opening Caseload + Admissions − Total Discharges

5. Flagged inconsistencies

---

## 3. KPI Calculation

Cure Rate = Cured / Total Discharges  
Death Rate = Death / Total Discharges  
Default Rate = Default / Total Discharges  

---

## 4. Analytical Methods

- Time-series trend analysis
- Seasonal pattern analysis
- SPHERE compliance tracking
- Caseload surge identification
- Woreda or Facility-level performance comparison

---

## 5. Validation Framework

- No negative admissions
- No cure rate > 100%
- Caseload reconciliation verified
