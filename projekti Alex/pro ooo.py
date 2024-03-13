import math
import sys
import random
import mysql.connector
import pycountry
import uuid

# Establish database connection
conn = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='flight_game',
    user='root',
    password='12345',
    autocommit=True
)
airport_list = []
name_list = []
# Functions related to database operations
def lento_kenta():
    sql = ("SELECT iso_country, ident, NAME, latitude_deg, longitude_deg FROM airport WHERE ident IN ('EFHK','ESSA','LIRF','LFPG','LOWW','EDDB','EPWA','ENGM','LGAV')")
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def airport_info(icao):
    sql = f"SELECT iso_country, ident, NAME, latitude_deg, longitude_deg FROM airport WHERE ident = '{icao}' LIMIT 1"
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        country_name = conn.get_country(result[0])  # Assuming you have a function to get country name
        return (result[1], result[2], result[3], result[4], country_name)
    else:
        return None

def country_answer(answers):
    sql = f"SELECT option_1, option_2, option_3, option_4 FROM answer WHERE name = '{answers}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return result
    else:
        return None

def correct_option(answer):
    sql = f"SELECT correct_option FROM answer WHERE name = '{answer}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        country_name = result[0]
        return country_name
    else:
        return None

def update_player_location(name, new_location):
    try:
        # Check if the airport exists in the airport table
        if check_airport_existence(new_location):
            sql = "UPDATE game SET location = %s WHERE screen_name = %s"
            cursor = conn.cursor()
            cursor.execute(sql, (new_location, name))
            conn.commit()
            print("Player's location updated successfully!")
        else:
            print("The selected airport does not exist.")
    except mysql.connector.Error as err:
        print(f"Error updating player's location: {err}")

def check_airport_existence(airport_code):
    sql = "SELECT COUNT(*) FROM airport WHERE ident = %s"
    cursor = conn.cursor()
    cursor.execute(sql, (airport_code,))
    count = cursor.fetchone()[0]
    return count > 0

def game(name):
    sql = "SELECT co2_consumed, co2_budget, location FROM game WHERE screen_name = %s"
    cursor = conn.cursor()
    cursor.execute(sql, (name,))
    result = cursor.fetchone()
    print("Player info:", result)  # Add this line to print player info
    if result:
        return result  # Return the result as it is
    else:
        return None

def goal(name):
    sql = "SELECT target_minvalue, target_maxvalue FROM goal WHERE name = %s"
    cursor = conn.cursor()
    cursor.execute(sql, (name,))
    result = cursor.fetchone()
    if result:
        return result  # Return the result as it is
    else:
        return None

def add_new_player(name, co2_consumed, co2_budget, location):
    player_id = uuid.uuid4()  # Generate a random UUID for the player
    sql = "INSERT INTO game (id, screen_name, co2_consumed, co2_budget, location) VALUES (%s, %s, %s, %s, %s)"
    cursor = conn.cursor()
    cursor.execute(sql, (str(player_id), name, co2_consumed, co2_budget, location))
    conn.commit()
def update_budget(name, amount):
    sql = "UPDATE game SET co2_budget = co2_budget - %s WHERE screen_name = %s"
    cursor = conn.cursor()
    cursor.execute(sql, (amount, name))
    conn.commit()

def update_add_money_budget(name, amount):
    sql = "UPDATE game SET co2_budget = %s WHERE screen_name = %s"
    cursor = conn.cursor()
    cursor.execute(sql, (amount, name))
    conn.commit()
def add_money_to_budget(name, amount):
    # Retrieve current budget
    player_info = game(name)
    if player_info:
        co2_consumed, co2_budget, location = player_info
        print(player_info)
        # Update budget with additional amount
        new_co2_budget = co2_budget - amount
        print(new_co2_budget)
        # Update the budget in the database
        update_budget(name, new_co2_budget)
    else:
        return
def correct_answer_money_to_budget(name, increase_amount):
    # Retrieve current budget
    player_info = game(name)
    if player_info:
        co2_consumed, co2_budget, location = player_info
        # Update budget with additional amount
        co2_budget = co2_budget + increase_amount
        print(co2_budget)
        # Update the budget in the database
        update_add_money_budget(name, co2_budget)
    else:
        return





# Function to ask the player if they want to play
def ask_to_play():
    while True:
        answer = input("Do you want to play? (yes/no): ").lower()
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print("Please enter either 'yes' or 'no'.")

# Function to check if the length of a name is valid
def name_length(name):
    if len(name) < 4 or len(name) > 10:
        return False
    else:
        return True

# Function to choose a random airport

