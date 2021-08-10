# -*- coding: utf-8 -*-
import requests
import os

os.system('cls')
wbh = input('Cole o Webhooks: ')
while True:
    os.system('cls')
    escUser = input('( Finalizazr CTLR + C )\n\nMensagem:\n')

    payload = '{"content":"'+ escUser +'"}'
    r1 = requests.post(wbh, data=payload, headers={"content-type":"application/json"})

    s = os.system('cls')