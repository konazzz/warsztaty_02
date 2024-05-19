from random import randint

random_numbs = []

for i in range(6):
    one_of_6 = randint(0, 50)
    if one_of_6 not in random_numbs:
        random_numbs.append(one_of_6)
    else:
        continue

print(random_numbs)

guessed = False

while guessed is not True:
    your_guess = input("input 6 numbers: ")
    your_list = your_guess.split()

    try:
        for i in your_list:
            i = int(i)
            if len(your_list) == 6:
                pass
            else:
                raise IndexError
    except ValueError:
        print("some of those aren't numbers")
        continue
    except IndexError:
        print("wrong amount of numbers")
        continue


    how_many =[]

    for i in your_list:
        i = int(i)
        if i in random_numbs:
            how_many.append(i)

    print(how_many)

    if len(how_many) < 3:
        print("didn't guess. try again")
        continue
    elif len(how_many) == 3:
        print("guessed 3!")
        guessed = True
    elif len(how_many) == 4:
        print("guessed 4!")
        guessed = True
    elif len(how_many) == 5:
        print("guessed 5!")
        guessed = True
    elif len(how_many) == 6:
        print("guessed 6!")
        guessed = True
