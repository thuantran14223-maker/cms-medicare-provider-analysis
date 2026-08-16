SELECT 
    rndrng_prvdr_state_abrvtn AS state,
    SUM(tot_srvcs) AS total_services,
    ROUND(SUM(tot_mdcr_pymt_amt), 2) AS total_medicare_payments,
    ROUND(
        SUM(tot_mdcr_pymt_amt) / NULLIF(SUM(tot_srvcs), 0),
        2
    ) AS payment_per_service
FROM medicare_provider_clean
WHERE rndrng_prvdr_state_abrvtn NOT IN ('XX', 'ZZ')
GROUP BY rndrng_prvdr_state_abrvtn
ORDER BY total_medicare_payments DESC;