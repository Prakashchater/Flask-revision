from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time

header = {
    # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url="https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.62909266515426%2C%22east%22%3A-122.08938929601364%2C%22south%22%3A37.612448356477266%2C%22north%22%3A37.931266472763504%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D",
                        headers=header)
website = response.text
soup = BeautifulSoup(website, "html.parser")

all_links = []


address = soup.select(selector="ul li article")
all_address = [add.getText().split(' | ')[-1] for add in address]
# print(all_address)


prices = soup.select(selector=".list-card-price")
all_price = [price.getText().split("+")[0].split("/")[0].split()[0] for price in prices]
# print(all_price)

links = soup.select(selector=".list-card-top a")
for link in links:
    href = link["href"]
    # print(href)
    if "https" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

google_sheet_link = "https://docs.google.com/forms/d/e/1FAIpQLScFZJSa9sT6Fz3HVWl3GWKWQGV8NYlFe7VMR_s8gWsX30jehg/viewform?usp=sf_link"
driver_path = "C:\Chrome driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)


for i in range(len(all_links)):

    driver.get(google_sheet_link)
    time.sleep(2)

    fill_address = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

    fill_prices = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

    fill_links = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )

    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')


    fill_address.send_keys(all_address[i])
    fill_prices.send_keys(all_price[i])
    fill_links.send_keys(all_links[i])
    submit.click()


