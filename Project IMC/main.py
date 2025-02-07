import json
def load_data(name):
    with open(name, 'r') as f:
        return json.load(f)
    def save_data(name, objet):
        with open(name, 'w') as f:
            json.dump(objet, f)

def main():
    print("Bonjour M. Comment allez vous\n Veuillez vous connecté ! \n)Connexion\n2)Creer un compte")
    option = input(input(''))
    if option == 1:
        
        pass
    if option == 2:
        pass