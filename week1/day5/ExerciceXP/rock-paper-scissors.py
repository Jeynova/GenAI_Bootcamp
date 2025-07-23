from game import Game

# menu
def get_user_menu_choice():
    print("\nMenu :")
    print("1 - Jouer une partie")
    print("2 - Afficher les scores")
    print("3 - Quitter")
    choice = input("Votre choix : ").strip().lower()

    # Autorise aussi 'q' ou 'quit' pour quitter
    if choice in ('q', 'quit'):
        return '3'
    return choice

# resultats
def print_results(results):
    print("\nRésultats des parties :")
    print(f"Victoires : {results['win']}")
    print(f"Défaites : {results['loss']}")
    print(f"Égalités (matches rejoués) : {results['draw']}")
    print("Merci d'avoir joué.")

# mode de jeu
def get_game_mode():
    print("\nChoisissez le mode de jeu :")
    print("1 - Une seule manche gagnante")
    print("3 - Best of 3")
    print("5 - Best of 5")
    mode = input("Entrez 1, 3 ou 5 : ").strip()
    if mode not in ('1', '3', '5'):
        print("Mode invalide. Par défaut : 1 manche gagnante.")
        return "1"
    return mode

# main
def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == '1':
            mode = get_game_mode()
            game = Game()
            result = game.play(mode=mode)
            results[result] += 1
        elif choice == '2':
            print_results(results)
        elif choice == '3':
            print_results(results)
            break
        else:
            print("Choix invalide. Veuillez entrer 1, 2, 3 ou q pour quitter.")

if __name__ == "__main__":
    main()