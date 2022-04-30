<img src="https://acontecendoaqui.com.br/wp-content/uploads/2019/05/grupo_nexxera.jpg" alt="exemplo imagem">

# Desafio - API

> Projeto criado a fins de teste de conhecimento.

## Listagem de todos os desafios passados e seus respectivos status:

#### Criar uma API que seja possível criar e utilizar uma conta virtual tendo as seguintes funcionalidades:
- [x] Criar conta virtual
- [x] Realizar débito
- [x] Realizar crédito
- [x] Exibir extrato

#### Critérios a serem seguidos:
- [x] O sistema pode comportar ao menos 1 conta
- [x] Cada débito ou crédito deve ter uma descrição que é exibida no extrato
- [x] A função extrato deve exibir o saldo inicial e final do período, listando as transações do período
- [x] Deve ser possível filtrar extrato apenas por crédito ou por débito
- [x] Deve ser disponibilizada API rest para utilizar o sistema

#### Requisitos técnicos:
- [x] Utilizar a stack: Django, Django Restframework
- [x] Disponibilizar no Git
- [x] Criar um README explicando como rodar o projeto
- [ ] Testes unitários cobertura 90% (sugestão pytest)


## 💻 Inicializando o Projeto:

Para começarmos, certifique-se de seguir os passos a seguir:
* Clonagem do repositório.
* Acessar pasta de clonagem e rodar os comandos: 
* pip install -r requirements.txt
* python manage.py makemigrations
* python manage.py migrate 


## :globe_with_meridians: Rotas criadas:

* http://admin.localhost:8000/api/healthcheck/ -> VERIFICAÇÃO DE SERVIÇO
* http://admin.localhost:8000/api/token/ -> PEGAR TOKEN 
* http://admin.localhost:8000/api/register/ -> CADASTRO DE USUÁRIO
* http://admin.localhost:8000/api/transactions/add/ -> INSERIR DINHEIRO **necesário token (Bearer)
* http://admin.localhost:8000/api/transactions/remove/ -> GASTER DINHEIRO **necesário token (Bearer)
* http://admin.localhost:8000/api/extract/ -> EXTRATO GERAL **necesário token (Bearer)
* http://admin.localhost:8000/api/extract/type - type = DEBIT / CREDIT -> FILTRAR POR TIPO **necesário token (Bearer)
* http://admin.localhost:8000/api/extract/date&date - date = 2022-04-30 -> FILTRAR POR DATA **necesário token (Bearer)
* http://admin.localhost:8000/api/extract/date&date/type -> FILTRAR POR DATA E TIPO **necesário token (Bearer)

## OBS: COLLECTIONS POSTMAN NA RAIZ DO PROJETO



