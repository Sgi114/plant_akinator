import requests
from bs4 import BeautifulSoup
import time
import re

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
        print(name)
        ac_url = requests.get(name)
        ac_url.encoding = ac_url.apparent_encoding  # 呪文
        soup = BeautifulSoup(ac_url.text, 'html.parser')

        # リンク集ページの場合はスキップ
        if("親から検索" in soup.text):
            continue

        violas = {}
        plants = []
        table = soup.find('table', summary="解説枠")

        # 解説枠の表が存在しない場合はスキップ
        if(table == None):
            continue
        tbody = table.find('tbody')
        trs = table.find_all(
            'tr') if tbody == None else tbody.find_all('tr')  # trタグを探す

        for tr in trs:
            for th in tr.find_all('th'):  # trタグからthタグを探す
                if not th.get('rowspan'):
                    violas[th.text] = ''
            for td in tr.find_all('td'):  # trタグからtdタグを探す
                text = str(td.text).replace("\t", "").replace(
                    "\\u3000", "").strip()  # 不要な文字を削除して整形（「\u3000」は全角スペース）
                text = re.sub("\n{2,}", "\n", text)  # 複数の改行を1つにまとめる
                violas[th.text] = text
        print(violas)
        time.sleep(0.1)  # 連続アクセス防止
    # 折りたたむ

