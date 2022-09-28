from tkinter import *
import mysql1
import datetime

def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    entry1.delete(0, END)
    entry1.insert(END, selected_tuple[0])
    entry2.delete(0, END)
    entry2.insert(END, selected_tuple[1])
    entry3.delete(0, END)
    entry3.insert(END, selected_tuple[2])
    Gender.set(selected_tuple[3])
    entry5.delete(0, END)
    entry5.insert(END, selected_tuple[4])
    entry6.delete(0, END)
    entry6.insert(END, selected_tuple[5])
    if selected_tuple[6]=="ACTIVE":
        b6["bg"]="red"
        changeText()
    else:
        b6["text"]=selected_tuple[6]
        b6["bg"] = "red"

    open_newwin()

def get_selected_rowN(event):
    global selected_tuple2
    index2 = list21.curselection()[0]
    selected_tuple2 = list21.get(index2)
    entry21.delete(0, END)
    entry21.insert(END, selected_tuple2[0])
    entry22.delete(0, END)
    entry22.insert(END, selected_tuple2[1])
    entry23.delete(0, END)
    entry23.insert(END, selected_tuple2[2])
    Gender2.set(selected_tuple2[3])
    entry25.delete(0, END)
    entry25.insert(END, selected_tuple2[4])
    entry26.delete(0, END)
    entry26.insert(END, selected_tuple2[5])
    if selected_tuple2[6]=="ACTIVE":
        b26["bg"]="red"
        changeTextN()
    else:
        b26["text"]=selected_tuple2[6]
        b26["bg"] = "red"
    open_newwinN()

def get_selected_rowP(event):
    global selected_tuple3
    index3 = list31.curselection()[0]
    selected_tuple3 = list31.get(index3)
    entry31.delete(0, END)
    entry31.insert(END, selected_tuple3[1])
    entry32.delete(0, END)
    entry32.insert(END, selected_tuple3[2])
    entry33.delete(0, END)
    entry33.insert(END, selected_tuple3[3])
    Gender3.set(selected_tuple3[4])
    entry35.delete(0, END)
    entry35.insert(END, selected_tuple3[5])
    entry36.delete(0, END)
    entry36.insert(END, selected_tuple3[6])
    entry37.delete(0, END)
    entry37.insert(END, selected_tuple3[7])
    entry38.delete(0, END)
    entry38.insert(END, selected_tuple3[8])
    entry39.delete(0, END)
    entry39.insert(END, selected_tuple3[0])
    if selected_tuple3[9]=='Present':
        b36["bg"]="red"
        changeTextP()
    else:
        b36["text"]=selected_tuple3[9]
        b36["bg"] = "red"
    open_newwinP()

def show_frame(frame):
    frame.tkraise()


def view_command():
    list1.delete(0,END)
    for row in mysql1.view():
        list1.insert(END,row)

def view_commandN():
    list21.delete(0,END)
    for row in mysql1.viewN():
        list21.insert(END,row)

def view_commandP():
    list31.delete(0,END)
    for row in mysql1.viewP():
        list31.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in mysql1.search(name_text.get(),address_text.get(),phone_number_text.get(),Speciality.get(),Gender.get(),Badge_Number.get(),b6['text']):
        list1.insert(END,row)

def search_commandN():
    list21.delete(0,END)
    for row in mysql1.searchN(name_text2.get(),address_text2.get(),phone_number_text2.get(),Patient_Assigned2.get(),Gender2.get(),Badge_Number2.get(),b26['text']):
        list21.insert(END,row)

def search_commandP():
    list31.delete(0,END)
    for row in mysql1.searchP(uhid3.get(),name_text3.get(),address_text3.get(),phone_number_text3.get(),Nurse_Assigned3.get(),Attendent3.get(),Gender3.get(),Date_of_admit3.get(),Date_of_Departure3.get(),b36['text']):
        list31.insert(END,row)

def add_command():
    mysql1.insert(name_text.get(),address_text.get(),phone_number_text.get(),Gender.get(),Speciality.get(),Badge_Number.get(),b6['text'])
    list1.delete(0,END)
    list1.insert(END,(name_text.get(),address_text.get(),phone_number_text.get(),Gender.get(),Speciality.get(),Badge_Number.get(),b6['text']))

def add_commandN():
    mysql1.insertN(name_text2.get(),address_text2.get(),phone_number_text2.get(),Gender2.get(),Patient_Assigned2.get(),Badge_Number2.get(),b26['text'])
    list21.delete(0,END)
    list21.insert(END,(name_text2.get(),address_text2.get(),phone_number_text2.get(),Gender2.get(),Patient_Assigned2.get(),Badge_Number2.get(),b26['text']))

