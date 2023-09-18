import requests
from bs4 import BeautifulSoup
import json
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

url = "https://www.baseball-reference.com/leagues/MLB/2023.shtml"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
# Find the table within the tbody
tbody = soup.find("tbody")
if not tbody:
    print("No tbody found.")
    exit()

rows = tbody.find_all("tr")

data_list = []

for row in rows:
    columns = row.find_all("td")
    if len(columns) >= 28:  # Ensure the row has enough columns
        team_name = row.select_one('th.left a')
        if team_name:
            team_name = team_name.text.strip()
        else:
            team_name = ""


        batters_used = columns[0].text.strip()
        batting_age = columns[1].text.strip()
        runs_per_game = columns[2].text.strip()
        games_played = columns[3].text.strip()
        plate_appearances = columns[4].text.strip()
        at_bats = columns[5].text.strip()
        runs_scored = columns[6].text.strip()
        hits = columns[7].text.strip()
        doubles = columns[8].text.strip()
        triples = columns[9].text.strip()
        home_runs = columns[10].text.strip()
        rbis = columns[11].text.strip()
        stolen_bases = columns[12].text.strip()
        caught_stealing = columns[13].text.strip()
        bases_on_balls = columns[14].text.strip()
        strikeouts = columns[15].text.strip()
        batting_avg = columns[16].text.strip()
        onbase_perc = columns[17].text.strip()
        slugging_perc = columns[18].text.strip()
        ops = columns[19].text.strip()
        ops_plus = columns[20].text.strip()
        total_bases = columns[21].text.strip()
        double_plays = columns[22].text.strip()
        hit_by_pitch = columns[23].text.strip()
        sac_hits = columns[24].text.strip()
        sac_flies = columns[25].text.strip()
        intentional_bb = columns[26].text.strip()
        left_on_base = columns[27].text.strip()

        numeric_data = [
            batters_used, batting_age, runs_per_game, games_played, plate_appearances,
            at_bats, runs_scored, hits, doubles, triples, home_runs, rbis, stolen_bases,
            caught_stealing, bases_on_balls, strikeouts, batting_avg, onbase_perc,
            slugging_perc, ops, ops_plus, total_bases, double_plays, hit_by_pitch,
            sac_hits, sac_flies, intentional_bb, left_on_base
        ]
        
        numeric_data_decimal = [Decimal(value) for value in numeric_data]

        data_document = {
            "Team": team_name,
            "#Bat": numeric_data_decimal[0],
            "BatAge": numeric_data_decimal[1],
            "R/G": numeric_data_decimal[2],
            "G": numeric_data_decimal[3],
            "PA": numeric_data_decimal[4],
            "AB": numeric_data_decimal[5],
            "R": numeric_data_decimal[6],
            "H": numeric_data_decimal[7],
            "2B": numeric_data_decimal[8],
            "3B": numeric_data_decimal[9],
            "HR": numeric_data_decimal[10],
            "RBI": numeric_data_decimal[11],
            "SB": numeric_data_decimal[12],
            "CS": numeric_data_decimal[13],
            "BB": numeric_data_decimal[14],
            "SO": numeric_data_decimal[15],
            "BA": numeric_data_decimal[16],
            "OBP": numeric_data_decimal[17],
            "SLG": numeric_data_decimal[18],
            "OPS": numeric_data_decimal[19],
            "OPS+": numeric_data_decimal[20],
            "TB": numeric_data_decimal[21],
            "GDP": numeric_data_decimal[22],
            "HBP": numeric_data_decimal[23],
            "SH": numeric_data_decimal[24],
            "SF": numeric_data_decimal[25],
            "IBB": numeric_data_decimal[26],
            "LOB": numeric_data_decimal[27]
        }

        data_list.append(data_document)

# Save the data list as a JSON file
with open("baseball_data.json", "w") as json_file:
    json.dump(data_list, json_file, indent=4, cls=DecimalEncoder)

print("Data saved to JSON file: baseball_data.json")
