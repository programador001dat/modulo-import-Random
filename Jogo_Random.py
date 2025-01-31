import os
import random
import pyfiglet


desing_random = pyfiglet.figlet_format("SORTEIO - NUMERICO", font="digital")
desing_ganhar = pyfiglet.figlet_format("ACERTE TODOS PARA GANHAR", font="digital")

os.system("clear")
p1 = [24, 12, 18, 66,]
p2 = [17, 43, 92, 25,]
p3 = [34, 11, 78, 36,]
p4 = [70, 80, 42, 41,]

print(desing_random)
print(f"(1)\t{p1}")
print(f"(2)\t{p2}")
print(f"(3)\t{p3}")
print(f"(4)\t{p4}")

class GamerStart:

    def __on__(self):

        global p1

        segunda_chance = 1
        terceira_chance = 1

        choice_1 = random.choice(p1)
        choice_2 = random.choice(p1)
        choice_3 = random.choice(p1)
        choice_4 = random.choice(p1)
        print(f"\t\t[+1]\t\t|{choice_1}|{choice_2}|{choice_3}|{choice_4}|")

        x_1 = random.choice(p1)
        x_2 = random.choice(p1)
        x_3 = random.choice(p1)
        x_4 = random.choice(p1)

        y_1 = random.choice(p1)
        y_2 = random.choice(p1)
        y_3 = random.choice(p1)
        y_4 = random.choice(p1)

        while segunda_chance:
            press_button = input("\n>> Você tem mais +1 chance.\t>>(S) ou (N)<< : ")
            if press_button == "s":
                print(f"\t\t[+2]\t\t|{x_1}|{x_2}|{x_3}|{x_4}|")
                segunda_chance -=1

            else:
                print(">> Você desistiu :(")
                quit()

        while terceira_chance:
            press_button = input("\n>> Você tem mais +1 chance.\t>>(S) ou (N)<< : ")
            if press_button == "s":
                print(f"\t\t[+3]\t\t|{y_1}|{y_2}|{y_3}|{y_4}|")
                terceira_chance -= 1

            else:
                print(">> Você desistiu :(")
                quit()



    def __two__(self):

        global p2

        segunda_chance = 1
        terceira_chance = 1

        choice_1 = random.choice(p2)
        choice_2 = random.choice(p2)
        choice_3 = random.choice(p2)
        choice_4 = random.choice(p2)
        print(f"\t\t[+1]\t\t|{choice_1}|{choice_2}|{choice_3}|{choice_4}|")

        x_1 = random.choice(p2)
        x_2 = random.choice(p2)
        x_3 = random.choice(p2)
        x_4 = random.choice(p2)

        y_1 = random.choice(p2)
        y_2 = random.choice(p2)
        y_3 = random.choice(p2)
        y_4 = random.choice(p2)

        while segunda_chance:
            press_button = input("\n>> Você tem mais +1 chance.\t>>(S) ou (N)<< : ")
            if press_button == "s":
                print(f"\t\t[+2]\t\t|{x_1}|{x_2}|{x_3}|{x_4}|")
                segunda_chance -=1

            else:
                print(">> Você desistiu :(")
                quit()

        while terceira_chance:
            press_button = input("\n>> Você tem mais +1 chance.\t>>(S) ou (N)<< : ")
            if press_button == "s":
                print(f"\t\t[+3]\t\t|{y_1}|{y_2}|{y_3}|{y_4}|")
                terceira_chance -= 1

            else:
                print(">> Você desistiu :(")
                quit()



    def __three__(self):

        global p3

        segunda_chance = 1
        terceira_chance = 1

        choice_1 = random.choice(p3)
        choice_2 = random.choice(p3)
        choice_3 = random.choice(p3)
        choice_4 = random.choice(p3)
        print(f"\t\t[+1]\t\t|{choice_1}|{choice_2}|{choice_3}|{choice_4}|")

        x_1 = random.choice(p3)
        x_2 = random.choice(p3)
        x_3 = random.choice(p3)
        x_4 = random.choice(p3)

        y_1 = random.choice(p3)
        y_2 = random.choice(p3)
        y_3 = random.choice(p3)
        y_4 = random.choice(p3)

        while segunda_chance:
            press_button = input("\n>> Você tem mais +1 chance.\t>>(S) ou (N)<< : ")
            if press_button == "s":
                print(f"\t\t[+2]\t\t|{x_1}|{x_2}|{x_3}|{x_4}|")
                segunda_chance -=1

            else:
                print(">> Você desistiu :(")
                quit()

        while terceira_chance:
            press_button = input("\n>> Você tem mais +1 chance.\t>>(S) ou (N)<< : ")
            if press_button == "s":
                print(f"\t\t[+3]\t\t|{y_1}|{y_2}|{y_3}|{y_4}|")
                terceira_chance -= 1

            else:
                print(">> Você desistiu :(")
                quit()



    def __four__(self):

        global p4

        segunda_chance = 1
        terceira_chance = 1

        choice_1 = random.choice(p4)
        choice_2 = random.choice(p4)
        choice_3 = random.choice(p4)
        choice_4 = random.choice(p4)
        print(f"\t\t[+1]\t\t|{choice_1}|{choice_2}|{choice_3}|{choice_4}|")

        x_1 = random.choice(p4)
        x_2 = random.choice(p4)
        x_3 = random.choice(p4)
        x_4 = random.choice(p4)

        y_1 = random.choice(p4)
        y_2 = random.choice(p4)
        y_3 = random.choice(p4)
        y_4 = random.choice(p4)

        while segunda_chance:
            press_button = input("\n>> Você tem mais +1 chance.\t>>(S) ou (N)<< : ")
            if press_button == "s":
                print(f"\t\t[+2]\t\t|{x_1}|{x_2}|{x_3}|{x_4}|")
                segunda_chance -=1

            else:
                print(">> Você desistiu :(")
                quit()

        while terceira_chance:
            press_button = input("\n>> Você tem mais +1 chance.\t>>(S) ou (N)<< : ")
            if press_button == "s":
                print(f"\t\t[+3]\t\t|{y_1}|{y_2}|{y_3}|{y_4}|")
                terceira_chance -= 1

            else:
                print(">> Você desistiu :(")
                quit()



    def __player__(self, player):

        if player == "1":
            os.system("clear")
            print(desing_ganhar)
            print(f">> Seu jogo: {p1}\n")
            GamerStart.__on__(self)


        elif player == "2":
            os.system("clear")
            print(desing_ganhar)
            print(f">> Seu Jogo: {p2}\n")
            GamerStart.__two__(self)


        elif player == "3":
            os.system("clear")
            print(desing_ganhar)
            print(f">> Seu Jogo: {p3}\n")
            GamerStart.__three__(self)


        elif player == "4":
            os.system("clear")
            print(desing_ganhar)
            print(f">> Seu Jogo: {p4}\n")
            GamerStart.__four__(self)

        else:
            quit()



if __name__ == "__main__":
    GamerStart.__player__(self=None, player=input("\n(?)Choice(?): "))

