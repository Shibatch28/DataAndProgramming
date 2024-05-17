'''
    課題4: アンケート集計のプログラム2
    日にち: 2024-05-15
    学籍番号: 50111012
    名前: 大芝 峻平
    どんな処理か: アンケートの集計結果のグラフ化
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    result_dict = []

    # dictionaryに含まれる各価に対して，data配列内の出現回数をカウント
    for key in dictionary:
        result_dict.append(np.count_nonzero(data == key))

    return result_dict

# データの読み込み
q1, q2, q3 = read_survey_data()

# 結果の取得
survey_dict_q1 = [1, 2, 3, 4, 5]
survey_dict_q2 = [1, 2, 3, 4, 5]
survey_dict_q3 = [1, 2, 3, 4, 5, 6, 7]

result_q1 = check_survey_data(survey_dict_q1, q1)
result_q2 = check_survey_data(survey_dict_q2, q2)
result_q3 = check_survey_data(survey_dict_q3, q3)

q1_mean = q1.mean()
q2_mean = q2.mean()
q3_mean = q3.mean()

print('問1 集計結果: ' , result_q1 , ', 平均値' , q1_mean)
print('問2 集計結果: ' , result_q2 , ', 平均値' , q2_mean)
print('問3 集計結果: ' , result_q3 , ', 平均値' , q3_mean)

# フォントをMSゴシックに(日本語化対応)
plt.rcParams['font.family'] = 'MS Gothic'
# サブプロットの作成
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 5))

# 最初のグラフ
axes[0].bar(survey_dict_q1, result_q1, color='blue')
axes[0].set_title('問1 集計結果')
axes[0].set_xlabel('スコア')
axes[0].set_ylabel('人数')

# 二番目のグラフ
axes[1].bar(survey_dict_q2, result_q2, color='red')
axes[1].set_title('問2 集計結果')
axes[1].set_xlabel('スコア')
axes[1].set_ylabel('人数')

# 三番目のグラフ
axes[2].bar(survey_dict_q3, result_q3, color='green')
axes[2].set_title('問3 集計結果')
axes[2].set_xlabel('スコア')
axes[2].set_ylabel('人数')

# グラフのレイアウトを調整
plt.tight_layout()

# グラフの表示
plt.show()