from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0




from twocaptcha import TwoCaptcha
from requests import Request, Session
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
import re
import cloudscraper
import chromedriver_autoinstaller 
import time 
import undetected_chromedriver as uc

driver = uc.Chrome()
headers = {
    "Host":"auth.dubizzle.com.eg",
      "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
      "Accept":"application/json",
      "Cache-Control":"no-cache",
      "Connection":"keep-alive",
      "Accept-Language":"en-US,en;q=0.5",
      "Accept-Encoding":"gzip, deflate, br",
      "Content-Type":"application/json",
      "Origin":"https://www.dubizzle.com.eg",
      "Pragma":"no-cache",
      "Referer":"https://www.dubizzle.com.eg/",
      "Sec-Fetch-Dest":"empty",
      "Sec-Fetch-Mode":"no-cors",
      "Sec-Fetch-Site":"same-site",
      "TE":"trailers"
}
jar = []
payload = '[9,,{"vendor":"Google Inc. (NVIDIA)","renderer":"ANGLE (NVIDIA, NVIDIA GeForce GTX 1660 SUPER Direct3D11 vs_5_0 ps_5_0, D3D11)"},false,{"maxTouchPoints":1,"onTouchStart":false,"canHandleTouchEvents":false},"function get width() { [native code] }",{"ogg":"probably","mp3":"probably","wav":"probably","m4a":"","aac":""},{"__nightmare":false,"callPhantom":false,"_phantom":false,"phantom":false,"webdriver":false,"_Selenium_IDE_Recorder":false,"callSelenium":false,"_selenium":false,"__webdriver_script_fn":false,"__driver_evaluate":false,"__webdriver_evaluate":false,"__selenium_evaluate":false,"__fxdriver_evaluate":false,"__driver_unwrapped":false,"__webdriver_unwrapped":false,"__selenium_unwrapped":false,"__fxdriver_unwrapped":false,"__webdriver_script_func":false,"documentSelenium":false,"documentWebdriver":false,"documentDriver":false},["en-US","en"],"422808721","Win32",["-application/pdf-pdf","Portable Document Format-application/x-google-chrome-pdf-pdf"],"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.171 Safari/537.36",{"window":{"innerHeight":720,"outerHeight":814,"innerWidth":856,"outerWidth":872,"screenX":3360,"screenY":304,"pageXOffset":0,"pageYOffset":0,"devicePixelRation":1},"client":{"width":839,"height":703},"screen":{"width":5120,"height":1440,"availWidth":5120,"availHeight":1400,"colorDepth":24,"pixelDepth":24}},null,[{"deviceId":"","kind":"audioinput","label":"","groupId":""},{"deviceId":"","kind":"videoinput","label":"","groupId":""},{"deviceId":"","kind":"audiooutput","label":"","groupId":""}],33,{"ogg":"probably","h264":"","webm":"probably"},{"vendorSub":"function get vendorSub() { [native code] }","productSub":"function get productSub() { [native code] }","vendor":"function get vendor() { [native code] }","maxTouchPoints":"function get maxTouchPoints() { [native code] }","scheduling":"function get scheduling() { [native code] }","userActivation":"function get userActivation() { [native code] }","doNotTrack":"function get doNotTrack() { [native code] }","geolocation":"function get geolocation() { [native code] }","connection":"function get connection() { [native code] }","plugins":"function get plugins() { [native code] }","mimeTypes":"function get mimeTypes() { [native code] }","pdfViewerEnabled":"function get pdfViewerEnabled() { [native code] }","webkitTemporaryStorage":"function get webkitTemporaryStorage() { [native code] }","webkitPersistentStorage":"function get webkitPersistentStorage() { [native code] }","hardwareConcurrency":"function get hardwareConcurrency() { [native code] }","cookieEnabled":"function get cookieEnabled() { [native code] }","appCodeName":"function get appCodeName() { [native code] }","appName":"function get appName() { [native code] }","appVersion":"function get appVersion() { [native code] }","platform":"function get platform() { [native code] }","product":"function get product() { [native code] }","userAgent":"function get userAgent() { [native code] }","language":"function get language() { [native code] }","languages":"function get languages() { [native code] }","onLine":"function get onLine() { [native code] }","webdriver":"function get webdriver() { [native code] }","getGamepads":"function getGamepads() { [native code] }","javaEnabled":"function javaEnabled() { [native code] }","sendBeacon":"function sendBeacon() { [native code] }","vibrate":"function vibrate() { [native code] }","constructor":"function Navigator() { [native code] }","bluetooth":"function get bluetooth() { [native code] }","clipboard":"function get clipboard() { [native code] }","credentials":"function get credentials() { [native code] }","keyboard":"function get keyboard() { [native code] }","managed":"function get managed() { [native code] }","mediaDevices":"function get mediaDevices() { [native code] }","storage":"function get storage() { [native code] }","serviceWorker":"function get serviceWorker() { [native code] }","virtualKeyboard":"function get virtualKeyboard() { [native code] }","wakeLock":"function get wakeLock() { [native code] }","deviceMemory":"function get deviceMemory() { [native code] }","ink":"function get ink() { [native code] }","hid":"function get hid() { [native code] }","locks":"function get locks() { [native code] }","mediaCapabilities":"function get mediaCapabilities() { [native code] }","mediaSession":"function get mediaSession() { [native code] }","serial":"function get serial() { [native code] }","gpu":"function get gpu() { [native code] }","usb":"function get usb() { [native code] }","windowControlsOverlay":"function get windowControlsOverlay() { [native code] }","xr":"function get xr() { [native code] }","userAgentData":"function get userAgentData() { [native code] }","canShare":"function canShare() { [native code] }","share":"function share() { [native code] }","clearAppBadge":"function clearAppBadge() { [native code] }","getBattery":"function getBattery() { [native code] }","getUserMedia":"function getUserMedia() { [native code] }","requestMIDIAccess":"function requestMIDIAccess() { [native code] }","requestMediaKeySystemAccess":"function requestMediaKeySystemAccess() { [native code] }","setAppBadge":"function setAppBadge() { [native code] }","webkitGetUserMedia":"function webkitGetUserMedia() { [native code] }","getInstalledRelatedApps":"function getInstalledRelatedApps() { [native code] }","registerProtocolHandler":"function registerProtocolHandler() { [native code] }","unregisterProtocolHandler":"function unregisterProtocolHandler() { [native code] }"}]'

def convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct
         

# Initializing a list with two Useragents 
useragentarray = [ 
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", 
] 
for i in range(len(useragentarray)): 
	# Setting user agent iteratively as Chrome 108 and 107 
	cookie_dict = {}
	driver.get("https://www.dubizzle.com.eg") # Get base cookie
	time.sleep(1)
	cookies = driver.get_cookies() 
	headers = driver.execute_script("var req = new XMLHttpRequest();req.open('GET', document.location, false);req.send(null);return req.getAllResponseHeaders()")
	headers = headers.splitlines()
	for cookie in cookies:
		cookie_dict[cookie['name']] = cookie['value']
		if cookie['name'] == 'hb-session-id':
			print("[+] Created session id: " + cookie['value'])
driver.close()

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
if captcha_code == None:
	print(result)
payload = {f"client_id":"frontend","medium":"call","phone_number":"+201019444480","captcha":"{captcha_code}"}
print(convert(headers))
print(type(headers))


