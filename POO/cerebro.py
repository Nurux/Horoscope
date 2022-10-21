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

#Logica completa do sistema
class Cerebro():

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
    def relacionar(self, pessoa, name_input, name_input2):
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
            self.calcular(person, person2)

    #Calcula o nivel de match das pessoas selecionadas
    def calcular(self, person, person2):
        if person.element == person2.element:
            sg.popup_ok(f'{person.name} e {person2.name} Deram Match!!!')
        else:
            sg.popup_ok(f'Infelizmente {person.name} com {person2.name} não deram match ;-;\n\nMas não fique assim signos de elemento {person.element} não costumam se dar bem com o signo de {person2.signo}\nProcure novas experiencias  :C')

class Cadastro():
    def __init__(self, values):
        self.name = values['nome']
        self.age = int(values['idade'])
        self.nasc = values['date']
    
    #Realiza o cadastro da pessoa
    def cadastro(self):
        while True:
            sig = self.designar_signo(self.nasc)
            elemento = self.designar_elemental(sig)

            if self.verificar_idade(self.nasc, self.age) == True:
                pessoa = Person(self.name, self.age, self.nasc, sig, elemento)

                adicionar = Dados()
                adicionar.lista(pessoa)

                option = sg.popup_yes_no('Deseja fazer um novo cadastro?') 

                if option.lower() == 'yes':
                    return 1 

                if option.lower() == 'no':
                    return -1    
            else:
                print('Verifique a idade informada e tente novamente')

    #Verifica idade da pessoa
    def verificar_idade(self, data, idade):
        time = date.today().strftime('%d/%m/%Y')
        data_nascimento = int(data[6:10])
        data_atual = int(time[6:10])

        idade_real = data_atual - data_nascimento 
            
        if idade+1 < idade_real:
            return False
        
        return True
    
    #Define o signo da pessoa
    def designar_signo(self, data):
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
    def designar_elemental(self, signo):
        if signo == 'Áries' or  signo == 'Sargitário' or  signo == 'Leão':
            elemento = 'Fogo'
        elif signo == 'Touro' or signo == 'Virgem' or signo == 'Capricórnio':
            elemento = 'Terra'
        elif signo == 'Gêmeos' or signo == 'Libra' or signo == 'Aquário':
            elemento = 'Ar'
        elif signo == 'Câncer' or signo == 'Escorpião' or signo == 'Peixes':
            elemento = 'Água'
        
        return elemento
