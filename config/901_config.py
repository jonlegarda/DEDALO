# leer el archivo config.cfg y sacar el valor de la API
#   https://python-para-impacientes.blogspot.com/2015/01/gestionar-la-configuracion-de-un.html

import configparser

configuracion = configparser.ConfigParser()


# Leer el archivo de configuración:

configuracion.read('config.cfg')


api_shodan= configuracion['SHODAN']['API_SHODAN'] 

print(api_shodan)


"""
with open('config.cfg', 'w') as archivoconfig:
    configuracion.write(archivoconfig)
"""