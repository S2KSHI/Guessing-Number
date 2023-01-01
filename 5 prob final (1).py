import random


def alpha_checker1():
    while True:
        a = input("Enter the lower limit: ")
        if a.isdigit():
            a = int(a)
            if a >= 0:
                break
        else:
            print("Please enter a number.")

    return a


def alpha_checker2():
    while True:
        b = input("Enter the upper limit: ")
        if b.isdigit():
            b = int(b)
            if b >= 0:
                break
        else:
            print("Please enter a number.")

    return b


def main():
    l_check = alpha_checker1()
    u_check = alpha_checker2()
    d = l_check
    e = u_check
    print(f" The selected range is:- ({d}, {e})")

    while True:
        c = random.randint(d, e)
        guess = ""
        guess_count = 0
        guess_limit = 3
        out_of_guesses = False
        initial_score = 0
        guesses_remaining = ""

        while guess != c and not out_of_guesses:

            if guess_count < guess_limit:
                guesses_remaining = (guess_limit - guess_count) - 1
                guess = int(input("Enter your guess: "))
                print(f"Remaining guess = {guesses_remaining}")
                guess_count += 1

                if guess > c and guess_count <= 2:
                    print("Your guess was too high, Try again.")

                elif guess < c and guess_count <= 2:
                    print("Your guess was too Low, Try again.")

                elif guess < c and guess_count == 3:
                    print("Your guess was too Low.")

                elif guess > c and guess_count == 3:
                    print("Your guess was too High.")

            else:
                out_of_guesses = True

        final_score = (guesses_remaining * 5) + 5

        if out_of_guesses:
            print("Out of guesses, You lose")
            print(f"Your score is:- {initial_score} ")
            print(f"The chosen number is:- {c}")
            break

        else:
            print("YAY!! you win!! ")
            print(f"Your score is {final_score}")
            break

    p_a = input("Do you want to play again? Yes/No: ")
    if p_a == "yes" or p_a == "yes":
        main()

    elif p_a == "no" or p_a == "No":
        print("Thank You!")


main()
