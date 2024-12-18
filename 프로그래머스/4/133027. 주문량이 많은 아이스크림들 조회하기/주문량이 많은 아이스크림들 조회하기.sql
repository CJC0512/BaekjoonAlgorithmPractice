-- 코드를 입력하세요
SELECT
    A.FLAVOR
FROM FIRST_HALF AS A
JOIN (
    SELECT
        FLAVOR,
        SUM(TOTAL_ORDER) AS TOTAL
    FROM JULY
    GROUP BY FLAVOR
)
AS B ON A.FLAVOR = B.FLAVOR
ORDER BY (A.TOTAL_ORDER + B.TOTAL) DESC
LIMIT 3;

# SELECT
#     *
#     , SUM(TOTAL_ORDER)
# FROM JULY
# GROUP BY FLAVOR