from tkinter import *
from tkinter import ttk

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
poke_nome = Label(frame_pokemon, text= 'poke teste', relief='flat', anchor=CENTER, font=('Fixedsys 20'), bg=co1, fg=co0)
poke_nome.place(x=12, y=15)


janela.mainloop()
