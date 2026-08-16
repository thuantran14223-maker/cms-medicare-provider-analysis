SELECT 
    rndrng_prvdr_type AS provider_type,
    ROUND(SUM(tot_sbmtd_chrg), 2) AS total_submitted_charges,
    ROUND(SUM(tot_mdcr_pymt_amt), 2) AS total_medicare_payments,
    ROUND(
        SUM(tot_sbmtd_chrg) - SUM(tot_mdcr_pymt_amt),
        2
    ) AS charge_gap,
    ROUND(
        100.0 * SUM(tot_mdcr_pymt_amt) /
        NULLIF(SUM(tot_sbmtd_chrg), 0),
        2
    ) AS payment_to_charge_pct
FROM medicare_provider_clean
GROUP BY rndrng_prvdr_type
ORDER BY charge_gap DESC;