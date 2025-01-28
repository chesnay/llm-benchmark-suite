import random
import time
import json
import os

# Constants
MAX_PLAYERS = 24
MAX_TEAMS = 64
MAX_DIVISIONS = 4

# Initialize game variables with data from the original code
player_names = [
    "P.Shilton", "N.Spink", "P.Thompson", "K.Sansom", "G.McQueen", "A.Martin",
    "R.Osman", "V.Anderson", "R.Wilkins", "G.Mabbutt", "S.Lee", "T.Brooking",
    "B.Robson", "G.Hoddle", "S.Williams", "A.Muhren", "G.Shaw", "K.Dalglish",
    "T.Woodcock", "F.Stapleton", "I.Rush", "C.Nicholas", "N.Whiteside",
    "P.Mariner"
]
team_names = [
    "Arsenal", "Aston V.", "Coventry", "Everton", "Ipswich", "Liverpool", "Luton",
    "Man.Utd.", "Newcastle", "Norwich", "Notts.F.", "Q.P.R.", "Sheff Wed.",
    "Spurs", "Watford", "West Ham", "Blackburn", "Brighton", "Cardiff", "Carlisle",
    "Charlton", "Crystal P.", "Fulham", "Grimsby", "Leeds", "Man.City",
    "Middlesbro", "Notts Co.", "Oldham", "Oxford", "Portsmouth", "Sheff Utd",
    "Bournemouth", "Brentford", "Bristol R.", "Cambridge", "Doncaster", "Hull",
    "Lincoln", "Millwall", "Newport", "Orient", "Plymouth", "Preston", "Reading",
    "Rotherham", "Walsall", "York City", "Blackpool", "Bury", "Colchester",
    "Crewe", "Darlington", "Exeter", "Halifax", "Hartlepool", "Hereford",
    "Mansfield", "Port Vale", "Rochdale", "Scunthorpe", "Stockport", "Southend",
    "Torquay"
]
action_names = ["Energy", "Morale", "Defence", "Midfield", "Attack"]
level_names = [
    "Beginner", "Novice", "Average", "Good", "Expert", "Super-Expert", "Genius"
]

def get_input(prompt, valid_chars=None, max_length=None):
    """Gets user input with optional validation and length checks."""
    while True:
        user_input = input(prompt).upper()
        if valid_chars and any(char not in valid_chars for char in user_input):
            print("Invalid characters entered. Please try again.")
            continue
        if max_length and len(user_input) > max_length:
            print("Input too long. Please try again.")
            continue
        return user_input

def display_menu():
    """Displays the main menu options."""
    print("\nFootball Manager")
    print("Copyright Addictive Games 1984")
    print("\nTO - TYPE -")
    print("Sell/list your players - a")
    print("Print score etc. - s")
    print("Obtain a loan - o")
    print("Pay off loan - p")
    print("Display league table - d")
    print("Change your skill level - l")
    print("Change team or player names - c")
    print("Save game - k")
    print("Restore saved game - r")
    print("Exit - x")

