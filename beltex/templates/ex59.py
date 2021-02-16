# 1. Используя api описание которого тут http://www.nbrb.by/apihelp/exrates
# Сделате django страничку на которой отобразить среднюю цену доллара в белорусских рублях за последние 7 дней.
# Параметры (GET):
#
# startdate** – дата начала запрашиваемого периода
# enddate** – дата окончания запрашиваемого периода
# "Cur_ID":145,"Date":"2021-02-03T00:00:00","Cur_Abbreviation":"USD","Cur_Scale":1,"Cur_Name":"Доллар США","Cur_OfficialRate":2.6293

import requests
import json

response = requests.get(
    'https://www.nbrb.by/api/exrates/rates/dynamics/145?startdate=2021-01-28&enddate=2021-02-03'
)

data = json.loads(response.text)
print(data)
aver = 0
for i in data:
    x = i['Cur_OfficialRate']
    aver = aver + x/7

print(aver)
