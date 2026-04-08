from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from player import Player
from player import players


def scrape():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://www.oldcardboard.com/ref/rookies/RookiesList.asp")


    table = driver.find_elements(By.XPATH, "//table")
    rows = table[2].find_elements("tag name", "tr")

    for row in rows[3:-5]:
        cells = row.find_elements("tag name", "td")
        attr = []
        for cell in cells:
            attr.append(cell.text)
            if len(attr)>5:    
                newPlayer = Player(*attr)
                players.append(newPlayer)
    
    driver.quit()

scrape()