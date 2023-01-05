# 1ra pre-entrega
import json
from os import getcwd
ruta = getcwd()

user = {}
state = {}
users_list = []

def register():
    username = input("Resgistre su nombre de usuario: ")
    password = input("Registre su contraseña: ")
    # user["usuario"] = username
    # user["password"] = password
    user[username] = password
   

def getUser(user_db):
    return user_db


def login(user):
    username =input("Ingrese nombre de usuario registrado: ")
    password = input("Ingrese su contraseña registrada: ")
    
    for key, value in user.items():
        if key == username and value == password:
            state["success"] = True
            state["message"] = "Login exitoso"
            
        else: 
            state["success"] = False
            state["message"] = "Usuario y/o contraseña incorrectos"
            
    return state


def getJson():

    f = open(ruta + "/primera-entrega.json", "r")
    json_content = f.read()
    json_parse = json.loads(json_content)
    f.close()
    return json_parse

def update_json(element):

    json_content = getJson()
    json_content.append(element)
    with open(ruta + "/primera-entrega.json", "w") as file:
        file.write(json.dumps(json_content))
    

def saveUser(user):
    import json
    from os import getcwd

    content = getJson()

    if state["success"] == False:
        return print("No se puede guardar usuarios incorrectos")
    
    elif len(content) == 0:
        ruta = getcwd()
        with open(ruta + "/primera-entrega.json" , "w") as f:
            userDB = getUser(user)
            users_list.append(userDB)
            f.write(json.dumps(users_list))
    else:
        update_json(user)
    

register()
print(getUser(user))
print(login(user))
saveUser(user)
