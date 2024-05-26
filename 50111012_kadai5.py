'''
    課題5: アンケート結果をグラフで表示するプログラム
    日にち: 2024-05-22
    学籍番号: 50111012
    名前: 大芝 峻平
    どんな処理か: アンケートの集計結果のグラフ化
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# データの読み込みと使用する部分の切り出し
def read_survey_data():
    df = pd.read_csv('./2023_第6回データとプログラミングアンケート（回答）.csv')
    # データの振り分け
    q1_data = df['1. 進み具合はどうですか？'].to_numpy()
    q2_data = df['2. 難易度はどうですか？'].to_numpy()
    q3_data = df['3. 授業教材で欲しいのは？'].to_numpy()
    q4_data = df['3. h. その他'].to_numpy()
    q5_data = df['4. 授業の形式はやっぱりどれが一番いい？'].to_numpy()

    return q1_data, q2_data, q3_data, q4_data, q5_data

# 番号回答をカウント
def check_survey_data(dictionary, data):
    # 出現回数をカウントする辞書配列
    result_dict = []

    # dictionaryに含まれる各価に対して，data配列内の出現回数をカウント
    for key in dictionary:
        result_dict.append(np.count_nonzero(data == key))

    return result_dict

# 文章回答をカウント
def count_survey_data(dictionary, data):
    result = np.zeros(len(dictionary))
    
    for get_data in data:
        for i in range(len(dictionary)):
            if dictionary[i] in get_data:
                result[i] += 1
    return result


# データの読み込み
q1, q2, q3, _, q5 = read_survey_data()

# 結果の辞書
survey_dict_q1 = [1, 2, 3, 4, 5]
survey_dict_q2 = [1, 2, 3, 4, 5]
survey_dict_q3 = ['a.', 'b.', 'c.', 'd.', 'e', 'f', 'g']
survey_dict_q5 = ['a.', 'b.', 'c.', 'd.']

# 結果の取得
result_q1 = check_survey_data(survey_dict_q1, q1)
result_q2 = check_survey_data(survey_dict_q2, q2)
result_q3 = count_survey_data(survey_dict_q3, q3)
result_q4 = count_survey_data(survey_dict_q5, q5)

# フォントをMSゴシックに(日本語化対応)
plt.rcParams['font.family'] = 'Hiragino Sans'

# 最初のグラフ
fig1, ax1 = plt.subplots()
ax1.pie(result_q1, labels=survey_dict_q1, autopct='%1.1f%%', startangle=90)
ax1.set_title('問1 集計結果')
fig1.savefig('survey_question1.png')

# 二番目のグラフ
fig2, ax2 = plt.subplots()
ax2.pie(result_q2, labels=survey_dict_q2, autopct='%1.1f%%', startangle=90)
ax2.set_title('問2 集計結果')
fig2.savefig('survey_question2.png')

# 三番目のグラフ
fig3, ax3 = plt.subplots()
ax3.bar(survey_dict_q3, result_q3, color='green')
ax3.set_title('問3 集計結果')
ax3.set_xlabel('スコア')
ax3.set_ylabel('人数')
ax3.set_xticks(survey_dict_q3)  # x軸の刻み設定
fig3.savefig('survey_question3.png')

# 五番目の円グラフ
fig4, ax4 = plt.subplots()
ax4.pie(result_q4, labels=survey_dict_q5, autopct='%1.1f%%', startangle=90)
ax4.set_title('問5 集計結果の円グラフ')
fig4.savefig('survey_question5.png')
plt.show()

