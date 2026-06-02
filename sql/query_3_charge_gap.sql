SELECT 
    rndrng_prvdr_type AS provider_type,
    SUM(tot_sbmtd_chrg) AS total_submitted_charges,
    SUM(tot_mdcr_pymt_amt) AS total_medicare_payments,
    SUM(tot_sbmtd_chrg - tot_mdcr_pymt_amt) AS charge_gap
FROM medicare_provider_clean
GROUP BY rndrng_prvdr_type
ORDER BY charge_gap DESC;