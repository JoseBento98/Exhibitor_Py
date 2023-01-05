#Utilizando PySimpleGUI fiz uma janela interativa para loguin de usuarios


from PySimpleGUI import PySimpleGUI as sg

#Layout
    #tema da tela
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='Usuário',size=(20,1))],
    [sg.Text('Senha'), sg.Input(key='Senha', password_char='*',size=(20,1))],
    [sg.Checkbox('Salvar Loguin ?')],
    [sg.Button('Recuperar Senha')],
    [sg.Button('Entrar'), sg.Button('Cadastro')]
]
#janela
janela = sg.Window('Tela de Loguin', layout)
#ler Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores ['Usuário'] == 'jldbento@gmail.com' and valores ['Senha'] == '12345':
            print('Seja Bem vindo!')
