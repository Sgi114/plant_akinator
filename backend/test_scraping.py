import requests
from bs4 import BeautifulSoup
import time
import re
import json


def scraping():
    name_url = requests.get("http://www.io-net.com/violet/abcindex.htm")
    name_url.encoding = name_url.apparent_encoding  # 呪文

    soup = BeautifulSoup(name_url.text, 'html.parser')
    tags = soup.find_all('td', class_='white')

    name_url_list = []
    for tag in tags:  # 一つづつ取り出した〇〇〇クラスの中の"a"タグの情報を取得
        for a in tag.select("a"):  # aタグの中の　href="リンク先のURL"　というようなhref=のあとの情報を取得する
            url = a.get('href')
            url_new = url[1:]
            name_url_list.append("http://www.io-net.com/violet"+url_new)

    # URLの重複を削除
    name_url_list = list(set(name_url_list))

    for name in name_url_list:
        name = "http://www.io-net.com/violet/violet1/sumire.htm"  # NOTE: デバッグ用
        print(name)
        ac_url = requests.get(name)
        ac_url.encoding = ac_url.apparent_encoding  # 呪文
        soup = BeautifulSoup(ac_url.text, 'html.parser')

        # リンク集ページの場合はスキップ
        if ("親から検索" in soup.text):
            continue

        violas = {}
        plants = []
        table = soup.find('table', summary="解説枠")
        th_colspan = None
        th_rowspan = None

        # 解説枠の表が存在しない場合はスキップ
        if (table == None):
            continue
        tbody = table.find('tbody')
        trs = table.find_all(
            'tr') if tbody == None else tbody.find_all('tr')  # trタグを探す

        for tr in trs:
            for th in tr.find_all('th'):  # trタグからthタグを探す
                # if not th.get('rowspan'):
                if th.has_attr('colspan'):
                    th_colspan = tr.find('th', {'colspan': '2'})
                    th_rowspan = None
                elif th.has_attr('rowspan'):
                    th_colspan = None
                    th_rowspan = th

                key = None

                if th_colspan == th:
                    key = th.text
                elif th_rowspan != None and th_rowspan != th:
                    key = (th_rowspan.text+'_'+th.text)

                if (key is None):
                    continue

                violas[key] = ''

            for td in tr.find_all('td'):  # trタグからtdタグを探す
                text = str(td.text).replace("\t", "").replace(
                    "\\u3000", "").strip()  # 不要な文字を削除して整形（「\u3000」は全角スペース）
                text = text.replace("\r", "").replace("\n", "")
                # text = re.sub("\n{2,}", "\n", text)  # 複数の改行を1つにまとめる
                violas[key] = text
        print(violas)
        time.sleep(0.1)  # 連続アクセス防止
        break  # NOTE: デバッグ用
    # 折りたたむ
    return violas


if __name__ == "__main__":
    violas = scraping()
    json_text = json.dumps(violas).encode().decode("unicode-escape")
    with open('violas.json', 'w', encoding="utf-8") as f:
        f.write(json_text)
    print("完了")
