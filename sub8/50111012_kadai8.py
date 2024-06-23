"""
    課題8: 
    日にち: 2024-06-12
    学籍番号: 50111012
    名前: 大芝 峻平
    どんな処理か: カテゴリごとに店舗をまとめ, HTML化して書き出すプログラム
"""

import os

import numpy as np
import pandas as pd

CONFIGFILE = "./insyokuten_web_config.csv"
CONTENTSFILE = "./insyokuten_ninsyo.csv"

def read_certified_restaurants_data(file_path):
    """
    認証飲食店データの読み込み用関数
    パラメータ: 認証飲食店データを記録したCSVファイルのパス
    """
    df = pd.read_csv(file_path, dtype=object)
    df.fillna("", inplace=True)
    store_name          = df["店舗_名称"].to_numpy(dtype=object)
    store_site          = df["店舗_所在地"].to_numpy(dtype=object)
    store_postcode      = df["店舗_所在地_郵便番号"].to_numpy(dtype=object)
    store_industcode    = df["店舗_業態_産業分類コード"].to_numpy(dtype=object)
    store_industclass   = df["店舗_業態_産業分類名"].to_numpy(dtype=object)
    store_tel           = df["店舗_電話番号"].to_numpy(dtype=object)
    store_website       = df["店舗_Webサイト"].to_numpy(dtype=object)
    store_register      = df["店舗_登録日"].to_numpy(dtype=object)
    return store_name, store_site, store_postcode,\
          store_industcode, store_industclass, store_tel, store_website, store_register

def get_config(file_path):
    """
    設定ファイルから様々なパラメータをインポートする関数
    パラメータ: 設定ファイルのパス
    """
    df = pd.read_csv(file_path, header=None)
    df_t = df.T
    df_t.columns = df_t.iloc[0]
    df_t = df_t[1:]
    title = df_t["title"].iloc[0]
    date = df_t["date"].iloc[0]
    description = df_t["description"].iloc[0]
    link = df_t["link"].iloc[0]
    link_title = df_t["link_title"].iloc[0]
    copyright_text = df_t["copyright"].iloc[0]
    path = df_t["path"].iloc[0]
    top_filename = df_t["top_filename"].iloc[0]
    cat_prefix = df_t["cat_prefix"].iloc[0]
    return title, date, description, link,\
          link_title, copyright_text, path, top_filename, cat_prefix

def output_html(html_code, filename):
    """
    HTMLファイルを出力する関数
    パラメータ: HTMLのソースコード, 出力するファイル名
    """
    html_string = "".join(html_code)
    f = open(filename, "w", encoding="utf-8")
    f.write(html_string)
    f.close()

def make_dict(ndarray):
    """
    辞書配列を作る関数
    パラメータ: numpy.ndarray配列
    """
    dictionary_count = {}
    for element in ndarray:
        if element in dictionary_count:
            dictionary_count[element] += 1
        else:
            dictionary_count[element] = 1
    return dictionary_count

def make_head(titlename):
    """
    HTMLの<HEAD>タグ部分を作る関数
    パラメータ: ページのタイトル名
    """
    head_row = [
        "<!DOCTYPE html>",
    "<html lang=\"en\">",
    "<head>",
    "<meta charset=\"UTF-8\">",
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">",
    "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">",
    "<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>",
    "<link href=\"https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@100..900&display=swap\" rel=\"stylesheet\">",
    "<title>"+titlename+"</title>",
    "<style>",
    "header {",
    "  padding: 5px;",
    "  margin: 5px;",
    "  top: 0;",
    "  left: 0;",
    "  text-align: center;",
    "  font-family: \"Noto Sans JP\", sans-serif;",
    "  font-optical-sizing: auto;",
    "  font-weight: 400;",
    "  font-style: normal;",
    "}",
    ".bold {",
    "  font-family: \"Noto Sans JP\", sans-serif;",
    "  font-optical-sizing: auto;",
    "  font-weight: 800;",
    "  font-style: normal;",
    "}",
    ".normal {",
    "  font-family: \"Noto Sans JP\", sans-serif;",
    "  font-optical-sizing: auto;",
    "  font-weight: 400;",
    "  font-style: normal;",
    "}",
    "main {",
    "  margin: auto;",
    "  font-family: \"Noto Sans JP\", sans-serif;",
    "  font-optical-sizing: auto;",
    "  font-weight: 400;",
    "  font-style: normal;",
    "  width: 60%;",
    "}",
    "footer {",
    "  text-align: center;",
    "  padding: 5px;",
    "  margin: 5px;",
    "  font-family: \"Noto Sans JP\", sans-serif;",
    "  font-optical-sizing: auto;",
    "  font-weight: 400;",
    "  font-style: normal;",
    "}",
    "ul {",
    "  list-style-type: none;",
    "  margin: 10px;",
    "}",
    "p.heading {",
    "  font-weight: bold;",
    "  display: inline;",
    "}",
    ".detail {",
    "  display: inline;",
    "}",
    "</style>",
    "</head>"
    ]
    return "\n".join(head_row)

