select a.animal_id, a.name
from animal_outs as a
left outer join animal_ins as b on a.animal_id=b.animal_id
where b.animal_id is null;