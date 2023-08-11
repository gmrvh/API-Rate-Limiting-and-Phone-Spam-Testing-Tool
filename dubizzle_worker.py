#FingerprintJS Bypass

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from rich import print
import requests
from twocaptcha import TwoCaptcha
from requests import Request, Session
from seleniumwire import webdriver  
from seleniumwire.undetected_chromedriver.v2 import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
import re
import cloudscraper
import chromedriver_autoinstaller 
import time 
import undetected_chromedriver as uc


def sendRequest(target):
        chrome_options = ChromeOptions()
        driver = Chrome(options=chrome_options) 
        header = {
            "Host":"auth.dubizzle.com.eg",
            "Sec-Ch-Ua": "",
            "Accept":"application/json",
            "Content-Type":"application/json",
            "Sec-Ch-Ua-Mobile":"?0",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "Sec-Ch-Ua-Platform":"",
            "Origin":"https://www.dubizzle.com.eg",
            "Sec-Fetch-Site":"same-site",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Dest":"empty",
            "Referer":"https://www.dubizzle.com.eg/",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"en-US,en;q=0.9"
            }
        def captcha_solver() :
            url = "https://auth.dubizzle.com.eg/auth/realms/olx-eg/passwordless-login/phone-number/generate-challenge"
            scraper = cloudscraper.create_scraper(
                        interpreter="nodejs",
                        browser={
                            "browser": "firefox",
                            "platform": "windows",
                            "mobile": True,
                        },
                        captcha={
                            "provider": "2captcha",
                            "api_key": "feff5f62d5a6737c2dc45946d1854e80",
                        },
                    )
            solver = TwoCaptcha('feff5f62d5a6737c2dc45946d1854e80')
            result = solver.recaptcha(sitekey='6LdijU4iAAAAAPS5LzPDrsUYaessDfxTIPLzqRDh',
                                    url='dubizzle.com.eg',
                                    param1=...)
            captcha_code = result['code']
            return captcha_code

        cookie_dict = {}
        driver.header_overrides = header
        driver.get("https://www.dubizzle.com.eg")
        time.sleep(15)
        driver.find_element(By.CLASS_NAME, '_1b04dcc1').click()
        for request in driver.requests:
            if request.response:
                if request.url == 'https://www.dubizzle.com.eg/.humbucker/challenge/js/generate/script':
                    pre_headers = request.response.headers
                   
                if request.url == 'https://www.dubizzle.com.eg/.humbucker/challenge/js/validate':
                    set_cookie=request.response.headers['set-cookie'] if 'set-cookie' in request.response.headers else None
                    headers_dict = request.response.headers
                new_headers = request.headers

        if set_cookie:
            secret = set_cookie.split('=')[1] 
            print(secret)
            secret_length = len(secret)
            secret = secret[:secret_length-7]
            print("[+] hb-session-id found : ",secret)
            
        for cookie in driver.get_cookies():
            c = {cookie['name']: cookie['value']}
            

        payload = {"client_id":"frontend","medium":"call","phone_number":"+201277775763","captcha":f"{captcha_solver()}"}
        header['Content-Length'] = str(len(str(payload)))
        with requests.post('https://auth.dubizzle.com.eg/auth/realms/olx-eg/passwordless-login/phone-number/generate-challenge', json=payload, headers=new_headers, stream=True,cookies=c, verify=False ) as r:
            return r
        return None
        
