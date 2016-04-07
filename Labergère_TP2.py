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
from __future__ import division
from math import *
from random import *
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
        print("DEBUG: " + baseChars[0:base])
        if c not in baseChars[0:base]:
            return False
    return True


def str_is_numeric(string):
    return str_is_int(string) or str_is_float(string)


"""
CHAPITRE 1
"""


#########################
# Exercice 1.1
#########################
def exercise_1_1():
    test_again = True
    while test_again:  # Infinite loop. Will break out when all conditions are verified.
        in_sec = -1
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
        print("")
        answer = raw_input("Voulez-vous tester le programme de nouveau ? (y/n) : ")
        if answer != "y":
            test_again = False
        else:
            print("")


#########################
# Exercice 1.2
#########################
def exercise_1_2():
    test_again = True
    while test_again:  # Infinite loop. Will break out when all conditions are verified.
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
        print("")
        answer = raw_input("Voulez-vous tester le programme de nouveau ? (y/n) : ")
        if answer != "y":
            test_again = False
        else:
            print("")


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
        else:
            print("")


#########################
# Exercice 1.4
#########################
def exercise_1_4():
    test_again = True
    while test_again:  # Infinite loop. Will break out when all conditions are verified.
        grades = list()
        add_grade = True
        while add_grade:
            while True:
                in_grade = raw_input("Entrez une note : ")
                in_weight = raw_input("Entrez le coefficient correspondant : ")
                if not (str_is_numeric(in_grade) and str_is_numeric(in_weight)):
                    print("Les notes et coefficients doivent être des nombres !")
                elif not (0 <= float(in_grade) <= 20):
                    print("Les notes doivent être comprisent entre 0 et 20 !")
                else:
                    grades.append(in_grade + ":" + in_weight)
                    break
            answer = raw_input("Voulez-vous ajouter une autre note ? (y/n) : ") if len(grades) > 1 else "y"
            if answer != "y":
                add_grade = False
        moy = 0
        weights_sum = 0
        for grade_str in grades:
            grade = grade_str.split(":")[0]
            weight = grade_str.split(":")[1]
            moy += float(grade) * float(weight)
            weights_sum += float(weight)
        moy /= weights_sum
        print("La moyenne des " + str(len(grades)) + " notes est de " + ("{0:.2f}".format(moy)))
        print("")
        answer = raw_input("Voulez-vous tester le programme de nouveau ? (y/n) : ")
        if answer != "y":
            test_again = False
        else:
            print("")


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
# Exercice 1.6
#########################
def exercise_1_6():
    test_again = True
    while test_again:  # Infinite loop. Will break out when all conditions are verified.
        a, b, c = 0, 0, 0
        print("Vous allez devoir entrer les réels a, b et c pour former le polynôme \"ax^2 + bx + c\".")
        while True:
            in_a = raw_input("Saisissez a : ")
            in_b = raw_input("Saisissez b : ")
            in_c = raw_input("Saisissez c : ")
            if not (str_is_numeric(in_a) and str_is_numeric(in_b) and str_is_numeric(in_c)):
                print("Vous devez entrer des nombres uniquement !")
            else:
                a, b, c = float(in_a), float(in_b), float(in_c)
                break
        delta = b * b - 4 * a * c
        print("Le discriminant est : Δ = " + "{0:.2f}".format(delta))
        if delta < 0:
            print("Δ < 0 donc aucune racine.")
        elif delta == 0:
            x1 = -b / (2 * a)
            print("Δ = 0 donc une seule racine : x = " + "{0:.2f}".format(x1))
        else:
            x1, x2 = (-b - sqrt(delta)) / (2 * a), (-b + sqrt(delta)) / (2 * a)
            print("Δ > 0 donc deux racines : x1 = " + "{0:.2f}".format(x1) + " et x2 = " + "{0:.2f}".format(x2))
        print("")
        answer = raw_input("Voulez-vous tester le programme de nouveau ? (y/n) : ")
        if answer != "y":
            test_again = False
        else:
            print("")


