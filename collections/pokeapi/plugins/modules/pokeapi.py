#!/usr/bin/python

# Importar la clase 'AnsibleModule' de 'ansible.module_utils.basic', que permite la creación de módulos personalizados
from ansible.module_utils.basic import AnsibleModule

# Importar la biblioteca 'requests', que sirve para realizar solicitudes HTTP
import requests

# Función para realizar la petición a la Api
def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    answer = requests.get(url)
    if answer.status_code == 200:
        return answer.json()
    else:
        return None

# Función principal
def main():
    module = AnsibleModule(
        argument_spec=dict(
            pokemon=dict(type='str', required=True)
        )
    )
    
    pokemon_name = module.params['pokemon']
    pokemon_data = get_pokemon_data(pokemon_name)
    
    if pokemon_data:
        module.exit_json(changed=False, pokemon_data=pokemon_data)
    else:
        module.fail_json(msg=f"Pokemon {pokemon_name} not found")
        
if __name__ == '__main__':
    main()