#utilizando Lib Tkinter para elaboração de janelas interativas e personalizadas para analise de Dados

#importando Lib e seus recursos
import customtkinter as ctk
from tkinter import *

#costumizando temas
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

#costumizando janelas
janela = ctk.CTk()
janela.geometry('730x400')
janela.title('Midnight Analise')
janela.resizable(False, False)

#exportando o Icone
janela.iconbitmap('icon.ico')

#trabalhando com a Imagem da tela
img = PhotoImage(file='new-image_resized.png')
label_img = Label(master=janela, image=img)
label_img.place(x=5, y=65)

label_tt = ctk.CTkLabel(master=janela, text="Welcome to Smart Database",
                                  font=ctk.CTkFont(family='Roboto',size=18),
                                  text_color='#00B0F0').place(x=60, y=10)
#frame
frame = ctk.CTkFrame(master=janela, width=350, height=396)
frame.pack(side=RIGHT)

#frame widgets/ Ajustando Fontes
label = ctk.CTkLabel(master=frame, text='Sistema de Analise de Dados',
                               font=ctk.CTkFont(family='Roboto', size=20))
label.place(x=40, y=5)

entry1 = ctk.CTkEntry(master=frame, placeholder_text='Nome de Usuario', width=300,
                               font=ctk.CTkFont(family='Roboto', size=15)).place(x=25, y=105)
label1 = ctk.CTkLabel(master=frame, text='* Campo Obrigatorio.', text_color='green',
                               font=ctk.CTkFont(family='Roboto', size=10)).place(x=30, y=135)

entry2 = ctk.CTkEntry(master=frame, placeholder_text='Senha do Usuario', width=300,
                               font=ctk.CTkFont(family='Roboto', size=15), show='*').place(x=25, y=175)
label2 = ctk.CTkLabel(master=frame, text='* Campo Obrigatorio.', text_color='green',
                               font=ctk.CTkFont(family='Roboto', size=10)).place(x=30, y=205)

chekbox = ctk.CTkCheckBox(master=frame, text='Salvar Acesso').place(x=25, y=235)

button = ctk.CTkButton(master=frame, text='LOGUIN', width=300). place(x=25, y=285)



janela.mainloop()
