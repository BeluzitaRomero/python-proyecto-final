import json
from os import getcwd

ruta = getcwd()

user = {}
state = {}
users_list = []

def register():
    username = input("Resgistre su nombre de usuario: ").strip()
    password = input("Registre su contraseña: ").strip()
    
    while len(username) < 3:
        print("El nombre de suario debe tener al menos 3 caracteres")
        username = input("Resgistre su nombre de usuario: ").strip()
        

    while len(password) < 3:
        print("La contraseña deben tener al menos 3 caracteres")
        password = input("Registre su contraseña: ").strip()

    user[username] = password
   

def get_user(user_db):
    return user_db


def login(user):
    username =input("Ingrese nombre de usuario registrado: ")
    password = input("Ingrese su contraseña registrada: ")

    content = get_json()
    
    for user in content:
        
        for key, value in user.items():
            if  key == username and value == password:
                state["success"] = True
                state["message"] = "Login exitoso"
            else: 
                state["success"] = False
                state["message"] = "Usuario y/o contraseña incorrectos"
            
    return state

def file_exists():
    from os.path import exists
    file_exists = exists(ruta +"/primera-entrega.json" )
    return file_exists

def get_json():
    if file_exists():
        f = open(ruta + "/primera-entrega.json", "r")
        json_content = f.read()
        json_parse = json.loads(json_content)
        f.close()
        return json_parse
    else: return []


def update_json(element):

    json_content = get_json()
    json_content.append(element)
    with open(ruta + "/primera-entrega.json", "w") as file:
        file.write(json.dumps(json_content))
    

def save_user(user):
    
    if not file_exists():
        with open(ruta + "/primera-entrega.json" , "w") as f:
            users_list.append(user)
            f.write(json.dumps(users_list))
    else:
        print("va al update")
        update_json(user)
    

# register()
# print(get_user(user))
# save_user(user)
print(login(user))
