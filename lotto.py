from random import randint

random_numbs = []


guessed = False

while guessed is not True:

    for i in range(6):
        one_of_6 = randint(0, 50)
        if one_of_6 not in random_numbs:
            random_numbs.append(one_of_6)
        else:
            continue

    your_guess = input("input 6 numbers: ")
    your_list = your_guess.split()

    def has_no_duplicates(lst):
        """ checking if input has no duplicates with True or False as a result """
        return len(lst) == len(set(lst))

    try:
        for i in your_list:
            i = int(i)
            if i <= 49 and len(your_list) == 6 and has_no_duplicates(your_list) is True:
                pass
            else:
                raise IndexError
    except ValueError:
        print("some of those aren't numbers")
        continue
    except IndexError:
        print("wrong amount of numbers or some of them are too big")
        continue

    how_many = []
    your_guess_sorted = sorted(your_list)

    for i in your_list:
        i = int(i)
        if i in random_numbs:
            how_many.append(i)

    print(how_many)

    def the_guess(amount):
        """ checking how many numbers have been guessed """
        print(your_guess_sorted)
        print(random_numbs)
        print(f"guessed {amount}!")

    if len(how_many) < 3:
        print(your_guess_sorted)
        print(random_numbs)
        print("didn't guess. try again")
        continue
    elif the_guess(len(how_many)):
        guessed = True

