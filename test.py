import requests
import json
from twocaptcha import TwoCaptcha

import cloudscraper

url = "https://auth.dubizzle.com.eg/auth/realms/olx-eg/passwordless-login/phone-number/generate-challenge"
cookie = "device_id=lkg5eq3eqfeqgsr1l; settings=%7B%22area%22%3Anull%2C%22currency%22%3A%22EGP%22%2C%22installBanner%22%3Atrue%2C%22searchHitsLayout%22%3A%22LIST%22%7D; abTests=%7B%7D; banners=%7B%7D; userGeoLocation=%7B%22coordinates%22%3Anull%2C%22closestLocation%22%3Anull%2C%22loading%22%3Afalse%2C%22error%22%3Anull%7D; g_state={\"i_p\":1690172145679,\"i_l\":1}; anonymous_session_id=62aabbd4-34cb-4a56-9ad3-18d53c9ecee7; hb-session-id=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..vKU1OU2yUlBdR63_.RaXJeR0AqcxDqYkHR-zWu64Ho4lVtWaoUpABDArnq3RFGlLMgG0O6YhvwEtxLbtJX5FnyEhISAS3KctHIdwgJvtJxfHDIIbQuPSafKw6BMWkXg8XAytCs0XbZS847JQa-bvk4bfU1P4FVpdYGJd0R-Dx4_DwuSVe99Ih0s6DXUpdxe-cTj_wLmbH741HCK-mOqA806vAHwPmx6KHYtWAKKehqqhYmej-jqQO273LN9auCXYgDGNBn8T_V_QmPCcXpYLXfZeYmJYGFijZcNXEr_XSw01khX72ZczYprOXQE2KWV9hTkAhj1FMYNq2WBqz0exl2lrAWii5TxJIWtk.KNk3599HHojCirZdCPjX4A; landing_url=%2F"
headers = {
    "Host":"auth.dubizzle.com.eg",
      "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
      "Accept":"application/json",
      "Cache-Control":"no-cache",
      "Connection":"keep-alive",
      "Accept-Language":"en-US,en;q=0.5",
      "Accept-Encoding":"gzip, deflate, br",
      "Content-Type":"application/json",
      "Cookie":f"{cookie}",
      "Origin":"https://www.dubizzle.com.eg",
      "Pragma":"no-cache",
      "Referer":"https://www.dubizzle.com.eg/",
      "Sec-Fetch-Dest":"empty",
      "Sec-Fetch-Mode":"no-cors",
      "Sec-Fetch-Site":"same-site",
      "TE":"trailers"
}



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
captcha_code = ""
payload = {f"client_id":"frontend","medium":"call","phone_number":"+201019444480","captcha":"{captcha_code}"}
headers = {key: value.encode('utf-8') for key, value in headers.items()} #Fix Unicode
resp = scraper.post(url, json=payload, headers=headers)

print(resp.text)

	