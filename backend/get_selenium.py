# ChromeWebDriver自動ダウンロード
# 参考サイト：http://holiday-programmer.net/webdriver_auto_update/#WebDriver-4

import os
import re
import shutil
import zipfile
from pip._vendor import requests
from selenium import webdriver
from selenium.webdriver.chrome import service as cs
from selenium.common.exceptions import SessionNotCreatedException
from bs4 import BeautifulSoup


PYTHON_DIR_PATH = os.path.dirname(os.path.abspath(__file__))  # pyファイルが置かれているパス


def setup():
    webdriver_url = "https://chromedriver.storage.googleapis.com/"  # ウェブドライバーページ
    file_name = "chromedriver_win32.zip"  # Windows用のファイル名

    executable_path = PYTHON_DIR_PATH + "\\webdriver\\chromedriver.exe"

    # Sereniumの初期設定
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Chromeウィンドウを表示せずに実行

    # ChromeWebdriverファイルのパス指定
    try:
        if os.path.isfile(executable_path) == False:
            raise FileNotFoundError()

        driver = webdriver.Chrome(
            chrome_options=options, executable_path=executable_path)
        driver.close()
    except (FileNotFoundError, SessionNotCreatedException) as e:
        if type(e) == SessionNotCreatedException:
            print("WebDriverファイルが古い可能性があります。最新バージョンのダウンロードを開始開始します。")
        elif type(e) == FileNotFoundError:
            print("WebDriverファイルが存在しません。ダウンロードを開始開始します。")
        else:
            print("不明な例外です。")
            print(e)
            exit()

        response = requests.get(webdriver_url)
        soup = BeautifulSoup(response.text, "lxml-xml")  # lxmlのインストールが必要

        if not os.path.exists(PYTHON_DIR_PATH+ "\\webdriver\\tmp\\"):
            os.makedirs(PYTHON_DIR_PATH + "\\webdriver\\tmp\\")

        success_flg = False
        version_arr = {}
        cnt = 0
        for version in reversed(soup.find_all("Key")):
            cnt += 1
            if file_name in version.text:
                version_name = re.compile(r'/.*').sub("", version.text)
                version_name = re.compile(
                    r'\..*').sub("", version_name).zfill(5)+str(cnt).zfill(5)

                version_arr[version_name] = version.text

        for version in sorted(version_arr.items(), reverse=True):
            zip_source = requests.get(webdriver_url+version[1])
            print("起動テストを開始します\t"+webdriver_url+version[1])

            # ダウンロードしたZIPファイルの書き出し
            with open(PYTHON_DIR_PATH+ "\\webdriver\\tmp\\" + file_name, "wb") as file:
                for chunk in zip_source.iter_content():
                    file.write(chunk)

            # ZIPファイルの解凍
            with zipfile.ZipFile(PYTHON_DIR_PATH + "\\webdriver\\tmp\\" + file_name) as file:
                file.extractall(PYTHON_DIR_PATH + "\\webdriver\\tmp\\")

            try:
                driver = webdriver.Chrome(chrome_options=options,
                                          executable_path=PYTHON_DIR_PATH + "\\webdriver\\tmp\\chromedriver.exe")
                if(os.path.isfile(PYTHON_DIR_PATH + "\\webdriver\\chromedriver.exe")):
                    os.remove(PYTHON_DIR_PATH + "\\webdriver\\chromedriver.exe")
                shutil.move(PYTHON_DIR_PATH + "\\webdriver\\tmp\\chromedriver.exe",
                            PYTHON_DIR_PATH + "\\webdriver\\chromedriver.exe")

                print("正常に起動しました。WebDriverを上書きします。")

                shutil.rmtree(PYTHON_DIR_PATH + "\\webdriver\\tmp\\")
                success_flg = True
                break
            except SessionNotCreatedException as e:
                print("起動中にエラーが発生しました。\t"+webdriver_url+version[1])
        # print(version_arr)
        if not success_flg:
            print("WebDriverファイルの上書き中に例外が発生しました。処理を中断します")

    # ▼以降にWebDriverの処理を記述。。。
    print("Good Luck!!")


if __name__ == "__main__":
    setup()
