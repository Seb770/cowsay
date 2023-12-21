#!/usr/bin/python3
class Vache:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        return f"Moo ! Je m'appelle {self.nom} et je suis une vache heureuse."

# Fonction principale
def main():
    # Créer une vache
    ma_vache = Vache("Bella")

    # Faire parler la vache
    message = ma_vache.parler()

    # Afficher le message
    print(message)

# Appeler la fonction principale
if __name__ == "__main__":
    main()
