import PySimpleGUI as sg
from cerebro import Cadastro, Cerebro

# Resolver bug de janela e tela de consulta

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
            Cerebro.consultar(pessoa)
        
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
            pessoa = Cadastro(values)
            retorno = pessoa.cadastro()

            if retorno == -1 :
                print('retornou', retorno)
                break

            if retorno == 1:
                print('Cadastrado com sucesso')
                tela_cadastro()
                
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
            Cerebro.relacionar(pessoa, value['name'], value['name2'])

    janela.close()

if __name__ == '__main__':
    tela_menu()