from tkinter import *
window=Tk()

# add widgets here


window.title('BMI Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

def calculate_BMI () :
    weight=int(weight_e.get())
    height=int(height_e.get())/100 
    BMI = (weight/(height*height))
    BMI=round(BMI,1)
    name=username.get()
    result_label.destroy()
    msg=''
    if BMI<18.5 :
        msg='You are under weight'
    elif BMI>18.5 and BMI<=24.9:
        msg='Your BMI is normal'
    elif BMI>25 and BMI<=29.9:
        msg='You are over weight'  
    elif BMI>30 :
        msg='you are obese'
    else:
        msg='Something went wrong'
    output_msg = Label(result_frame,text=name+' your BMI is '+ str(BMI) + ' and '+ msg,bg='lightcyan',font=('Calibri',12),bd=1,width=42)    
    output_msg.place(x=20,y=40)
    output_msg.pack()

app_label=Label(window, text="BMI CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

height_label=Label(window,text='Enter Height (CM)',fg='black',bg='lightcyan',font=('Calibri',12),bd=1)
height_label.place(x=20,y=140)

height_e = Entry(window,text='',bd=2,width=15)
height_e.place(x=150,y=142)

weight_label=Label(window,text='Enter Weigth (KG)',fg='black',bg='lightcyan',font=('Calibri',12),bd=1)
weight_label.place(x=20,y=185)

weight_e = Entry(window,text='',bd=2,width=15)
weight_e.place(x=150,y=187)


result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

calculate_button = Button(window,text="Calculate",fg='black',bg='lightcyan',bd=4,command=calculate_BMI)
calculate_button.place(x=20,y=250)

window.mainloop()

