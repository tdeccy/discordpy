# -*- coding: utf-8 -*-
import os
import requests
from tkinter import *
from requests.sessions import merge_setting
from datetime import date, datetime

janela = Tk()
janela.geometry('250x100+100+100')

def avisoG():
    os.system('cls')
    print("""
    #############################-0604-#############################
    # Um simples script com interface feito em py3 usando tkinter  #
    # Aqui voce tera o log de mensagens com data/hora/ mensagem    #
    # Ex: [YYYY-MM-DD] [Mesangem] Bom dia                          #
    # by: SlimFord#0404 (AKA: deccy/tgam)                          #
    #############################-0404-#############################
    """)
avisoG()


def enviarMsg():
    linkHook = escUserWB.get()
    sendMsg = msgUser.get()
    payload = '{"content":"'+ sendMsg +'"}'
    r1 = requests.post(linkHook, data=payload, headers={"content-type":"application/json"})
    print(datetime.today().strftime(f'[%Y-%m-%d | %H:%M] [Mesangem] {sendMsg}'))


lb1 = Label(janela, text='WebHook Link: ')
lb1.grid(row=0, column=0)
escUserWB = Entry(janela) 
escUserWB.grid(row=0, column=1)

lb2 = Label(janela, text='Mesagem: ')
lb2.grid(row=1,column=0)
msgUser = Entry(janela)
msgUser.grid(row=1,column=1)

bt2 = Button(janela, text='Enviar Mensagem', command=enviarMsg)
bt2.grid(row=3,column=1)


janela.mainloop()