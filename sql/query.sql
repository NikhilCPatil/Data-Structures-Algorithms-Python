/*select even ids without duplicates in city*/
select CITY from STATION where MOD(ID,2) = 0 group by CITY;
-- first character having vovels
Select Distinct CITY from STATION where CITY REGEXP '^[aeiou].*';
-- last character having vovels
Select Distinct CITY from STATION where CITY REGEXP '[aeiou]{1}$';

select name from Employee where salary > 2000 and months < 10;

-- select trangle or not

SELECT 
CASE 
	WHEN A + B > C AND A+C>B AND B+C>A THEN 
		CASE 
        	WHEN A = B AND B = C THEN 'Equilateral' 
            WHEN A = B OR B = C OR A = C THEN 'Isosceles' 
            WHEN A != B OR B != C OR A != C THEN 'Scalene' 
            END ELSE 'Not A Triangle' END 
FROM TRIANGLES;

-- select Nikhil (E)

select concat(Name,'(',LEFT(Occupation,1),')') from OCCUPATIONS Order by Name;

--
select concat('There are a total of ',COUNT(Occupation),' ',lower(Occupation),'s.') 
as total from OCCUPATIONS group by Occupation order by total;



---select rows as columns

set @r1=0, @r2=0, @r3=0, @r4=0;
select min(Doctor), min(Professor), min(Singer), min(Actor)
from(
  select case when Occupation='Doctor' then (@r1:=@r1+1)
            when Occupation='Professor' then (@r2:=@r2+1)
            when Occupation='Singer' then (@r3:=@r3+1)
            when Occupation='Actor' then (@r4:=@r4+1) end as RowNumber,
    case when Occupation='Doctor' then Name end as Doctor,
    case when Occupation='Professor' then Name end as Professor,
    case when Occupation='Singer' then Name end as Singer,
    case when Occupation='Actor' then Name end as Actor
  from OCCUPATIONS
  order by Name
) Temp
group by RowNumber