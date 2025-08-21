import random
import time

def spin_row():
    symbols = ['😺', '🦁', '🐷', '🐼', '🐶']

    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results


def print_row(row):
    time.sleep(1)
    print(' | '.join(row))

def payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '😺':
            return bet * 3
        elif row[0] == '🐶':
            return bet * 4
        elif row[0] == '🐷':
            return bet * 5
        elif row[0] == '🐼':
            return bet * 7
        elif row[0] == '🦁':
            return bet * 10
    else:
        return 0


def main():
    balance = 1000

    print('Welcome to Sugalan Simulator!'.center(55))
    print('Symbols: 😺 🦁 🐷 🐼 🐶'.center(50))


    while balance > 0:
        print(f'Your balance is {balance}')
        bet = input('Place an amount to bet ("." for ALL IN): ')
        if bet == '.':
            bet = balance
            print('TAPANG! ALL IN!!!!!!!!!!!!')

        elif bet.isdigit():
            bet = int(bet)
        
        else:
            print("Select a valid amount to bet!")
            continue
        
        row = spin_row()
        balance -= bet
        print('Spinning....\n')
        print_row(row)

        prize = payout(row,bet)
        if prize > 0:
            print(f'CONGRATS! YOU WON ₱{prize}')
        else:
            print('BETTER LUCK NEXT TIME!')

        balance += prize

        play_again = input('Play again???? (Y/N): ').upper()

        if play_again != 'Y':
            break

    print(f'Game Over! Your remaining balance is {balance}')

if __name__ == '__main__':
    main()