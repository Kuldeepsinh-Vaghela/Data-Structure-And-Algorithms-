# Write your MySQL query statement below
select a1.machine_id, Round(((sum(a2.timestamp) - sum(a1.timestamp)) / count(a1.process_id)),3) as processing_time
from activity a1 inner join activity a2 
where a1.activity_type = 'start' 
    and a2.activity_type = 'end' 
    and a1.machine_id = a2.machine_id 
    and a1.process_id = a2.process_id
group by a1.machine_id

