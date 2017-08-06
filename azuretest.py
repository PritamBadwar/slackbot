from selenium import webdriver
import requests, bs4, BeautifulSoup

driver = webdriver.Firefox()
driver.get("https://www.google.com/search?q=9393033723")

results = driver.find_elements_by_css_selector('div.g')

link = results[0].find_element_by_tag_name("a")
href = link.get_attribute("href")
print href

##driver.get(href)
##
##results2 = driver.find_elements_by_class_name("mreinfwpr")

r = requests.get(href)
print r.content
