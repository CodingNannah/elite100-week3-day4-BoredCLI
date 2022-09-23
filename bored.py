from colorizer import *
import ascii_magic
from pyfiglet import figlet_format
import requests
import time

def display(self, cols=100):
    url = "https://www.pngmart.com/image/32119"
    welcome_img = ascii_magic.from_url(self.image, columns=cols)
    ascii_magic.to_terminal(welcome_img)
print(display)

input_cyan("Now entering The Boredom Random Activity Generator!")
time.sleep(3)
clear_screen()

def activity_generator():
    while True:
        try_again = "That was not a proper response. Try again"

        boredom = input_cyan("You're here because you're bored or you're curious.\
            Are you ready to explore a random activity? (Y/N) ")
        
        if boredom.lower() == "n":
            print("Thanks for visiting The Boredom Random Activity Generator!")
            break

        elif boredom.lower() == "y":
            print("Try generating an activity with a monetary value first.")
            
            # min & max prices called below directly in the url
            min_price = input_cyan("What is the minimum you would spend on an \
                activity to alleviate your boredom? (use cents, like this: 0.0 to 0.50): ")
            if min_price != float():
                return try_again
                continue

            max_price = input_cyan("What is the maximum you would spend on an \
                activity to alleviate your boredom? (use cents, like this: 0.50 to 0.99): ")
            if max_price != float():
                return try_again
                continue

            # activity as "type" is called below, directly in url
            activity = input_cyan("Would you like to try generating an activity by type? (Y/N) ")
            if activity.lower() == "n":
                print("Thanks for visiting The Boredom Random Activity Generator!")
                break

            elif activity.lower() == "y":

                ask_type = input_cyan("Is there a particular type of activity you think \
                you might enjoy? Type your choice from: \n\t education \n\t recreational\
                \n\t social \n\t diy \n\t charity \n\t cooking \n\t relaxation \
                \n\t music \n\t OR \n\t busywork: ")
            
                if ask_type.lower() == "education":
                    type = "education"
                elif ask_type.lower() == "recreational":
                    type="recreational"
                elif ask_type.lower() == "social":
                    type="social"
                elif ask_type.lower() == "diy":
                    type="diy"
                elif ask_type.lower() == "charity":
                    type="charity"
                elif ask_type.lower() == "cooking":
                    type="cooking"
                elif ask_type.lower() == "relaxation":
                    type="relaxation"
                elif ask_type.lower() == "music":
                    type="music"
                elif ask_type.lower() == "busywork":
                    type="busywork"
                else:
                    return try_again  
        else:
            print(try_again)
            continue

        go_or_stop = input_cyan("Would you like to try this again? (Y/N) ")

        if go_or_stop.lower() == "n":
            print("Thanks for visiting The Boredom Random Activity Generator!")
            break
        else:
            continue

    # call for Bored url must be down here to define {type}, {min_price}, and {max_price} and stay in front of continue/return
    # must be above the print_color statements to define {data}
    url_bored = f'http://www.boredapi.com/api/activity?type={type}&minprice={min_price}&maxprice={max_price}'
    response = requests.get(url_bored)
    data = response.json()

    # print statements must be last to be defined by the url inside the def
    print_blue(f"Here's your generated activity: {data['activity']}")
    print_red(f"Here's the type of your activity: {data['activity']['type']}")
    print_yellow(f"Here's how many people this activity is meant for:{data['activity']['participants']}")
    print_green(f"Here's the estimated cost of your generated activity: ${data['price']}")
        
print_blue("We hope you enjoyed The Boredom Random Activity Generator! (Y/N) ")
print_yellow(figlet_format("Goodbye!", font = "doh"))

activity_generator()