# T_20_DATA_ANALYTICS
This project employs data analytics to construct a T20 cricket team that consistently scores 180+ runs and defends against scores below 150. By analyzing player performance and historical data, we aim to strategically form a team capable of securing victories in the fiercely competitive world of T20 cricket.
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2022-23-14450"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    team_names = []
    match_results = []

    # Extract team names
    team_name_elements = soup.find_all("span", class_="mat-TeamText")
    for team_element in team_name_elements:
        team_names.append(team_element.text)

    # Extract match results
    result_elements = soup.find_all("div", class_="score-detail")
    for result_element in result_elements:
        match_results.append(result_element.text.strip())

    # Print the extracted data
    print("Team Names:", team_names)
    print("Match Results:", match_results)

    # Create a DataFrame
    df = pd.DataFrame({"Team": team_names, "Match Result": match_results})

    # Save to CSV
    df.to_csv("t20_world_cup_2022_23_results.csv", index=False)

    print("Data saved to t20_world_cup_2022_23_results.csv.")
else:
    print("Failed to retrieve data. HTTP status code:", response.status_code)
