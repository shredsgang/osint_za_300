import json
import os
import pandas as pd


df = pd.read_csv('Лакомка.csv', index_col=False)
files = os.listdir('Data')
loc_index = 0

for district_name in files:

    with open('Data/' + district_name, 'r') as file:
        data = json.load(file)
        data = data["data"]["items"]

    for item in data:

        title = item["title"]
        address = item["address"]
        try:
            metro = item["metro"][0]["name"]
        except IndexError:
            metro = 'Не указано'
        try:
            phone = item["phones"][0]["number"]
        except KeyError:
            phone = 'Нет телефона'

        parsed_data = [title, district_name, address, metro, phone]
        print(parsed_data)
        df.loc[loc_index] = parsed_data
        loc_index += 1

df.to_csv('Лакомка.csv')
