import asyncio

from IMPOC.queries import delete_tables, get, create_tables, insert_val, select_val, select_last_val, ret

# delete_tables()
# get()
# create_tables()
# asyncio.run(get())
# asyncio.run(create_tables())
delete_tables()
create_tables()
# insert_val(7560, 13.02)
# select_val()
# data = select_last_val()
# print(data)
# print(type(data))
# print(data[0])
# print(type(data[0]))
# tipaa_dict_data = list(data[0])
# print(type(tipaa_dict_data[1]))
# data2 = [dict(row) for row in data[0]]

# str_1: str = '"impoc": impoc, "hardness": hardness'
# print(str_1)
# print(type(str_1))
# dict_1: dict = {}
# print(type(dict_1))
# dict_1 = str_1
# print(dict_1)
# print(type(dict_1))
# print(type({"title": "Data Scientist", "compensation": 300000}))
print(ret())




l1=[1,2,3,4]
l2=['a','b','c','d']
d1=zip(l1,l2)
print (d1)#Output:<zip object at 0x01149528>
#Converting zip object to dict using dict() contructor.
print (dict(d1))
print (type(dict(d1)))
