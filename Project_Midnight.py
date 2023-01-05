#utilizando Lib Tkinter para elaboração de janelas interativas e personalizadas para analise de Dados

#importando Lib e seus recursos
import customtkinter
from tkinter import *

#costumizando temas
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

#costumizando janelas
janela = customtkinter.CTk()
janela.geometry('730x400')
janela.title('Midnight Analise')
janela.resizable(False, False)

#exportando o Icone
janela.iconbitmap('icon.ico')

#trabalhando com a Imagem da tela
img = PhotoImage(file='new-image_resized.png')
label_img = Label(master=janela, image=img)
label_img.place(x=5, y=65)

label_tt = customtkinter.CTkLabel(master=janela, text="Welcome to Smart Database",
                                  font=customtkinter.CTkFont(family='Roboto',size=18),
                                  text_color='#00B0F0').place(x=60, y=10)
#frame
frame = customtkinter.CTkFrame(master=janela, width=350, height=396)
frame.pack(side=RIGHT)

#frame widgets/ Ajustando Fontes
label = customtkinter.CTkLabel(master=frame, text='Sistema de Analise de Dados',
                               font=customtkinter.CTkFont(family='Roboto', size=20))
label.place(x=40, y=5)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text='Nome de Usuario', width=300,
                               font=customtkinter.CTkFont(family='Roboto', size=15)).place(x=25, y=105)
label1 = customtkinter.CTkLabel(master=frame, text='* Campo Obrigatorio.', text_color='green',
                               font=customtkinter.CTkFont(family='Roboto', size=10)).place(x=30, y=135)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text='Senha do Usuario', width=300,
                               font=customtkinter.CTkFont(family='Roboto', size=15)).place(x=25, y=175)
label2 = customtkinter.CTkLabel(master=frame, text='* Campo Obrigatorio.', text_color='green',
                               font=customtkinter.CTkFont(family='Roboto', size=10)).place(x=30, y=205)

chekbox = customtkinter.CTkCheckBox(master=frame, text='Salvar Acesso').place(x=25, y=235)

button = customtkinter.CTkButton(master=frame, text='LOGUIN', width=300). place(x=25, y=285)



janela.mainloop()
