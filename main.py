from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import requests
import pandas as pd
driver = webdriver.Chrome()

driver.get("https://www.flipkart.com")

try:
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'✕')]"))
    )
    close_button.click()
except:
    pass  

search_bar_path = '//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input'
search_bar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, search_bar_path))
)

###### !!!!!!!!!!!!!!!! ENTER YOUR QUERY HERE !!!!!!!!!!!!!!!!###### 
search_query = "laptop under 50000"
search_bar.send_keys(search_query)
search_bar.send_keys(Keys.RETURN)

WebDriverWait(driver, 10)

current_url = driver.current_url



Prod_Name = []
Prod_Price = []
Prod_Description = []


for page in range(1,3):
    paginated_url = f"{current_url}&page={page}" 
    r = requests.get(paginated_url)
    soup = BeautifulSoup(r.text, "lxml")

    names = soup.find_all("div", class_ = "KzDlHZ")
    prices = soup.find_all("div", class_ = "Nx9bqj _4b5DiR")
    descriptions = soup.find_all("ul", class_ = "G4BRas")
    for i in range(0, len(names)):
        name = names[i].text
        price = prices[i].text
        description = descriptions[i].text
        Prod_Name.append(name)
        Prod_Price.append(price) 
        Prod_Description.append(description)

driver.quit()

# Create a DataFrame
df = pd.DataFrame({
    "Product Name": Prod_Name,
    "Price": Prod_Price,
    "Description": Prod_Description
})

df.to_csv("flipkart_laptops_under_50000.csv")