#########################
# Exercice 1.7
#########################
def exercise_1_7():
    test_again = True
    while test_again:  # Infinite loop. Will break out when all conditions are verified.
        moy = 0
        while True:
            in_moy = raw_input("Saisissez votre moyenne : ")
            if not (str_is_numeric(in_moy) and 0 <= float(in_moy) <= 20):
                print("Vous devez entrer un nombre entre 0 et 20 !")
            else:
                moy = float(in_moy)
                break
        if moy < 10:
            print("Votre moyenne de " + str(moy) + " est inférieure à 10, vous n'êtes pas reçu.")
        elif moy < 12:
            print("Votre moyenne de " + str(moy) + " vous permet d'être reçu sans mention.")
        elif moy < 14:
            print("Votre moyenne de " + str(moy) + " vous permet d'être reçu avec la mentien 'Assez Bien'.")
        elif moy < 16:
            print("Votre moyenne de " + str(moy) + " vous permet d'être reçu avec la mentien 'Bien'.")
        elif moy < 18:
            print("Votre moyenne de " + str(moy) + " vous permet d'être reçu avec la mentien 'Très Bien'.")
        else:
            print("Votre moyenne de " + str(moy) +
                  " vous permet d'être reçu avec la mentien 'Très Bien' et les félicitations du Jury.")
        print("")
        answer = raw_input("Voulez-vous tester le programme de nouveau ? (y/n) : ")
        if answer != "y":
            test_again = False
        else:
            print("")


#########################
# Exercice 1.8
#########################
def exercise_1_8():
    test_again = True
    while test_again:  # Infinite loop. Will break out when all conditions are verified.
        in_width, in_height = 0, 0
        while True:
            in_width = raw_input("Entrez la largeur : ")
            in_height = raw_input("Entrez la hauteur : ")
            if not (str_is_int(in_width) and str_is_int(in_height)):
                print("Vous ne pouvez entrer que des nombres !")
            elif not (0 < int(in_width) <= 80 and 0 < int(in_height) <= 25):
                print("La largeur doit être comprise entre 1 et 80 et la hauteur entre 1 et 25")
            else:
                break
        in_char = "*"
        while True:
            in_char = raw_input("Entrez le caractère à utiliser : ")
            if len(in_char) != 1:
                print("Vous devez entrer un seul caractère !")
            else:
                break
        in_mode = 0
        while True:
            in_mode = raw_input("Sélectionnez le mode (1 = rectangle, 2 = cadre) : ")
            if not (str_is_int(in_mode) and int(in_mode) in (1, 2)):
                print("Le mode sélectionné n'est pas correct !")
            else:
                break
        mode, width, height = int(in_mode), int(in_width), int(in_height)
        if mode == 1:
            print(height * (width * in_char + "\n"))
        else:
            print(width * in_char + "\n" +
                  (height - 2) * (in_char + (width - 2) * " " + in_char + "\n") + width * in_char)
        print("")
        answer = raw_input("Voulez-vous tester le programme de nouveau ? (y/n) : ")
        if answer != "y":
            test_again = False
        else:
            print("")


#########################
# Exercice 1.9
#########################
def exercise_1_9():
    """
                            Erreur d'énoncé
                                  V
    On veut écrire (ax + b)/(cx + d) sous la forme E + R/(cx + d)
    Or E + R/(cx + d) = [ E(cx + d) + R ] / (cx + d) = (Ecx + Ed + R)/(cx + d)
    Par identification, on a :
     * Ecx    = ax
     * Ed + R = b
     Donc E = a/c et R = b-Ed = b - ad/c
    """
    test_again = True
    while test_again:  # Infinite loop. Will break out when all conditions are verified.
        in_a, in_b, in_c, in_d = 0, 0, 0, 0
        while True:
            in_a = raw_input("Entrez a : ")
            in_b = raw_input("Entrez b : ")
            in_c = raw_input("Entrez c : ")
            in_d = raw_input("Entrez d : ")
            if not (str_is_numeric(in_a) and str_is_numeric(in_b) and str_is_numeric(in_c) and str_is_numeric(in_d)):
                print("Vous ne pouvez entrer que des nombres !")
            else:
                break
        a, b, c, d = float(in_a), float(in_b), float(in_c), float(in_d)
        var_e = a / c
        var_r = b - var_e * d
        print("({0}x + {1}) / ({2}x + {3}) peut s'écrire : {4} + {5} / ({2}x + {3})"
              .format(round(a, 2), round(b, 2), round(c, 2), round(d, 2), round(var_e, 2), round(var_r, 2)))
        answer = raw_input("Voulez-vous tester le programme de nouveau ? (y/n) : ")
        if answer != "y":
            test_again = False
        else:
            print("")


