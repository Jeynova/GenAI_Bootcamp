import random

class Game:
    def __init__(self):
        self.valid_choices = {
            "rock": "rock", "r": "rock",
            "paper": "paper", "p": "paper",
            "scissors": "scissors", "s": "scissors"
        }

    def get_user_item(self):
        # input user
        while True:
            item = input("Choisissez rock (r), paper (p) ou scissors (s) : ").lower()
            if item in self.valid_choices:
                return self.valid_choices[item]
            print("Choix invalide. Essayez encore.")

    def get_computer_item(self):
        # choix ordi
        return random.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item, computer_item):
        # choix
        if user_item == computer_item:
            return "draw"
        elif (
            (user_item == "rock" and computer_item == "scissors") or
            (user_item == "scissors" and computer_item == "paper") or
            (user_item == "paper" and computer_item == "rock")
        ):
            return "win"
        else:
            return "loss"

    def play(self, mode="1"):
        # Jeux
        user_score = 0
        computer_score = 0
        draw_count = 0
        round_number = 1

        rounds_to_win = {"1": 1, "3": 2, "5": 3}.get(mode, 1)

        while user_score < rounds_to_win and computer_score < rounds_to_win:
            print(f"\nManche {round_number} :")
            user_item = self.get_user_item()
            computer_item = self.get_computer_item()

            print(f"Vous avez choisi : {user_item}")
            print(f"L'ordinateur a choisi : {computer_item}")

            result = self.get_game_result(user_item, computer_item)
            if result == "win":
                print("Vous gagnez cette manche.")
                user_score += 1
            elif result == "loss":
                print("Vous perdez cette manche.")
                computer_score += 1
            else:
                print("Égalité. On rejoue cette manche.")
                draw_count += 1
                continue

            round_number += 1

        if user_score > computer_score:
            print("\nVous avez gagné le match !")
            return "win"
        else:
            print("\nVous avez perdu le match.")
            return "loss"