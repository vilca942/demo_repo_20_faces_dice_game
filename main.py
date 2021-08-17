""" Le jeu de dés à implémenter suit les règles suivantes :
- Le jeu se joue avec des paires de dés à 20 faces.
- Les joueurs entrent leurs noms pour entrer dans la partie.
- Le modérateur lance une paire de dés à 20 faces.
- Tous les joueurs lancent leur paire de dés et notent leur score.
- Pour chaque score supérieur à celui du modérateur, le joueur marque un point.
- Le premier joueur à atteindre 10 points gagne la partie.
"""
from controlers.controler import Controler


def main():
    controler = Controler()
    controler.run()


if __name__ == "__main__":
    main()
