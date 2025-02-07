import json

ROOT_PROJECT = 'Project Python/Project IMC'

def load_data(name):
    with open(f'{ROOT_PROJECT}/{name}', 'r') as f:
        return json.load(f)
    def save_data(name, objet):
        with open(f'{ROOT_PROJECT}/{name}', 'w') as f:
            json.dump(objet, f)

def main():
    print("Bonjour M. Comment allez vous\n Veuillez vous connecté ! \n1)Connexion\n2)Creer un compte")
    option = input(input(''))
    if option == 1:
        users = load_data('users.json')
        datas = load_data('datas.json')
        
        for user in users :
            print(f"{user['id']} - {user['nom']} {user['prenom']}")
        user_choice = int(input(''))
        print('Que souhaitez vous ?:\n1)Modification de données\n2)Verification IMC\n3)Etat de santé')
        action = int(input(''))
        
        if action == 1:
            pass
        
        if option==2:
          pass
        elif action==3:
          pass
        else:
            print("Valeur non reconnue")
    
    if option == 2:
        pass
        
main()