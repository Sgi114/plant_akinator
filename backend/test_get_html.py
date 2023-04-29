from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import get_selenium
import os


PYTHON_DIR_PATH = os.path.dirname(os.path.abspath(__file__))  # pyファイルが置かれているパス
CHROME_DRIVER_PATH = os.path.join(
    PYTHON_DIR_PATH, "webdriver", "chromedriver.exe")
TARGET_URL="https://blog.interstellar.co.jp/2019/01/28/python-scraping-4/"

# Selenium準備
get_selenium.setup()

# Sereniumの初期設定
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Chromeウィンドウを表示せずに実行
driver = webdriver.Chrome(chrome_options=options,
                          executable_path=CHROME_DRIVER_PATH)

# スクレイピング
driver.get(TARGET_URL)  # URLにアクセスする
# すべての要素が読み込まれるまで待機：https://qiita.com/uguisuheiankyo/items/cec03891a86dfda12c9a
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)

html = driver.page_source

# 結果を表示
print(html)

# クリップボードにコピー
pyperclip.copy(html)