def add_commandP():
    mysql1.insertP(uhid3.get(),name_text3.get(),address_text3.get(),phone_number_text3.get(),Nurse_Assigned3.get(),Attendent3.get(),Gender3.get(),Date_of_admit3.get(),Date_of_Departure3.get(),b36['text'])
    list31.delete(0,END)
    list31.insert(END,(uhid3.get(),name_text3.get(),address_text3.get(),phone_number_text3.get(),Gender3.get(),Nurse_Assigned3.get(),Attendent3.get(),Date_of_admit3.get(),Date_of_Departure3.get(),b36['text']))

def delete_command():
    mysql1.delete(selected_tuple[5])
    view_command()

def delete_commandN():
    mysql1.deleteN(selected_tuple2[5])
    view_commandN()

def delete_commandP():
    mysql1.deleteP(selected_tuple3[5])
    view_commandP()
def changeText():
    if b6["bg"]=='red':
        b6['text'] = 'ACTIVE'
        b6["bg"]= 'green'
    else:
        b6['text'] = 'NOT ACTIVE'
        b6["bg"]= 'red'

def changeTextN():
    if b26["bg"]=='red':
        b26['text'] = 'ACTIVE'
        b26["bg"]= 'green'
    else:
        b26['text'] = 'NOT ACTIVE'
        b26["bg"]= 'red'

def changeTextP():
    if b36["bg"]=='red':
        b36['text'] = 'Present'
        b36["bg"]= 'green'
    else:
        b36['text'] = 'Left'
        b36["bg"]= 'red'

def update_command():
    mysql1.update(name_text.get(),address_text.get(),phone_number_text.get(),Speciality.get(),Gender.get(),Badge_Number.get(),b6['text'])
    view_command()

def update_commandN():
    mysql1.updateN(name_text2.get(),address_text2.get(),phone_number_text2.get(),Patient_Assigned2.get(),Gender2.get(),Badge_Number2.get(),b26['text'])
    view_commandN()

def update_commandP():
    mysql1.updateP(selected_tuple3[0],name_text3.get(),address_text3.get(),phone_number_text3.get(),Nurse_Assigned3.get(),Attendent3.get(),Gender3.get(),Date_of_admit3.get(),Date_of_Departure3.get(),b36['text'])
    view_commandP()

def clear():
    entry1.delete(0, END)

    entry2.delete(0, END)

    entry3.delete(0, END)

    Gender.set('Other')

    entry5.delete(0, END)

    entry6.delete(0, END)
def clearN():
    entry21.delete(0, END)

    entry22.delete(0, END)

    entry23.delete(0, END)

    Gender.set('Other')

    entry25.delete(0, END)

    entry26.delete(0, END)

def clearP():
    entry31.delete(0, END)

    entry32.delete(0, END)

    entry33.delete(0, END)

    Gender3.set('Other')

    entry35.delete(0, END)

    entry36.delete(0, END)

    entry37.delete(0, END)

    entry38.delete(0, END)

    entry39.delete(0, END)

Font_tuple = ("Comic Sans MS", 20, "bold")

def open_newwin():
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    top= Toplevel()
    top.title("RESULTS")
    top.iconbitmap(f"Dapino-Medical-Hospital.ico")


    label15 = Label(top, text=f"Name={selected_tuple[0]}")
    label15.grid(row=1, column=0)
    label15.configure(font=Font_tuple)
    label13 = Label(top, text=f"Address={selected_tuple[1]}")
    label13.grid(row=2, column=0)
    label13.configure(font=Font_tuple)
    label14 = Label(top, text=f"Phone number={selected_tuple[2]}")
    label14.grid(row=3, column=0)
    label14.configure(font=Font_tuple)
    label12 = Label(top, text=f"Gender={selected_tuple[3]}")
    label12.grid(row=4, column=0)
    label12.configure(font=Font_tuple)
    label16 = Label(top, text=f"Speciality={selected_tuple[4]}")
    label16.grid(row=5, column=0)
    label16.configure(font=Font_tuple)
    label17 = Label(top, text=f"Badge Number= {selected_tuple[5]}")
    label17.grid(row=6, column=0)
    label17.configure(font=Font_tuple)
    label18 = Label(top, text=f"Status= {selected_tuple[6]}")
    label18.grid(row=7, column=0)
    label18.configure(font=Font_tuple)

