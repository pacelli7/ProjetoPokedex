from tkinter import *
from tkinter import ttk

#importando pillow
from PIL import Image, ImageTk


#cores#
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#ef5350"   # vermelha

#cria janela
janela = Tk()
janela.title ('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

#criar frame

frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

#nome
poke_nome = Label(frame_pokemon, text='Bulbasaur ', relief='flat', anchor=CENTER, font=('Fixedsys 20'), bg=co1, fg=co0)
poke_nome.place(x=12, y=15)

#categoria
poke_tipo = Label(frame_pokemon, text='Grass / Poison', relief='flat', anchor=CENTER, font=('Fixedsys 10'), bg=co1, fg=co0)
poke_tipo.place(x=12, y=50)

#ID
poke_id = Label(frame_pokemon, text='#001', relief='flat', anchor=CENTER, font=('Fixedsys 10'), bg=co1, fg=co0)
poke_id.place(x=12, y=75)

#poke imagem
poke_imagem = Image.open('imagens/001.png')
poke_imagem = poke_imagem.resize((238, 238))
poke_imagem = ImageTk.PhotoImage(poke_imagem)

poke_imagem_label = Label(frame_pokemon, image=poke_imagem, relief='flat', bg=co1, fg=co0)
poke_imagem_label.place(x=150, y=60)

#status
poke_status = Label(janela, text='STATUS', relief='flat', anchor=CENTER, font=('Fixedsys 20 bold'), bg=co1, fg=co0)
poke_status.place(x=15, y=310)

#info
poke_info = Label(janela, text='Altura: 0,7 m \n Peso: 6,9Kg \n Gender: \u26A5 ',  relief='flat', anchor=CENTER, font=('Fixedsys 10'), bg=co1, fg=co4)
poke_info.place(x=15, y=360)

#habilidade
poke_habilit = Label(janela, text='Habilidade', relief='flat', anchor=CENTER, font=('Fixedsys 20 bold'), bg=co1, fg=co0)
poke_habilit.place(x=180, y=310)

#info
poke_infoh = Label(janela, text='Overgrow \n Chlorophyll',  relief='flat', anchor=CENTER, font=('Fixedsys 10'), bg=co1, fg=co4)
poke_infoh.place(x=180, y=360)

janela.mainloop()
