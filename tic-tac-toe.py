import tkinter as tk

root = tk.Tk()
root.geometry('300x325')
root.title('tic-tac-toe')

a = "x"
listx = []
listo = []
playing = []
botoes = {}
xwin = 0
owin = 0

def check_win(lista):
    wins = [[1,2,3], [4,5,6], [7,8,9],[1,4,7], [2,5,8], [3,6,9],[1,5,9], [3,5,7]]
    return any(all(pos in lista for pos in w) for w in wins)

def tic_tac_toe(val):
    global a, xwin, owin
    if val in playing:
        return
    botoes[val].configure(text=a)

    if a == "x":
        listx.append(val)
        if check_win(listx):
            xwin += 1
            replay()
            return
        a = "o"
    else:
        listo.append(val)
        if check_win(listo):
            owin += 1
            replay()
            return
        a = "x"
    playing.append(val)

def replay():
    global playing, listx, listo, botoes, a
    playing = []
    listx = []
    listo = []
    a = "x"

    for bt in botoes.values():
        bt.destroy()
    botoes = {}


    pos = 1
    for y in range(3):
        for x in range(3):
            bt = tk.Button(root,text="",font=("Arial", 32, "bold"),command=lambda v=pos: tic_tac_toe(v))
            bt.place(x=x*100, y=y*100, width=100, height=100)
            botoes[pos] = bt
            pos += 1

    bt10 = tk.Button(root, text='replay', font=("Arial", 14, "bold"), command=replay)
    bt10.place(x=0, y=300, width=300, height=25)

replay()
root.mainloop()