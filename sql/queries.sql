SELECT *
FROM fact_aum
ORDER BY aum DESC
LIMIT 5;

SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

SELECT
year,
SUM(amount) AS total_sip
FROM fact_transactions
WHERE transaction_type='SIP'
GROUP BY year;

SELECT
state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state;

SELECT *
FROM fact_performance
WHERE expense_ratio < 1;

SELECT *
FROM fact_performance
ORDER BY one_year_return DESC
LIMIT 10;

SELECT
category,
AVG(expense_ratio)
FROM fact_performance
GROUP BY category;

SELECT
strftime('%Y-%m', date) AS month,
COUNT(*) AS transactions
FROM fact_transactions
GROUP BY month;

SELECT *
FROM fact_nav
ORDER BY nav DESC
LIMIT 1;

SELECT
category,
COUNT(*) AS fund_count
FROM dim_fund
GROUP BY category;