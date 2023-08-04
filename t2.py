#Humbucker bypass
# 1.0.0  04/08/23  Initial.
from requests import Request, Session
from selenium import webdriver 
import cloudscraper
import chromedriver_autoinstaller 
 
chromedriver_autoinstaller.install() 
driver = webdriver.Chrome() 
 
# Initializing a list with two Useragents 
useragentarray = [ 
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", 
] 
for i in range(len(useragentarray)): 
	# Setting user agent iteratively as Chrome 108 and 107 
	driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": useragentarray[i]}) 
	print(driver.execute_script("return navigator.userAgent;")) 
	driver.get("https://www.dubizzle.com.eg") 
	driver.get_cookies()
driver.close()