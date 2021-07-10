import sys

def calculatrice():
    while True:
        try:
            choix = int(input("1) Addition\n2) Soustraction\n3) Multiplication\n4) Division\n\nChoisissez le type d'opération : "))
            if choix == 1 or choix == 2 or choix == 3 or choix == 4:
                valeur()
                if choix == 1:
                    calcul = int(value1) + int(value2)
                    print("Le resultat de l'addition de ", value1, " avec ", value2, " est égal à ", calcul, "\n")

                if choix == 2:
                    calcul = int(value1) - int(value2)
                    print("Le résultat de la soustraction entre", value1, "et", value2, "est égal à", calcul)

                if choix == 3:
                    calcul = int(value1) * int(value2)
                    print("Le résultat de la multiplication de", value1, "par", value2, "est égal à", calcul)

                if choix == 4:
                    calcul = int(value1) / int(value2)
                    print("Le résultat de la division de", value1, "par", value2, "est égal à", calcul)
                re_start()
                break
        except ValueError:
            print("!!! Choisissez un des 4 chiffres pour effectuer une opération !!!\n")
            continue


def re_start():
    inpt = str(input("\nVoulez-vous refaire un autre calcul ?  (oui ou non)\n"))
    if inpt.lower() == "oui":
        print("")
        calculatrice()
    elif inpt.lower() == "non":
        sys.exit()
    else:
        re_start()


def valeur():
    while True:
        try:
            global value1
            value1 = int(input("Enter le premier nombre : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre ! \n")
    while True:
        try:
            global value2
            value2 = int(input("Enter le deuxième nombre : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre ! \n")

calculatrice()