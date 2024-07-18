import requests
import time
from web3 import Web3
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

NOPECHA_KEY = 'itcl6asla5bo32r2' # Edit your key


w3 = Web3()
w3.eth.account.enable_unaudited_hdwallet_features()

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)

with open('ext.crx', 'wb') as f:
    f.write(requests.get('https://nopecha.com/f/ext.crx').content)
options.add_extension('ext.crx')

f = open("addrs.txt", "r")
lines = f.readlines()

proxies = open('proxy.txt').read().splitlines()

for addr in lines:
    addr = addr.replace("\n", "")
    print(f'Getting faucet of account={addr}...')
    
    lopt = options
    
    proxy =random.choice(proxies)
    seleniumwire_options = {
        "proxy": {
            "http": proxy,
            "https": proxy
        },
    }
    lopt.add_argument(f"--proxy-server={proxy}")

    driver = webdriver.Chrome(
        options=lopt,                    
        seleniumwire_options=seleniumwire_options
    )

    driver.get('https://faucet.0g.ai/')

    # wait until request button active
    button = WebDriverWait(driver, 36000).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Request AOGI Token')]")))
    
    #fill address
    driver.find_element(By.ID, 'address').send_keys(addr)
    # press button
    button.click()
    print(f'Requested faucet of account={addr}')
    # wait until success or fail
    time.sleep(10)

    driver.close()

time.sleep(10)
print(f'Finished')