# Pacote de Checagem de CEP

Este pacote oferece a função `consulta()` que permite verificar se um CEP é válido e retorna informações sobre o endereço associado ao CEP.

## Instalação

Para instalar o pacote, basta executar o seguinte comando:


     pip install -i https://test.pypi.org/simple/ cep-consulta-gvolpatolima


## Uso

Para utilizar a função consulta(), primeiro importe o pacote:


 
    from consulta_cep_gvolpatolima import consulta()

 

Em seguida, chame a função consulta() passando o CEP desejado como parâmetro:


    endereco = check_cep.consulta('01001000')
    print(endereco)

O resultado será um dicionário contendo as informações do endereço associado ao CEP:
```
{
    'cep': '01001-000',
    'logradouro': 'Praça da Sé',
    'complemento': 'lado ímpar',
    'bairro': 'Sé',
    'localidade': 'São Paulo',
    'uf': 'SP',
    'ibge': '3550308',
    'gia': '1004',
    'ddd': '11',
    'siafi': '7107'
}
```
## Contribuição

Contribuições são sempre bem-vindas! Se você encontrou um bug ou tem alguma sugestão de melhoria, abra uma issue ou envie um pull request para o repositório do projeto.

## Licença

Este pacote é distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.