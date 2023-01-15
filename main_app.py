import PySimpleGUI as sg


sg.theme('DarkAmber')


def front ():
    flayout = [
        [sg.Text('Smarth Database')],
        [sg.Button('ENTRAR'), sg.Button('SAIR')]
    ]
    window = sg.Window('Midnight Analysis', flayout, size=(750, 450), element_justification='center')
    button, values = window.read()

    if button == 'ENTRAR' :
        window.close()

    if button == 'SAIR' :
        window.exite()

layout = [
    [sg.Text('Digite o Nome do Funcionario'), sg.InputText('', key='-NAME-')],
    [sg.Button('Adicionar')],
    [sg.Text('')],
    [sg.Text('Funcionários Cadastrados')],
    [sg.Listbox('NAME',size=(50, 10), key='-BOX-')],
    [sg.Button('Deletar'), sg.Button('Sair')]
]

front()

window = sg.Window('Main Page', layout)

button, values = window.read()