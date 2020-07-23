# zip and unpacking tuple

from typing import NamedTuple
class Record(NamedTuple):
    name:str
    value:float

names = ["Keats","Salazar","Sineboi"]
values = [10,13,45]

Zipped_record = zip(names,values)

# records = [Record(name=name,value=value) for (name,value) in Zipped_record]
#or
records = [Record(*record) for record in Zipped_record]

print(list(records))