# Start of the game
if ask_to_play():
    print("Great! Let's start play!")

    # Player's name input
    name = input("Give your name: ")
    if name_length(name):
        print("Welcome to the game, " + name + "!")
    else:
        print("Okay, see you next time!")
        sys.exit()



    # Check if the player exists in the database
    # Check if the player exists in the database
    player_info = game(name)
    if player_info:
        co2_consumed, co2_budget, location = player_info
        print("Your CO2 consumed:", co2_consumed)
        print("Your CO2 budget:", co2_budget)
        print("Your location:", location)
    else:
        print("No budget information found for the player.")
        # Prompt to add the new player to the database
        while True:  # Loop until a valid input is received
            add_player = input("Do you want to add this player to the game? (yes/no): ").lower()
            if add_player == "yes":
                initial_co2_consumed = 0  # You can set initial CO2 consumed and budget values as per your game design
                initial_co2_budget = 1000
                initial_location = "EFHK"  # You can set an initial location value
                add_new_player(name, initial_co2_consumed, initial_co2_budget, initial_location)
                print("Player added successfully!")
                break  # Exit the loop after successful addition
            elif add_player == "no":
                print("Add failed. See you later.")
                print("Okay, see you next time!")
                sys.exit()  # Exit the program
            else:
                print("Please enter either 'yes' or 'no'.")


    def choose_random_airport():
        airports = lento_kenta()
        chosen_airport = random.choice(airports)
        if chosen_airport[-1] not in airport_list:
            airport_list.append(chosen_airport[-1])
            return chosen_airport
        else:
            return chosen_airport


    # Function to ask the player if they want to play with a randomly chosen airport
    def ask_to_play_with_random_airport():
        random_airport = choose_random_airport()
        if random_airport:
            print("Your random airport:")
            print("Country:", random_airport[0])
            print("Ident:", random_airport[1])
            print("Name:", random_airport[2])
            print("Latitude:", random_airport[3])
            print("Longitude:", random_airport[4])

            # Print the randomly chosen airport identifier
            print("Random Airport Identifier:", random_airport[0])

            while True:
                answer = input("Do you want to play with this airport? (yes/no): ").lower()
                if answer == "yes":
                    # Update player's location to the country of the airport
                    update_player_location(name, random_airport[1])
                    # Deduct budget for choosing a new airport
                    add_money_to_budget(name, 1000-10)  # Adjust the deduction amount as needed
                    return True, random_airport
                elif answer == "no":
                    return False, None
                else:
                    print("Please enter either 'yes' or 'no'.")

    def getQuestion(country):
        sql = "select question from answer where name = " + "'" + country +"'"
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result[-1]



    # Asking to play with a random airport
    play, random_airport = ask_to_play_with_random_airport()

    # Rest of your game logic...

    if play:
        print("Great! Let's start play!")

        # Define a dictionary of questions for each country
        country_questions = {
            'FI': getQuestion("fi"),
            'SE': getQuestion("se"),
            'IT': getQuestion("it"),
            'AT': getQuestion("at"),
            'FR': getQuestion("fr"),
            'PL': getQuestion("pl"),
            'DE': getQuestion("de"),
            'NO': getQuestion("no"),
            'GR': getQuestion("gr")
            # Add more countries and their respective questions as needed
        }

        # Function to get a question for a given country
        def get_question_for_country(country_name):
            if country_name in country_questions:
                questions = country_questions[country_name]
                return random.choice(questions)
            else:
                return None

        # Function to get a question for a random country
        def get_question_for_random_country():
            random_country = random.choice(list(country_questions.keys()))
            return get_question_for_country(random_country)

        # Example usage
        if random_airport[0] in country_questions:
            question = get_question_for_country(random_airport[0])
            if question:
                print("Question for the selected country:")
            else:
                print("No question found for the selected country.")
        else:
            print("No questions available for the selected country.")


        option = country_answer(random_airport[0])  # Assuming random_airport[0] is the country ISO code

        # Function to ask a question and check the answer
        def ask_question_and_check_answer(question, option):
            print(question)
            for idx, opt in enumerate(option, start=1):
                print(f"Option {idx}: {opt}")

            # Get player's answer
            player_answer = input("Your answer (enter the option answer): ")

            # Assuming the correct answer is stored as 'correct_option' in the database
            correct_opt = correct_option(random_airport[0])

            # Check if the player's answer matches the correct option
            if player_answer == correct_opt:
                print("Correct! You get 50 points!")
                increase_amount = 50
                # Update player's budget
                correct_answer_money_to_budget(name, increase_amount)
                # Increase budget by 10 points
            else:
                print("Incorrect.")

            return ask_to_continue()

        # Function to ask if the player wants to continue playing
        # Function to ask if the player wants to continue playing
        def ask_to_continue():
            while True:
                answer = input("Do you want to continue playing? (yes/no): ").lower()
                if answer == "yes":
                    # Deduct a fixed amount from the player's budget
                    deduct_amount = 20  # Adjust the deduction amount as needed
                    update_budget(name, deduct_amount)
                    return True
                elif answer == "no":
                    return False
                else:
                    print("Please enter either 'yes' or 'no'.")


        MINIMUM_BUDGET = 10
        for i in range(10):
            if question:
                continue_playing = ask_question_and_check_answer(question, option)
                if continue_playing:
                    # Check if the player's budget is above the minimum threshold
                    player_info = game(name)
                    if player_info:
                        _, co2_budget, _ = player_info

                        if co2_budget >= MINIMUM_BUDGET:
                            random_airport = choose_random_airport()
                            print(random_airport)
                            if random_airport:
                                print("Your new random airport:")
                                print("Country:", random_airport[0])
                                print("Ident:", random_airport[1])
                                print("Name:", random_airport[2])
                                print("Latitude:", random_airport[3])
                                print("Longitude:", random_airport[4])

                                question = get_question_for_country(random_airport[0])
                                option = country_answer(
                                    random_airport[0])  # Assuming this retrieves options for the question
                            else:
                                print("No more airports available.")
                                print(airport_list)
                                break
                        else:
                            print("You don't have enough money to continue playing.")
                            print("Okay, see you next time!")
                            break
                    else:
                        print("Player information not found.")
                        break
                else:
                    print("Okay, see you next time!")
                    break
            else:
                print("No question found for the selected country.")
                break

        if game(name)[1] > 500:
            print("You won!")
        else:
            print("You lost!")

else:
    print("Okay, see you next time!")