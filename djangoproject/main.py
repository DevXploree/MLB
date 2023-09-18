import requests
import csv
from bs4 import BeautifulSoup
import re

def get_game_data_by_date(input_date):
    url = "https://www.baseball-reference.com/leagues/MLB-schedule.shtml"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    game_elements = soup.find_all("p", class_="game")

    game_data = []

    for game in game_elements:
        date = game.find_previous("h3").text.strip()
        if input_date == date:
            teams = game.find_all("a")
            team1 = teams[0].text.strip()
            score1 = re.search(r"\d+", teams[0].find_next("strong").text).group()
            team2 = teams[1].text.strip()
            score2 = re.search(r"\d+", teams[1].find_next("strong").text).group()

            boxscore_link = game.find("a", href=True)["href"]
            boxscore_url = f"https://www.baseball-reference.com{boxscore_link}"

            game_data.append([date, f"{team1} ({score1}) @ {team2} ({score2})", boxscore_url])

    if not game_data:
        print(f"No games found for {input_date}")
        return

    csv_filename = f"mlb_games_{input_date}.csv"

    with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Game", "Boxscore Link"])
        writer.writerows(game_data)

    print(f"Data saved to {csv_filename}.")


if __name__ == "__main__":
    date_to_search = input("Enter the date (YYYY-MM-DD) to get MLB game data: ")
    get_game_data_by_date(date_to_search)
