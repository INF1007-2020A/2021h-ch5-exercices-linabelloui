#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        return number * (-1)

'''ou return (number ** 2) ** 0.5'''

def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    liste_nom = []
    for pre in prefixes:
        liste_nom.append(pre + suffixe)

    return liste_nom


def prime_integer_summation() -> int:
    nombre = 6
    nombre_premier = [2, 3, 5]

    while len(nombre_premier) < 100:
        premier = True
        for i in range(2, nombre // 2):
            if nombre % i == 0:
                premier = False
                break
        if premier:
            nombre_premier.append(nombre)
        nombre += 1
    return sum(nombre_premier)


def factorial(number: int) -> int:
    facto = 1
    for n in range(2, number+1):
        facto *= n
    return facto


def use_continue() -> None:
    for i in range(1, 11):
        if i == 5:
            continue
        print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    acceptance = []
    for sub_group in groups:
        if len(sub_group) > 10 or len(sub_group) <= 3:
            acceptance.append(False)
            continue
        if 25 in sub_group:
            acceptance.append(True)
            continue
        if 50 in sub_group:
            is_50 = True
        else:
            is_50 = False
        is_accepted = True
        for age in sub_group:
            if (age < 18) or (is_50 and age > 70):
                is_accepted = False
                break

        acceptance.append(is_accepted)

    return acceptance


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
