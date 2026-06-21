-- Q1 Price distribution

SELECT [Day-ahead Price (EUR/MWh)]
FROM electricity;

-- Q2 Average price by year

SELECT
    year,
    AVG([Day-ahead Price (EUR/MWh)]) AS avg_price
FROM electricity
GROUP BY year
ORDER BY year;

-- Q3 Demand vs price

SELECT 
    [Day-ahead Total Load Forecast (MW)_load],
    [Day-ahead Price (EUR/MWh)]
FROM electricity;

-- Q4 Residual demand

SELECT 
CASE 
    WHEN ([Day-ahead Total Load Forecast (MW)_load] - 
        ([Day-ahead (MW)_wind_offshore] + [Day-ahead (MW)_wind_onshore] + [Day-ahead (MW)_solar])) < 40000 THEN "LOW"
    WHEN ([Day-ahead Total Load Forecast (MW)_load] - 
        ([Day-ahead (MW)_wind_offshore] + [Day-ahead (MW)_wind_onshore] + [Day-ahead (MW)_solar])) < 60000 THEN "MEDIUM"
    ELSE "HIGH"
END AS demand_bucket,
AVG([Day-ahead Price (EUR/MWh)]) AS avg_price
FROM electricity
GROUP BY demand_bucket
ORDER BY avg_price;

-- Q5 Solar impact 

SELECT 
    hour,
    AVG([Day-ahead Price (EUR/MWh)]) AS hourly_price
FROM electricity
GROUP BY hour
ORDER BY hour;

-- Q6 Solar generations

SELECT 
    hour,
    AVG([Day-ahead (MW)_solar]) AS solar_avg_gen
FROM electricity
GROUP BY hour
ORDER BY hour;


-- Q7 Negative prices by year

SELECT 
    year,
    COUNT(*) AS negative_hours
FROM electricity
WHERE [Day-ahead Price (EUR/MWh)] < 0
GROUP BY year
ORDER BY year; 

-- Q8.1 Extreme price events

-- Top 1% price range

SELECT 
    [Day-ahead Price (EUR/MWh)]
FROM electricity
ORDER BY [Day-ahead Price (EUR/MWh)] DESC
LIMIT (
    SELECT CAST(COUNT(*) * 0.01 AS INTEGER)
    FROM electricity
);

SELECT 
    year,
    COUNT(*) AS extreme_hours,
    ROUND(
        100 * COUNT(*) / SUM(COUNT(*)) OVER (), 2
    ) AS pct_of_all_extrem_hours
FROM electricity
WHERE [Day-ahead Price (EUR/MWh)] > 490
GROUP BY year
ORDER BY year;

-- Q8.2 Top 20 price spikes

SELECT 
    [Day-ahead Total Load Forecast (MW)_load],
    [Day-ahead (MW)_wind_onshore], 
    [Day-ahead (MW)_solar],
    [Day-ahead Price (EUR/MWh)]
FROM electricity
ORDER BY [Day-ahead Price (EUR/MWh)] DESC
LIMIT 20;

-- Q8.3 Extreme events by hour of the day

SELECT 
    hour,
    COUNT(*) AS extrem_by_hour,
    ROUND(
        100 * COUNT(*) / SUM(COUNT(*)) OVER (), 2
    ) AS pct_of_all_extrem_by_hour
FROM electricity
WHERE [Day-ahead Price (EUR/MWh)] > 490
GROUP BY hour
ORDER BY hour;

-- Q8.4 Extreme events by month

SELECT 
    month,
    COUNT(*) AS count_extrem_month,
    ROUND(
        100 * COUNT(*) / SUM(COUNT(*)) OVER (), 2
    ) AS pct_of_all_extrem_by_month
FROM electricity
WHERE [Day-ahead Price (EUR/MWh)] > 490
GROUP BY month
ORDER BY month;

-- Q8.5 System conditions during extreme events

SELECT 
    AVG([Day-ahead Total Load Forecast (MW)_load]) AS avg_load,
    AVG([Day-ahead (MW)_wind_offshore]) AS avg_wind_offshore,
    AVG([Day-ahead (MW)_wind_onshore]) AS avg_wind_onshore,
    AVG([Day-ahead (MW)_solar]) AS avg_solar,
    AVG([Day-ahead Price (EUR/MWh)]) AS avg_price
FROM electricity
WHERE [Day-ahead Price (EUR/MWh)] > 490;

SELECT 
    AVG([Day-ahead Total Load Forecast (MW)_load]) AS avg_load,
    AVG([Day-ahead (MW)_wind_offshore]) AS avg_wind_offshore,
    AVG([Day-ahead (MW)_wind_onshore]) AS avg_wind_onshore,
    AVG([Day-ahead (MW)_solar]) AS avg_solar,
    AVG([Day-ahead Price (EUR/MWh)]) AS avg_price
FROM electricity;
    