-- Question 1
CREATE VIEW q1table AS
    SELECT
        adwords.spend,
        adwords_conversions.conversions,
        adwords.spend/adwords_conversions.conversion AS "cost per conversion"
    FROM adwords
    INNER JOIN adwords_conversions ON adwords.account = adwords_conversions.account
    WHERE conversion_type_name = "Ticket Purchase"
      AND adwords.account = "Account X"
    ORDER BY adwords.date;


-- Question 2
SELECT
    bing.spend as "bing_spend",
    bing.impressions as "bing_impressions",
    bing.conversions,
    bing.spend/bing.conversions as "bing_cost_per_converion"
FROM bing
INNER JOIN q1table ON q1table.account = bing.account
GROUP BY bing.date;