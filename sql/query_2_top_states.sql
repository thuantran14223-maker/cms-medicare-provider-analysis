SELECT 
    rndrng_prvdr_state_abrvtn AS state,
    SUM(tot_srvcs) AS total_services,
    SUM(tot_mdcr_pymt_amt) AS total_medicare_payments
FROM medicare_provider_clean
WHERE rndrng_prvdr_state_abrvtn NOT IN ('XX', 'ZZ')
GROUP BY rndrng_prvdr_state_abrvtn
ORDER BY total_medicare_payments DESC;