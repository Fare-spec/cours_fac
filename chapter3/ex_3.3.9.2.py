# --- Version 1 ---
def ask_number(letter: str):
    return int(input(f"{letter}=? "))


def correct():
    print("réponse correcte, Bravo")
    global number_correct_a
    number_correct_a += 1


def incorrecte():
    print("réponse incorrecte")


def questions():
    while True:
        print("Donner trois entiers :")
        a = ask_number("a")
        b = ask_number("b")
        c = ask_number("b")
        global number_correct_a
        number_correct_a = 0

        print('Jeu du "Vrai ou Faux ?"\n(répondez en tapant V ou F)')
        # ---Q1
        print("Question 1.")
        print(f"{a}<{b}<{c} ?")
        answer = input("")
        if a < b < c and answer == "V":
            correct()
        elif (a < b < c) and answer == "F":
            correct()
        else:
            incorrecte()
        """
        elif:
            print("mauvais format de reponse")
            break
        """
        # ---Q2
        print("Question 2.")
        print(f"Un seul nombre impair parmi {a}, {b}, {c} ?")
        answer = input("")
        if ((a % 2 - 1) ^ (b % 2 - 1) ^ (c % 2 - 1)) and answer == "V":
            correct()
        elif not ((a % 2 - 1) ^ (b % 2 - 1) ^ (c % 2 - 1)) and answer == "F":
            correct()
        else:
            incorrecte()

        """
        elif:
            print("mauvais format de reponse")
            break
        """
        # ---Q3
        print("Question 3")
        print(f"{a},{b},{c} sont-ils distincts deux à deux ?")
        answer = input("")
        if a != b != c != a and answer == "V":
            correct()
        elif not (a != b != c != a) and answer == "F":
            correct()
        else:
            incorrecte()

        # --- Summary:
        print(f"{number_correct_a} bonnes réponse sur 3")
        wanna_play = input("Voulez vous encore jouer ? (y/n)")
        if wanna_play == "n":
            break
    print("Le jeu est terminé : Au revoir !")
