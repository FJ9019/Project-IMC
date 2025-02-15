import json

#ROOT_PROJECT = 'Desktop/Project IMC'

def load_data(name):
    with open(name, 'r') as f:
        return json.load(f)
def save_data(name, objet):
    with open(name, 'w') as f:
        json.dump(objet, f)

def get_users_datas(id_, users, datas):
    user = [user1 for user1 in users if id_==user1['id']][0]
    data = [data_ for data_ in datas if id_== data_['user_id']][0]

    user_index = users.index(user)
    user_data_index = datas.index(data)

    return user, data, user_index, user_data_index

def imc_calculator(taille, poids):
    return round(poids/taille**2, 2)

def default_input(name, default):
    val = input(name)
    return val if val else default

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
        class_health = 4
    else:
        class_health = 5
    return class_health                  

def main():
    print("Bonjour M. comment allez vous\nVeuillez vous connecté !\n1)Connexion\n2)Creer un compte")
    option = int(input(''))
    if option == 1:
        users = load_data('users.json')
        datas = load_data('datas.json')

        for user in users :
            print(f"{user['id']} - {user['nom']} {user['prenom']}")
        user_id = int(input(''))
        print('Que souhaitez vous ?:\n1)Modification de données\n2)Verification IMC\n3)Etat de sante')
        action = int(input(''))

        if action == 1:
            user, data, user_index, user_data_index = get_users_datas(user_id, users, datas)

            user['nom'] = default_input('Nom :', user['nom'])
            user['prenom'] = default_input('Prenom :', user['prenom'])
            user['age'] = default_input('Age :', user['age'])
            user['sex'] = default_input('Sexe :', user['sex'])
            user['travail'] = default_input('Travail :', user['travail'])

            data['data']['taille'] = int(default_input('Taille (cm) :',  data['data']['taille']))/100
            data['data']['poids'] = int(default_input('Poids (kg) :',  data['data']['poids']))

            imc = imc_calculator(data['data']['taille'], data['data']['poids'])

            data['data']['imc']= imc

            data['data']['class_health'] = get_health_class(imc)

            datas[user_data_index] = data
            users[user_index] = user

            save_data('data.json', datas)
            save_data('users.json', users)

            pass

        elif action==2:
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
        users = load_data('users.json')
        datas = load_data('datas.json')
        

        user = {}
        data = {'data':{}}
        user_id = None
        try:
            user_id = users[-1]['id']+1
            pass
        except IndexError:
            user_id = 1
            pass

        user['id'] = user_id
        user['nom'] = default_input('Nom :', f"Utilisateur{user_id}")
        user['prenom'] = input('Prenom :')
        user['age'] = input('Age :')
        user['sex'] = input('Sexe :')
        user['travail'] = input('Travail :')

        data['data']['taille'] = int(input('Taille (cm) :'))/100
        data['data']['poids'] = int(input('Poids (kg) :'))

        imc = imc_calculator(data['data']['taille'], data['data']['poids'])

        data['user_id'] = user['id']
        data['data']['imc']= imc

        data['data']['class_health'] = get_health_class(imc)

        users.append(user)
        datas.append(data)

        save_data('users.json', users)
        save_data('datas.json', datas)


        pass

main()