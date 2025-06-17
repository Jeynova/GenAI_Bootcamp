from utils import unzip_with_7z
""" from itertools import product
for combo in product(letters, repeat=2):
    password = ''.join(combo) + 'bcmpda' """

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
# ----------------------------------------
def password_cracking():
    letters = 'abcdefghijklmnopqrstuvwxyz'

    for first in letters:
        for second in letters:
            secret_password = first + second + 'bcmpda'

            if unzip_with_7z(zip_file_path, dest_path, secret_password):
                print(f"Bingo le password est: {secret_password}")
                return

            print(first, second)

    print("Aucune combinaison trouvée")

password_cracking()
