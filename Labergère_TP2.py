# -*- coding: utf-8 -*-


#########################
# Labergère
# Rémi
# Groupe 1
# TP 2
#########################


#############################
# Helpers / Utility functions
#############################
from math import *
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


def str_is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


#########################
# Exercice 1.1
#########################
def exercise_1_1():
    in_sec = -1  # Initialization of in_sec variable to remove further warnings about undefined variable
    while True:  # Infinite loop. Will break out when all conditions are verified.
        in_sec = raw_input("Veuillez entrer un nombre de secondes à convertir en heures minutes et secondes : ")
        if not str_is_int(in_sec):
            print("Vous devez spécifier un nombre en entrée !")
        elif int(in_sec) < 0:
            print("Vous ne pouvez pas convertir un nombre négatif de secondes !")
        else:
            in_sec = int(in_sec)
            break
    hours = in_sec // 3600
    mins = (in_sec % 3600) // 60
    secs = (in_sec % 3600) % 60
    time_str = ""
    if hours != 0:
        time_str += str(hours) + " heure" + ("s " if hours > 1 else " ")
    if mins != 0:
        time_str += str(mins) + " minute" + ("s et " if mins > 1 else " et ")
    time_str += str(secs) + " seconde" + ("s." if secs > 1 else ".")
    print(str(in_sec) + " seconde" + ("s sont égales" if in_sec > 1 else " est égale") + " à " + time_str)


#########################
# Exercice 1.2
#########################
def exercise_1_2():
    in_radius = -1  # Initialization of in_sec variable to remove further warnings about undefined variable
    while True:  # Infinite loop. Will break out when all conditions are verified.
        in_radius = raw_input("Veuillez préciser un rayon : ")
        if not str_is_int(in_radius):
            print("Vous devez spécifier un nombre en entrée !")
        elif int(in_radius) < 0:
            print("Vous devez entrer un rayon positif !")
        else:
            in_radius = int(in_radius)
            break
    perimeter = 2 * pi * in_radius
    area = pi * (in_radius ** 2)
    print("Un disque de rayon " + str(in_radius) + " a pour propriétés :")
    print(" - Un périmètre de " + str("{0:.2f}".format(perimeter)))
    print(" - Une aire de " + str("{0:.2f}".format(area)))


#########################
# Exercice 1.3
#########################
def exercise_1_3():
    print("Fonction du programme en question : attribuer le maximum de a, b ou c à la variable m.")
    test_again = True
    while test_again:  # Infinite loop. Will break out when all conditions are verified.
        while True:
            in_a = raw_input("Entrez un nombre a : ")
            in_b = raw_input("Entrez un nombre b : ")
            in_c = raw_input("Entrez un nombre c : ")
            a, b, c = 0, 0, 0
            if not (str_is_int(in_a) and str_is_int(in_b) and str_is_int(in_c)):
                print("Vous devez entrer des nombres uniquement !")
            else:
                a, b, c = int(in_a), int(in_b), int(in_c)
                break
        # Tested program
        if a > b:
            if a > c:
                m = a
            else:
                m = c
        else:
            if b > c:
                m = b
            else:
                m = c
        # End of tested program
        print("Maximum retourné par le programme : " + str(m))
        print("")
        answer = raw_input("Voulez-vous tester le programme de nouveau ? (y/n) : ")
        if answer != "y":
            test_again = False


#########################
# Exercice 1.4
#########################
def exercise_1_4():
    test_again = True
    while test_again:  # Infinite loop. Will break out when all conditions are verified.
        a, b, c = 0, 0, 0
        while True:
            in_a = raw_input("Entrez la 1ère note : ")
            in_b = raw_input("Entrez la 2nde note : ")
            in_c = raw_input("Entrez la 3ème note : ")
            if not (str_is_int(in_a) and str_is_int(in_b) and str_is_int(in_c)):
                print("Vous devez entrer des nombres uniquement !")
            elif not (0 < int(in_a) < 20 and 0 < int(in_b) < 20 and 0 < int(in_c) < 20):
                print("Les notes doivent être comprisent entre 0 et 20 !")
            else:
                a, b, c = int(in_a), int(in_b), int(in_c)
                break
        moy = (a + b + c) / 3
        print("La moyenne des 3 notes est de " + ("{0:.2f}".format(moy)))
        print("")
        answer = raw_input("Voulez-vous tester le programme de nouveau ? (y/n) : ")
        if answer != "y":
            test_again = False


#########################
# Exercice 1.5
#########################
def exercise_1_5():
    x, y = 1, 2
    print("#     Exchange with temp variable    #")
    print("Initialement :")
    print(" - x vaut : " + str(x))
    print(" - y vaut : " + str(y))
    temp = x
    x = y
    y = temp
    print("Après échange :")
    print(" - x vaut : " + str(x))
    print(" - y vaut : " + str(y))
    print("")
    x, y = 1, 2
    print("# Exchange with multiple affectation #")
    print("Initialement :")
    print(" - x vaut : " + str(x))
    print(" - y vaut : " + str(y))
    x, y = y, x
    print("Après échange :")
    print(" - x vaut : " + str(x))
    print(" - y vaut : " + str(y))


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
                for ex in sorted(exercises):
                    print(" - " + ex)
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


main()
