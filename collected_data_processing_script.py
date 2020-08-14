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
        vk = 'Не указано'
        instagram = 'Не указано'

        try:
            social_links = item["socialLinks"]
            for link in social_links:
                if link['type'] == 'vkontakte':
                    vk = link['href']
                    print(vk)
                elif link['type'] == 'instagram':
                    instagram = link['href']
                    print(instagram)

        except KeyError:
            vk = 'Не указано'
            instagram = 'Не указано'

        try:
            metro = item["metro"][0]["name"]
        except IndexError:
            metro = 'Не указано'

        try:
            phone = item["phones"][0]["number"]
        except KeyError:
            phone = 'Нет телефона'

        parsed_data = [title, district_name, address, metro, phone, vk, instagram]
        df.loc[loc_index] = parsed_data
        loc_index += 1

df.to_csv('Лакомка.csv')
