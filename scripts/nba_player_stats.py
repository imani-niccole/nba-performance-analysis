# NBA Traditional Stats Scraper by Klara Johnson

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import pandas as pd
import time


# ===============================
# DRIVER SETUP
# ===============================
service = Service(GeckoDriverManager().install())
options = webdriver.FirefoxOptions()

driver = webdriver.Firefox(options=options, service=service)
wait = WebDriverWait(driver, 10)

URL = "https://www.nba.com/stats/players/traditional?SeasonType=Regular+Season"


# ===============================
# DATA EXTRACTION
# ===============================
traditionalPlayerStats = []

try:
    driver.get(URL)

    # Reject cookies when the banner is present.
    try:
        rejectCookiesButton = wait.until(
            EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler"))
        )
        rejectCookiesButton.click()
    except Exception:
        print("Cookie banner not found or already handled.")

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr")))
    time.sleep(3)

    while True:
        # Use the table rows currently visible on the page.
        players = driver.find_elements(By.CSS_SELECTOR, ".Crom_body__PXe4p tr")

        for player in players:
            try:
                playerInfoCells = player.find_elements(By.TAG_NAME, "td")

                # Skip incomplete/non-data rows.
                if len(playerInfoCells) <= 21:
                    continue

                playerData = {
                    "player_name": playerInfoCells[1].text.strip(),
                    "team_name": playerInfoCells[2].text.strip(),
                    "games_played": float(playerInfoCells[4].text.strip()),
                    "minutes_played": float(playerInfoCells[7].text.strip()),
                    "wins": float(playerInfoCells[5].text.strip()),
                    "losses": float(playerInfoCells[6].text.strip()),
                    "pts": float(playerInfoCells[8].text.strip()),
                    "three_pt_percentage": float(playerInfoCells[14].text.strip()),
                    "free_throw_percentage": float(playerInfoCells[17].text.strip()),
                    "REB": float(playerInfoCells[20].text.strip()),
                    "AST": float(playerInfoCells[21].text.strip()),
                }

                traditionalPlayerStats.append(playerData)

            except (ValueError, IndexError) as item_error:
                print("Player row extraction failed:", item_error)
                driver.save_screenshot("error.png")

        # Move to the next page, or stop after the final page.
        nextButton = driver.find_element(
            By.CSS_SELECTOR, "button[title='Next Page Button']"
        )

        if nextButton.get_attribute("disabled"):
            print("Reached the end of the list.")
            break

        nextButton.click()
        time.sleep(1)

except Exception as item_error:
    print("Scraper failed:", item_error)
    driver.save_screenshot("NBATraditionalScraper_error.png")

finally:
    driver.quit()


# ===============================
# DATA CLEANING / EXPORT
# ===============================
cleanTraditionalPlayerStats = []

for player in traditionalPlayerStats:
    cleanTraditionalPlayerStats.append(
        {
            "Player": player.get("player_name"),
            "Team Abbreviation": player.get("team_name"),
            "Games Played": player.get("games_played"),
            "Average Minutes Played": player.get("minutes_played"),
            "Wins": player.get("wins"),
            "Losses": player.get("losses"),
            "Points": player.get("pts"),
            "Three Point Percentage": player.get("three_pt_percentage"),
            "Free Throw Percentage": player.get("free_throw_percentage"),
            "Rebounds": player.get("REB"),
            "Assists": player.get("AST"),
        }
    )

TraditionalPlayerDF = pd.DataFrame(cleanTraditionalPlayerStats)
TraditionalPlayerDF.drop_duplicates(inplace=True)
TraditionalPlayerDF.to_json("PlayerOutput.json", orient="records", indent=1)

print(f"Exported {len(TraditionalPlayerDF)} player records to PlayerOutput.json")
