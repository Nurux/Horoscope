from datetime import date
import PySimpleGUI as sg

#Define as caracteristicas da pessoa
class Person():
    def __init__(self, name, age, date, signo, elemento):
        self.name = name
        self.age = age
        self.nasc_date = date
        self.signo = signo
        self.element = elemento

#Cria lista de pessoas  
class Dados():
    lista_dados = []

    def lista(self, objeto): 
        self.lista_dados.append(objeto)
        print('Dados cadastrados')

#Define o tema das janelas
class Tema():
    dark = sg.theme('DarkAmber')
    ideal = sg.theme('Topanga')


#Menu
def tela_menu():
    Tema.ideal

    layout = [[sg.Text('--'*20)],
              [sg.Text('HOROSCOPE')],
              [sg.Text('--'*20)],
              [sg.Button(' Cadastro ', key='cadastrar')],
              [sg.Button('  Listar  ', key='listar')],
              [sg.Button(' Calcular ', key='calcular')],
              [sg.Button('   Sair   ', key='sair')]]

    janela = sg.Window('Menu', layout, finalize=True)

    while True:
        event, value = janela.read()

        if event == sg.WIN_CLOSED or event == 'sair':
            break

        if event == 'cadastrar':
            pessoa = tela_cadastro()
        
        if event == 'listar':
            consultar(pessoa)
        
        if event == 'calcular':
            tela_consulta(pessoa)

    janela.close()

#Tela de cadastramento
def tela_cadastro():
    Tema.dark

    layout = [[sg.Text('Cadastro')],
              [sg.Text('Nome: '), sg.InputText(key='nome')],
              [sg.Text('Idade: '), sg.InputText(key='idade')],
              [sg.Text('Data de nascimento: '), sg.InputText(key='date')],
              [sg.Button('Cadastrar', key='cadastro'), sg.Button('Cancelar', key='quit')]]
    
    janela = sg.Window('Tela de cadastro', layout, finalize=True, size=(500, 150))

    while True:
        event, values = janela.read()

        if event == sg.WIN_CLOSED or event == 'quit':
            break

        if event == 'cadastro':
            pessoa = cadastro(values)

            if pessoa == -1 :
                break

            return pessoa
        
    janela.close()
            
#Tela de consulta
def tela_consulta(pessoa):
    Tema.ideal

    layout = [[sg.Text('Digite o nome seu nome: '), sg.InputText(key='name')],
              [sg.Text('Digite o nome da pessoa desejada: '), sg.InputText(key='name2')],
              [sg.Button('Relacionar', key='relacionar'), sg.Button('Cancelar', key='quit')]]

    janela = sg.Window('Tela de relacionamento', layout, finalize=True)

    while True:
        event, value = janela.read()

        if event == sg.WINDOW_CLOSED or event == 'quit':
            break

        if event == 'relacionar':
            relacionar(pessoa, value['name'], value['name2'])

    janela.close()
            


#Realiza o cadastro da pessoa
def cadastro(values):
    while True:
        nome = values['nome']
        idade = int(values['idade'])
        data = values['date']
        sig = designar_signo(data)
        elemento = designar_elemental(sig)

        if verificar_idade(data, idade) == True:
            pessoa = Person(nome, idade, data, sig, elemento)

            adicionar = Dados()
            adicionar.lista(pessoa)

            option = sg.popup_yes_no('Deseja fazer um novo cadastro?') 

            if option.lower() == 'yes':
                tela_cadastro()

            if option.lower() == 'no':
                return -1    
        else:
            print('Verifique a idade informada e tente novamente')

#Verifica idade da pessoa
def verificar_idade(data, idade):
    time = date.today().strftime('%d/%m/%Y')
    data_nascimento = int(data[6:10])
    data_atual = int(time[6:10])

    idade_real = data_atual - data_nascimento 
        
    if idade+1 < idade_real:
        return False
    
    return True

