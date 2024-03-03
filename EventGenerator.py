import random
import numpy as np
import requests
import json
import config


# List of drinks and names
drinks = ["Double Xp", "Triple Xp", "half a pint of sours is -20", "Use of funnel/snorkel encouraged", 
          "Each house member/attende must do a web This weekend, if not +30", "8 pints before 8 each missed is 2",
          "no drinking with your hands", "Everyone present must immediatly do a shot/down drink","invite ben",
          "Drinking Buddy","International Drinking rules","+40 percentage shots only ","anything but a glass",
          "People drinking with the same type of drink must drink together, e.g mugs are mates", "Tom does a shot", "Olly does a shot", "Jake does a shot", "Bence does a shot", "Oliver does a shot","first person and you drink"]

names = ["Jake", "Bence", "Oliver", "Tom","Olly"]  # Add your names here

# Function to select random drinks
def select_random_drinks():
    num_drinks = np.random.choice([3, 4, 5, 6, 7], p=[0.5, 0.2, 0.15, 0.1, 0.05])  # Adjust probabilities as needed
    selected_drinks = random.sample(drinks, num_drinks)
    return selected_drinks

# Function to select two random names
def select_two_random_names():
    selected_names = random.sample(names, 2)
    return selected_names

# Function to send message to discord
def send_discord_message(message_content):
    webhook_url = config.webhook_url
    data = {
        'content': message_content
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f'Error: {err}')
    else:
        print('Payload delivered successfully, code {}.'.format(response.status_code))

# Main function to handle user input and call other functions
def main():
    handle_drinks_time()
#     while True:
#         user_input = input("\n\nEnter a command: ")
#         if user_input.lower() == "drinks time":
#             handle_drinks_time()
#         elif user_input.lower() == "edit":
#             handle_edit()
#         elif user_input.lower() == "exit":
#             break
#         else:
#             print("\nInvalid command")

# Function to select a random name
def select_random_name():
    return random.choice(names)

# Function to handle 'drinks time' command
def handle_drinks_time():
    selected_drinks = select_random_drinks()
    message = "\n\nWhats happening this weekend???\n"
    for i, drink in enumerate(selected_drinks, 1):
        message += f"{i}. {drink}\n"
    if "Double Xp" in selected_drinks and "Triple Xp" in selected_drinks:
        message += "\nNote: Double Xp and Triple Xp together means Quadrupled Xp!\n"
    if "Drinking Buddy" in selected_drinks:
        selected_names = select_two_random_names()
        message += f"\nSpecial Event: {selected_names[0]} is a drinking Buddy and {selected_names[1]} is the master!\n"
    speaker = select_random_name()
    message += f"\n{speaker} is on the speaker this weekend!\n"
    print(message)
    send_discord_message(message)

# Function to handle 'edit' command
def handle_edit():
    print("\nCurrent drinks:")
    for i, drink in enumerate(drinks, 1):
        print(f"{i}. {drink}")
    new_drink = input("\nEnter a new drink: ")
    drinks.append(new_drink)
    print("\nUpdated drinks:")
    for i, drink in enumerate(drinks, 1):
        print(f"{i}. {drink}")

# Call the main function
if __name__ == "__main__":
    main()