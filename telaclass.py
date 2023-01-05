#projeto de uma versão antiga do SimpleGUI ainda em Analise

import PySimpleGUI as sg

class TelaPython:
    def __int__(self):
        #layout
        layout = [
            [sg.Text('Nome'),sg.input()],
            [sg.Text('Idade'), sg.input()],
            [sg.Button('Enviar Dados')]
        ]
        #janela
        janela = sg.Window('Dados de Usuario').layout(layout)
        #Extrair dados da tela
        self.button,self.values = janela.Read()

    def Iniciar (self):
        print(self.values)
tela = TelaPython()
tela.Iniciar()