def display_score(money, loan, manager_name, managerial_rating, level,
                 level_name, seasons, team_name, division, league_position,
                 morale, match_number):  # Added match_number as an argument
    """Displays the current score and financial status."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    print("\n*** YOUR CURRENT STATUS ***")
    print("Manager:", manager_name)
    print("Managerial Rating (Max 100):", managerial_rating)
    print("Level:", level, level_name)
    print("Seasons:", seasons)
    print("Team:", team_name)
    print("Division:", division)
    print("League Position:", league_position)
    print("League Match Number:", match_number)  # Display match number
    print("Morale:", morale)
    print("\nMoney in Bank (£):", money)
    print("Money owed (£):", loan)

def obtain_loan(money, loan, division):
    """Allows the user to obtain a loan."""
    print("\n*** OBTAIN A LOAN ***")
    credit_limit = 250000 * (5 - division)
    print("Your credit limit is £", credit_limit)
    while True:
        try:
            loan_amount = int(input("Type loan amount required (£): "))
            if loan_amount + loan > credit_limit:
                print("Loan amount exceeds your credit limit. Please try again.")
            else:
                money += loan_amount
                loan += loan_amount
                print("Loan granted. Your new balance is £", money)
                return money, loan
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def pay_off_loan(money, loan):
    """Allows the user to pay off their loan."""
    print("\n*** PAY OFF LOAN ***")
    while True:
        try:
            pay_amount = int(input("Type amount to pay off (£): "))
            if pay_amount > loan:
                print("You don't owe that much! Please try again.")
            elif pay_amount > money:
                print("You don't have enough money! Please try again.")
            else:
                loan -= pay_amount
                money -= pay_amount
                print("Payment successful. Your remaining loan is £", loan)
                return money, loan
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def change_skill_level(level, level_name):
    """Allows the user to change their skill level."""
    print("\n*** CHANGE SKILL LEVEL ***")
    print("Your present skill level is:")
    print("Level", level, level_name)
    print("\nThe choices are:")
    for i, name in enumerate(level_names):
        print(i + 1, name)
    while True:
        try:
            new_level = int(
                input("Type your new level (1-{}): ".format(len(level_names))))
            if 1 <= new_level <= len(level_names):
                return new_level, level_names[new_level - 1]
            else:
                print("Invalid level. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def change_team_names():
    """Allows the user to change team names."""
    print("\n*** CHANGE TEAM NAMES ***")
    while True:
        division = int(
            input("Choose division to change (1-{}): ".format(MAX_DIVISIONS)))
        if 1 <= division <= MAX_DIVISIONS:
            break
        else:
            print("Invalid division. Please try again.")
    start_index = (division - 1) * 16
    end_index = start_index + 16
    for i, name in enumerate(team_names[start_index:end_index]):
        print(i + 1, name)
    while True:
        try:
            team_index = int(input("Type no. of team to be changed: "))
            if 1 <= team_index <= 16:
                break
            else:
                print("Invalid team number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    new_name = input("Type new team name: ")
    team_names[start_index + team_index - 1] = new_name
    print("Team name changed successfully.")

def change_player_names():
    """Allows the user to change player names."""
    print("\n*** CHANGE PLAYER NAMES ***")
    while True:
        category = int(
            input("Choose category to change (1-3): "))  # 1-3 for D, M, A
        if 1 <= category <= 3:
            break
        else:
            print("Invalid category. Please try again.")
    start_index = (category - 1) * 8
    end_index = start_index + 8
    for i, name in enumerate(player_names[start_index:end_index]):
        print(i + 1, name)
    while True:
        try:
            player_index = int(input("Type no. of player to be changed: "))
            if 1 <= player_index <= 8:
                break
            else:
                print("Invalid player number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    new_name = input("Type new player name: ")
    player_names[start_index + player_index - 1] = new_name
    print("Player name changed successfully.")

def sell_list_players(players, player_names, money):
    """Allows the user to sell or list players."""
    print("\n*** SELL/LIST PLAYERS ***")
    print("p: picked to play, i: injured")
    print(
        "NAME                 NO. SKILL ENERGY VALUE(£) STATUS"
    )  # Adjust spacing as needed
    for i, player in enumerate(players):
        status = " "
        if player["picked"]:
            status = "p"
        elif player["injured"]:
            status = "i"
        print(
            f"{player_names[i]:<12} {i + 1:>3} {player['skill']:>5} {player['energy']:>6} {player['value']:>7} {status}"
        )
    while True:
        try:
            player_index = int(input("Type no. of player to be sold: "))
            if 1 <= player_index <= len(players):
                break
            else:
                print("Invalid player number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    player = players[player_index - 1]
    if player["injured"]:
        print("He is injured - nobody wants him!")
        return
    offer = int(((random.random() * 5 + 8) * player["value"]) / 10)
    print(
        f"Another team has offered £{offer} for {player_names[player_index - 1]}"
    )
    print(f"He is worth £{player['value']}. Do you accept? (y/n)")
    accept = get_input("", valid_chars="YN").lower()
    if accept == "y":
        money += offer
        players[player_index - 1] = {
            "skill": 0,
            "energy": 0,
            "value": 0,
            "picked": False,
            "injured": False
        }
        print("Player sold.")
    else:
        if random.randint(1, 3) == 1:
            return
        players[player_index - 1]["injured"] = True
        print("Player injured.")

def display_league_table(teams, division):
    """Displays the league table for the current division."""
    print("\n*** LEAGUE TABLE ***")
    print("POS TEAM           F   A   PTS")
    division_teams = teams[(division - 1) * 16:division * 16]
    for i, team in enumerate(division_teams):
        print(
            f"{i + 1:>3} {team['name']:<12} {team['for']:>3} {team['against']:>3} {team['points']:>4}"
        )

def save_game(filename, **game_data):
    """Saves the game to a JSON file."""
    print("\n*** SAVE GAME ***")
    try:
        with open(filename, "w") as f:
            json.dump(game_data, f)
        print("Game saved successfully.")
    except Exception as e:
        print("Error saving game:", e)

def restore_saved_game(filename):
    """Restores a saved game from a JSON file."""
    print("\n*** RESTORE SAVED GAME ***")
    try:
        with open(filename, "r") as f:
            game_data = json.load(f)
        print("Game restored successfully.")
        return game_data
    except Exception as e:
        print("Error restoring game:", e)
        return None

def play_match(home_team, away_team, players, player_names, morale, money,
               division):
    """Simulates a football match."""
    print("\n********MATCH HIGHLIGHTS TO FOLLOW******")
    home_attack = 0
    away_attack = 0
    home_score = 0
    away_score = 0

    # Calculate attacking strength based on player skills and morale
    for player in players:
        if player["picked"]:
            if player["skill"] <= 8:
                home_attack += player["skill"]
            else:
                away_attack += player["skill"]
    home_attack = int(home_attack * (morale / 10))
    away_attack = int(away_attack * (morale / 10))

    # Simulate match events
    for _ in range(5):
        if random.randint(1, 100) + home_attack - away_attack > 74:
            home_score += 1
        if random.randint(1, 100) + away_attack - home_attack > 74:
            away_score += 1

    print("\n****FINAL SCORE****")
    print(f"{home_team['name']:<12} {home_score} - {away_score} {away_team['name']}")

    # Update team statistics
    home_team["for"] += home_score
    home_team["against"] += away_score
    away_team["for"] += away_score
    away_team["against"] += home_score
    if home_score > away_score:
        home_team["points"] += 3
    elif home_score == away_score:
        home_team["points"] += 1
        away_team["points"] += 1
    else:
        away_team["points"] += 3

    # Update morale
    morale += int((20 - morale) / 2) if home_score >= away_score else int(
        morale / 2)

    # Update money
    gate_receipts = (17 - away_team["points"]) * division * 500
    money += gate_receipts
    print("Gate receipts: £", gate_receipts)

    return morale, money

def main():
    """Main game loop."""

    # Initialize game variables
    money = 100000
    loan = 0
    managerial_rating = 0
    level = 1
    level_name = level_names[level - 1]
    seasons = 0
    division = 4  # Start in division 4
    league_position = 1  # Initial league position
    morale = 10  # Initial morale
    match_number = 0  # Initialize match_number
    # Initialize player data
    players = [{
        "skill": random.randint(1, 10),
        "energy": random.randint(1, 100),
        "value": random.randint(1000, 100000),
        "picked": False,
        "injured": False
    } for _ in range(MAX_PLAYERS)]
    teams = [{
        "name": team_names[i],
        "for": 0,
        "against": 0,
        "points": 0
    } for i in range(MAX_TEAMS)]

    manager_name = get_input("Type your name: ", max_length=20)

    # --- Choose team ---
    team_display_index = 0  # New variable to track the displayed teams
    while True:
        start_index = team_display_index * 16
        end_index = start_index + 16
        for i, name in enumerate(team_names[start_index:end_index]):
            print(i + 1 + start_index, name)
        while True:
            try:
                team_index = input("Type no. of team to manage: ")
                if not team_index:
                    team_display_index += 1
                    if team_display_index * 16 >= len(team_names):
                        team_display_index = 0
                    break
                team_index = int(team_index)
                if 1 <= team_index <= len(team_names):
                    team_name = team_names[team_index - 1]
                    home_team = {
                        "name": team_name,
                        "for": 0,
                        "against": 0,
                        "points": 0
                    }
                    break
                else:
                    print("Invalid team number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        if team_index:
            break



    # --- Choose skill level ---
    print("\nThe available skill levels are:")
    for i, level_name in enumerate(level_names):
        print(f"{i + 1} - {level_name}")  # Print level number and name

    while True:
        try:
            level = int(input("Type your skill level (1-7): "))
            if 1 <= level <= 7:
                level_name = level_names[level - 1]
                break
            else:
                print("Invalid skill level. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # --- Main game loop ---
    while True:
        display_menu()
        choice = get_input("Enter your choice: ",
                            valid_chars="AOSPLCKRDX").lower()

        if choice == "a":
            sell_list_players(players, player_names, money)
        # Display score (call display_score with match_number)
        if choice == "s":
            display_score(money, loan, manager_name, managerial_rating, level,
                           level_name, seasons, team_name, division,
                           league_position, morale,
                           match_number)  # Pass match_number here
        elif choice == "o":
            money, loan = obtain_loan(money, loan, division)
        elif choice == "p":
            money, loan = pay_off_loan(money, loan)
        elif choice == "d":
            display_league_table(teams, division)
        elif choice == "l":
            level, level_name = change_skill_level(level, level_name)
        elif choice == "c":
            while True:
                sub_choice = get_input(
                    "Change team names (t) or player names (p)? ",
                    valid_chars="TP").lower()
                if sub_choice == "t":
                    change_team_names()
                    break
                elif sub_choice == "p":
                    change_player_names()
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "k":
            # Gather all game data to save
            game_data = {
                "money": money,
                "loan": loan,
                "managerial_rating": managerial_rating,
                "level": level,
                "level_name": level_name,
                "seasons": seasons,
                "division": division,
                "league_position": league_position,
                "morale": morale,
                "team_index": team_index,
                "team_name": team_name,
                "players": players,
                "teams": teams,
                "manager_name": manager_name
            }
            save_game("savegame.json", **game_data)
        elif choice == "r":
            restored_data = restore_saved_game("savegame.json")
            if restored_data:
                # Update game variables with restored data
                money = restored_data["money"]
                loan = restored_data["loan"]
                managerial_rating = restored_data["managerial_rating"]
                level = restored_data["level"]
                level_name = restored_data["level_name"]
                seasons = restored_data["seasons"]
                division = restored_data["division"]
                league_position = restored_data["league_position"]
                morale = restored_data["morale"]
                team_index = restored_data["team_index"]
                team_name = restored_data["team_name"]
                players = restored_data["players"]
                teams = restored_data["teams"]
                manager_name = restored_data["manager_name"]
        elif choice == "x":
            print("Exiting game...")
            break
        else:
            print("Invalid choice. Please try again.")


        # Simulate a match
        if choice not in ["x", "c", "l", "k", "r", "s"]:
            match_number += 1  # Increment match_number
            opponent_index = random.randint(0, 15)
            while opponent_index == team_index:
                opponent_index = random.randint(0, 15)
            away_team = teams[opponent_index]
            morale, money = play_match(home_team, away_team, players,
                                       player_names, morale, money, division)


if __name__ == "__main__":
    main()