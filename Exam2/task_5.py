# 5. Есть словарь песен группы Depeche Mode violator songsdict = { 'World in
#  My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30,
# 'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68, }
#  Выведите общее время звучания всех песен. Создайте список песен, время звучаниях которых больше 5 минут
#  Создайте новый словарь тех песен, в название которых состоит из одного слова

Depeche_Mode_song = {'World in My Eyes': 4.76,'Sweetest Perfection': 5.43,'Personal Jesus': 4.56,'Halo': 4.30,'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.6,'Policy of Truth': 4.88,'Blue Dress': 4.18,'Clean': 5.68,}

all_time = 0
all_time2 = []
all_time5 = []
dict1 = {}
dict2 = {}
for key, value in Depeche_Mode_song.items():
    all_time2.append(value)
    all_time = sum(all_time2)
    if value > 5:
        all_time5.append(key)
    if ' ' not in key:
        dict1 = {key: value}
        dict2.update(dict1)

print(f'Dремя звучания всех песен: {all_time}')
print(f'Песни больше 5 минут: {all_time5}')
print(f'Песни с названием из одного слова: {dict2}')









