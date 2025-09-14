def ask_question(question: str) -> bool:
    answer = input(f"Question: {question} (y/n)")
    return answer == "y"


def correct():
    print("réponse correcte, Bravo")


def incorrecte():
    print("réponse incorrecte")


def ask_q_a() -> tuple[str, bool]:
    q = input("Entrer votre question: \n")
    a = input("réponse (y/n)") == "y"
    return (q, a)


if __name__ == "__main__":
    dico_q_a = dict()
    correct_as = 0
    while True:
        q, a = ask_q_a()
        dico_q_a[q] = a
        continuer = "y" == input("Questions suplémentaire ? (y/n)")
        if not continuer:
            break
    for q, a in dico_q_a.items():
        u_a = ask_question(q)
        if u_a == a:
            correct()
            a += 1
        else:
            incorrecte()
