import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

# 検索結果を表にまとめる
def search_task(search_words):
    search_word_list = []
    rank_list = []
    site_title_list = []
    site_url_list = []
    for search_word in search_words:
        # 上位から何件までのサイトを抽出するか指定する
        pages_num = 100+ 1
        print(f'【検索ワード】{search_word}')
        # Googleから検索結果ページを取得する
        url = f'https://www.google.co.jp/search?hl=ja&num={pages_num}&q={search_word}'
        request = requests.get(url)
        time.sleep(5)
        # Googleのページ解析を行う
        soup = BeautifulSoup(request.text, "html.parser")
        search_site_list = soup.select('div.kCrYT > a')
        # ページ解析と結果の出力
        for rank, site in zip(range(1, pages_num), search_site_list):
            try:
                site_title = site.select('h3.zBAuLc')[0].text
            except IndexError:
                site_title = site.select('img')[0]['alt']
            site_url = site['href'].replace('/url?q=', '')
            # 結果を出力する
            print(str(rank) + "位: " + site_title + ": " + site_url)
            search_word_list.append(search_word)
            rank_list.append(rank)
            site_title_list.append(site_title)
            site_url_list.append(site_url)
    return search_word_list, rank_list, site_title_list, site_url_list

def G_search(search_words):
    result_list = search_task(search_words)
    search_word_list = result_list[0]
    rank_list = result_list[1]
    site_title_list = result_list[2]
    site_url_list = result_list[3]
    df = pd.DataFrame({
    "順位":rank_list,
    "検索ワード":search_word_list,
    "URL":site_url_list,
    "タイトル":site_title_list
    })
    # 検索ワードごとに票を横並びに変更
    result = pd.DataFrame()
    for word in search_words:
        tmp_df = df[df["検索ワード"] == word].reset_index(drop=True)
        tmp_rank = "順位" + word
        tmp_word = "検索ワード" + word
        tmp_url = "URL" + word
        tmp_title = "タイトル" + word
        tmp_df = tmp_df.rename(columns={'順位': tmp_rank, '検索ワード':tmp_word, 'URL':tmp_url, 'タイトル':tmp_title})
        result = pd.concat([result, tmp_df], axis=1)
    c_path = os.getcwd()
    # os.remove(c_path + "/flask_blog/add/DL_BOX/result.xlsx")
    result.to_csv("result.csv", encoding="utf-8")
    return "完了しました"
