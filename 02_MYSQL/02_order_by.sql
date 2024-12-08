# ORDER BY

-- 결과 집합을 하나의 열 기준으로 정렬
SELECT menu_code, menu_name, menu_price
  FROM tbl_menu
ORDER BY menu_price DESC; # DESC 붙이면 역순이 된다. ASC는 생략가능하며, 오름차순이다. 기원은 descending, ascending

SELECT menu_code, menu_name, menu_price
  FROM tbl_menu
ORDER BY menu_price DESC, menu_name ASC; # 우선 기준을 순서대로 적용, 결과 집합을 여러 개의 열로 정렬

SELECT menu_code, menu_name, menu_price, menu_code*menu_price
 FROM tbl_menu
ORDER BY menu_code*menu_price DESC;    # ORDER BY의 기준이 column name에 없더라도, 적용 가능함.

SELECT menu_code, menu_name, menu_price, menu_code * menu_price AS '연산결과' # 내가 별칭을 제어 가능함
  FROM tbl_menu
ORDER BY 연산결과 DESC;

# 사용자 지정 목록을 사용하여 정렬

SELECT FIELD('c','A','B','C','C'); # c를 그 이후 목록에서 첫번째 위치를 찾

SELECT FIELD(orderable_status,'N','Y')
  FROM tbl_menu;
  
SELECT menu_name, orderable_status, FIELD(orderable_status,'N','Y') # status에 대해 넘버링이 가능하다.
  FROM tbl_menu;
  
SELECT menu_name, orderable_status
  FROM tbl_menu
ORDER BY FIELD(orderable_status, 'N', 'Y') ;

# Null이 있는 경우
-- 오름차순(ASC) 정렬 시 Null이 맨 처음 (default)
SELECT category_code, category_name, ref_category_code
  FROM tbl_category
ORDER BY ref_category_code;

SELECT category_code, category_name, ref_category_code
  FROM tbl_category
ORDER BY ref_category_code IS NULL; # null이 맨 위에 오는 것을 방지, 다 뒤로 보내줌, is null (asc) - null 우선 기준

SELECT category_code, category_name, ref_category_code
  FROM tbl_category
ORDER BY ref_category_code IS NULL DESC, ref_category_code DESC; # 직접 따로 빼서 배정해 줘야지 안 그러면 중복 명령 오류 생기는 듯

