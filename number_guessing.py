import random

def get_guess():
    guess = int(input('Come, Guess The Number!: '))
    return guess

def get_tries():
    return 10

def game_over(answer):
    print('Game Over!')
    print(f'The number is {answer}')


def main():
    answer = random.randint(1,100)
    tries_left = get_tries()
    print('A random number has been chosen! Take a guess!')

    while tries_left > 0:
        the_guess = get_guess()

        if the_guess == answer:
            print('Congratulations! You Guessed Right!')
            break

        else:
            print('NOPE, Thats Wrong!')
            if the_guess > answer:
                print('Too High!')
            elif the_guess < answer:
                print('Too Low!')

            tries_left -= 1
            print(tries_left)

        if tries_left == 0:
            game_over(answer)

if __name__ == "__main__":
    main()