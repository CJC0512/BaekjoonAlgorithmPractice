-- 코드를 작성해주세요
SELECT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
    FROM DEVELOPERS D
JOIN SKILLCODES S ON (D.SKILL_CODE & S.CODE) = S.CODE
WHERE S.CATEGORY = 'Front End'
GROUP BY D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
ORDER BY D.ID ASC;