"""
CHAPITRE 2
"""


#########################
# Exercice 2.1
#########################
def exercise_2_1():
    test_again = True
    while test_again:  # Infinite loop. Will break out when all conditions are verified.
        in_width, in_height = 0, 0
        while True:
            in_width = raw_input("Entrez la largeur : ")
            in_height = raw_input("Entrez la hauteur : ")
            if not (str_is_int(in_width) and str_is_int(in_height)):
                print("Vous ne pouvez entrer que des nombres !")
            elif not (0 < int(in_width) <= 80 and 0 < int(in_height) <= 25):
                print("La largeur doit être comprise entre 1 et 80 et la hauteur entre 1 et 25")
            else:
                break
        in_char = "*"
        while True:
            in_char = raw_input("Entrez le caractère à utiliser : ")
            if len(in_char) != 1:
                print("Vous devez entrer un seul caractère !")
            else:
                break
        in_mode = 0
        while True:
            in_mode = raw_input("Sélectionnez le mode (1 = rectangle, 2 = cadre) : ")
            if not (str_is_int(in_mode) and int(in_mode) in (1, 2)):
                print("Le mode sélectionné n'est pas correct !")
            else:
                break
        mode, width, height = int(in_mode), int(in_width), int(in_height)
        for h in range(0, height):
            line = ""
            for w in range(0, width):
                if mode == 1 or h == 0 or h == height - 1 or w == 0 or w == width - 1:
                    line += in_char
                else:
                    line += " "
            print(line)
        print("")
        answer = raw_input("Voulez-vous tester le programme de nouveau ? (y/n) : ")
        if answer != "y":
            test_again = False
        else:
            print("")


#########################
# Exercice 2.2
#########################
def exercise_2_2():
    test_again = True
    while test_again:  # Infinite loop. Will break out when all conditions are verified.
        in_size = 0
        while True:
            in_size = raw_input("Entrez la taille du modèle : ")
            if not (str_is_int(in_size) and 0 < int(in_size)):
                print("La taille doit être un entier strictement positif !")
            else:
                break
        in_char = "*"
        while True:
            in_char = raw_input("Entrez le caractère à utiliser : ")
            if len(in_char) != 1:
                print("Vous devez entrer un seul caractère !")
            else:
                break
        in_model = 0
        while True:
            in_model = raw_input("Sélectionnez le modèle (1 à 4) : ")
            if not (str_is_int(in_model) and int(in_model) in range(1, 5)):
                print("Le modèle sélectionné n'est pas correct !")
            else:
                break
        model, size = int(in_model), int(in_size)
        print("")
        if model == 1:
            for i in range(1, size + 1):
                print((size - i) * " " + i * in_char)
        elif model == 2:
            for i in range(size, 0, -1):
                print(i * in_char)
        elif model == 3:
            for i in range(1, size + 1):
                print((size - i) * " " + (i * 2 - 1) * in_char + (size - i) * " ")
        else:
            for i in range(1, size + 1):
                print(i * in_char)
            for i in range(size - 1, 0, -1):
                print(i * in_char)
        print("")
        answer = raw_input("Voulez-vous tester le programme de nouveau ? (y/n) : ")
        if answer != "y":
            test_again = False
        else:
            print("")


