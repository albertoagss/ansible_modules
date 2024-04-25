#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule                    # Importar la clase 'AnsibleModule' de 'ansible.module_utils.basic', que permite la creación de módulos personalizados
import requests                                                         # Importar la biblioteca 'requests', que sirve para realizar solicitudes HTTP

def get_pokemon_data(pokemon_name):                                     # Función para realizar la petición a la Api
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"   # URL para la llamada a la API
    answer = requests.get(url)                                          # Lanzamos una petición get a la url y almacenamos su contenido en la variable answer
    if answer.status_code == 200:                                       # Si la petición es exitosa (código de estado 200) devolvemos el contenido de la variable en formato json
        return answer.json()
    else:
        return None

def main():                                                             # Función principal
    module = AnsibleModule(                                             # Definimos el módulo de Ansible
        argument_spec=dict(                                             # Definimos los argumentos que acepta el módulo
            pokemon=dict(type='str', required=True)                     # Argumento 'pokemon', siempre requerido
        )
    )
    
    pokemon_name = module.params['pokemon']                             # Obtenemos el valor del argumento pokemon y lo almacenamos en la variable 'pokemon_name'
    pokemon_data = get_pokemon_data(pokemon_name)                       # Llamamos a la función 'get_pokemon_data'

    if pokemon_data:                                                    # Si la función 'get_pokemon_data' devuelve datos, salimos del módulo 'module.exit_json'
        module.exit_json(changed=False, pokemon_data=pokemon_data)    
    else:                                                               # Si la función 'get_pokemon_data' NO devuelve datos, fallamos el módulo con 'module.fail_json'
        module.fail_json(msg=f"Pokemon {pokemon_name} not found")       
        
if __name__ == '__main__':                                              # Flujo principal
    main()