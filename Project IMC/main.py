import json

ROOT_PROJECT = 'Project Python/Project IMC'

def load_data(name):
    with open(f'{ROOT_PROJECT}/{name}', 'r') as f:
        return json.load(f)
    def save_data(name, objet):
        with open(f'{ROOT_PROJECT}/{name}', 'w') as f:
            json.dump(objet, f)

def get_users_datas(id_, users, datas):
    user = [user1 for user1 in users if id_==user1['id']][0]
    data = [data_ for data_ in datas if id_ == data_['user_id']][0]
    
    user_index = users.index(user)
    user_data_index = datas.index(data)
    
    return user, data, user_index, user_data_index

def imc_calculator(taille, poids):
    return round(poids/taille**2, 2)

def get_health_class(imc):
    class_health = None
    if 18.5<= imc <= 24.9:
        class_health =0
    elif imc<18.5:
        class_health =1
    elif 25<= imc <= 30:
        class_health = 2
    elif 30<=imc<=35:
        class_health = 3
    elif 35<=imc<=40:
        class_health =4
    else:
        class_health = 5
    return class_health                          
    
def main():
    print("Bonjour M. Comment allez vous\n Veuillez vous connecté ! \n1)Connexion\n2)Creer un compte")
    option = input(input(''))
    if option == 1:
        users = load_data('users.json')
        datas = load_data('datas.json')
        
        for user in users :
            print(f"{user['id']} - {user['nom']} {user['prenom']}")
        user_id = int(input(''))
        print('Que souhaitez vous ?:\n1)Modification de données\n2)Verification IMC\n3)Etat de santé')
        action = int(input(''))
        
        if action == 1:
            user, data, user_index, user_data_index = get_users_datas(user_id, users, datas)
            
            user['nom'] = input('Nom')
            user['prenom'] = input('Prenom')
            user['age'] = input('Age')
            user['sexe'] = input('Sexe')
            user['travail'] = input('Travail')
            
            data['data']['taille'] = int(input('Taille (cm)'))/100
            data['data']['poids'] = int(input('Poids (kg)'))
            
            imc = imc_calculator(data['data']['taille'], data['data']['poids'])
            
            data['data']['imc'] = imc
            
            data['data']['class_health'] = get_health_class(imc)
            
            datas[user_data_index] = data
            users[user_index] = user
            
            save_data('datas.json', datas)
            save_data('users.json', users)
            
            pass
        
        if option==2:
          user, data, user_index, user_data_index = get_users_datas(user_id, users, datas)
          print(data['data']['imc'])
          pass
        elif action==3:
            healths = load_data('health.json')
            user, data, user_index, user_data_index = get_users_datas(user_id, users, datas)
            user_health = [health for health in healths if health['id']==data['data']['class_health']][0]
            print(f"Etat : {user_health['maladie']}\nAnalyse : {user_health['reason']}\nConseil : {user_health['conseil']}")
            pass
        else:
            print("Valeur non reconnue")
    
    if option == 2:
        pass
        
main()