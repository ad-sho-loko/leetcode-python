# Write your MySQL query statement below

select
    prn.FirstName,
    prn.LastName,
    addr.City,
    addr.State
from Person prn
    left join Address addr
    on addr.PersonId = prn.PersonId
