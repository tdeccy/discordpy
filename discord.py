# -*- coding: utf-8 -*-
import requests
import os

s = os.system('cls')
#https://discord.com/api/webhooks/867855034418724938/zar74u8Ai8w85Xs3fh3-pQDfxAlm38hvEZSftsMfLkuG6zbhZgZ5-ukcfXtPOMXoxK_B
wbc = input('Webhooks: ')
escUser = input('Mensagem:\n')

payload = '{"content":"'+escUser+'"}'
r1 = requests.post(wbc, data=payload, headers={"content-type":"application/json"})

s = os.system('cls')
print('Mensagem enviada foi:\n',escUser)