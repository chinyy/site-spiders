# coding=utf8

from tables import *
from numpy import *

from stock import get_all_price, STOCK

realtime_quotes = dtype([
    ("name"     , "S16"),
    ("code"     , "S16"),
    ("date"     , "datetime64"),
    ("time"     , "datetime64"),
    ("open_price", float32),
    ("pre_close", float32), 
    ("price", float32),
    ("high_price", float32),
    ("low_price", float32),
    ("bid", float32),
    ("ask", float32),
    ("volume" , uint32),
    ("amount", float64),
    ("a1_v", float32),
    ("a2_v", float32),
    ("a3_v", float32),
    ("a4_v", float32),
    ("a5_v", float32),
    ("a1_p", float32),
    ("a2_p", float32),
    ("a3_p", float32),
    ("a4_p", float32),
    ("a5_p", float32)
])

fileh = open_file("stock.h5", mode = "w")
root = fileh.root
group = fileh.create_group(root, "tushare")

table = fileh.create_table(root.tushare, "realtime_quote", realtime_quotes, "tock data")

event = table.row
records = get_all_price(STOCK)
for record in records:
    for name in realtime_quotes.names:
        event[name]  = record.get(name)
    event.append()
table.flush()

