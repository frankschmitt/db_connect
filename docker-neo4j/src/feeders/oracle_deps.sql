select distinct d.owner as "source", d.referenced_owner as "target", 'db' as "type"
from dba_dependencies d
join dba_users o
  on o.username = d.owner
join dba_users r
  on r.username = d.referenced_owner
where 1=1
  and d.owner != d.referenced_owner -- ignore self-references
  and o.oracle_maintained = 'N' -- ignore Oracle-internal referencing schemata
  and r.oracle_maintained = 'N' -- ignore Oracle-internal referenced schemata
  -- and d.owner not in ( <schemas_to_exclude>)
order by d.owner, d.referenced_owner
;

 
