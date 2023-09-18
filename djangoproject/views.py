from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
import requests
from bs4 import BeautifulSoup
import re
from .models import Stats
from decimal import Decimal
from django.shortcuts import HttpResponse
from prediction.models import Prediction

url = "https://www.baseball-reference.com/leagues/MLB-schedule.shtml"

def results(request):
    return render(request, 'results.html')

def home(request):
    if request.method == "POST":
        email = request.POST["email"]
        password1 = request.POST["password"]
        signup_login = request.POST["signup_login"]

        if signup_login == "signup":
            password2 = request.POST["confirm_password"]
            if password1 == password2:
                # Create a new user
                user = User.objects.create_user(
                    username=email, email=email, password=password1
                )
                login(request, user)
                return redirect("stats")
            else:
                return render(
                    request, "index.html", {"error_message": "Passwords do not match."}
                )

        if signup_login == "login":
            user = authenticate(request, username=email, password=password1)
            if user is not None:
                login(request, user)
                return redirect("stats")
        else:
            messages.error(request, "Invalid email or password.")
    return render(request, "index.html")


@login_required(login_url="home")
def logout_(request):
    logout(request)
    return redirect("home")


@login_required(login_url="home")
def stats(request):
    team1_db = ""
    team2_db = ""
    try:
        team1_db = Stats.objects.get(team_name = request.GET.get("team1"))
        team2_db = Stats.objects.get(team_name = request.GET.get("team2"))
    except Exception as e:
        print(e)
       
    context_arr = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    game_elements = soup.find_all("p", class_="game")
    for game in game_elements:
        date = game.find_previous("h3").text.strip()

        teams = game.find_all("a")
        team1 = teams[0].text
        score1 = score1 = re.search(r"\d+", teams[0].find_next("strong").text).group()
        team2 = teams[1].text
        # score2 = re.search(r"\d+", teams[1].find_next("strong").text).group()

        boxscore_link = game.find("a", href=True)["href"]
        boxscore_url = f"https://www.baseball-reference.com{boxscore_link}"  # Remove /leagues/MLB-schedule.shtml

        context = {
            "date": date,
            "team1": team1,
            "team2": team2,
            "score1": score1,
            # "score2": score2,
        }

        context_arr.append(context)


    return render(request, "stats.html", {"context_arr": context_arr, "team1": team1_db, "team2": team2_db})


