from tkinter import*
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text=text1,src=src1,dest=dest1)
    return trans1.text

def data():
    s=comb_sor.get()
    d=comb_dest.get()
    msg=Sor_txt.get(1.0,END)
    print (msg)
    textget=change(text=msg,src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)


root= Tk()
root.title("Translator")
root.geometry("500x600")
root.config(bg='#36393F')

lab_txt=Label(root, text="Translator",font=("Uni Sans", 40,"bold"),bg='#36393F',fg='white')
lab_txt.place(x=100,y=30,height=50,width=300)

frame=Frame(root).pack(side=BOTTOM)

lab_txt=Label(root, text="Source Text",font=("Uni Sans", 20,"bold"),bg='#36393F',fg='#FF6347')
lab_txt.place(x=100,y=100,height=20,width=300)

Sor_txt= Text(frame, font=("Uni Sans", 15,"bold"), wrap=WORD,bg='#1a1b1c',fg='white',insertbackground='white')
Sor_txt.place(x=10,y=130,height=150,width=480)

list_text=list(LANGUAGES.values())

comb_sor=ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=300,height=30,width=150)
comb_sor.set("English")


button_change=Button(frame,text="Translate", relief=RAISED,bg='#5865F2',command=data)
button_change.place(x=170,y=300,height=33,width=150)

comb_dest=ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330,y=300,height=30,width=150)
comb_dest.set("English")

lab_txt=Label(root, text="Destination Text",font=("Uni Sans", 20,"bold"),bg='#36393F',fg='#FF6347')
lab_txt.place(x=100,y=370,height=20,width=300)

dest_txt= Text(frame, font=("Uni Sans", 15,"bold"), wrap=WORD,bg='#1a1b1c',fg='#57f287',insertbackground='#57f287')
dest_txt.place(x=10,y=400,height=150,width=480)


root.mainloop()
    