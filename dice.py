import random
import time

def roll():
    dice_choice1 = random.randint(1,6)
    dice_choice2 = random.randint(1,6)
    print('Tossing... ... ...')
    time.sleep(1)
    print(f'The dice rolled..........')
    print(f'***{dice_choice1}***and***{dice_choice2}***')
    return dice_choice1, dice_choice2

def main():
    is_running = True

    while is_running:
        play = input('Do you want to roll the dice? (Y/N): ').upper()
        if play == 'Y':
            roll()
        elif play == 'N':
            break
        else:
            print('Invalid choice')
            continue


if __name__ == '__main__':
    main()
    

