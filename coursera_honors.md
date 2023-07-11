# Honors Peer-graded Assignment: Advanced SQL for Data Engineers
## Exercise 1, Question 1
Write and execute a SQL query to list the school names, community names, and average attendance for communities with a hardship index of 98
```SQL
SELECT CHICAGO_PUBLIC_SCHOOLS.NAME_OF_SCHOOL, CENSUS_DATA.COMMUNITY_AREA_NAME, CHICAGO_PUBLIC_SCHOOLS.AVERAGE_STUDENT_ATTENDANCE, CENSUS_DATA.HARDSHIP_INDEX 
FROM CENSUS_DATA
INNER JOIN CHICAGO_PUBLIC_SCHOOLS 
ON CHICAGO_PUBLIC_SCHOOLS.COMMUNITY_AREA_NUMBER = CENSUS_DATA.COMMUNITY_AREA_NUMBER
WHERE CENSUS_DATA.HARDSHIP_INDEX == 98;
```
### Output
| NAME_OF_SCHOOL                                        | COMMUNITY_AREA_NAME | AVERAGE_STUDENT_ATTENDANCE | HARDSHIP_INDEX |
|-------------------------------------------------------|---------------------|----------------------------|----------------|
| George Washington Carver Military Academy High School | Riverdale           | 91.60%                     | 98             |
| George Washington Carver Primary School               | Riverdale           | 90.90%                     | 98             |
| Ira F Aldridge Elementary School                      | Riverdale           | 92.90%                     | 98             |
| William E B Dubois Elementary School                  | Riverdale           | 93.30%                     | 98             |
## Exercise 1, Question 2
Write and execute a SQL query to list all crimes that took place at a school. Include case number, crime type, and community name.
```SQL
SELECT CHICAGO_CRIME_DATA.CASE_NUMBER, CHICAGO_CRIME_DATA.PRIMARY_TYPE, CHICAGO_CRIME_DATA.DESCRIPTION, 
	   CHICAGO_CRIME_DATA.LOCATION_DESCRIPTION, CENSUS_DATA.COMMUNITY_AREA_NAME 
FROM CHICAGO_CRIME_DATA
INNER JOIN CENSUS_DATA 
ON CENSUS_DATA.COMMUNITY_AREA_NUMBER = CHICAGO_CRIME_DATA.COMMUNITY_AREA_NUMBER
WHERE CHICAGO_CRIME_DATA.LOCATION_DESCRIPTION LIKE '%SCHOOL%'
```
### Output 
| CASE_NUMBER | PRIMARY_TYPE      | DESCRIPTION                    | LOCATION_DESCRIPTION   | COMMUNITY_AREA_NAME |
|-------------|-------------------|--------------------------------|------------------------|---------------------|
| HL353697    | BATTERY           | SIMPLE                         | SCHOOL PUBLIC GROUNDS  | South Shore         |
| HL725506    | BATTERY           | PRO EMP HANDS NO/MIN INJURY    | SCHOOL PUBLIC BUILDING | Lincoln Square      |
| HP716225    | BATTERY           | SIMPLE                         | SCHOOL PUBLIC BUILDING | Douglas             |
| HH639427    | BATTERY           | SIMPLE                         | SCHOOL PUBLIC BUILDING | Austin              |
| JA460432    | BATTERY           | SIMPLE                         | SCHOOL PUBLIC GROUNDS  | Ashburn             |
| HS200939    | CRIMINAL DAMAGE   | TO VEHICLE                     | SCHOOL PUBLIC GROUNDS  | Austin              |
| HK577020    | NARCOTICS         | POSS: HEROIN(WHITE)            | SCHOOL PUBLIC GROUNDS  | Rogers Park         |
| HS305355    | NARCOTICS         | MANU/DEL:CANNABIS 10GM OR LESS | SCHOOL PUBLIC BUILDING | Brighton Park       |
| HT315369    | ASSAULT           | PRO EMP HANDS NO/MIN INJURY    | SCHOOL PUBLIC GROUNDS  | East Garfield Park  |
| HR585012    | CRIMINAL TRESPASS | TO LAND                        | SCHOOL PUBLIC GROUNDS  | Ashburn             |
## Exercise 2, Question 1
Write and execute a SQL statement that returns just the school name and leaders' icon from the view
```SQL
CREATE VIEW School_Icon
AS
	SELECT
		NAME_OF_SCHOOL AS "Name",
		Leaders_Icon AS "Icon"
		FROM CHICAGO_PUBLIC_SCHOOLS;

SELECT * FROM School_Icon;
```
### Output
| Name                                                              | Icon |
|-------------------------------------------------------------------|------|
| Abraham Lincoln Elementary School                                 | Weak |
| Adam Clayton Powell Paideia Community Academy Elementary School   | Weak |
| Adlai E Stevenson Elementary School                               | Weak |
| Agustin Lara Elementary Academy                                   | Weak |
| Air Force Academy High School                                     | Weak |
| Albany Park Multicultural Academy                                 | Weak |
| Albert G Lane Technical High School                               | Weak |
| Albert R Sabin Elementary Magnet School                           | Weak |
| Alcott High School for the Humanities                             | Weak |
| Alessandro Volta Elementary School                                | Weak |
| Alexander Graham Bell Elementary School                           | Weak |
| Alexander Graham Elementary School                                | Weak |
.....
## Exercise 3, Question 1:
Write the structure of a query to create or replace a stored procedure called `UPDATE_LEADERS_SCORE` that takes a `in_School_ID` parameter as an integer and a `in_Leader_Score` parameter as an integer. Don't forget to use the `#SET TERMINATOR` statement to use the `@` for the `CREATE` statement terminator
```SQL
--#SET TERMINATOR @
CREATE PROCEDURE UPDATE_LEADERS_SCORE (
    IN in_School_ID INTEGER, 
    IN in_Leader_Score INTEGER
    )
  
LANGUAGE SQL
MODIFIES SQL DATA

BEGIN

END 
@
```
## Exercise 3, Question 2:
Inside your stored procedure, write a SQL statement to update the `Leaders_Score` in `CHICAGO_PUBLIC_SCHOOLS` table for the school indentified by `in_School_ID` to the value in the `in_Leader_Score` parameter.
- Reference: SQL Cheat Sheet: Views, Stored Procedures and Transactions
```SQL
--#SET TERMINATOR @
CREATE PROCEDURE UPDATE_LEADERS_SCORE (
    IN in_School_ID INTEGER, 
    IN in_Leader_Score INTEGER
    )
  
LANGUAGE SQL
MODIFIES SQL DATA

BEGIN
	UPDATE DVY37834.CHICAGO_PUBLIC_SCHOOLS
	SET LEADERS_SCORE = in_Leader_Score
	WHERE SCHOOL_ID = in_School_ID;
END 
@
```
## Exercise 3, Question 3:
Inside your stored procedure, write a SQL `IF` statement to update the `Leaders_Icon` field in the `CHICAGO_PUBLIC_SCHOOLS` table for the school identified by `in_School_ID` using the following information.
| Score lower limit | Score upper limit | Icon |
| --- | --- | --- |
| 80 | 99 | Very strong |
| 60 | 79 | Strong |
| 40 | 59 | Average |
| 20 | 39 | Weak |
| 0 | 19 | Very weak |

