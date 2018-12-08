-- 1.
select scooter_id, name, founded, model, weight, max_speed, acquired_date, retired
  from scooter
  inner join scooter_type on scooter.scooter_type_id = scooter_type.scooter_type_id
  inner join company on scooter_type.company_id = company.company_id limit 10;
-- 2.
select retired, count(*) from scooter group by retired;
-- 3.
select to_char(acquired_date, 'YYYY-MM'), count(*) from scooter group by to_char(acquired_date, 'YYYY-MM');
-- 4. 
select company_id, count(*) from scooter_type group by company_id;
