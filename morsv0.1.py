import random
import vlc
import time
from tkinter import *



window = Tk()
window.title("mors egzersiz")



numlist = ["a","b","c","d","e","f","g","h","ı","j","k","l","m","n","o","p","r","s","t","u","v","y","z"]
morslist = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.",".-.","...","-","..-","...-","-.--","--.."]

AP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/a.mp3")
BP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/b.mp3")
CP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/c.mp3")
DP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/d.mp3")
EP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/e.mp3")
FP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/f.mp3")
GP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/g.mp3")
HP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/h.mp3")
IP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/ı.mp3")
JP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/j.mp3")
KP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/k.mp3")
LP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/l.mp3")
MP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/m.mp3")
NP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/n.mp3")
OP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/o.mp3")
PP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/p.mp3")
RP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/r.mp3")
SP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/s.mp3")
TP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/t.mp3")
UP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/u.mp3")
VP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/v.mp3")
YP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/y.mp3")
ZP = vlc.MediaPlayer("C:/Users/altay/Desktop/mors/ses/z.mp3")











while True:
    rastgele = random.randint(0,len(morslist)-1)

    b = (morslist[rastgele])
    print(b)
    a = (numlist[rastgele])
    if(a == "a"):
        AP.play()
        time.sleep(3)
        AP.stop()
    elif(a == "b"):
        BP.play()
        time.sleep(3)
        BP.stop()
    elif(a == "c"):
        CP.play()
        time.sleep(3)
        CP.stop()
    elif(a == "d"):
        DP.play()
        time.sleep(3)
        DP.stop()
    elif(a == "e"):
        EP.play()
        time.sleep(3)
        EP.stop()
    elif(a == "f"):
        FP.play()
        time.sleep(3)
        FP.stop()
    elif(a == "g"):
        GP.play()
        time.sleep(3)
        GP.stop()
    elif(a == "h"):
        HP.play()
        time.sleep(3)
        HP.stop()
    elif(a == "ı"):
        IP.play()
        time.sleep(3)
        IP.stop()
    elif(a == "j"):
        JP.play()
        time.sleep(3)
        JP.stop()
    elif(a == "k"):
        KP.play()
        time.sleep(3)
        KP.stop()
    elif(a == "l"):
        LP.play()
        time.sleep(3)
        LP.stop()
    elif(a == "m"):
        MP.play()
        time.sleep(3)
        MP.stop()
    elif(a == "n"):
        NP.play()
        time.sleep(3)
        NP.stop()
    elif(a == "o"):
        OP.play()
        time.sleep(3)
        OP.stop()
    elif(a == "p"):
        PP.play()
        time.sleep(3)
        PP.stop()
    elif(a == "r"):
        RP.play()
        time.sleep(3)
        RP.stop()
    elif(a == "s"):
        SP.play()
        time.sleep(3)
        SP.stop()
    elif(a == "t"):
        TP.play()
        time.sleep(3)
        TP.stop()
    elif(a == "u"):
        UP.play()
        time.sleep(3)
        UP.stop()
    elif(a == "v"):
        VP.play()
        time.sleep(3)
        VP.stop()
    elif(a == "y"):
        YP.play()
        time.sleep(3)
        YP.stop()
    elif(a == "z"):
        ZP.play()
        time.sleep(3)
        ZP.stop()


    c =("")
    
    
    def submit():
        global c
        c = entry.get()

    def click():
        print("nothing")

    def delete():
        entry.delete(len(entry.get())-1,END)

    entry = Entry(window,font=("Arial",50))
    entry.pack(side=LEFT)

    submit_button = Button(window,text="submit",command=submit)
    submit_button.pack(side=RIGHT)

    delete_button = Button(window,text="delete",command=delete)
    delete_button.pack(side=RIGHT)

    donate_button = Button(window,text="Click if you want to donate",command=click)
    donate_button.pack(side=RIGHT)
    
    
    if(c == a):
        print("doğru")
    else:
        print("yanlış")
    window.mainloop()
