import requests

def consulta(cep):


    if len(cep) != 8:
        print("Cep invalido")
        exit()

    r = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    a = r.json()

    return a
        
print(consulta("77019050"))