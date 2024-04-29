#!/usr/bin/python

# Este módulo devuelve los datos de un Pokemon, movimiento o habilidad realizando una llamada a la API Rest 'PokeAPI'
# Esta v4 añade la funcionalidad de listar pokedex completas, especificando una región.

# Importar la clase 'AnsibleModule' de 'ansible.module_utils.basic', que permite la creación de módulos personalizados
from ansible.module_utils.basic import AnsibleModule
# Importar la biblioteca 'requests', que sirve para realizar solicitudes HTTP
import requests

# Función para realizar la petición a la Api
def get_pokemon_data(name, search_type):
    # URL para la llamada a la API
    base_url = f"https://pokeapi.co/api/v2"
    if search_type == "pokemon":
        url = f"{base_url}/pokemon/{name.lower()}"
    elif search_type == "move":
        url = f"{base_url}/move/{name.lower()}" 
    elif search_type == "ability":
        url = f"{base_url}/ability/{name.lower()}"
    elif search_type == "pokedex":
        url = f"{base_url}/pokedex/{name.lower()}"
    else:
        return None

    # Lanzamos una petición get a la url y almacenamos su contenido en la variable answer
    answer = requests.get(url)
    # Si la petición es exitosa (código de estado 200) devolvemos el contenido de la variable en formato json
    if answer.status_code == 200:
        return answer.json()
    else:
        return None

# Función principal
def main():
    # Definimos el módulo de Ansible
    module = AnsibleModule(
        # Definimos los argumentos que acepta el módulo
        argument_spec=dict(
            search_type=dict(type='str', required=True, choices=['pokemon', 'move', 'ability', 'pokedex']),
            name=dict(type='str', required=True),
        ),
    )

    # Obtenemos el valor de los argumentos y los almacenamos en variables
    name = module.params['name']
    search_type = module.params['search_type']
    
    # Llamamos a la función 'get_pokemon_data'
    pokemon_data = get_pokemon_data(name, search_type)

    # Si la función 'get_pokemon_data' devuelve datos, salimos del módulo 'module.exit_json'
    if pokemon_data:
        module.exit_json(changed=False, pokemon_data=pokemon_data)
    # Si la función 'get_pokemon_data' NO devuelve datos, fallamos el módulo con 'module.fail_json'
    else:
        module.fail_json(msg=f"No {search_type} found with name {name}")

# Flujo principal
if __name__ == '__main__':
    main()