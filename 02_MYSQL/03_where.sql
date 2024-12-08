# where, join, subquery : mysql의 중요 3요소

-- WHERE절 : 조건절

-- 1) 비교 연산자와 WHERE절
SELECT menu_name, menu_price, orderable_status
  FROM tbl_menu
 WHERE menu_price = 5000;
 
SELECT menu_name, menu_price, orderable_status # !=, <> : 같지 않은
  FROM tbl_menu
-- WHERE orderable_status != 'Y';
WHERE orderable_status <> 'Y';

-- 대소 비교 연산자
SELECT menu_name, menu_price, orderable_status
FROM tbl_menu
WHERE menu_price <= 20000;

SELECT menu_name, menu_price, orderable_status
FROM tbl_menu
WHERE menu_price > 10000;

SELECT 1 AND 1;
SELECT 1 AND 0, 0 AND 1, 0 AND 0, 0 AND Null; -- 0과 Null중에 0이 우선됨 그보다 1이 우선됨

SELECT 1 And Null, Null AND Null ;


SELECT menu_name, menu_price, category_code
FROM tbl_menu
WHERE menu_price > 10000
  AND menu_price < 20000 ;
  
SELECT menu_name, menu_price, category_code, orderable_status
  FROM tbl_menu
 WHERE orderable_status = 'Y'
   AND category_code = 10;
   
   
-- 3) OR
SELECT 1 OR 0, 0 OR 1, 1 OR 1, 0 OR 0;

SELECT 1 OR Null, 0 OR Null, Null OR Null; -- 더 극단적인 Null을 반환? 또는 1이 될 수 있는 가능성 있는 Null?

SELECT menu_name, menu_price, category_code, orderable_status
  FROM tbl_menu
 WHERE orderable_status = 'Y'
    OR category_code = 6;

SELECT * FROM tbl_menu WHERE orderable_status = 'N'; -- 별은 모든 내용

SELECT menu_name, menu_price, category_code, orderable_status
  FROM tbl_menu
 WHERE menu_price > 15000
    OR category_code = 10;

-- < AND와 OR의 우선순위 > 

SELECT 1 OR 0 AND 0, (1 OR 0) AND 0; -- AND가우선순위가높다. 

SELECT menu_name, menu_price, category_code, orderable_status
  FROM tbl_menu
 WHERE category_code = 4
    OR menu_price = 9000
   AND category_code > 10;
   
-- 4) BETWEEN

SELECT menu_name, menu_price, category_code
  FROM tbl_menu
 WHERE menu_price BETWEEN 10000 AND 20000; #포함임
 
-- NOT : 부정표현, 여집합
SELECT menu_name, menu_price, category_code
  FROM tbl_menu
 WHERE menu_price NOT BETWEEN 10000 AND 20000
   AND category_code < 11;
   
-- 5) LIKE : %를 사용해서 문자가 포함된 것을 찾을 수 있다.
SELECT menu_name, menu_price
  FROM tbl_menu
 WHERE menu_name LIKE '%마늘%' # %마늘은 마늘로 끝나는 애, 마늘%은 마늘로 시작하는 애, 생마늘% %마%늘%은?
ORDER BY menu_name;

-- 메뉴명에 민트를 포함하고, 금액이 10000원 이상이며, category_code가 4인 메뉴의 모든 컬럼 조회
SELECT *
  FROM tbl_menu
 WHERE menu_name LIKE '%민%트%' AND menu_price >= 10000 AND category_code >= 4;
 
-- NOT 

SELECT menu_name, menu_price
  FROM tbl_menu
 WHERE menu_name NOT LIKE '%마늘%' 
ORDER BY menu_name;

-- 6) IN

SELECT menu_name, category_code
  FROM tbl_menu
 WHERE category_code = 4 
    OR category_code = 5  
    OR category_code = 6;
    
-- SELECT menu_name, category_code
--   FROM tbl_menu
--  WHERE category_code IN (4, 5, 6)
-- ORDER BY category_code;

SELECT menu_name, category_code
  FROM tbl_menu
 WHERE category_code NOT IN (4, 5, 6)
ORDER BY category_code;

-- 7) IS NULL

SELECT category_code, category_name, ref_category_code
  FROM tbl_category
 WHERE ref_category_code IS NOT NULL;