def open_newwinN():
    global selected_tuple2
    index2 = list21.curselection()[0]
    selected_tuple2 = list21.get(index2)
    top2= Toplevel()
    top2.title("RESULTS")
    top2.iconbitmap(f"Dapino-Medical-Hospital.ico")
    label215 = Label(top2, text=f"Name={selected_tuple2[0]}")
    label215.grid(row=1, column=0)
    label215.configure(font=Font_tuple)
    label213 = Label(top2, text=f"Address={selected_tuple2[1]}")
    label213.grid(row=2, column=0)
    label213.configure(font=Font_tuple)
    label214 = Label(top2, text=f"Phone number={selected_tuple2[2]}")
    label214.grid(row=3, column=0)
    label214.configure(font=Font_tuple)
    label212 = Label(top2, text=f"Gender={selected_tuple2[3]}")
    label212.grid(row=4, column=0)
    label212.configure(font=Font_tuple)
    label216 = Label(top2, text=f"Patient assigned={selected_tuple2[4]}")
    label216.grid(row=5, column=0)
    label216.configure(font=Font_tuple)
    label217 = Label(top2, text=f"Badge Number= {selected_tuple2[5]}")
    label217.grid(row=6, column=0)
    label217.configure(font=Font_tuple)
    label218 = Label(top2, text=f"Status= {selected_tuple2[6]}")
    label218.grid(row=7, column=0)
    label218.configure(font=Font_tuple)

def open_newwinP():
    global selected_tuple3
    index3 = list31.curselection()[0]
    selected_tuple3 = list31.get(index3)
    top3= Toplevel()
    top3.title("RESULTS")
    top3.iconbitmap(f"Dapino-Medical-Hospital.ico")
    label314 = Label(top3, text=f"UHID={selected_tuple3[0]}")
    label314.grid(row=1, column=0)
    label314.configure(font=Font_tuple)
    label315 = Label(top3, text=f"Name={selected_tuple3[1]}")
    label315.grid(row=2, column=0)
    label315.configure(font=Font_tuple)
    label313 = Label(top3, text=f"Address={selected_tuple3[2]}")
    label313.grid(row=3, column=0)
    label313.configure(font=Font_tuple)
    label314 = Label(top3, text=f"Phone number={selected_tuple3[3]}")
    label314.grid(row=4, column=0)
    label314.configure(font=Font_tuple)
    label312 = Label(top3, text=f"Gender={selected_tuple3[4]}")
    label312.grid(row=5, column=0)
    label312.configure(font=Font_tuple)
    label316 = Label(top3, text=f"Nurse Assigned={selected_tuple3[5]}")
    label316.grid(row=6, column=0)
    label316.configure(font=Font_tuple)
    label317 = Label(top3, text=f"Attendent= {selected_tuple3[6]}")
    label317.grid(row=7, column=0)
    label317.configure(font=Font_tuple)
    label318 = Label(top3, text=f"Date of admit= {selected_tuple3[7]}")
    label318.grid(row=8, column=0)
    label318.configure(font=Font_tuple)
    date_str1 =  selected_tuple3[7]
    format_str1 = '%d/%m/%Y'
    datetime_obj1 = datetime.datetime.strptime(date_str1, format_str1)
    date_str2 = selected_tuple3[8]
    format_str2 = '%d/%m/%Y'
    datetime_obj2 = datetime.datetime.strptime(date_str2, format_str2)
    label3110=Label(top3, text=f"Days admitted={(datetime_obj2.date()-datetime_obj1.date()).days}")
    label3110.grid(row=9, column=0)
    label319 = Label(top3, text=f"Date of Departure={selected_tuple3[8]}")
    label319.grid(row=10, column=0)
    label3171 = Label(top3, text=f"Recipt\n{(datetime_obj2.date()-datetime_obj1.date()).days * 2000}rs for Room\n 1000 rs per day as doctor fee \n Total= {((datetime_obj2.date()-datetime_obj1.date()).days * 3000)}rs")
    label3171.grid(row=11, column=0)


root= Tk()
root.title("Hospital Management System")
root.iconbitmap("Dapino-Medical-Hospital.ico")




frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky='nsew')

frame3_btn = Button(frame3, text="Doctor", command=lambda: show_frame(frame1))
frame3_btn.grid(row=0,column=0)

frame2_btn = Button(frame2, text='Patient', command=lambda: show_frame(frame3))
frame2_btn.grid(row=0,column=2)

frame1_btn = Button(frame1, text='Nurse', command=lambda: show_frame(frame2))
frame1_btn.grid(row=0,column=1)

frame2_btn = Button(frame1, text='Patient', command=lambda: show_frame(frame3))
frame2_btn.grid(row=0,column=2)

