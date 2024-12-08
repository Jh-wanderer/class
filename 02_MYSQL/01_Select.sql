# SELECT FROM (둘이 붙어 다님) 컴퓨터는 FROM(테이블명) WHERE(조건식) SELECT(컬럼) 순이다.
-- 단일 열 데이터 검색

SELECT menu_name
  FROM tbl_menu;
  
-- 다중 열 데이터 검색

SELECT menu_code, menu_name, menu_price, orderable_status
  FROM tbl_menu; # Semicolon은 하나의 sql 문임을 나타냄
  
-- 모든 열 데이터 검색 (Schemas에서 해당 테이블에 있는 모든 column을 넣어주면 된다.)

SELECT*FROM tbl_menu; # 별표는 테이블에 있는 모든 컬럼 조회 시. 실무에서는 테이블 구조가 바뀌기도 하기 때문에 지양.alter

# 연산자 

SELECT 6 + 3; #FROM DUAL;(ORACLE 사용시) MYSQL은 FROM 없이 사용 가능
SELECT 6 - 3;
SELECT 6 * 3;
SELECT 6 / 3;
SELECT 6 % 3;

# 내장함수 
SELECT NOW(); # 현 시간
SELECT CONCAT('홍','','길동'); #문자열 합치기

# 컬럼 별칭
SELECT CONCAT('호','-','랑이') AS NAME;
SELECT CONCAT('다','-','람쥐') AS 'Character name'; # 별칭으로 인지 못할 때 - 띄어쓰기 혹은 특수문자가 있는 경우 ''으로 감싸줘야 한다. 혹은 _으로 연결