#########################
# Exercice 2.3
#########################
def exercise_2_3():
    test_again = True
    while test_again:  # Infinite loop. Will break out when all conditions are verified.
        while True:
            in_x = raw_input("Entrez la valeur de x : ")
            if not (str_is_numeric(in_x)):
                print("x doit être un nombre !")
            else:
                break
        x = abs(float(in_x))
        log_fct_result = log10(x)
        magnitude = 0
        print("")
        while x >= 10:
            x //= 10
            magnitude += 1
        print("L'ordre de grandeur de " + in_x + " est : 10^" + str(magnitude))
        print("La valeur retournée par la fonction 'log10' du module 'math' est : {0:.5f}".format(log_fct_result) +
              ("-" if log_fct_result < round(log_fct_result, 5) else "+"))
        print("Le résultat est donc vérifié !" if magnitude == int(log_fct_result)
              else "Il semble donc qu'il y ai eu un problème...")
        print("")
        answer = raw_input("Voulez-vous tester le programme de nouveau ? (y/n) : ")
        if answer != "y":
            test_again = False
        else:
            print("")


#########################
# Exercice 2.4
#########################
def exercise_2_4():
    test_again = True
    while test_again:  # Infinite loop. Will break out when all conditions are verified.
        while True:
            in_a = raw_input("Entrez la valeur de a : ")
            in_b = raw_input("Entrez la valeur de b : ")
            if not (str_is_int(in_a) and str_is_int(in_b)):
                print("a et b doivent être des entiers !")
            else:
                break
        ppcm = None
        a, b, i = int(in_a), int(in_b), 1
        while ppcm is None:
            if modf(i / float(a))[0] == modf(i / float(b))[0] == 0:
                ppcm = i
            else:
                i += 1
        print("Le PPCM de " + in_a + " et " + in_b + " est " + str(ppcm) +
              " (" + str(ppcm / a) + "x" + in_a + " et " + str(ppcm / b) + "x" + in_b + ")")
        print("")
        answer = raw_input("Voulez-vous tester le programme de nouveau ? (y/n) : ")
        if answer != "y":
            test_again = False
        else:
            print("")


#########################
# Exercice 2.5
#########################
def exercise_2_5():
    test_again = True
    while test_again:  # Infinite loop. Will break out when all conditions are verified.
        while True:
            in_n = raw_input("Entrez la valeur de n : ")
            if not (str_is_int(in_n) and int(in_n) >= 0):
                print("n doit être un nombre !")
            else:
                break
        n = int(in_n)
        n_fact, n_sum, n_is_prime, div = 1, 0, True, 0
        for i in range(1, n + 1):
            n_fact *= i
            n_sum += i
            if n_is_prime and i != 1 and i != n and modf(float(n) / i)[0] == 0:
                n_is_prime = False
                div = i
        print(in_n + "! = " + str(n_fact))
        print("Somme des entiers de " + ("0" if n == 0 else "1") + " à " + in_n + " : " + str(n_sum))
        print(in_n + (" est premier." if n_is_prime else " n'est pas premier. (divisible par " + str(div) + ")"))
        print("")
        answer = raw_input("Voulez-vous tester le programme de nouveau ? (y/n) : ")
        if answer != "y":
            test_again = False
        else:
            print("")


#########################
# Exercice 2.6
#########################
def exercise_2_6():
    test_again = True
    while test_again:  # Infinite loop. Will break out when all conditions are verified.
        in_n = ""
        while True:
            in_n = raw_input("Entrez le nombre de lancé à effectuer : ")
            if not (str_is_int(in_n) and int(in_n) > 0):
                print("n doit être un nombre positif !")
            else:
                break
        n = int(in_n)
        results = dict()
        for i in range(0, n):
            results[i] = randint(2, 12)
        print(results.values())
        print("")
        answer = raw_input("Voulez-vous tester le programme de nouveau ? (y/n) : ")
        if answer != "y":
            test_again = False
        else:
            print("")


