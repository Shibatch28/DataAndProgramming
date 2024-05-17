'''
    課題2: データを扱うプログラム
    日にち: 2024/05/01
    学籍番号: 50111012
    名前: 大芝 峻平
    処理の説明: 各区ごとの人口を取得し, 辞書型配列に格納してそれを表示するプログラム
'''
import csv
import matplotlib.pyplot as plt

# CSVのデータをコラムごとに分ける函数
def split_data_for_column(source):
    prefecture_code = []
    prefecture_name = []
    city_name = []
    area_cd = []
    area_name = []
    ooaza_cd = []
    ooaza = []
    population = []
    number_of_men = []
    number_of_women = []
    for i in range(1, len(source)):
        prefecture_code.append(source[i][1])
        prefecture_name.append(source[i][2])
        city_name.append(source[i][3])
        area_cd.append(source[i][5])
        area_name.append(source[i][6])
        ooaza_cd.append(source[i][8])
        ooaza.append(source[i][9])
        population.append(source[i][11])
        number_of_men.append(source[i][12])
        number_of_women.append(source[i][13])
    return prefecture_code, prefecture_name, city_name, area_cd, area_name, ooaza_cd, ooaza, population, number_of_men, number_of_women

# 重複なく区の名前を取得する
def get_areas(area_name):
    areas = [area_name[0]]
    for i in range(1, len(area_name)):
        is_overlap = 0
        for j in range(len(areas)):
            if areas[j] == area_name[i]:
                is_overlap = 1;
                break;
        if is_overlap == 0:
            areas.append(area_name[i])
    return areas

# 区ごとの人口を取得する
def get_populations(areas, area_name, population, number_of_men, number_of_women):
    pop_s = [0 for i in range(len(areas))]
    pop_m = [0 for i in range(len(areas))]
    pop_w = [0 for i in range(len(areas))]
    for i in range(len(area_name)):
        for j in range(len(areas)):
            if area_name[i] == areas[j]:
                pop_s[j] += int(population[i])
                pop_m[j] += int(number_of_men[i])
                pop_w[j] += int(number_of_women[i])
    comp_population_s = dict(zip(areas, pop_s))
    comp_popiuation_m = dict(zip(areas, pop_m))
    comp_population_w = dict(zip(areas, pop_w))
    return comp_population_s, comp_popiuation_m, comp_population_w

with open('./221309_town_age_population.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    town_age_population_data = [row for row in reader]

_, pnames, cnames, _, anames, _, ooaza, pops, popm, popw = split_data_for_column(town_age_population_data)
areas = get_areas(anames)
a_pop_s, a_pop_m, a_pop_w = get_populations(areas, anames, pops, popm, popw)

print('区ごとの合計人口: ', a_pop_s)
print('区ごとの男性人口: ', a_pop_m)
print('区ごとの女性人口: ', a_pop_w)
