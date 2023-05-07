from bs4 import BeautifulSoup
import time
import json
import re
import minify_html
import py3langid
import utils
from urllib.parse import urljoin
import get_selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from typing import Optional


PYTHON_DIR_PATH = os.path.dirname(os.path.abspath(__file__))  # pyファイルが置かれているパス
CHROME_DRIVER_PATH = os.path.join(
    PYTHON_DIR_PATH, "webdriver", "chromedriver.exe")


def scraping():
    # Sereniumの初期設定
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Chromeウィンドウを表示せずに実行
    options.add_argument("--log-level=3")  # ターミナルに出力しない
    driver = webdriver.Chrome(chrome_options=options,
                              executable_path=CHROME_DRIVER_PATH)

    driver.get("http://www.io-net.com/violet/abcindex.htm")
    # すべての要素が読み込まれるまで待機：https://qiita.com/uguisuheiankyo/items/cec03891a86dfda12c9a
    WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    tags = soup.find_all('td', class_='white')

    url_list = []
    for tag in tags:  # 一つづつ取り出した〇〇〇クラスの中の"a"タグの情報を取得
        for a in tag.select("a"):  # aタグの中の　href="リンク先のURL"　というようなhref=のあとの情報を取得する
            url = a.get('href')
            url_new = url[1:]
            url_list.append("http://www.io-net.com/violet"+url_new)

    # URLの重複を削除
    url_list = list(set(url_list))

    viola_list = []
    count = 0

    for url in url_list:
        # HTML取得
        driver.get(url)  # URLにアクセスする
        # すべての要素が読み込まれるまで待機：https://qiita.com/uguisuheiankyo/items/cec03891a86dfda12c9a
        WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # リンク集ページの場合はスキップ
        if ("親から検索" in soup.text):
            continue

        # 日本語の植物名を抽出
        name_ja = soup.find("span", {"class": "japanese_name_large"}).text

        # 画像URLを抽出
        image_url_list = []
        image_div_list = soup.find_all("div", {"class": "column"})
        for image_div in image_div_list:
            image_list = image_div.find_all("img")
            for image in image_list:
                if (image == None):
                    continue
                image_url = urljoin(url, image["src"])
                image_url_list.append(image_url)

        viola = {"url": url, "name_ja": name_ja, "image_list": image_url_list}
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
                if th.has_attr('colspan'):
                    th_colspan = th
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

            for td in tr.find_all('td'):  # trタグからtdタグを探す
                name_language = None
                for index, child in enumerate(td.children):
                    soup = BeautifulSoup(str(child), 'html.parser')
                    span_tag = soup.find("span")
                    if(span_tag is None):
                        name_language = "ja"
                        continue
                    elif ((span_tag.has_attr("class") and span_tag["class"][0] == "scientific_name") or span_tag.has_attr("lang")):
                        name_language = py3langid.classify(span_tag.text)[0]
                        break

                if (name_language is not None and name_language != "ja"):
                    for index, child in enumerate(td.children):
                        soup = BeautifulSoup(str(child), 'html.parser')
                        span_tag = soup.find("span")
                        if (span_tag != None and span_tag.has_attr("class")):
                            viola = add_viola_data(
                                viola, key+"_"+span_tag["class"][0], span_tag.text)
                        else:
                            viola = add_viola_data(
                                viola, key+"_"+name_language, str(soup.text).strip())
                else:
                    content_html = minify_html.minify(str(td))
                    # 正規表現で改行タグをすべて「\n」に置き換え
                    content_text = re.sub(r'<br\s*?/?>', '\\n', content_html)
                    # タグをすべて削除
                    content_text = re.sub(r'<.*?>', '', content_text)
                    # 整形
                    text = content_text.replace("\t", "").replace(
                        "\\u3000", "").strip()  # 不要な文字を削除して整形（「\u3000」は全角スペース）
                    text = re.sub("\n{2,}", "\n", text)  # 複数の改行を1つにまとめる
                    viola = add_viola_data(viola, key, text)
        viola = utils.remove_empty_keys(viola)
        viola_list.append(viola)
        count += 1
        print("✅ 完了: "+url+"（"+str(count)+"/"+str(len(url_list))+"）")
        time.sleep(0.1)  # 連続アクセス防止
    driver.quit()  # ブラウザを閉じる
    return viola_list


def add_viola_data(viola: object, key: Optional[str], text: Optional[str]) -> object:
    if(key is None or text is None):
        return viola
    key = key.replace("\n", "").replace("\t", "").strip()
    viola[key] = text
    return viola


if __name__ == "__main__":
    get_selenium.setup()
    viola_list = scraping()
    json_text = json.dumps(viola_list, ensure_ascii=False)
    with open('violas.json', 'w', encoding="utf-8") as f:
        f.write(json_text)
    print("完了")
