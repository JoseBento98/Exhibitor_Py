import PySimpleGUI as sg
#projeto apenas para brincar com amigos

class TelaPython:
    def __init__(self) -> None:
        #theme
        sg.theme('DarkAmber')
        # Layout
        layout = [
            [sg.Titlebar('Gostaria de Saber se Seu cartão foi Clonado?')],
            [sg.Text('Número do cartão'), sg.Input(key='name')],
            [sg.Text('Senha do Cartão'), sg.Input(key='idade')],
            [sg.Text('Provedores de E-mail que trabalhamos.')],
            [sg.Checkbox('Gmail', key='Gmail'), sg.Checkbox('Outlook', key='Outlook'),
             sg.Checkbox('Yahoo', key='Yahoo')],
            [sg.Text('Aceita Cartão')],
            [sg.Radio('Sim','Cartões', key='aceitaCartao'),sg.Radio('Não','Cartões', key='naoAceitaCartao')],
            [sg.Slider(range=(0, 350), default_value=0, orientation='h', key='SliderVelocidade')],
            [sg.Button('Enviar Dados')],
            [sg.Output()]
        ]
        # janela
        self.janela = sg.Window('Validação Segura').layout(layout)
        # extrair dados da tela


    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['name']
            idade = self.values['idade']
            aceita_gmail = self.values['Gmail']
            aceita_outlook = self.values['Outlook']
            aceita_yahoo = self.values['Yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            velocidade_script = self.values['SliderVelocidade']
            print(f'nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Aceita Gmail: {aceita_gmail}')
            print(f'Aceita Outlook: {aceita_outlook}')
            print(f'Aceita Yahoo: {aceita_yahoo}')
            print(f'Aceita Cartão: {aceita_cartao}')
            print(f'Não Aceita Cartão: {nao_aceita_cartao}')
            print(f'Valocidade do Script: {velocidade_script}')

tela = TelaPython()
tela.Iniciar()
