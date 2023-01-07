# utilizando Lib Tkinter para elaboração de janelas interativas e personalizadas para analise de Dados

# importando Lib e seus recursos
import customtkinter as ctk
from tkinter import *

janela = ctk.CTk()


class Application():
    def __int__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.tela_loguin()
        janela.mainloop()

    def tema(self):
        # costumizando temas
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')

    def tela(self):
        # costumizando janelas
        janela.geometry('730x400')
        janela.title('Midnight Analise')
        janela.resizable(False, False)

    def tela_loguin(self):
        # exportando o Icone
        janela.iconbitmap('icon.ico')
        # trabalhando com a Imagem da tela
        img = PhotoImage(file='new-image_resized.png')
        label_img = Label(master=janela, image=img)
        label_img.place(x=5, y=65)

        label_tt = ctk.CTkLabel(master=janela, text="Welcome to Smart Database",
                                font=ctk.CTkFont(family='Roboto', size=18),
                                text_color='#00B0F0').place(x=60, y=10)
        # frame de entrada
        loguin_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        loguin_frame.pack(side=RIGHT)

        # frame widgets (Dentro do Frame da tela de Loguin) / Ajustando Fontes
        title_label = ctk.CTkLabel(master=loguin_frame, text='Sistema de Analise de Dados',
                                   font=ctk.CTkFont(family='Roboto', size=20))
        title_label.place(x=40, y=5)

        # Entradas e Rotulos do Loguin
        username_entry = ctk.CTkEntry(master=loguin_frame, placeholder_text='Nome de Usuario', width=300,
                                      font=ctk.CTkFont(family='Roboto', size=15)).place(x=25, y=105)
        username_label = ctk.CTkLabel(master=loguin_frame, text='* Campo Obrigatorio.', text_color='green',
                                      font=ctk.CTkFont(family='Roboto', size=10)).place(x=30, y=135)
        #Entradas e Rotulos de Senha
        password_entry = ctk.CTkEntry(master=loguin_frame, placeholder_text='Senha do Usuario', width=300,
                                      font=ctk.CTkFont(family='Roboto', size=15), show='*').place(x=25, y=175)
        password_label = ctk.CTkLabel(master=loguin_frame, text='* Campo Obrigatorio.', text_color='green',
                                      font=ctk.CTkFont(family='Roboto', size=10)).place(x=30, y=205)

        chekbox = ctk.CTkCheckBox(master=loguin_frame, text='Salvar Acesso').place(x=25, y=235)

        loguin_button = ctk.CTkButton(master=loguin_frame, text='LOGUIN', width=300).place(x=25, y=285)


Application()
