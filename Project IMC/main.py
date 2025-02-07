import json

ROOT_PROJECT = 'PROJECT PYTHON\Project IMC'


def load_data(name):
    with open(f'{ROOT_PROJECT}{name}', 'r') as f:
        return json.load(f)
    def save_data(name, objet):
        with open(f'{ROOT_PROJECT}{name}', 'w') as f:
            json.dump(objet, f)

def main():
    print("Bonjour M. Comment allez vous\n Veuillez vous connecté ! \n)Connexion\n2)Creer un compte")
    option = input(input(''))
    if option == 1:
        
        pass
    if option == 2:
        pass