- Note: Since `REORG TABLE` is a DB2 command line, there fore `CALL SYSPROC.ADMIN_CMD()` has to be used.
- Reference: https://www.ibm.com/docs/en/db2/11.5?topic=commands-reorg-table-command-using-admin-cmd

```SQL
--#SET TERMINATOR @
CREATE PROCEDURE UPDATE_LEADERS_SCORE (
    IN in_School_ID INTEGER, 
    IN in_Leader_Score INTEGER
    )
  
LANGUAGE SQL
MODIFIES SQL DATA

BEGIN
	CALL SYSPROC.ADMIN_CMD('REORG TABLE CHICAGO_PUBLIC_SCHOOLS');
		IF in_Leader_Score BETWEEN 80 AND 99 THEN
			UPDATE DVY37834.CHICAGO_PUBLIC_SCHOOLS 
			SET LEADERS_SCORE = in_Leader_Score, LEADERS_ICON = 'Very Strong'
			WHERE SCHOOL_ID = in_School_ID;
		ELSEIF in_Leader_Score BETWEEN 60 AND 79 THEN
			UPDATE DVY37834.CHICAGO_PUBLIC_SCHOOLS 
			SET LEADERS_SCORE = in_Leader_Score, LEADERS_ICON = 'Strong'
			WHERE SCHOOL_ID = in_School_ID;
		ELSEIF in_Leader_Score BETWEEN 40 AND 59 THEN
			UPDATE DVY37834.CHICAGO_PUBLIC_SCHOOLS 
			SET LEADERS_SCORE = in_Leader_Score, LEADERS_ICON = 'Average'
			WHERE SCHOOL_ID = in_School_ID;		
		ELSEIF in_Leader_Score BETWEEN 20 AND 39 THEN
			UPDATE DVY37834.CHICAGO_PUBLIC_SCHOOLS 
			SET LEADERS_SCORE = in_Leader_Score, LEADERS_ICON = 'Weak'
			WHERE SCHOOL_ID = in_School_ID;	
		ELSE
			UPDATE DVY37834.CHICAGO_PUBLIC_SCHOOLS 
			SET LEADERS_SCORE = in_Leader_Score, LEADERS_ICON = 'Very Weak'
			WHERE SCHOOL_ID = in_School_ID;	
		END IF;
END
@
```