#Define o signo da pessoa
def designar_signo(data):
    dia = int(data[0:2])
    mes = int(data[3:5])

    if mes == 1:
        if dia >= 21:
            sig = "Aquário"
        if dia <= 20:
            sig = "Capricórnio" 

    if mes == 2:
        if dia >= 19:
            sig = "Peixes"
        if dia <= 18:
            sig = "Aquário"

    if mes == 3:
        if dia >= 21:
            sig = "Áries"
        if dia <= 20:
            sig = "Peixes"

    if mes == 4:
        if dia <= 20:
            sig = "Áries"
        if dia >= 21:
            sig = "Touro"
    
    if mes == 5:
        if dia <= 20:
            sig = "Touro"
        if dia >= 21: 
            sig = "Gêmeos"
    
    if mes == 6:
        if dia <= 20:
            sig = "Gêmeos"
        if dia >= 21:
            sig = "Câncer"

    if mes == 7:
        if dia <= 22:
            sig = "Câncer"
        if dia >= 23:
            sig = "Leão"
    
    if mes == 8:
        if dia <= 22:
            sig = "Leão"
        if dia >= 23:
            sig = "Virgem"
    
    if mes == 9:
        if dia <= 22:
            sig = "Virgem"
        if dia >= 23:
            sig = "Libra"
    
    if mes == 10:
        if dia <= 22:
            sig = "Libra"
        if dia >= 23:
            sig = "Escorpião"
    
    if mes == 11:
        if dia <= 21:
            sig = "Escorpião"
        if dia >= 22:
            sig = "Sargitário"

    if mes == 12:
        if dia <= 21:
            sig = "Sargitário"
        if dia >= 22:
            sig = "Capricórnio"
    
    return sig

#Define o elemnto do signo
def designar_elemental(signo):
    if signo == 'Áries' or  signo == 'Sargitário' or  signo == 'Leão':
        elemento = 'Fogo'
    elif signo == 'Touro' or signo == 'Virgem' or signo == 'Capricórnio':
        elemento = 'Terra'
    elif signo == 'Gêmeos' or signo == 'Libra' or signo == 'Aquário':
        elemento = 'Ar'
    elif signo == 'Câncer' or signo == 'Escorpião' or signo == 'Peixes':
        elemento = 'Água'
    
    return elemento

#Mostra a lista de pessoas cadastradas
def consultar(pessoa):
    pessoa = Dados()
    cont = 0

    while cont < len(pessoa.lista_dados):
        ilust_person = pessoa.lista_dados[cont]
        print('-'*20)
        print(f'Nome: {ilust_person.name}')
        print(f'Idade: {ilust_person.age}')
        print(f'Dat.Nasc: {ilust_person.nasc_date}')
        print(f'Signo: {ilust_person.signo}')
        print(f'Elemento: {ilust_person.element}')
        print('-'*20)

        cont += 1

#Busca e verifica as pessoas a serem selecionadas
def relacionar(pessoa, name_input, name_input2):
    cont = 0
    pessoa = Dados()
    content = False
    i = 0
    content2 = False

    while cont < len(pessoa.lista_dados):
        person = pessoa.lista_dados[cont]
        
        if person.name == name_input:
            print(f'{person.name} foi encontrada com sucesso!')

            content = True
            cont = len(pessoa.lista_dados)
        
        cont += 1
    
    if content == False:
        sg.popup_ok(f'O nome {name_input} não foi encontrado!\nPorfavor tente outro nome ou cadastre a pessoa desejada')
        return 
    
    if content == True:

        while i < len(pessoa.lista_dados):
            person2 = pessoa.lista_dados[i]

            if person2.name == name_input2:
                print(f'{person2.name} foi encontrada com sucesso!')
                        
                content2 = True
                i = len(pessoa.lista_dados)
                    
            i += 1

    if content2 == False:
        sg.popup_ok(f'O nome {name_input2} não foi encontrado!\nPorfavor tente outro nome ou cadastre a pessoa desejada')
    
    if content and content2 == True:
        calcular(person, person2)

#Calcula o nivel de match das pessoas selecionadas
def calcular(person, person2):
   if person.element == person2.element:
        sg.popup_ok(f'{person.name} e {person2.name} Deram Match!!!')
   else:
        sg.popup_ok(f'Infelizmente {person.name} com {person2.name} não deram match ;-;\n\nMas não fique assim signos de elemento {person.element} não costumam se dar bem com o signo de {person2.signo}\nProcure novas experiencias  :C')

#inicio
def main():
    tela_menu()


if __name__ == '__main__':
    main()