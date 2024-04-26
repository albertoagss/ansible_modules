#!/usr/bin/python
# Importar la clase 'AnsibleModule' de 'ansible.module_utils.basic', que permite la creación de módulos personalizados
from ansible.module_utils.basic import *
# Importar la biblioteca 'requests', que sirve para realizar solicitudes HTTP
import requests

# Función para realizar la petición 'BUSCAR POKEMON' a la Api
def get_pokemon_data(pokemon_name):
    # URL para la llamada a la API
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    # Lanzamos una petición get a la url y almacenamos su contenido en la variable answer
    answer = requests.get(url)
    # Si la petición es exitosa (código de estado 200) devolvemos el contenido de la variable en formato json
    if answer.status_code == 200:
        return answer.json()
    else:
        return None

# Función principal
#def main():
    # Definimos el módulo de Ansible
#    module = AnsibleModule(
        # Definimos los argumentos que acepta el módulo
#        argument_spec=dict(
            # Argumento 'pokemon', siempre requerido
#            pokemon=dict(type='str', required=False)
            #move=dict(type='str', required=False)
#        )
#    )
    
# Función principal
def main():
    # Definimos el módulo de Ansible
    module = AnsibleModule(
        # Definimos los argumentos que acepta el módulo
        argument_spec = {
            'pokemon' : {'type':'str'}, 
            'move' : {'type':'str'}
        }
            # Argumento 'pokemon', siempre requerido
    )

    # Obtenemos el valor del argumento pokemon y lo almacenamos en la variable 'pokemon_name'
    pokemon_name = module.params['pokemon']
    # Llamamos a la función 'get_pokemon_data'
    pokemon_data = get_pokemon_data(pokemon_name)

    # Si la función 'get_pokemon_data' devuelve datos, salimos del módulo 'module.exit_json'
    if pokemon_data:
        module.exit_json(changed=False, pokemon_data=pokemon_data)
    # Si la función 'get_pokemon_data' NO devuelve datos, fallamos el módulo con 'module.fail_json'
    else:
        module.fail_json(msg=f"Pokemon {pokemon_name} not found")

# Flujo principal
if __name__ == '__main__':
    main()