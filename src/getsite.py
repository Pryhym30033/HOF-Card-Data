from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from .player import Player
from .player import players


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

    for player in players:
        match player.name:
            case "Pete Alexander":
                player.name = "Grover Cleveland Alexander"
            case "Walt Alston":
                player.name = "Walter Alston"
            case "Raymond Brown":
                player.name = "Ray Brown"
            case "Martin Dihigo":
                player.name = "Martín Dihigo"
            case "Willie Foster":
                player.name = "Bill Foster"
            case "Jimmy Foxx":
                player.name = "Jimmie Foxx"
            case "Frank Frisch":
                player.name = "Frankie Frisch"
            case "Ken Griffey, Jr.":
                player.name = "Ken Griffey Jr."
            case "William Harridge":
                player.name = "Will Harridge"
            case "Bill Herman":
                player.name = "Billy Herman"
            case "Fergie Jenkins":
                player.name = "Ferguson Jenkins"
            case "Tony LaRussa":
                player.name = "Tony La Russa"
            case "Tom LaSorda":
                player.name = "Tommy Lasorda"
            case "Fred Lindstrom":
                player.name = "Freddie Lindstrom"
            case "Al Lopez":
                player.name = "Al López"
            case "Ed Mathews":
                player.name = "Eddie Mathews"
            case "Jose Mendez":
                player.name = "José Méndez"
            case "Satchell Paige":
                player.name = "Satchel Paige"
            case "Tony Perez":
                player.name = "Tony Pérez"
            case "Charles Radbourne":
                player.name = "Charles Radbourn"
            case "Cal Ripken Jr":
                player.name = "Cal Ripken Jr."
            case "Ivan Rodriguez":
                player.name = "Iván Rodríguez"
            case "Cristobal Torriente":
                player.name = "Cristóbal Torriente"
            case "John Ward":
                player.name = "John Montgomery Ward"
            case "Zach Wheat":
                player.name = "Zack Wheat"
            case "Kirby Puckett":
                player.frstYear = "1984"
    