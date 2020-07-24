from tkinter import *
import tkinter.messagebox as MessageBox
import sqlite3 as lit
from sqlCreate import Database

db=Database('projet.db')

def open_window():
    top=Toplevel()
    top.title("Filière")
    top.geometry("500x300")

    def get_data1():
        list_app1.delete(0,END)
        for row in db.fetch2():
            list_app1.insert(END,row)
    
    def ajouter1():
        if(Idfiliere1_text.get()=="" or nomFil_text.get()==""):
            MessageBox.showerror("Insert Status", "Tous les champs doivent être remplis")
            return
        
        db.insertFel(Idfiliere1_text.get(), nomFil_text.get())
        
        list_app1.delete(0,END)
        list_app1.insert(END, (Idfiliere1_text.get(), nomFil_text.get()))
        reset1()
        get_data1()
    
    def select_item1(event):
        global selectected_item1
        index=list_app1.curselection()[0]
        selectected_item1=list_app1.get(index)
        
        Idfiliere1_entry.delete(0,END)
        Idfiliere1_entry.insert(END, selectected_item1[0])
        nomFil_entry.delete(0,END)
        nomFil_entry.insert(END, selectected_item1[1])
    
    def supprimer1():
        msg=MessageBox.askquestion('Delete Status','Vous êtes sûr que vous voulez supprimer cette filière?')
        if msg=='yes':
            db.removeFel(selectected_item1[0])
            get_data1()
            reset1()
        else:
            MessageBox.showinfo('Return','Vous retournerez maintenant à l\'application!')

    def modifier1():
        db.updateFel(selectected_item1[0], nomFil_text.get())
        get_data1()

    def reset1():
        Idfiliere1_entry.delete(0,END)
        nomFil_entry.delete(0,END)


    #Idfiliere
    Idfiliere1_text=StringVar()
    Idfiliere1_label=Label(top, text='Id filiere', font=('bold',14))
    Idfiliere1_label.grid(row=0, column=0, sticky=W)
    Idfiliere1_entry=Entry(top, textvariable=Idfiliere1_text)
    Idfiliere1_entry.grid(row=0, column=1)
    #nomFil
    nomFil_text=StringVar()
    nomFil_label=Label(top, text=str(' '+'Nom de Filière'), font=('bold',14))
    nomFil_label.grid(row=0, column=2, sticky=W)
    nomFil_entry=Entry(top, textvariable=nomFil_text)
    nomFil_entry.grid(row=0, column=3)
    #Buttons
    add_btn=Button(top,bg='#d3d3d3', text='Ajouter',width=12,command=ajouter1)
    add_btn.grid(row=3,column=0, pady=20, padx=10)

    supp_btn=Button(top, bg='#d3d3d3', text='Supprimer',width=12,command=supprimer1)
    supp_btn.grid(row=3,column=1, pady=20)

    modif_btn=Button(top,bg='#d3d3d3', text='Modifer',width=12,command=modifier1)
    modif_btn.grid(row=3,column=2, pady=20)

    clr_btn=Button(top,bg='#d3d3d3', text='Reset',width=12,command=reset1)
    clr_btn.grid(row=3,column=3, pady=20)
    
    back_btn=Button(top,bg='#817679',activebackground='#FAAFBE', text="Table d'étudiants", width=12,command=top.destroy)
    back_btn.grid(row=10,column=0)
    #listbox
    list_app1=Listbox(top,height=8,width=50, border=5)
    list_app1.grid(row=4,column=0, columnspan=4, rowspan=6, pady=20, padx=20)
    #Create scrollbar
    scrollbar1=Scrollbar(top)
    scrollbar1.grid(row=4,column=3)
    #Set scroll to listbox
    list_app1.configure(yscrollcommand=scrollbar.set)
    scrollbar1.configure(command=list_app1.yview)
    get_data1()
    #bind select
    list_app1.bind('<<ListboxSelect>>',select_item1)
    
    

def get_data():
    list_app.delete(0,END)
    for row in db.fetch1():
        list_app.insert(END,row)

def ajouter():
    if(idEtudiant_text.get()=="" or Idfiliere_text.get()=="" or lname_text.get()=="" or fname_text.get()=="" or age_text.get()==""):
        MessageBox.showerror("Insert Status", "Tous les champs doivent être remplis")
        return
    db.inFiliere(Idfiliere_text.get())
    db.insertEtu(idEtudiant_text.get(), Idfiliere_text.get(),lname_text.get(), fname_text.get(), age_text.get())
    
    list_app.delete(0,END)
    list_app.insert(END, (idEtudiant_text.get(), Idfiliere_text.get(),lname_text.get(), fname_text.get(), age_text.get()))
    reset()
    get_data()

