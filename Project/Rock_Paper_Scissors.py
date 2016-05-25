import random
import time

#Här är alternativen man kan välja mellan

options = ('Rock', 'Paper', 'Scissors')

#wins = 0
#losses = 0

#Koden för introt

def intro():
    print("Welcome to Rock, Paper, Scissors. Let's begin!")    
    
def start_timer():
    print()
    time.sleep(1)
    print()

def wait():
    time.sleep(.5)
    print(' ') #Jag printar ut mellanrum för att det ska se snyggare ut när man spelar.
    time.sleep(.5)

    
def countdown():
    game_time = 3
    print(game_time)
    wait()
    game_time = game_time - 1
    print(game_time)
    wait()
    game_time = game_time - 1
    print(game_time)
    wait()

#Själva metoden för spelets grund, här bestämmer man när spelaren vinner eller förlorar

def game_on():
    comp = random.choice(options)
    print(' ')
    player_input = input()
    print('_____')
    print('Rock!')
    time.sleep(.5)
    print('Paper!')
    time.sleep(.5)
    print('Scissors!')
    time.sleep(.5)
    print('_____')
    if player_input == comp:
        print('It seems to be a tie!')
        print('Because I also picked', comp)
    else:
        if (player_input != comp and player_input == 'Rock'):
            if comp == 'Scissors':
                print('Ouch!')
                print('You broke my', comp, 'you win!')
                print()
            if comp == 'Paper':
                print('Sorry about that...')
                print('I won with', comp)
                print()
        else:
            if player_input != comp and player_input == 'Paper':
                if comp == 'Rock':
                    print('Well played..')
                    print('It seems I lost with', comp, 'but I will get you next time!')
                    print()
                if comp == 'Scissors':
                    print('My apologies...')
                    print('I won with', comp)
                    print()
            else:
                if player_input != comp and player_input == 'Scissors':
                    if comp == 'Paper':
                        print('You win this time...')
                        print('I had', comp)
                    if comp == 'Rock':
                        print('Oh dear, sorry...')
                        print('I won with', comp)
                else:
                    print('That was not a valid choice, try again please.')
                    game_on()

#Introt ska vara unikt och bara spelas i början av spelet

intro()

#Loopen som ska skapa alternativet att spela igen efter varje runda eller stänga ner spelet

play_again = 'yes'
if play_again == 'yes' or play_again == 'Yes':
    start_timer()
    countdown()
    print('Select one of the three options: Rock, Paper or Scissors (Type Rock, Paper or Scissors)')
    game_on()
    start_timer()
    print('Want a rematch? (Type: "Yes" to play again or Type: "No" to exit')
    play_again = input()
else:
    if play_again == 'no' or play_again == 'No':
        quit()