frame3_btn = Button(frame2, text="Doctor", command=lambda: show_frame(frame1))
frame3_btn.grid(row=0,column=0)

frame1_btn = Button(frame3, text='Nurse', command=lambda: show_frame(frame2))
frame1_btn.grid(row=0,column=1)
#-----------------------------------------------------------------1---------------------------------------------------------------------
label2=Label(frame1,text="Name")
label2.grid(row=1,column=0)

label3=Label(frame1,text="Address")
label3.grid(row=2,column=0)

label4=Label(frame1,text="Phone number")
label4.grid(row=3,column=0)

label5=Label(frame1,text="Gender")
label5.grid(row=4,column=0)

label6=Label(frame1,text="Speciality")
label6.grid(row=5,column=0)

label7=Label(frame1,text="Badge Number")
label7.grid(row=6,column=0)

label8=Label(frame1,text="Status")
label8.grid(row=7,column=0)

name_text=StringVar()
entry1=Entry(frame1,textvariable=name_text)
entry1.grid(row=1,column=1)

address_text=StringVar()
entry2=Entry(frame1,textvariable=address_text)
entry2.grid(row=2,column=1)

phone_number_text=StringVar()
entry3=Entry(frame1,textvariable=phone_number_text)
entry3.grid(row=3,column=1)

OPTIONS = [
"Male",
"Female",
"Other"
    ]
Gender=StringVar(frame1)
Gender.set(OPTIONS[2])
entry4=OptionMenu(frame1,Gender, *OPTIONS)
entry4.grid(row=4,column=1)

Speciality=StringVar()
entry5=Entry(frame1,textvariable=Speciality)
entry5.grid(row=5,column=1)

Badge_Number=StringVar()
entry6=Entry(frame1,textvariable=Badge_Number)
entry6.grid(row=6,column=1)

list1=Listbox(frame1,height=20,width=59)
list1.grid(row=1,column=3, rowspan=6, columnspan=2)

scrl=Scrollbar(frame1)
scrl.grid(row=1,column=2, sticky='ns',rowspan=6)

list1.configure(yscrollcommand=scrl.set)
scrl.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(frame1,text="view all",width=12, command=view_command)
b1.grid(row=9, column=0)

b2=Button(frame1,text="add entry",width=12,command=add_command)
b2.grid(row=10, column=0)

b3=Button(frame1,text="delete entry",width=12,command=delete_command)
b3.grid(row=11, column=0)

b4=Button(frame1,text="search",width=12,command=search_command)
b4.grid(row=9, column=1)

b5=Button(frame1,text="update",width=12,command=update_command)
b5.grid(row=10, column=1)

b7=Button(frame1,text="Clear",width=12,command=clear)
b7.grid(row=11, column=1)

b6=Button(frame1,text="NOT ACTIVE",width=12,command=changeText,bg="red")
b6.grid(row=7,column=1)
#------------------------------------------------------2----------------------------------------------------------------------------
label22=Label(frame2,text="Name")
label22.grid(row=1,column=0)

label23=Label(frame2,text="Address")
label23.grid(row=2,column=0)

label24=Label(frame2,text="Phone number")
label24.grid(row=3,column=0)

label25=Label(frame2,text="Gender")
label25.grid(row=4,column=0)

label26=Label(frame2,text="Assigned Patient")
label26.grid(row=5,column=0)

label27=Label(frame2,text="Badge Number")
label27.grid(row=6,column=0)

label28=Label(frame2,text="Status")
label28.grid(row=7,column=0)

name_text2=StringVar()
entry21=Entry(frame2,textvariable=name_text2)
entry21.grid(row=1,column=1)

address_text2=StringVar()
entry22=Entry(frame2,textvariable=address_text2)
entry22.grid(row=2,column=1)

phone_number_text2=StringVar()
entry23=Entry(frame2,textvariable=phone_number_text2)
entry23.grid(row=3,column=1)

OPTIONS = [
"Male",
"Female",
"Other"
    ]
Gender2=StringVar(frame2)
Gender2.set(OPTIONS[2])
entry24=OptionMenu(frame2,Gender2, *OPTIONS)
entry24.grid(row=4,column=1)

Patient_Assigned2=StringVar()
entry25=Entry(frame2,textvariable=Patient_Assigned2)
entry25.grid(row=5,column=1)

Badge_Number2=StringVar()
entry26=Entry(frame2,textvariable=Badge_Number2)
entry26.grid(row=6,column=1)

list21=Listbox(frame2,height=20,width=59)
list21.grid(row=1,column=3, rowspan=6, columnspan=2)

