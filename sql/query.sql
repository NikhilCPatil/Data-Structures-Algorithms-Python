/*select even ids without duplicates in city*/
select CITY from STATION where MOD(ID,2) = 0 group by CITY;
-- first character having vovels
Select Distinct CITY from STATION where CITY REGEXP '^[aeiou].*';
-- last character having vovels
Select Distinct CITY from STATION where CITY REGEXP '[aeiou]{1}$';

select name from Employee where salary > 2000 and months < 10;