import requests
from bs4 import BeautifulSoup
import time
import json
import re
import minify_html
import py3langid
import utils


def scraping():
    name_url = requests.get("http://www.io-net.com/violet/abcindex.htm")
    name_url.encoding = name_url.apparent_encoding  # 呪文

    soup = BeautifulSoup(name_url.text, 'html.parser')
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
        url = "http://www.io-net.com/violet/violet1/sumire.htm"  # NOTE: デバッグ用
        print(url)
        ac_url = requests.get(url)
        ac_url.encoding = ac_url.apparent_encoding  # 呪文
        soup = BeautifulSoup(ac_url.text, 'html.parser')

        # リンク集ページの場合はスキップ
        if ("親から検索" in soup.text):
            continue

        viola = {"url": url}
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
                        viola[key+"_"+name_language] = soup.text.strip()
                        continue
                    elif ((span_tag.has_attr("class") and span_tag["class"][0] == "scientific_name") or span_tag.has_attr("lang")):
                        name_language = py3langid.classify(span_tag.text)[0]
                        break

                if (name_language is not None):
                    for index, child in enumerate(td.children):
                        soup = BeautifulSoup(str(child), 'html.parser')
                        span_tag = soup.find("span")
                        if (span_tag != None and span_tag.has_attr("class")):
                            viola[key+"_"+span_tag["class"][0]] = span_tag.text
                        else:
                            viola[key+"_"+name_language] = str(child).strip()
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
                    viola[key] = text
        viola=utils.remove_empty_keys(viola)
        viola_list.append(viola)
        count += 1
        print("✅ 完了: "+url+"（"+str(count)+"/"+str(len(url_list))+"）")
        if (count == 1):
            break  # デバッグ用
        time.sleep(0.1)  # 連続アクセス防止
    return viola_list


if __name__ == "__main__":
    viola_list = scraping()
    json_text = json.dumps(viola_list, ensure_ascii=False)
    with open('violas.json', 'w', encoding="utf-8") as f:
        f.write(json_text)
    print("完了")
