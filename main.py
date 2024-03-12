from bs4 import BeautifulSoup
import requests 
import pandas as pd

htmlWork = requests.get('https://www.basketball-reference.com/teams/TOR/2024.html')

soup1 = BeautifulSoup(htmlWork.text, 'html5lib')

players_table = soup1.find('table', {'class': 'stats_table', 'id': 'per_game'})

if players_table:
    # Create lists to store player data
    names = []
    ages = []
    ppgs = []
    # Find all rows in the table
    rows = players_table.find_all('tr')

    # Iterate through each row
    for row in rows[1:]:  # Skip the header row
        # Extract player data from the row
        cells = row.find_all('td')
        player_name = cells[0].text.strip()
        player_age = cells[1].text.strip() 
        player_ppg = cells[26].text.strip()  


        # Append these values onto each array        
        names.append(cells[0].text.strip())
        ages.append(cells[1].text.strip())
        ppgs.append(cells[26].text.strip()) 

         # Create a DataFrame from the lists
        df = pd.DataFrame({'Name': names, 'Age': ages, 'PPG': ppgs})

        # Export DataFrame to CSV file
        df.to_csv('toronto_raptors_2023_2024_ppg.csv', index=False)

        # Print player data on cmdline
        print(f'Name: {player_name}, Age: {player_age}, PPG: {player_ppg}')

else:
    print("Table not found or couldn't retrieve data.")






'''html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3> \
<b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p> \
<h3>Stephen Curry</h3><p> Salary: $85,000,000</p> \
<h3>Kevin Durant</h3><p> Salary: $73,200,000</p></body></html>"

soup = BeautifulSoup(html, 'html5lib')
soup.prettify()

players =  soup.find_all('h3')

for player in players:
    player_name = player.text
    player_salary = player.find_next_sibling('p').text.split()[-1]

    print(f'Name: {player_name} Salary: {player_salary}') 
    '''

