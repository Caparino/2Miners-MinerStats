import tkinter as tk
from tkinter import *
import requests

HEIGHT = 500
WIDTH = 600

def test_function(entry):
	print("This is the entry:", entry)

def format_response(stats):
    try:
        CMH = round(int(stats['currentHashrate']) / 1000000, 2)
        AMH = round(int(stats['hashrate']) / 1000000, 2)
        income = round(int(stats['24hreward']) / 1000000000, 5)
        balance = round(int(stats['stats']['balance']) / 1000000000, 5)
        workers = (stats['workersOnline'])
        final_str = 'Workers Online: %s \nCurrent Hashrate: %s \nAverage Hashrate: %s \n24Hr Income: %s \nUnpaid Balance: %s ' % (
        workers, CMH, AMH, income, balance)
    except:
        final_str = 'There was a problem retrieving that information'
    return final_str

twompools = ["AE",
            "BEAM",
            "BTG",
            "BTCZ",
            "CKB",
            "ETC",
            "ETH",
            "ETP",
            "EXP",
            "GRIN",
            "MOAC",
            "PIRL",
            "RVN",
            "XCZ",
            "XMR",
            "ZCL",
            "ZEC",
            "ZEL",
            "ZEN"
]

def get_stats(wallet):
    response = requests.get('https://'+str(tkvarq.get())+'.2miners.com/api/accounts/'+str(entry.get()))
    #print(response.json())
    stats = (response.json())
    label['text'] = format_response(stats)

# def get_stats(wallet):
#     url = 'http://api.bsod.pw/api/wallet'
#     params = {'address': wallet}
#     response = requests.get(url, params=params)
#     stats = (response.json())
#
#     label['text'] = format_response(stats)


#0xe4c9c956c9d8cffec5f01bec09541e4c892dbd15
    # print(stats['currency'])
    # print(stats['balance'])
    # print(stats['paid24h'])
    # print(stats['total'])
# http://api.bsod.pw/api/wallet?address=WALLET_ADDRESS
# http://api.bsod.pw/api/wallet?address=PKReQMTmrwG1RR1b2n9Gx6wTQgKoWRa7gJ
# def format_response(address):
# 	try:
# 		balance = address['balance']
#
# 		final_str = 'Balance: %s' % (balance)
# 	except:
# 		final_str = 'There was a problem retrieving that information'
#
# 	return final_str
#
# def get_stats(address):
# 	weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
# 	url = 'http://api.bsod.pw/api/wallet?address='
# 	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
# 	response = requests.get(url, params=params)
# 	address = response.json()
#
# 	label['text'] = format_response(address)
root = tk.Tk()
root.title('2Miners')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=30)
entry.place(relwidth=0.65, relheight=1)

tkvarq = StringVar(frame)
tkvarq.set(twompools[0])
question_menu = OptionMenu(frame, tkvarq, *twompools)
question_menu.place(relx=0.68, relheight=1, relwidth=0.12)

button = tk.Button(frame, text="Get Stats", font=25, command=lambda: get_stats(entry.get()))
button.place(relx=0.82, relheight=1, relwidth=0.18)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=40, anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()