#########################
# Exercice 2.7
#########################
def exercise_2_7():
    to_999, to_9999 = 0, 0
    for i in range(1, 1000):
        if i < 1000:
            to_999 += str(i).count("1")
        to_9999 += str(i).count("1")
    print("Il y a " + str(to_999) + " '1' dans les nombres de 1 à 999 et " + str(to_9999) + " dans ceux de 1 à 9999.")
    print("")


#########################
# Exercice 2.8
#########################
def exercise_2_8():
    test_again = True
    while test_again:  # Infinite loop. Will break out when all conditions are verified.
        in_n = ""
        while True:
            in_n = raw_input("Entrez la valeur de n : ")
            if not (str_is_int(in_n) and 0 < int(in_n) <= 100):
                print("n doit être un nombre positif compris entre 1 et 100 !")
            else:
                break
        n = int(in_n)
        max_mult = int(ceil(100 // n))
        for mult in range(0, min(10, max_mult)):
            m = mult
            line = ""
            while True:
                if m > max_mult:
                    break
                line += (("{0:" + str(len(in_n)) + "} x {1:" + str(len(str(m))) + "} = {2:3}     ")
                         .format(n, m, n * m))
                m += 10
            print(line)
        print("")
        answer = raw_input("Voulez-vous tester le programme de nouveau ? (y/n) : ")
        if answer != "y":
            test_again = False
        else:
            print("")


#########################
# Exercice 2.9
#########################
def exercise_2_9():
    n = 1
    while True:
        frac_sum = 0
        for k in range(1, n + 1):
            frac_sum += 1 / k
        if frac_sum >= 5:
            break
        n += 1
    print("Le plus petit entier n non nul vérifiant 'somme(1/k, k : (1 -> n)) >= 5' est : n = " + str(n))


#########################
# Exercice 2.10
#########################
def exercise_2_10():
    test_again = True
    while test_again:  # Infinite loop. Will break out when all conditions are verified.
        in_n = ""
        while True:
            in_n = raw_input("Entrez la valeur de n : ")
            if not (str_is_int(in_n) and int(in_n) > 0):
                print("n doit être un nombre positif !")
            else:
                break
        n = int(in_n)
        if n < 2:
            n_fib = 1
        else:
            fibonacci = [1, 1]
            for i in range(2, n):
                fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])
            print(fibonacci)
            n_fib = fibonacci[n - 1]
        print("Le " + str(n) + ("er" if n == 1 else "ème") + " terme de la suite de Fibonacci est : " +
              str(n_fib) + "\n")
        answer = raw_input("Voulez-vous tester le programme de nouveau ? (y/n) : ")
        if answer != "y":
            test_again = False
        else:
            print("")


#########################
# Exercice 2.11
#########################
def exercise_2_11():
    test_again = True
    while test_again:  # Infinite loop. Will break out when all conditions are verified.
        in_nb = ""
        in_base = ""
        to_base = ""
        while True:
            in_nb = str(raw_input("Entrez un nombre brut, sans indication de base : "))
            in_base = raw_input("En quelle base avez-vous entré votre nombre ? ")
            to_base = raw_input("En quelle base voulez-vous le convertir ? ")
            if not (2 <= int(in_base) <= 36 and 2 <= int(to_base) <= 36 and str_is_base(in_nb, int(in_base))):
                print("Vous devez entrer un nombre quelconque et des bases entre 2 et 36 !")
            else:
                break
        from_base, to_base = int(in_base), int(to_base)
        base10_value = 0
        for i in range(len(in_nb)):
            base10_value += baseChars.find(in_nb[i]) * (from_base ** (len(in_nb) - 1 - i))
        result = ""
        while base10_value >= to_base:
            result = baseChars[base10_value % to_base] + result
            base10_value //= to_base
        result = baseChars[base10_value] + result
        print("La valeur de {} (base {}) en base {} est : {}\n".format(in_nb, in_base, to_base, result))
        answer = raw_input("Voulez-vous tester le programme de nouveau ? (y/n) : ")
        if answer != "y":
            test_again = False
        else:
            print("")


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


main()
