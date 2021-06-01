import random   # random module used to generate PC input
import time     # time module to simulate game-like delayed output

lst = ['R', 'P', 'S']  # permitted inputs
user = 0  # initial score of the user
pc = 0  # initial score of the PC
rounds = 10  # total rounds in the game, excluding the tie-breaker


def print_rules():
    """Function to print the game rules"""
    print('------------RULES------------')
    print('-> Choose one of R, P or S for your move')
    print('-> R for Rock, P for Paper and S for Scissors')
    print('-> R wins over S, S wins over P and P wins over R in each round')
    print('-> There are 10 rounds in each game, the player with more wins at the end is the winner')
    print('-> In case of a tie, a final tie-breaker round is played')
    print('-' * 30)


def check_winner(user_choice, pc_choice):
    """Function to check the winner of each round"""
    if user_choice == 'R' and pc_choice == 'S':
        return 1
    elif user_choice == 'R' and pc_choice == 'P':
        return 2
    elif user_choice == 'S' and pc_choice == 'P':
        return 1
    elif user_choice == 'S' and pc_choice == 'R':
        return 2
    elif user_choice == 'P' and pc_choice == 'R':
        return 1
    elif user_choice == 'P' and pc_choice == 'S':
        return 2
    else:
        return 0


def tie_breaker():
    """Function to execute the tie-breaker round, in case of a tie after 10 regular rounds"""
    user_choice = input('Enter R, P or S: ')
    user_choice = user_choice.upper()
    while user_choice not in lst:
        print('Incorrect input, try again')
        user_choice = input('Enter R, P or S:')
        user_choice = user_choice.upper()
    pc_choice = random.choice(lst)
    print(f'You entered {user_choice} and PC entered {pc_choice}')
    winner = check_winner(user_choice, pc_choice)
    if winner == 0:
        print('No winner yet, play again')
        print('-' * 30)
        tie_breaker()
    if winner == 1:
        print('You won the tie-breaker! Congratulations!')
        game_over()
    if winner == 2:
        print('PC won the tie-breaker! Better luck next time!')
        game_over()


def game_result(user, pc):
    """Function to return the game status after 10 rounds"""

    time.sleep(1.25)
    print('Game status after 10 rounds:')
    print(f'User: {user} \nPC: {pc}')
    if user > pc:
        print('You won! Congratulations!')
        print('-' * 30)
        game_over()
    elif pc > user:
        print('PC won! Better luck next time!')
        print('-' * 30)
        game_over()
    else:
        print('Time for tie-breaker')
        print('-' * 30)
        tie_breaker()


def play_round(rounds, user, pc):
    """Function to handle 10 rounds of play"""
    user_choice = input('Enter R, P or S: ')
    user_choice = user_choice.capitalize()
    while user_choice not in lst:
        print('Incorrect input, try again')
        user_choice = input('Enter R, P or S: ')
        user_choice = user_choice.capitalize()
    rounds -= 1
    pc_choice = random.choice(lst)  # PC generates random choice
    print(f'You entered {user_choice} and PC entered {pc_choice}')
    winner = check_winner(user_choice, pc_choice)
    if winner == 0:
        print('No winner this round')
    if winner == 1:
        user += 1
        print('You won this round')
    if winner == 2:
        pc += 1
        print('PC won this round')
    print(f'User: {user} \nPC: {pc}')
    print(f'Rounds left: {rounds}')
    print('-' * 30)
    if rounds > 0:
        play_round(rounds, user, pc)
    else:
        game_result(user, pc)


def game_over():
    s = input('Do you want to play again? (y/n): ')
    s = s.lower()
    if s == 'y':
        play_game()
    else:
        print('Thanks for playing!')
        exit()


def play_game():
    """Function acts like a menu for the user"""
    print('-' * 30)
    print('Welcome to Rock Paper Scissors')
    try:  # checking whether input is an integer
        x = int(input('Enter 1 to Start\nEnter 2 for Rules\nEnter 3 to Exit: '))
        while x < 1 or x > 3:
            print('Incorrect input, try again')
            try:  # checking whether input is an integer
                x = int(input('Enter 1 to Start\nEnter 2 for Rules\nEnter 3 to Exit: '))
                if x == 1:
                    print('-' * 30)
                    play_round(rounds, user, pc)
                if x == 2:
                    print_rules()
                if x == 3:
                    exit()
            except Exception as e:
                print(e)
                game_over()
        if x == 1:
            print('-' * 30)
            play_round(rounds, user, pc)
        if x == 2:
            print_rules()
        if x == 3:
            exit()
    except Exception as e:
        print(e)
    game_over()


play_game()
