    ex 1:
# Demandez à l'utilisateur de saisir N
2N = int(input("Entrez N: "))
3
4# Initialisez la somme à 0
5somme = 0
6
7# Ajoutez les entiers de 0 à N à la somme
8for i in range(N+1):
9    somme += i
10
11# Affichez la somme
12print("La somme des N entiers naturels est:", somme)

    ex1 b:
# Initialisez la somme à 0
somme = 0

# Demandez à l'utilisateur de saisir une valeur
val = int(input("Entrez une valeur (100 pour arrêter): "))

# Tant que la valeur n'est pas 100
while val != 100:
    # Ajoutez la valeur à la somme
    somme += val

    # Demandez à l'utilisateur de saisir une nouvelle valeur
    val = int(input("Entrez une nouvelle valeur (100 pour arrêter): "))

# Affichez la somme
print("La somme des valeurs entrées est:", somme)
    c :
# Initialisez les compteurs à 0
inf_10 = 0
sup_10_inf_15 = 0
sup_15 = 0

# Demandez à l'utilisateur de saisir 10 valeurs
for i in range(10):
    # Lecture d'une valeur réelle
    val = float(input("Entrez une valeur réelle comprise entre 0 et 20: "))

    # Vérification des conditions et mise à jour des compteurs
    if val < 0 or val > 20:
        print("Erreur: La valeur doit être comprise entre 0 et 20.")
        i -= 1
    elif val < 10:
        inf_10 += 1
    elif val < 15:
        sup_10_inf_15 += 1
    else:
        sup_15 += 1

# Affichage des résultats
print("Nombre de valeurs inférieur strictement à 10:", inf_10)
print("Nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15:", sup_10_inf_15)
print("Nombre de valeurs supérieur ou égale à 15:", sup_15)
    d:
# Demandez à l'utilisateur de saisir une valeur supérieure à 1
X = float(input("Entrez une valeur supérieure à 1: "))

# Vérification de la condition
if X <= 1:
    print("Erreur: La valeur doit être supérieure à 1.")
else:
    # Calcul du nombre recherché
    N = 1
    while True:
        somme = N * (N + 1) // 2
        if somme > X:
            break
        N += 1

    # Affichage du résultat
    print("Le nombre N recherché est:", N - 1)
ex 2:
import time

n = int(input("Entrez un nombre entier n positif: "))

for i in range(n, 0, -1):
    print(i)
    time.sleep(1)

import time

n = int(input("Entrez un nombre entier n positif: "))

while n >= 0:
    print(n)
    n -= 1
    time.sleep(1)

ex3:
import random

def generate_random_number():
    return random.randint(0, 100)

def play_game():
    secret_number = generate_random_number()
    count = 0
    guess = -1

    while guess != secret_number:
        try:
            guess = int(input("Entrez un nombre entre 0 et 100: "))
        except ValueError:
            print("Veuillez entrer un nombre entier.")
            continue

        count += 1

        if guess == secret_number:
            print("Félicitations! Vous avez deviné le nombre correct en {} tours.".format(count))
        elif guess > secret_number:
            print("Le nombre à deviner est plus petit.")
        else:
            print("Le nombre à deviner est plus grand.")

    play_again = input("Voulez-vous jouer à nouveau? (O/N) ")
    if play_again.lower() == "o":
        play_game()

if __name__ == "__main__":
    play_game()

ex4:
def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def calculate_factorial_iteratively(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    n = int(input("Entrez un entier: "))
    print("1. Boucle récursive")
    print("2. Boucle itérative")
    choice = int(input("Choisissez le type de boucle à utiliser: "))

    if choice == 1:
        result = calculate_factorial(n)
        print("La factorielle de {} est {}.".format(n, result))
    elif choice == 2:
        result = calculate_factorial_iteratively(n)
        print("La factorielle de {} est {}.".format(n, result))
    else:
        print("Choix non valide.")

ex5:
def calculate_cost(start_hour, end_hour):
    if not(0 <= start_hour <= 24) or not(0 <= end_hour <= 24):
        return "Les heures doivent être comprises entre 0 et 24 !"
    elif start_hour > end_hour:
        return "Attention ! le début de la location est après la fin ..."
    elif start_hour == end_hour:
        return "Attention ! l’heure de fin est identique à l’heure de début."
    else:
        early_hours = min(end_hour, 7) - start_hour
        late_hours = max(0, end_hour - 17)
        night_hours = max(0, 24 - end_hour) + max(0, start_hour - 7)
        return early_hours * 1 + late_hours * 2 + night_hours * 1,

def get_hours():
    while True:
        try:
            start_hour = int(input("Donnez l'heure de début de la location (un entier) : "))
            end_hour = int(input("Donnez l'heure de fin de la location (un entier) : "))
            return start_hour, end_hour
        except ValueError:
            print("Veuillez entrer des entiers.")

def main():
    start_hour, end_hour = get_hours()
    cost = calculate_cost(start_hour, end_hour)
    if isinstance(cost, tuple):
        early_hours, late_hours, night_hours = cost
        print(f"Vous avez loué votre vélo pendant {early_hours} heure(s) au tarif horaire de 1.0 euro(s) ")
        print(f"{late_hours} heure(s) au tarif horaire de 2.0 euro(s) ")
        print(f"{night_hours} heure(s) au tarif horaire de 1.0 euro(s) ")
        print(f"Le montant total à payer est de {early_hours + late_hours * 2 + night_hours} euro(s).")
    else:
        print(cost)

if __name__ == "__main__":
    main()