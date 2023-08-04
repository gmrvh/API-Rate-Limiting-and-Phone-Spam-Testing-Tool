#Humbucker bypass
# 1.0.0  04/08/23  Initial.
from requests import Request, Session
from selenium import webdriver 
import cloudscraper
import chromedriver_autoinstaller 
 
chromedriver_autoinstaller.install() 
driver = webdriver.Chrome() 

url = "https://www.dubizzle.com.eg/.humbucker/challenge/js/validate"
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
payload = '[{"window":{"innerHeight":1021,"outerHeight":1112,"innerWidth":1598,"outerWidth":1610,"screenX":1825,"screenY":70,"pageXOffset":0,"pageYOffset":0,"devicePixelRation":1},"client":{"width":1581,"height":1021},"screen":{"width":5120,"height":1440,"availWidth":5120,"availHeight":1400,"colorDepth":24,"pixelDepth":24}},"Win32","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",{"ogg":"probably","h264":"probably","webm":"probably"},{"vendor":"Google Inc. (NVIDIA)","renderer":"ANGLE (NVIDIA, NVIDIA GeForce GTX 980 Direct3D11 vs_5_0 ps_5_0)"},["Portable Document Format-application/pdf-pdf","Portable Document Format-text/pdf-pdf"],[{"deviceId":"moIKYAqud7H8cw2g3FyeZjFfMsCKyjbFDqcuW3vrHAE=","kind":"audioinput","label":"","groupId":"cidEOYc7U88AuJ6BNZQs8EwOj4I+4Iz6nEsaV4nPxnI="},{"deviceId":"mPANMaBw2ZttUER5af72tS0QLgeOPMDlv00MCgVF1xU=","kind":"audioinput","label":"","groupId":"cidEOYc7U88AuJ6BNZQs8EwOj4I+4Iz6nEsaV4nPxnI="},{"deviceId":"UVD79xAS7ER1doCfewucP/LMl8JDtKwJSw0DY16AnDw=","kind":"audioinput","label":"","groupId":"I8U46AYijgGl7Q5/ahxLU1SXfVSaKYzXIgibeUq7W9w="},{"deviceId":"cyLWGWw4ry4YnnJQ91HNkidLFbdvZwiACqclVCHBNuE=","kind":"audioinput","label":"","groupId":"Tj6qcoJHzlj37VPmjc5R3gqgYTluWHHL8bOrS7xEPIs="},{"deviceId":"pTeZSfwlGandAhrEQc0HLBfXYFk2NKBKSgxCEcLeXIw=","kind":"audioinput","label":"","groupId":"4cwHEHqZT9eQGWPTpnyr24s4ADPQvuyVFPiz547Fqdw="},{"deviceId":"YBnysqPAtSz5OsS9DdjGzd6XVcndA+hW11OoAorrpXw=","kind":"videoinput","label":"","groupId":"6K83r3mjXng63l7uuXxLg5S9TVkNqf6Rk/DCkXjiLXM="}],false,37,null,{"vibrate":"function vibrate() {\n    [native code]\n}","javaEnabled":"function javaEnabled() {\n    [native code]\n}","getGamepads":"function getGamepads() {\n    [native code]\n}","requestMIDIAccess":"function requestMIDIAccess() {\n    [native code]\n}","mozGetUserMedia":"function mozGetUserMedia() {\n    [native code]\n}","sendBeacon":"function sendBeacon() {\n    [native code]\n}","requestMediaKeySystemAccess":"function requestMediaKeySystemAccess() {\n    [native code]\n}","getAutoplayPolicy":"function getAutoplayPolicy() {\n    [native code]\n}","registerProtocolHandler":"function registerProtocolHandler() {\n    [native code]\n}","taintEnabled":"function taintEnabled() {\n    [native code]\n}","permissions":"function permissions() {\n    [native code]\n}","mimeTypes":"function mimeTypes() {\n    [native code]\n}","plugins":"function plugins() {\n    [native code]\n}","pdfViewerEnabled":"function pdfViewerEnabled() {\n    [native code]\n}","doNotTrack":"function doNotTrack() {\n    [native code]\n}","maxTouchPoints":"function maxTouchPoints() {\n    [native code]\n}","mediaCapabilities":"function mediaCapabilities() {\n    [native code]\n}","oscpu":"function oscpu() {\n    [native code]\n}","vendor":"function vendor() {\n    [native code]\n}","vendorSub":"function vendorSub() {\n    [native code]\n}","productSub":"function productSub() {\n    [native code]\n}","cookieEnabled":"function cookieEnabled() {\n    [native code]\n}","buildID":"function buildID() {\n    [native code]\n}","mediaDevices":"function mediaDevices() {\n    [native code]\n}","serviceWorker":"function serviceWorker() {\n    [native code]\n}","credentials":"function credentials() {\n    [native code]\n}","clipboard":"function clipboard() {\n    [native code]\n}","mediaSession":"function mediaSession() {\n    [native code]\n}","webdriver":"function webdriver() {\n    [native code]\n}","hardwareConcurrency":"function hardwareConcurrency() {\n    [native code]\n}","geolocation":"function geolocation() {\n    [native code]\n}","appCodeName":"function appCodeName() {\n    [native code]\n}","appName":"function appName() {\n    [native code]\n}","appVersion":"function appVersion() {\n    [native code]\n}","platform":"function platform() {\n    [native code]\n}","userAgent":"function userAgent() {\n    [native code]\n}","product":"function product() {\n    [native code]\n}","language":"function language() {\n    [native code]\n}","languages":"function languages() {\n    [native code]\n}","locks":"function locks() {\n    [native code]\n}","onLine":"function onLine() {\n    [native code]\n}","storage":"function storage() {\n    [native code]\n}","constructor":"function Navigator() {\n    [native code]\n}"},["en-US","en"],{"maxTouchPoints":0,"onTouchStart":false,"canHandleTouchEvents":false},{"name":"notifications","state":"prompt"},"function width() {\n    [native code]\n}","-1607895184",{"__nightmare":false,"callPhantom":false,"_phantom":false,"phantom":false,"webdriver":false,"_Selenium_IDE_Recorder":false,"callSelenium":false,"_selenium":false,"__webdriver_script_fn":false,"__driver_evaluate":false,"__webdriver_evaluate":false,"__selenium_evaluate":false,"__fxdriver_evaluate":false,"__driver_unwrapped":false,"__webdriver_unwrapped":false,"__selenium_unwrapped":false,"__fxdriver_unwrapped":false,"__webdriver_script_func":false,"documentSelenium":false,"documentWebdriver":false,"documentDriver":false},{"ogg":"probably","mp3":"maybe","wav":"probably","m4a":"maybe","aac":"maybe"}]'


# Initializing a list with two Useragents 
useragentarray = [ 
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", 
] 
for i in range(len(useragentarray)): 
	# Setting user agent iteratively as Chrome 108 and 107 
    driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": useragentarray[i]}) 
    driver.get("https://www.dubizzle.com.eg")
    cookies = driver.get_cookies()
    driver.close()

# ... (rest of the code)

# Converting Selenium cookies to a format suitable for 'requests'
cookie_dict = {}
for cookie in cookies:
    cookie_dict[cookie['name']] = cookie['value']

# Using 'requests' session and adding cookies to the request
s = Session()
req = Request('POST', url, data=payload, headers=headers)
s.cookies.update(cookie_dict)  # Add cookies to the session

prepped = req.prepare()

# Use the prepared request with the cookies
resp = s.send(prepped)

print(resp.status_code)
print(resp.text)
print(resp.cookies)


