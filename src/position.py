from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from .player import *

def position():

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://en.wikipedia.org/wiki/List_of_members_of_the_National_Baseball_Hall_of_Fame")


    table = driver.find_elements(By.XPATH, "//table")
    rows = table[2].find_elements('tag name', 'tr')

    plyerPos = {}
    
    for row in rows[1:]:
        name = row.find_element('tag name', 'th')
        
        posCell = row.find_elements('tag name', 'td')

        plyerPos[name.text] = posCell[1].text
        
    for player in players:
        player.pos = plyerPos[player.name]
    