def select_item(event):
    global selectected_item
    index=list_app.curselection()[0]
    selectected_item=list_app.get(index)
    
    idEtudiant_entry.delete(0,END)
    idEtudiant_entry.insert(END, selectected_item[0])
    Idfiliere_entry.delete(0,END)
    Idfiliere_entry.insert(END, selectected_item[1])
    lname_entry.delete(0,END)
    lname_entry.insert(END, selectected_item[2])
    fname_entry.delete(0,END)
    fname_entry.insert(END, selectected_item[3])
    age_entry.delete(0,END)
    age_entry.insert(END, selectected_item[4])
    

def supprimer():
    msg=MessageBox.askquestion('Delete Status','Vous êtes sûr que vous voulez supprimer cet étudiant?')
    if msg=='yes':
        db.removeEtu(selectected_item[0])
        get_data()
        reset()
    else:
        MessageBox.showinfo('Return','Vous retournerez maintenant à l\'application!')

def modifier():
    db.updateEtud(selectected_item[0], Idfiliere_text.get(),lname_text.get(), fname_text.get(), age_text.get())
    get_data()

def reset():
    idEtudiant_entry.delete(0,END)
    Idfiliere_entry.delete(0,END)
    lname_entry.delete(0,END)
    fname_entry.delete(0,END)
    age_entry.delete(0,END)

app=Tk()


#idEtudiant
idEtudiant_text=StringVar()
idEtudiant_label=Label(app, text='Id étudiant', font=('bold',14), pady=20)
idEtudiant_label.grid(row=0, column=0, sticky=W)
idEtudiant_entry=Entry(app, textvariable=idEtudiant_text)
idEtudiant_entry.grid(row=0, column=1)
#Idfiliere
Idfiliere_text=StringVar()
Idfiliere_label=Label(app, text='Id filiere', font=('bold',14))
Idfiliere_label.grid(row=0, column=2, sticky=W)
Idfiliere_entry=Entry(app, textvariable=Idfiliere_text)
Idfiliere_entry.grid(row=0, column=3)
#lname
lname_text=StringVar()
lname_label=Label(app, text='Nom', font=('bold',14))
lname_label.grid(row=1, column=0, sticky=W)
lname_entry=Entry(app, textvariable=lname_text)
lname_entry.grid(row=1, column=1)
#fname
fname_text=StringVar()
fname_label=Label(app, text='Prénom', font=('bold',14))
fname_label.grid(row=1, column=2, sticky=W)
fname_entry=Entry(app, textvariable=fname_text)
fname_entry.grid(row=1, column=3)
#age
age_text=StringVar()
age_label=Label(app, text='Age', font=('bold',14),pady=10)
age_label.grid(row=2, column=0, sticky=W)
age_entry=Entry(app, textvariable=age_text)
age_entry.grid(row=2, column=1)
#listbox
list_app=Listbox(app,height=8,width=50, border=5)
list_app.grid(row=4,column=0, columnspan=4, rowspan=6, pady=10, padx=20)
#Create scrollbar
scrollbar=Scrollbar(app)
scrollbar.grid(row=4,column=3)
#Set scroll to listbox
list_app.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_app.yview)
get_data()
#bind select
list_app.bind('<<ListboxSelect>>',select_item)

#Buttons
add_btn=Button(app,bg='#d3d3d3', text='Ajouter',width=12,command=ajouter)
add_btn.grid(row=3,column=0, pady=20, padx=20)

supp_btn=Button(app, bg='#d3d3d3', text='Supprimer',width=12,command=supprimer)
supp_btn.grid(row=3,column=1, pady=20)

modif_btn=Button(app,bg='#d3d3d3', text='Modifer',width=12,command=modifier)
modif_btn.grid(row=3,column=2, pady=20)

clr_btn=Button(app,bg='#d3d3d3', text='Reset',width=12,command=reset)
clr_btn.grid(row=3,column=3, pady=20)

next_btn=Button(app,bg='goldenrod1',activebackground='green', text='table de filère', width=12,command=open_window)
next_btn.grid(row=10,column=3)



app.title('Mini-projet DSE Achraf BALIJ')
app.geometry('520x400')


app.mainloop()