scrl2=Scrollbar(frame2)
scrl2.grid(row=1,column=2, sticky='ns',rowspan=6)

list21.configure(yscrollcommand=scrl2.set)
scrl2.configure(command=list21.yview)

list21.bind('<<ListboxSelect>>',get_selected_rowN)
b21=Button(frame2,text="view all",width=12, command=view_commandN)
b21.grid(row=9, column=0)

b22=Button(frame2,text="add entry",width=12,command=add_commandN)
b22.grid(row=10, column=0)

b23=Button(frame2,text="delete entry",width=12,command=delete_commandN)
b23.grid(row=11, column=0)

b24=Button(frame2,text="search",width=12,command=search_commandN)
b24.grid(row=9, column=1)

b25=Button(frame2,text="update",width=12,command=update_commandN)
b25.grid(row=10, column=1)

b27=Button(frame2,text="Clear",width=12,command=clearN)
b27.grid(row=11, column=1)

b26=Button(frame2,text="NOT ACTIVE",width=12,command=changeTextN,bg="red")
b26.grid(row=7,column=1)
#-----------------------------------------------------------------------3-----------------------------------------------------------------
label32=Label(frame3,text="Name")
label32.grid(row=1,column=0)

label33=Label(frame3,text="Address")
label33.grid(row=2,column=0)

label34=Label(frame3,text="Phone number")
label34.grid(row=3,column=0)

label35=Label(frame3,text="Gender")
label35.grid(row=4,column=0)

label36=Label(frame3,text="Nurse assigned")
label36.grid(row=5,column=0)

label37=Label(frame3,text="Attendent")
label37.grid(row=6,column=0)

label38=Label(frame3,text="Date_of_admit")
label38.grid(row=7,column=0)

label41=Label(frame3,text="UHID")
label41.grid(row=9,column=0)

label39=Label(frame3,text="Date_of_departure")
label39.grid(row=10,column=0)

label40=Label(frame3,text="Status")
label40.grid(row=11,column=0)

name_text3=StringVar()
entry31=Entry(frame3,textvariable=name_text3)
entry31.grid(row=1,column=1)

address_text3=StringVar()
entry32=Entry(frame3,textvariable=address_text3)
entry32.grid(row=2,column=1)

phone_number_text3=StringVar()
entry33=Entry(frame3,textvariable=phone_number_text3)
entry33.grid(row=3,column=1)

OPTIONS = [
"Male",
"Female",
"Other"
    ]
Gender3=StringVar(frame3)
Gender3.set(OPTIONS[2])
entry34=OptionMenu(frame3,Gender3, *OPTIONS)
entry34.grid(row=4,column=1)

Nurse_Assigned3=StringVar()
entry35=Entry(frame3,textvariable=Nurse_Assigned3)
entry35.grid(row=5,column=1)

Attendent3=StringVar()
entry36=Entry(frame3,textvariable=Attendent3)
entry36.grid(row=6,column=1)

Date_of_admit3=StringVar()
entry37=Entry(frame3,textvariable=Date_of_admit3)
entry37.grid(row=7,column=1)

Date_of_Departure3=StringVar()
entry38=Entry(frame3,textvariable=Date_of_Departure3)
entry38.grid(row=10,column=1)

uhid3=StringVar()
entry39=Entry(frame3,textvariable=uhid3)
entry39.grid(row=9,column=1)

list31=Listbox(frame3,height=20,width=59)
list31.grid(row=1,column=3, rowspan=6, columnspan=2)

scrl3=Scrollbar(frame3)
scrl3.grid(row=1,column=2, sticky='ns',rowspan=6)

list31.configure(yscrollcommand=scrl3.set)
scrl.configure(command=list31.yview)

list31.bind('<<ListboxSelect>>',get_selected_rowP)

b31=Button(frame3,text="view all",width=12, command=view_commandP)
b31.grid(row=12, column=0)

b32=Button(frame3,text="add entry",width=12,command=add_commandP)
b32.grid(row=13, column=0)

b33=Button(frame3,text="delete entry",width=12,command=delete_commandP)
b33.grid(row=14, column=0)

b34=Button(frame3,text="search",width=12,command=search_commandP)
b34.grid(row=12, column=1)

b35=Button(frame3,text="update",width=12,command=update_commandP)
b35.grid(row=13, column=1)

b37=Button(frame3,text="Clear",width=12,command=clearP)
b37.grid(row=14, column=1)

b36=Button(frame3,text="Left",width=12,command=changeTextP,bg="red")
b36.grid(row=11,column=1)


show_frame(frame1)
root.mainloop()
