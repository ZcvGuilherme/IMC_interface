import tkinter as tk 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()

class validadores:
    def validate_entry11(self, text):
        if text == '': return True
        allowed_characters = set('0123456789.')

        for char in text:
            if char not in allowed_characters:
                return False
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 10000

class Funcs(validadores):
 def limpa_tela(self):
    self.peso_entry.delete(0, END)
    self.altura_entry.delete(0, END)
    self.nome_entry.delete(0, END)

 def limpa_lista(self):
        self.lista1.heading.delete(0, END)


class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.botoes()
        self.lista_frame2()
        self.validaEntradas()
        root.mainloop()

    def tela(self):
        self.root.title('Calculadora IMC')
        self.root.configure(background= '#800000')
        self.root.geometry('800x700')
        self.root.resizable(True, True)
        self.root.maxsize(width= 900, height= 780)
        self.root.minsize(width=400, height=300)

    def frames_da_tela(self):
        self.frame1 = Frame(self.root, bd= 4, bg= '#87CEFA', highlightbackground= '#708090',
                            highlightthickness = 6 )
        self.frame1.place(relx=0.1 , rely=0.1, relwidth=0.81, relheight=0.3)

        self.frame2 = Frame(self.root, bd= 4, bg= '#87CEFA', highlightbackground= '#708090',
                             highlightthickness = 6)
        self.frame2.place(relx=0.1, rely=0.5, relwidth=0.81, relheight=0.3)

    def botoes(self):
        ###Criar botoes: limpar e calcular
        #botao limpar 
        self.bt_limpar = Button(self.frame1, text='Limpar', bd=4, bg= '#E9967A', fg='#8B4513',
                                font=('courier', 20, 'italic', 'bold'), command= self.limpa_tela)
        self.bt_limpar.place(relx=0.7, rely=0.7, relheight=0.2, relwidth=0.2)
        #----------------------------------------------------------------------------------------#
        #botao calcular
        self.bt_calcular = Button(self.frame1, text='Calcular', bd=6, bg='#FFE4C4', font=('arial',
                             20, 'bold' ),
                             command= self.calcular_imc)
        self.bt_calcular.place(relx=0.35, rely=0.7, relheight=0.3, relwidth=0.3)
#----------------------------------------------------------------------------------------#
       # label peso
        self.lb_peso = Label(self.frame1, text = 'PESO', font=('MS Sans Serif',16, 'bold'))
        self.lb_peso.place(relx=0.1, rely=0.1, relheight=0.2, relwidth=0.2)
        self.peso_entry = Entry(self.frame1, font=('Corbel', 16, 'italic'), bd= 4)
        self.peso_entry.place(relx=0.1, rely=0.4, relheight=0.2, relwidth=0.2)
        #----------------------------------------------------------------------------------------#
       #label altura 
        self.lb_altura = Label(self.frame1, text = 'ALTURA', font=('MS Sans Serif', 16, 'bold'))
        self.lb_altura.place(relx=0.4, rely=0.1, relheight=0.2, relwidth=0.2)
        self.altura_entry = Entry(self.frame1, font=('Corbel', 16, 'italic'), bd= 4)
        self.altura_entry.place(relx=0.4, rely=0.4, relheight=0.2, relwidth=0.2)
        #----------------------------------------------------------------------------------------#
        #label Nome 
        self.lb_nome = Label(self.frame1, text = 'NOME', font=('MS Sans Serif', 16, 'bold'))
        self.lb_nome.place(relx=0.7, rely=0.1, relheight=0.2, relwidth=0.2)
        self.nome_entry = Entry(self.frame1, font=('Calibri Light', 16, 'italic', 'bold'), bd= 4)
        self.nome_entry.place(relx=0.7, rely=0.4, relheight=0.2, relwidth=0.2)
        #----------------------------------------------------------------------------------------#

    def calcular_imc(self):

       peso = float(self.peso_entry.get())
       altura = float(self.altura_entry.get())

       if altura == 0:
           messagebox.showerror('ERRO', 'A altura não pode ser zero')
           return
    
       imc = peso / (altura**2)

       if imc < 18.5:
           situacao = 'Abaixo do peso'
       elif 18.5 <= imc < 25:
           situacao = 'Peso normal'
       elif 25 <= imc < 30:
           situacao = 'Acima do peso'
       else:
           situacao = 'Obeso'

       nome = self.nome_entry.get()
       self.lista1.insert('', 'end', values=(imc, nome, situacao))
    

    def lista_frame2(self):
        self.lista1 = ttk.Treeview(self.frame2, height= 3, column=('coll1', 'coll2', 'coll3'))
        self.lista1.heading('#0', text='')
        self.lista1.heading('#1', text='IMC')
        self.lista1.heading('#2', text='NOME')
        self.lista1.heading('#3', text='SITUAÇÃO')

        self.lista1.column('#0', width=1)
        self.lista1.column('#1', width=125)
        self.lista1.column('#2', width=125)
        self.lista1.column('#3', width=150)

        self.lista1.place(relx=0.01, rely=0.01, relheight=0.99, relwidth=0.95)



        self.scroollista  = Scrollbar(self.frame2, orient='vertical', command=self.lista1.yview)
        self.lista1.configure(yscrollcommand=self.scroollista.set)
        self.scroollista.place(relx=0.96, rely=0.01, relwidth=0.04, relheight=0.99)

        #----------------------------------------------------------------------------------------#
    
    

    def validaEntradas(self):
        self.vcmd11 = (self.root.register(self.validate_entry11), '%P')
        self.principal_entry = Entry(self.frame1, font=('Calibri Light', 40, 'bold'), validate= 'key', validatecommand= self.vcmd11)





Application()