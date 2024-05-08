'''
    課題3: アンケート集計のプログラム
    日にち: 2024-05-08
    学籍番号: 50111012
    名前: 大芝 峻平
    どんな処理か: 
'''

import pandas as pd
import numpy as np

# データの読み込みと使用する部分の切り出し
def read_survey_data():
    df = pd.read_csv('./ank_data.csv')
    df = df.iloc[1:, 1:4]
    # データの振り分け
    q1_data = df['進み具合はどうですか？'].to_numpy()
    q2_data = df['難易度はどうですか？'].to_numpy()
    q3_data = df['この授業に対する期待は？'].to_numpy()

    return q1_data, q2_data, q3_data

def check_survey_data(dictionary, data):
    # 出現回数をカウントする辞書配列
    result_dict = {}

    # dictionaryに含まれる各価に対して，data配列内の出現回数をカウント
    for key in dictionary:
        result_dict[key] = np.count_nonzero(data == key)

    return result_dict

# データの読み込み
q1, q2, q3 = read_survey_data()

# 結果の取得
survey_dict_q1 = [1, 2, 3, 4, 5]
survey_dict_q2 = [1, 2, 3, 4, 5]
survey_dict_q3 = [1, 2, 3, 4, 5, 6, 7]

result_q1 = check_survey_data(survey_dict_q1, q1)
