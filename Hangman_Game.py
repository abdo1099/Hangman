import random
with open('words.txt') as f:
    words_list = [i.strip('\n') for i in f.readlines()]
lives= 3
word_chosen = random.choice(words_list)
my_board = '-'* len(word_chosen.strip())
print(my_board)
res = list(my_board)
greeting = ['Well Done!', 'Keep UP!', 'Nice Work!', 'Good Job!', 'You are a Rock!','Great!']

while lives != 0 and '-' in res:
    user_input = input('Enter a letter you might think it is in the word: ').lower()
    if user_input in word_chosen:
        if word_chosen.count(user_input) > 1:
            for i in range(len(word_chosen)):
                if user_input == word_chosen[i]:
                    res[i] = user_input
        elif word_chosen.count(user_input) == 1:
            res[word_chosen.index(user_input)] = user_input
        print(''.join(res)) 
        print(random.choice(greeting))
    elif user_input not in word_chosen:
        lives -= 1
        print(f'Sorry this letter not in the word you still have {lives} lives')
else:
    if '-' not in res:
        print('Congrats You Win!')
    elif '-' in res:
        print(f'Sorry You Lose!! The Word chosen was (%s)' % word_chosen)
