secret_word = 'iris'
guess_count = 0
guess_limit = 2
guess = ''
while guess != secret_word and not (guess_count > guess_limit):
    guess = input('Enter guess: ')
    guess_count += 1
    if guess_count > guess_limit:
        print('you are out of guesses, you lose')
    if guess == secret_word:
        print('You win')
        break
