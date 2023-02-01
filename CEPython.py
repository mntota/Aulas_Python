import requests

def buscacep():
  cep = input("Qual o CEP? ")
  while len(cep) != 8:
    print('Errrouuuuu')
    cep = input("Qual o CEP? ")

  caixinha = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
  endereço = caixinha.json()

  if 'erro' not in endereço:
    print("---- CEP ENCONTRADO ----")
    print('CEP: {}' .format(endereço['cep']))
    print('Cidade: {}' .format(endereço['localidade']))
    print('Estado: {}' .format(endereço['uf']))
    print('Logradouro: {}' .format(endereço['logradouro']))
  else:
    print('{} é um CEP invalido ou não foi encontrado.')


executar = True

while executar :
  print('---------- CEPython ----------')
  opcao = input('Escolha: \n[1]buscar um CEP \n[2]encerrar?')
  if opcao == '1':
    buscacep()
  else:
    executar = False
