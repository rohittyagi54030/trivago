import os

os.system("pip3 install -r requirements.txt")

# from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.alert import Alert
import time

try:
    os.system("pip3 install PyVirtualDisplay==1.3.2")
except:
    pass
from pyvirtualdisplay import Display
from sys import platform
import datetime
import random
import string
import json
import requests
import telegram_send_msg as tg

runBatFile = "no"
autocontrol = 'yes'

ip_address = "49.36.190.136"

run = 0
bounce_count = 0

bounce_percent = 30  # percent

options = webdriver.ChromeOptions()
uas = []
import csv

with open("./UserAgentMobile.csv", "r") as csvfile:
    reader_variable = csv.reader(csvfile, delimiter=",")
    for row in reader_variable:
        uas.append(row)
ua = random.choice(uas)
options.add_argument(f"user-agent={ua[0]}")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("detach", True)
options.add_argument("--window-size=320,780")
mobile_emulation = {
    "deviceMetrics": {"width": 375, "height": 612, "pixelRatio": 3.0},
    "userAgent": ua[0]
}
options.add_experimental_option("mobileEmulation", mobile_emulation)

# Autocontrol
if (autocontrol == 'yes'):
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--window-size=1420,1080")
    display = Display(visible=0, size=(1420, 1080))
    display.start()

proxies = {
    "proxy": {
        "http": f"http://madanrajat:pKQ85G0bWjPcgtqX_country-UnitedStates@proxy.packetstream.io:31112",
        "https": f"http://madanrajat:pKQ85G0bWjPcgtqX_country-UnitedStates@proxy.packetstream.io:31112",
    }
}

url = "https://www.trivago.com/"
while True:
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install(), seleniumwire_options=proxies, options=options)

        driver.get(url)
        time.sleep(20)
        # try:
        #     print("Finding Accept Button")
        #     accept_button = driver.find_element(By.XPATH,
        #                                         "/html/body/div[4]//div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/button[2]")
        #     # accept_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='uc-accept-all-button']")
        #     accept_button.click()
        # except Exception as E:
        #     print(E)
        #     pass

        search_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='search-form-destination']")
        if search_button:
            search_button.click()
            time.sleep(1)
            search_box = driver.find_element(By.ID, 'input-auto-complete')
            if search_box:
                letters = string.ascii_lowercase
                result_str = ''.join(random.choice(letters) for i in range(2))
                search_box.send_keys(result_str)
                # sug_list = driver.find_element(By.ID, 'suggestion-list')
                time.sleep(7)

                elem = driver.find_element(By.XPATH, '/html/body/div[3]/div/section/main/div/form/div[2]/ul/li[1]')
                elem.click()
                time.sleep(5)

                check_in_day = random.randint(28, 30)
                check_out_day = random.randint(10, 31)
                check_in = f'[data-testid="valid-calendar-day-2024-06-{check_in_day}"]'
                check_out = f'[data-testid="valid-calendar-day-2024-07-{check_out_day}"]'
                check_in_date_button = driver.find_element(By.CSS_SELECTOR, check_in)
                check_in_date_button.click()
                time.sleep(1)
                check_out_date_button = driver.find_element(By.CSS_SELECTOR, check_out)

                actions = ActionChains(driver)
                actions.move_to_element(check_out_date_button).perform()

                check_out_date_button.click()
                time.sleep(2)
                date_select_button = driver.find_element(By.CSS_SELECTOR,
                                                         '[data-testid="fullscreen-calendar-apply-dates-btn"]')
                date_select_button.click()
                time.sleep(2)
                guest_select_button = driver.find_element(By.CSS_SELECTOR,
                                                          '[data-testid="guest-selector-apply"]')
                guest_select_button.click()
                time.sleep(20)

                deal_button = random.choice(driver.find_elements(By.CSS_SELECTOR, '[data-testid="champion-deal"]'))

                actions.move_to_element(deal_button).perform()
                deal_button.click()
                time.sleep(40)
                driver.switch_to.window(driver.window_handles[1])

                driver.get_screenshot_as_file("screenshot.png")
                time.sleep(2)
                tg.telegram_bot_sendimage('screenshot.png', 2, '', 'ip_address::' + ip_address + "updated",
                                          'ip_address::' + ip_address + "updated", '')

        # RunBat
        if (runBatFile == "yes"):
            if (platform == 'linux'):
                activeNetworks = os.popen('nmcli con show --active').read()
                splitedActiveNetworks = activeNetworks.split('\n')
                b = splitedActiveNetworks[1][:splitedActiveNetworks[1].find('-')]
                c = b.split(' ')
                d = " "
                c = c[:-1]
                e = d.join(c)
                e = e.strip()

                os.popen("nmcli con down '" + e + "'").read()
                print("connection disconnected")
                time.sleep(10)
                os.popen("nmcli con up '" + e + "'").read()
                print("connection established")
                time.sleep(50)
            else:
                # driver.switch_to.window(driver.window_handles[1])
                driver.execute_script('javascript:document.title="run_bat1"')
                time.sleep(7)
                print("Chaning to hello world")
                driver.execute_script('javascript:document.title="hello_world"')
                time.sleep(33)
        driver.quit()

    except Exception as E:
        # print(E)
        try:
            driver.quit()
        except:
            pass
