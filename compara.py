from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#ef5350"  # vermelha

janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

poke_nome = Label(frame_pokemon, text='poke teste', relief='flat', anchor=CENTER, font=('Fixedsys 20'), bg=co1, fg=co0)
poke_nome.place(x=12, y=15)

poke_tipo = Label(frame_pokemon, text='poke tipo', relief='flat', anchor=CENTER, font=('Ivy 10'), bg=co1, fg=co0)
poke_tipo.place(x=12, y=50)

poke_id = Label(frame_pokemon, text='#001', relief='flat', anchor=CENTER, font=('Ivy 10'), bg=co1, fg=co0)
poke_id.place(x=12, y=75)

poke_imagem = Image.open('imagens/001.png')
poke_imagem = poke_imagem.resize((238, 238))
poke_imagem = ImageTk.PhotoImage(poke_imagem)

poke_imagem_label = Label(frame_pokemon, image=poke_imagem, relief='flat', bg=co1, fg=co0)
poke_imagem_label.place(x=60, y=50)

janela.mainloop()
