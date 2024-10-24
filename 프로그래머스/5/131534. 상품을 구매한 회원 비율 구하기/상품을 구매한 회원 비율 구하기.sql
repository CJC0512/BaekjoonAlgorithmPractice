-- 코드를 입력하세요
# SELECT
#     *
# FROM USER_INFO
# WHERE YEAR(JOINED) = 2021


# SELECT
#    COUNT(*) AS '2021년에 가입하여 상품을 구매한 회원수'
# FROM USER_INFO AS A
# JOIN ONLINE_SALE AS B ON A.USER_ID = B.USER_ID
# WHERE YEAR(A.JOINED) = 2021

# SELECT
#    COUNT(*) AS '2021년에 가입한 회원수'
# FROM USER_INFO AS A
# WHERE YEAR(A.JOINED) = 2021

# 2021년에 가입한 회원들
# SELECT
#   A.USER_ID,
#   (
#       SELECT
#            COUNT(*) AS '2021년에 가입하여 상품을 구매한 회원수'
#         FROM USER_INFO AS A
#         JOIN ONLINE_SALE AS B ON A.USER_ID = B.USER_ID
#        WHERE YEAR(A.JOINED) = 2021
#  ) AS PURCHASED_USERS,
#  (
#      SELECT
#        COUNT(*) AS '2021년에 가입한 회원수'
#     FROM USER_INFO AS A
#     WHERE YEAR(A.JOINED) = 2021
#  )
 
# FROM USER_INFO AS A
# WHERE YEAR(A.JOINED) = 2021

# 상품을 구매한 회원수
# SELECT
#     COUNT(*) AS '상품을 구매한 회원수'
# FROM ONLINE_SALE 
# GROUP BY USER_ID

# SELECT
#     *
# FROM ONLINE_SALE AS A
# JOIN USER_INFO AS B ON A.USER_ID = B.USER_ID


# SELECT
#     *
# FROM ONLINE_SALE AS A
# JOIN USER_INFO AS B ON A.USER_ID = B.USER_ID

# SELECT
#     YEAR(A.SALES_DATE) AS YEAR
#     , MONTH(A.SALES_DATE) AS MONTH
#     , COUNT(A.USER_ID) AS PURCHASED_USERS
#     , ROUND(
#         COUNT(A.USER_ID) / 
#         (
#             SELECT
#                 COUNT(*)
#             FROM USER_INFO
#             WHERE YEAR(JOINED) = 2021) 
#         , 1)
#     AS PUCHASED_RATIO
# FROM ONLINE_SALE AS A
# JOIN USER_INFO AS B 
#   ON A.USER_ID = B.USER_ID
# WHERE YEAR(B.JOINED) = 2021
# GROUP BY YEAR(A.SALES_DATE), MONTH(A.SALES_DATE)
# ORDER BY YEAR ASC, MONTH ASC

# 가입 일자 상관없이 년, 월 별로 구매한 회원 수
SELECT
    YEAR(A.SALES_DATE) AS YEAR
    , MONTH(A.SALES_DATE) AS MONTH
    , COUNT(DISTINCT A.USER_ID) AS PURCHASED_USERS
    , ROUND(
        COUNT(DISTINCT A.USER_ID)/
        
         (SELECT
            COUNT(*)
            FROM USER_INFO
          WHERE YEAR(JOINED) = 2021)
        , 1) AS PUCHASED_RATIO
FROM ONLINE_SALE AS A
JOIN USER_INFO AS B ON A.USER_ID = B.USER_ID
WHERE YEAR(B.JOINED) = 2021
GROUP BY YEAR, MONTH
ORDER BY YEAR ASC, MONTH ASC

# SELECT
#     COUNT(*)
# FROM USER_INFO
# WHERE YEAR(JOINED) = 2021