def make_body_header(title, date, desc, link, link_t):
    """
    ページのヘッダ部分を作る関数
    パラメータ: タイトル, 日付, 説明, リンク, リンクのタイトル
    """
    header_row = [
        "<body>",
        "<header>",
        "<h1 class=\"bold\">"+title+"</h1>",
        "<p>"+desc+"</p>",
        "<a href="+link+">"+link_t+"</a>",
        "<h2 class=\"bold\">"+link_t+"("+date+")</h2>",
        "</header>",
        "<main>"
    ]
    return "\n".join(header_row)

def make_body_footer(cpyrgt):
    """
    ページのフッタ部分を作る関数
    パラメータ: コピーライト表示
    """
    foot_row = [
        "</main>",
        "<footer>",
        cpyrgt,
        "</footer>",
        "</body>",
        "</HTML>"
    ]
    return "\n".join(foot_row)

def make_top_page(indust_code, indust_class):
    """
    トップページを作る関数
    パラメータ: 設定ファイルのパス, 産業分類コードの配列, 産業分類名
    """
    title, date, desc, link, link_t,\
          cpyrgt, top_directory, filename, prefix = get_config(CONFIGFILE)
    code_dict = make_dict(indust_code)
    class_dict = make_dict(indust_class)
    html_text = []
    html_text.append(make_head(title))
    html_text.append(make_body_header(title, date, desc, link, link_t))
    html_text.append("<ul>")
    for class_name, class_code in zip(class_dict, code_dict):
        html_text.append("<li><a href=\""+str(prefix)+str(class_code)+".html\"class=\"normal\">")
        html_text.append(class_name)
        html_text.append("</a>["+str(class_dict[class_name])+"件]</li>\n")
    html_text.append("</ul>")
    html_text.append(make_body_footer(cpyrgt))
    save_filename = top_directory + "/" + filename + ".html"
    os.makedirs(top_directory, exist_ok=True)
    output_html(html_text, save_filename)

def categorize(store_info, indust_class, category_list):
    """
    カテゴリリストに伴って店を振り分ける関数
    パラメータ: 店の情報, 産業分類名, カテゴリリスト
    """
    categorized = [[] for _ in range(len(category_list))]
    for i, _ in enumerate(indust_class):
        category_index = np.where(np.array(list(category_list.keys())) == indust_class[i])[0]
        if len(category_index) > 0:
            categorized[category_index[0]].append(store_info[i])
    return categorized

def make_category_page(indust_class, indust_code, store_name, tel, register_date, url, postcode, site):
    """
    カテゴリページを作る関数
    パラメータ: 産業分類名, 店名, 電話番号, 住所
    """
    title, date, desc, link, link_t,\
          cpyrgt, top_directory, filename, prefix = get_config(CONFIGFILE)
    category_list = make_dict(indust_class)
    code_list = make_dict(indust_code)
    number_of_category = len(category_list)
    name_categorized = categorize(store_name, indust_class, category_list)
    tel_categorized = categorize(tel, indust_class, category_list)
    url_categorized = categorize(url, indust_class, category_list)
    postcode_categorized = categorize(postcode, indust_class, category_list)
    site_categorized = categorize(site, indust_class, category_list)
    register_date_categorized = categorize(register_date, indust_class, category_list)
    category_keys = list(category_list.keys())
    code_keys = list(code_list.keys())
    for i in range(number_of_category):
        html_row = []
        row_text = [
            make_head(category_keys[i]),
            make_body_header(title, date, desc, link, link_t),
            "<a href=\"./"+filename+".html\" >戻る</a>",
            "<h3>"+str(category_keys[i])+"["+str(len(name_categorized[i]))+"件]</h3>",
            "<ul>"
        ]
        html_row.append("\n".join(row_text))
        for j in range(len(name_categorized[i])):
            li_text = "<li>"
            if url_categorized[i][j] != "":
                li_text += "<a href=\"" + str(url_categorized[i][j]) + ".html\">"
                li_text += str(name_categorized[i][j]) + "</a>"
            else:
                li_text += str(name_categorized[i][j])
            li_text += "(登録日: " + str(register_date_categorized[i][j]) + ")\n"
            li_text += "<ul>\n"
            li_text += "<li>TEL: " + str(tel_categorized[i][j]) + "</li>\n"
            li_text += "<li>〒 " + str(postcode_categorized[i][j]) + "</li>\n"
            li_text += "<li>住所: " + str(site_categorized[i][j]) + "</li>\n"
            li_text += "</ul>\n</li>\n"
            html_row.append(li_text)
        row_text = [
            "</ul>",
            make_body_footer(cpyrgt)
        ]
        html_row.append("\n".join(row_text))
        html_code = "".join(html_row)
        categpry_filename = top_directory + "/" + prefix + str(code_keys[i]) + ".html"
        output_html(html_code, categpry_filename)

def main():
    """
    メイン関数
    """
    name, site, postcode, industcode, \
        industclass, tel, weburl, register_date = read_certified_restaurants_data(CONTENTSFILE)
    make_top_page(industcode, industclass)
    make_category_page(industclass, industcode, name, tel, register_date, weburl, postcode, site)

if __name__ == "__main__":
    main()
