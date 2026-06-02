SELECT 
    rndrng_prvdr_type AS provider_type,
    SUM(tot_srvcs) AS total_services,
    SUM(tot_mdcr_pymt_amt) AS total_medicare_payments
FROM medicare_provider_clean
GROUP BY rndrng_prvdr_type
ORDER BY total_medicare_payments DESC
LIMIT 15;