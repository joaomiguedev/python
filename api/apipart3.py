from tkinter import Tk
from tkinter.ttk import Combobox
from tkinter import Entry,Label,Button,StringVar,messagebox
import requests

root = Tk()
root.geometry('400x300')
root.title('API in tkinter')
root.resizable(False, False)

def tradutor(val):
    if val=="EUR - Euro":
        return "EUR"
    elif val=="USD - Dólar americano":
        return "USD"
    elif val=="BRL - Real brasileiro":
        return "BRL"
    elif val=="JPY - Iene japonês":
        return "JPY"
    elif val=="RUB - Rublo russo":
        return "RUB"
    elif val=="GBP - Libra esterlina":
        return "GBP"
    else :
        return None
    
def Submit():
    moeda1=tradutor(Combobox1.get())
    moeda2=tradutor(Combobox2.get())
    
    if moeda1 == moeda2:
       messagebox.showerror("ERROR","http://economia.awesomeapi.com.br/json/last/{moeda1}-{moeda2} é moeda1 == moed2 é 100% Error")
    else:
        nome_do_API=f'http://economia.awesomeapi.com.br/json/last/{moeda1}-{moeda2}'
        url=requests.get(nome_do_API)
        data=url.json()
        data_moeda=float(data[f'{moeda1}{moeda2}']['bid'])

        try:
            Label1.configure(text=f"Amount: {float(Entry1.get())*data_moeda}")
        except ValueError:
            messagebox.showerror("ERROR","pls put numero")

bt1=Button(root,text="Submit",command=Submit)
bt1.place(x=170,y=260)

selected_value = StringVar()

Combobox1=Combobox(root, values=["EUR - Euro", "USD - Dólar americano", "BRL - Real brasileiro","JPY - Iene japonês","RUB - Rublo russo","GBP - Libra esterlina"])
Combobox1.place(x=10,y=200)

Combobox1['state'] = 'readonly'

Combobox2=Combobox(root, values=["EUR - Euro", "USD - Dólar americano", "BRL - Real brasileiro","JPY - Iene japonês","RUB - Rublo russo","GBP - Libra esterlina"])
Combobox2.place(x=240,y=200)

Combobox2['state'] = 'readonly'

Entry1=Entry(root)
Entry1.place(x=10, y=150)

Label1=Label(root, text="Amount:")
Label1.place(x=240, y=150)

ladel2=Label(root,text="BY joaomigue3790")
ladel2.place(x=296,y=284)

root.mainloop()