def update_stats_data(request):
    # URL and parsing logic...
    # Stroring the stats data in the database
    # URL of the webpage containing the table
    url_stats = "https://www.baseball-reference.com/leagues/MLB/2023.shtml"

    # Send a GET request to the URL
    response = requests.get(url_stats)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table within the tbody
    tbody = soup.find("tbody")
    if not tbody:
        print("No tbody found.")

    # Find all rows (tr elements) within the tbody
    rows = tbody.find_all("tr")

    # Loop through each row and extract specific data for each column

    for row in rows:
        columns = row.find_all("td")
        if len(columns) >= 28:
            team_name = row.select_one("th.left a")
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
                batters_used,
                batting_age,
                runs_per_game,
                games_played,
                plate_appearances,
                at_bats,
                runs_scored,
                hits,
                doubles,
                triples,
                home_runs,
                rbis,
                stolen_bases,
                caught_stealing,
                bases_on_balls,
                strikeouts,
                batting_avg,
                onbase_perc,
                slugging_perc,
                ops,
                ops_plus,
                total_bases,
                double_plays,
                hit_by_pitch,
                sac_hits,
                sac_flies,
                intentional_bb,
                left_on_base,
            ]

            numeric_data_decimal = [Decimal(value) for value in numeric_data]

            try:
                existing_stats = Stats.objects.get(team_name=team_name)
                # Update existing record
                existing_stats.batters_used = numeric_data[0]
                existing_stats.batting_age = numeric_data[1]
                existing_stats.runs_per_game = numeric_data[2]
                existing_stats.game_played = numeric_data[3]
                existing_stats.plate_appearances = numeric_data[4]
                existing_stats.at_bats = numeric_data[5]
                existing_stats.run_scored = numeric_data[6]
                existing_stats.hits = numeric_data[7]
                existing_stats.doubles = numeric_data[8]
                existing_stats.triples = numeric_data[9]
                existing_stats.home_runs = numeric_data[10]
                existing_stats.rbis = numeric_data[11]
                existing_stats.stolen_bases = numeric_data[12]
                existing_stats.caught_stealing = numeric_data[13]
                existing_stats.bases_on_balls = numeric_data[14]
                existing_stats.strikeouts = numeric_data[15]
                existing_stats.batting_avg = numeric_data[16]
                existing_stats.onbase_perc = numeric_data[17]
                existing_stats.slugging_perc = numeric_data[18]
                existing_stats.ops = numeric_data[19]
                existing_stats.ops_plus = numeric_data[20]
                existing_stats.total_bases = numeric_data[21]
                existing_stats.double_plays = numeric_data[22]
                existing_stats.hit_by_pitch = numeric_data[23]
                existing_stats.sac_hits = numeric_data[24]
                existing_stats.sac_flies = numeric_data[25]
                existing_stats.floatentional_bb = numeric_data[26]
                existing_stats.left_on_base = numeric_data[27]
                existing_stats.save()
            except Stats.DoesNotExist:
                # Create a new record
                new_stats = Stats(
                    team_name=team_name,
                    batters_used=numeric_data[0],
                    batting_age=numeric_data[1],
                    runs_per_game=numeric_data[2],
                    game_played=numeric_data[3],
                    plate_appearances=numeric_data[4],
                    at_bats=numeric_data[5],
                    run_scored=numeric_data[6],
                    hits=numeric_data[7],
                    doubles=numeric_data[8],
                    triples=numeric_data[9],
                    home_runs=numeric_data[10],
                    rbis=numeric_data[11],
                    stolen_bases=numeric_data[12],
                    caught_stealing=numeric_data[13],
                    bases_on_balls=numeric_data[14],
                    strikeouts=numeric_data[15],
                    batting_avg=numeric_data[16],
                    onbase_perc=numeric_data[17],
                    slugging_perc=numeric_data[18],
                    ops=numeric_data[19],
                    ops_plus=numeric_data[20],
                    total_bases=numeric_data[21],
                    double_plays=numeric_data[22],
                    hit_by_pitch=numeric_data[23],
                    sac_hits=numeric_data[24],
                    sac_flies=numeric_data[25],
                    floatentional_bb=numeric_data[26],
                    left_on_base=numeric_data[27],
                )
                new_stats.save()

    return HttpResponse("Update successful, kindly check the database")


@login_required(login_url="home")
def savePrediction(request):
    if request.method == "POST":
        #teams name
        team1 = request.POST.get("team1")
        team2 = request.POST.get("team2")
        #Left
        rdLeft = request.POST.get("rdLeft")
        eraLeft = request.POST.get("eraLeft")
        fipLeft = request.POST.get("fipLeft")
        lobLeft = request.POST.get("lobLeft")
        whipLeft = request.POST.get("whipLeft")
        obpLeft = request.POST.get("obpLeft")
        slgLeft = request.POST.get("slgLeft")
        percentageLeft = request.POST.get("percentageLeft")
        baLeft = request.POST.get("baLeft")
        
        #Right
        rdRight = request.POST.get("rdRight")
        eraRight = request.POST.get("eraRight")
        fipRight = request.POST.get("fipRight")
        lobRight = request.POST.get("lobRight")
        whipRight = request.POST.get("whipRight")
        obpRight = request.POST.get("obpRight")
        slgRight = request.POST.get("slgRight")
        baRight = request.POST.get("baRight")
        percentageRight = request.POST.get("percentageRight")
        
       
        if team1 is not "" or team2 is not "":
            new_prediction = Prediction.objects.create(
                user = request.user,
                team1 = team1,
                team2 = team2,
                rdLeft = rdLeft,
                eraLeft = eraLeft,
                fipLeft = fipLeft,
                lobLeft = lobLeft,
                whipLeft = whipLeft,
                obpLeft = obpLeft,
                slgLeft = slgLeft,
                percentageLeft =percentageLeft,
                baLeft = baLeft,
                #Right code

                rdRight = rdRight,
                eraRight = eraRight,
                fipRight = fipRight,
                lobRight = lobRight,
                whipRight = whipRight,
                obpRight = obpRight,
                slgRight = slgRight,
                baRight = baRight,
                percentageRight = percentageRight
            )
            new_prediction.save()
        else:
            return HttpResponse("Please select a match")
        
        return HttpResponse("saved")  