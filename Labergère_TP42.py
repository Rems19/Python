# -*- coding: utf-8 -*-


#########################
# Labergère
# Rémi
# Groupe 1
# TP 4
#########################


#############################
# Helpers / Utility functions
#############################
from __future__ import division
from math import *
import turtle as t
import sys

# Adding compatibility for Python 3+
version = sys.version.split(" ")[0]
print("")
print("Using Python " + str(version))
if version.startswith("3"):
    print("Adding compatibility functions for Python 3")
    print("")


    def raw_input(string):
        return input(string)

baseChars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def str_is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def str_is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def str_is_base(string, base):
    if not str_is_int(base):
        return False
    for c in string:
        if c not in baseChars[0:base]:
            return False
    return True


def str_is_numeric(string):
    return str_is_int(string) or str_is_float(string)


def cust_round(x, base):
    return int(base * round(float(x) / base))


def print_matrix(matrix):
    print("")
    print(" -" + len(matrix) * " -")
    for i in range(len(matrix)):
        print("| {} |".format(" ".join(str(n) for n in matrix[i])))
    print(" -" + len(matrix) * " -")
    print("")


"""
CHAPITRE 5
"""


#########################
# Exercice 5.1
#########################
def exercise_5_1():
    t.hideturtle()
    t.speed("fastest")
    t.goto(-5, 0)
    t.goto(-5, 10)
    t.goto(-5, -10)
    t.goto(-5, 0)
    t.goto(5, 0)
    t.goto(5, 10)
    t.goto(5, -10)
    t.mainloop()


#########################
# Exercice 5.2
#########################
def exercise_5_2():
    try:
        n = int(raw_input("Nombre de côtés (> 2) : "))  # Pas de verif, on suppose que l'utilisateur est intelligent
        assert(n > 2)
    except:
        print("Un nombre plus grand que 2. C'est pourtant pas compliqué.")
        return
    t.hideturtle()
    t.speed("fastest")
    for i in range(n):
        t.forward(500 / n)
        t.setheading(t.heading() + 360 / n)
    t.up()
    t.goto(0, -50)
    t.write(str(n) + " côtés", True, align="center", font=("Arial", 16, "normal"))
    t.mainloop()


#########################
# Exercice 5.3
#########################
def von_koch(l, n):
    t.forward(l)
    von_koch(l / 3, n - 1)
    t.setheading(t.heading() + 60)
    von_koch(l / 3, n - 1)
    t.setheading(t.heading() - 120)
    von_koch(l / 3, n - 1)
    t.setheading(t.heading() + 60)


#########################
# Main Function
#########################
def main():
    test_again = True
    while test_again:
        ex_to_test = 0
        func_name = ""
        while True:  # Infinite loop. Will break out when all conditions are verified.
            ex_to_test = raw_input("Veuillez entrer le numéro de l'exercice à tester : ")
            func_name = "exercise_" + ex_to_test.replace(".", "_")
            if func_name not in globals():
                print("L'exercice " + ex_to_test + " n'existe pas ou n'a pas encore été traité.")
                print("Liste des exercices disponibles : ")
                exercises = list()
                for func in globals():
                    if "exercise_" not in func:
                        continue
                    exercises.append(func.replace("exercise_", "").replace("_", "."))
                exercises.sort()
                for i in range(0, len(exercises), 2):
                    print(" - " + exercises[i] + ("    - " + exercises[i + 1] if len(exercises) > i + 1 else ""))
                print("")
            else:
                break
        print("")
        print(20 * "#")
        print("# Exercice " + ex_to_test)
        print(20 * "#")
        print("")
        globals()[func_name]()
        print("")
        print(20 * "#")
        print("")
        answer = raw_input("Voulez vous tester un autre exercice ? (y/n) : ")
        if answer != "y":
            test_again = False
        else:
            print("")
    print("Au revoir !")


von_koch(50, 5)
t.mainloop()
# main()
# coded_str = "lujyfwavnyhwoplsljopmmyltluawhykljhshnlhbzzpjvuubjvttlsljopmmylkljlzhyvbsljvklkljlzhylzabult" \
#             "laovklkljopmmyltluaaylzzptwslbapspzllwhyqbslzjlzhykhuzzlzjvyylzwvukhujlzzljylalzslalealjopmm" \
#             "ylzviaplualuyltwshjhuajohxblslaaylkbalealjshpyvypnpuhswhybulslaaylhkpzahujlmpelavbqvbyzkbtlt" \
#             "ljvalkhuzsvykylklshswohilawvbyslzklyuplylzslaaylzkhuzsljhzkbukljhshnlhkyvpalvuylwylukhbkliba" \
#             "whyleltwslhcljbukljhshnlklayvpzclyzshkyvpalhlzayltwshjlwhykiklcpluallahpuzpqbzxbhdxbpklcplua" \
#             "gwbpzeklcpluahlajpszhnpakbulwlytbahapvujpyjbshpylklshswohilashsvunblbykbkljhshnlayvpzkhuzsle" \
#             "ltwsllcvxbljvuzapablshjslkbjopmmyltluaxbpszbmmpaklayhuztlaaylhbklzapuhahpylzpszhpaklqhxbpszh" \
#             "npakbujopmmyltluakljlzhywvbyxbljlsbpjpwbpzzlkljopmmylysltlzzhnlkhuzsljhzklshswohilashapusljo" \
#             "pmmylkljlzhyuhxblcpunazpejslzwvzzpislzfjvtwypzshjslubsslxbpultvkpmplwhzslalealpszhnpakbujhzw" \
#             "hyapjbsplykljopmmyltluawhyzbizapabapvutvuvhswohilapxbljlzzbizapabapvuzylwvzluazbybuwypujpwlh" \
#             "uhsvnblthpzzvuavialublzwhyklzwlytbahapvuzxblsjvuxblzklzslaaylzklshswohilakhuzsljhznlulyhsshj" \
#             "sllzakvuullwhyshwlytbahapvulasluvtiylkljslzwvzzpislzlzahsvyzzhuzjvttbultlzbylhcljjlsbpklzjop" \
#             "mmyltluazkljlzhyjljopmmyltluakljlzhyhwblaylbapspzljvttllsltluakbultlaovklwsbzjvtwsleljvttlsl" \
#             "jopmmylklcpnlulylzlbspsuvmmylhbjbulzljbypalkljvttbupjhapvuhjhbzlkbaylzmhpisluvtiylkljslzjlxb" \
#             "pwlytlaklzzhflyzfzalthapxbltluajlsslzjpxbhukshtlaovklkljopmmyltlualzajvuublthpzhbzzpwhyjlxbl" \
#             "jvttlavbalujvkhnlwhyzbizapabapvutvuvhswohilapxblpswlbalaylaylzyhwpkltluajhzzlwhyhuhsfzlklmyl" \
#             "xblujlzjlyahpulzslaaylzhwwhyhpzzluailhbjvbwwsbzzvbcluaxblslzhbaylzkhuzbulshunbluhabylssl"
# cle = cle_code(coded_str)
# print("Cle : " + str(cle))
# print(decodage_cesar(coded_str, cle))

