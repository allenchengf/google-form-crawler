import random

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os, stat
import requests
import time
import logging
import platform
import random
import shutil
from ftplib import FTP
ftp = FTP()


def main():
    correct_path = get_path_by_os()
    current_directory = os.getcwd() + correct_path + "temp"
    chrome_options = Options()

    # 不需開啟瀏覽器
    # chrome_options.add_argument('--headless=new')
    # chrome_options.add_argument('--no-sandbox')

    chrome_options.add_argument('--disable-extensions')
    prefs = {"download.default_directory": current_directory}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.maximize_window()

    # Send a get request to the url
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSf9mSE9L6Wyq45rTlYypGEimQpMP3_6ysg7_3UFzWo6l2hjsA/viewform')
    original_window = driver.current_window_handle
    driver.implicitly_wait(90)

    try:
        rand = random.randint(4, 5)

        # 第一段
        radiobuttons = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label['+str(get_random_number())+']/div[2]/div/div')
        driver.execute_script("arguments[0].click();", radiobuttons)

        radiobuttons2 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label['+str(get_random_number())+']/div[2]/div/div')
        driver.execute_script("arguments[0].click();", radiobuttons2)

        radiobuttons3 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label['+str(get_random_number())+']/div[2]/div/div')
        driver.execute_script("arguments[0].click();", radiobuttons3)

        radiobuttons4 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label['+str(get_random_number())+']/div[2]/div/div')
        driver.execute_script("arguments[0].click();", radiobuttons4)

        radiobuttons5 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label['+str(get_random_number())+']/div[2]/div/div')
        driver.execute_script("arguments[0].click();", radiobuttons5)

        # 第二段
        radiobuttons6 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label['+str(get_random_number())+']/div[2]/div/div')
        driver.execute_script("arguments[0].click();", radiobuttons6)

        radiobuttons7 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label['+str(get_random_number())+']/div[2]/div/div')
        driver.execute_script("arguments[0].click();", radiobuttons7)

        radiobuttons8 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label['+str(get_random_number())+']/div[2]/div/div')
        driver.execute_script("arguments[0].click();", radiobuttons8)

        radiobuttons9 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label['+str(get_random_number())+']/div[2]/div/div')
        driver.execute_script("arguments[0].click();", radiobuttons9)

        radiobuttons10 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label['+str(get_random_number())+']/div[2]/div/div')
        driver.execute_script("arguments[0].click();", radiobuttons10)

        # 第三段
        radiobuttons11 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label['+str(get_random_number())+']/div[2]')
        driver.execute_script("arguments[0].click();", radiobuttons11)

        radiobuttons12 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label['+str(get_random_number())+']/div[2]/div/div')
        driver.execute_script("arguments[0].click();", radiobuttons12)

        radiobuttons13 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label['+str(get_random_number())+']/div[2]/div/div')
        driver.execute_script("arguments[0].click();", radiobuttons13)

        radiobuttons14 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label['+str(get_random_number())+']/div[2]/div/div')
        driver.execute_script("arguments[0].click();", radiobuttons14)

        radiobuttons15 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label['+str(get_random_number())+']/div[2]/div/div')
        driver.execute_script("arguments[0].click();", radiobuttons15)

        # 第四段
        radiobuttons16 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label['+str(get_random_number())+']/div[2]/div/div')
        driver.execute_script("arguments[0].click();", radiobuttons16)

        radiobuttons17 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label['+str(get_random_number())+']/div[2]/div/div')
        driver.execute_script("arguments[0].click();", radiobuttons17)

        radiobuttons18 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label['+str(get_random_number())+']/div[2]/div/div')
        driver.execute_script("arguments[0].click();", radiobuttons18)

        radiobuttons19 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label['+str(get_random_number())+']/div[2]/div/div')
        driver.execute_script("arguments[0].click();", radiobuttons19)

        radiobuttons20 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label['+str(get_random_number())+']/div[2]/div/div')
        driver.execute_script("arguments[0].click();", radiobuttons20)


        submit = driver.find_element(By.XPATH, '// *[ @ id = "mG61Hd"] / div[2] / div / div[3] / div / div[1] / div')
        driver.execute_script("arguments[0].click();", submit)

    except requests.exceptions.RequestException as e:
        logging_message(e)
        print(e)

    time.sleep(3)

    driver.quit()
    print("Process Done!")


def get_random_number():
    return random.randint(4, 5)


def get_path_by_os():
    os_name = platform.system()
    if os_name == 'Windows':
        return '\\'
    else:
        return '/'


def logging_message(message):
    print(message)
    logging.basicConfig(level=logging.INFO, filename='accesslog ' + time.strftime('%Y%m%d_%H_%M_%S') + '.log',
                        filemode='a', format='%(asctime)s %(levelname)s: %(message)s')
    logging.info(message)


if __name__ == '__main__':
    main()