### Rollback and Commits within SQL Stored Procedure
```SQL
--#SET TERMINATOR @
CREATE PROCEDURE UPDATE_LEADERS_SCORE (
    IN in_School_ID INTEGER, 
    IN in_Leader_Score INTEGER
    )
  
LANGUAGE SQL
MODIFIES SQL DATA

BEGIN
	CALL SYSPROC.ADMIN_CMD('REORG TABLE CHICAGO_PUBLIC_SCHOOLS');
		IF in_Leader_Score BETWEEN 80 AND 99 THEN
			UPDATE DVY37834.CHICAGO_PUBLIC_SCHOOLS 
			SET LEADERS_SCORE = in_Leader_Score, LEADERS_ICON = 'Very Strong'
			WHERE SCHOOL_ID = in_School_ID;
		ELSEIF in_Leader_Score BETWEEN 60 AND 79 THEN
			UPDATE DVY37834.CHICAGO_PUBLIC_SCHOOLS 
			SET LEADERS_SCORE = in_Leader_Score, LEADERS_ICON = 'Strong'
			WHERE SCHOOL_ID = in_School_ID;
		ELSEIF in_Leader_Score BETWEEN 40 AND 59 THEN
			UPDATE DVY37834.CHICAGO_PUBLIC_SCHOOLS 
			SET LEADERS_SCORE = in_Leader_Score, LEADERS_ICON = 'Average'
			WHERE SCHOOL_ID = in_School_ID;		
		ELSEIF in_Leader_Score BETWEEN 20 AND 39 THEN
			UPDATE DVY37834.CHICAGO_PUBLIC_SCHOOLS 
			SET LEADERS_SCORE = in_Leader_Score, LEADERS_ICON = 'Weak'
			WHERE SCHOOL_ID = in_School_ID;	
		ELSEIF in_Leader_Score BETWEEN 0 AND 19 THEN
			UPDATE DVY37834.CHICAGO_PUBLIC_SCHOOLS 
			SET LEADERS_SCORE = in_Leader_Score, LEADERS_ICON = 'Very Weak'
			WHERE SCHOOL_ID = in_School_ID;	
		ELSEIF in_Leader_Score < 0 THEN
			ROLLBACK WORK;
		ELSE 
			COMMIT WORK;
		END IF;
END
@
```
