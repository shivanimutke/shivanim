

from tkinter import *
from tkinter import Tk
from tkinter import messagebox as m_box




window: Tk = Tk()
window.title("time and work")
window.geometry("900x980")

scrollbar = Scrollbar(window)
scrollbar.pack( side = RIGHT, fill=Y )

window.configure(bg="pink", )




#----------------------------------------------------------------------------------------------------

def createNewWindow5():
    newWindowsssss = Toplevel(window)
    newWindowsssss.configure(bg="pink")
    newWindowsssss.geometry("600x400")



    labels = ['A can work', 'B can work','C can work','D can work','E can work','no of days']


    for i in range(len(labels)):
        cur_label = 'label' + str(i)  # label 0
        cur_lable = Label(newWindowsssss, text=labels[i])
        cur_lable.grid(row=i, column=0, sticky=W, padx=4, pady=4)
        # change the row value
        # get the label

    # entry boxes

    name_var = IntVar()
    user_info = {
        'Aw': IntVar(),
        'Bw': IntVar(),
        'Cw':IntVar(),
        'Dw': IntVar(),
        'Ew':IntVar(),
        'Days':IntVar(),
    }
    counter = 0
    for i in user_info:
        cur_entrybox = 'entry' + i  # entryname#entryage
        cur_entrybox = Entry(newWindowsssss, width=16, textvariable=user_info[i])
        cur_entrybox.grid(column=1, row=counter, padx=4, pady=4)
        counter = counter + 1

    def submit():
        A = user_info['Aw'].get()
        B = user_info['Bw'].get()
        C = user_info['Cw'].get()
        D = user_info['Dw'].get()
        E = user_info['Ew'].get()
        d = user_info['Days'].get()
        A_and_B = A + B
        A_and_C = A + C
        A_and_D = A + D
        A_and_E = A + E
        B_and_C = C + B
        B_and_D = B + D
        B_and_E = B + E
        C_and_D = C + D
        C_and_E = E + C
        D_and_E = E + D
        A_and_B_and_C = A + B + C
        A_and_B_and_D = A + B + D
        A_and_B_and_E = A + B + E
        B_and_C_and_D = B + C + D
        B_and_C_and_E = B + C + E
        B_and_D_and_E = B + D + E
        C_and_D_and_E = C + D + E
        A_and_B_and_C_And_D_and_E = A + B + C + D + E
        ABCD = A + B + C + D
        ACDE = A + C + D + E
        BCDE = B + C + D + E

        list_F_p = [B_and_C, BCDE, ACDE, ABCD, A_and_B_and_C_And_D_and_E, C_and_D_and_E, B_and_D_and_E, B_and_C_and_D,
                    B_and_C_and_E, D_and_E, C_and_E, A_and_B_and_E, C_and_D, B_and_E, B_and_D, A_and_E, A_and_D,
                    A_and_C, A_and_B_and_C, A_and_B_and_D]
        print(list_F_p)

        n = d
        while (n > 0):  # loop control-statememt



            print("D and E can work in ..   ", n, "  days ", n * D_and_E)
            print("E and C can work in ..   ", n, "  days ", n * C_and_E)
            print("C and D can work in ..   ", n, "  days ", n * C_and_D)
            print("B and E can work in ..   ", n, "  days ", n * B_and_E)
            print("D and B can work in ..   ", n, "  days ", n * B_and_D)
            print("C and B can work in ..   ", n, "  days ", n * B_and_C)
            print("E and A can work in ..   ", n, "  days ", A_and_E)
            print("A and D can work in ..   ", n, "  days ", n * A_and_D)
            print("A and C  can work in ..   ", n, "  days ", n * A_and_C)
            print("A and B  can work in ..   ", n, "  days ", n * A_and_B)
            print("A and B  and C can work in ..   ", n, "  days ", n * A_and_B_and_C)
            print("A and B and D can work in ..   ", n, "  days ", n * A_and_B_and_D)
            print("B and A and E can work in ..   ", n, "  days ", n * A_and_B_and_E)
            print("B and C and D can work in ..   ", n, "  days ", n * B_and_C_and_D)
            print("B and C and Ecan work in ..   ", n, "  days ", n * B_and_C_and_E)
            print("D and D  and E can work in ..   ", n, "  days ", B_and_D_and_E)
            print("E and C and D can work in ..   ", n, "  days ", n * C_and_D_and_E)
            print("A and B and c and D and E can work in ..   ", n, "  days ", n * A_and_B_and_C_And_D_and_E)
            print("A and B and C and D can work in ..   ", n, "  days ", n * ABCD)
            print("A and C and D and E can work in ..   ", n, "  days ", n * ACDE)
            print("B and C  and D  and E can work in ..   ", n, "  days ", n * BCDE)  # loop body
            print("A can work in..  ", n, "  days ", n * A)  # loop body
            print("B can work in..  ", n, "  days ", n * B)
            print("C can work in..  ", n, "  days ", n * C)
            print("D can work in..  ", n, "  days ", n * D)
            print("E can work in..  ", n, "  days ", n * E)  # loop body
            n -= 1

    submit_btn = Button(newWindowsssss, text='submit', command=submit)
    submit_btn.grid(row=6, columnspan=2)


def createNewWindow4():
    newWindow = Toplevel(window)
    newWindow.configure(bg="pink")
    newWindow.geometry("600x400")



    labels = ['A can work', 'B can work','C can work','D can work','no of days']
    name_lable = Label(newWindow, text='what is your name: ')
    name_lable.grid(row=0, column=0, sticky=W)

    for i in range(len(labels)):
        cur_label = 'label' + str(i)  # label 0
        cur_lable = Label(newWindow, text=labels[i])
        cur_lable.grid(row=i, column=0, sticky=W, padx=4, pady=4)
        # change the row value
        # get the label

    # entry boxes

    name_var = IntVar()
    user_info = {
        'Aw': IntVar(),
        'Bw': IntVar(),
        'Cw':IntVar(),
        'Dw': IntVar(),
        'Days':IntVar(),
    }
    counter = 0
    for i in user_info:
        cur_entrybox = 'entry' + i  # entryname#entryage
        cur_entrybox = Entry(newWindow, width=16, textvariable=user_info[i])
        cur_entrybox.grid(column=1, row=counter, padx=4, pady=4)
        counter = counter + 1

    def submit():
        A = user_info['Aw'].get()
        B = user_info['Bw'].get()
        C = user_info['Cw'].get()
        D = user_info['Dw'].get()
        d = user_info['Days'].get()
        A_and_B = A + B
        A_and_C = A + C
        B_and_C = B + C
        B_and_D = B + D
        A_B_C_D = B + C + A + D
        A_and_B_and_D = A + B + D
        A_and_C_and_D = A + C + D
        C_and_B_and_D = B + C + D
        C_and_B_and_A = B + C + A
        A_and_D = A + D
        C_and_D = C + D
        C_D_A = A + D + C
        list_fo_p = [A_and_B, B_and_D, C_D_A, A_and_B_and_D, A_and_C, A_and_C_and_D, A_B_C_D, B_and_C, C_and_B_and_A,
                     C_and_B_and_D]
        print(list_fo_p)
        n = d
        while (n > 0):  # loop control-statememt
            print("A and B can work in ..   ", n, "  days ", n * A_and_B)
            print("A and C can work in ..   ", n, "  days ", n * A_and_C)
            print("B and D can work in ..   ", n, "  days ", n * B_and_D)
            print("A and D can work in ..   ", n, "  days ", n * A_and_D)
            print("D and C can work in ..   ", n, "  days ", n * C_and_D)
            print("D and C  and A can work in ..   ", n, "  days ", C_D_A)
            print("A and B and C and D can work in ..   ", n, "  days ", n * A_B_C_D)
            print("A and C and D can work in ..   ", n, "  days ", n * A_and_C_and_D)
            print("A and B and D can work in ..   ", n, "  days ", n * A_and_B_and_D)
            print("B and C can work in ..   ", n, "  days ", n * B_and_C)
            print("B and C  and A can work in ..   ", n, "  days ", n * C_and_B_and_A)
            print("A can work in..  ", n, "  days", n * A)  # loop body
            print("B can work in..   ", n, "  days", n * B)
            print("C can work in ..  ", n, "  days", n * C)
            print("D can work in..   ", n, "  days", n * D)  # loop body
            n -= 1

    submit_btn = Button(newWindow, text='submit', command=submit)
    submit_btn.grid(row=6, columnspan=2)

def createNewWindow3():
    newWindow = Toplevel(window)
    newWindow.configure(bg="pink")
    newWindow.geometry("600x400")

    labels = ['A can work', 'B can work','C can work','no of days']



    for i in range(len(labels)):
        cur_label = 'label' + str(i)  # label 0
        cur_lable = Label(newWindow, text=labels[i])
        cur_lable.grid(row=i, column=0, sticky=W, padx=4, pady=4)
        # change the row value
        # get the label

    # entry boxes

    name_var = IntVar()
    user_info = {
        'Aw': IntVar(),
        'Bw': IntVar(),
        'Cw':IntVar(),
        'Days':IntVar(),

    }
    counter = 0
    for i in user_info:
        cur_entrybox = 'entry' + i  # entryname#entryage
        cur_entrybox = Entry(newWindow, width=16, textvariable=user_info[i])
        cur_entrybox.grid(column=1, row=counter, padx=4, pady=4)
        counter = counter + 1

    def submit():
        A = user_info['Aw'].get()
        B = user_info['Bw'].get()
        C = user_info['Cw'].get()
        d = user_info['Days'].get()
        A_and_B = A + B
        A_and_C = A + C
        B_and_C = B + C
        B_C_and_A = B + C + A
        list_th_people = [A_and_B, A_and_C, B_and_C, B_C_and_A]
        print(list_th_people)
        n = d
        while (n > 0):  # loop control-statememt
            print("A and B can work in ..   ", n, "  days ", n * A_and_B)
            print("A and C can work in ..   ", n, "  days ", n * A_and_C)
            print("B and C can work in ..   ", n, "  days ", n * B_and_C)
            print("B and C  and A can work in ..   ", n, "  days ", n * B_C_and_A)
            print("C can work in ..   ", n, "  days ", n * C)  # loop body
            print("A can work in..  ", n, "  days", n * A)  # loop body
            print("B can work in..   ", n, "  days", n * B)  # loop body
            n -= 1

    submit_btn = Button(newWindow, text='submit', command=submit)
    submit_btn.grid(row=6, columnspan=2)


def createNewWindow2():
    newWindow = Toplevel(window)
    newWindow.configure(bg="pink")
    newWindow.geometry("600x400")



    labels = ['A can work', 'B can work','no of days']



    for i in range(len(labels)):
        cur_label = 'label' + str(i)  # label 0
        cur_lable = Label(newWindow, text=labels[i])
        cur_lable.grid(row=i, column=0, sticky=W, padx=4, pady=4)
        # change the row value
        # get the label

    # entry boxes

    #name_var = IntVar()
    user_info = {
        'Aw': IntVar(),
        'Bw': IntVar(),
        'Days':IntVar(),

    }
    counter = 0
    for i in user_info:
        cur_entrybox = 'entry' + i  # entryname#entryage
        cur_entrybox = Entry(newWindow, width=16, textvariable=user_info[i])
        cur_entrybox.grid(column=4, row=counter, padx=10, pady=10)
        counter = counter + 1

    def submit():
        A=user_info['Aw'].get()
        B=user_info['Bw'].get()
        d = user_info['Days'].get()


        s1 = A + B
        n = d
        while (n > 0):  # loop control-statememt
            print("both can work in   ", n, "  days", n * s1)  # loop body
            print("A can work in  ", n, "  days", n * A)  # loop body
            print("B can work in   ", n, "  days", n * B)  # loop body
            n -= 1



    submit_btn = Button(newWindow, text='submit', command=submit)
    submit_btn.grid(row=6, columnspan=2)


#------------------------------------------------------------------------------

def createNewWindows():
    newWindows = Toplevel(window)
    newWindows.configure(bg="pink")
    #newWindows.geometry("600x400")

    scrollbar = Scrollbar(newWindows)
    scrollbar.pack(side=RIGHT, fill=Y)

    lbl3 = Label(newWindows)
    lbl3.config(anchor=CENTER,
                text="*************************************************************************************************************************************************",
                bg="pink", padx=70, pady=40, font="none 22 bold")
    lbl3.pack()


    lbl2 = Label(newWindows, text="If you have 2 people  in problem then go to this window", bg="light green",
                 fg="black", bd=3, font="none 12 bold")
    lbl2.config(anchor=CENTER)
    lbl2.pack()

    bt3 = Button(newWindows, text="  procceed ", command=createNewWindow2, pady=10, padx=20)
    bt3.config(anchor=CENTER, bg="light blue")
    bt3.pack()

    lbl5 = Label(newWindows)
    lbl5.config(anchor=CENTER, text="******", bg="pink", padx=70, pady=40)
    lbl5.pack()

    lbl2 = Label(newWindows, text="If you have 3 people  in problem then go to this window", bg="light green",
                 fg="black", bd=3, font="none 12 bold")
    lbl2.config(anchor=CENTER)
    lbl2.pack()

    bt3 = Button(newWindows, text="  procceed ", command=createNewWindow3, pady=10, padx=20)
    bt3.config(anchor=CENTER, bg="light blue")
    bt3.pack()

    lbl5 = Label(newWindows)
    lbl5.config(anchor=CENTER, text="******", bg="pink", padx=100, pady=40)
    lbl5.pack()

    lbl2 = Label(newWindows, text="If you have 4 people  in problem then go to this window", bg="light green",
                 fg="black", bd=3, font="none 12 bold")
    lbl2.config(anchor=CENTER)
    lbl2.pack()

    bt3 = Button(newWindows, text="  procceed ", command=createNewWindow4, pady=10, padx=20)
    bt3.config(anchor=CENTER, bg="light blue")
    bt3.pack()

    lbl5 = Label(newWindows)
    lbl5.config(anchor=CENTER, text="******", bg="pink", padx=100, pady=40)
    lbl5.pack()

    lbl2 = Label(newWindows, text="If you have 5 people  in problem then go to this window", bg="light green",
                 fg="black", bd=3, font="none 12 bold")
    lbl2.config(anchor=CENTER)
    lbl2.pack()

    bt3 = Button(newWindows, text="  procceed ", command=createNewWindow5, pady=10, padx=20)
    bt3.config(anchor=CENTER, bg="light blue")
    bt3.pack()


    lbl3 = Label(newWindows)
    lbl3.config(anchor=CENTER,
                text="*************************************************************************************************************************************************",
                bg="pink", padx=100, pady=40, font="none 22 bold")
    lbl3.pack()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# center this label

window.geometry("600x400")

lbl3 = Label(window)
lbl3.config(anchor=CENTER, text="*************************************************************************************************************************************************",bg="pink",padx=100,pady=40,font="none 22 bold")
lbl3.pack()

lbl1 = Label(window, text="Time and work", bg="orange red", fg="black", padx=100,pady=40 ,bd=2,font="none 24 bold")
lbl1.config(anchor=CENTER)
lbl1.pack()


lbl3 = Label(window)
lbl3.config(anchor=CENTER, text="******",bg="pink",padx=100,pady=40)
lbl3.pack()


lbl2 = Label(window, text="This application is based on time and work -mathematical problems", bg="light green", fg="black", bd=3, font="none 12 bold")
lbl2.config(anchor=CENTER)
lbl2.pack()

#Checkbutton(window, text="terms and condition").grid(row=0, sticky=W)


lbl5 = Label(window)
lbl5.config(anchor=CENTER, text="******",bg="pink",padx=100,pady=40)
lbl5.pack()

lbl6 = Label(window, text="  this is only a mathematical function based application it does need any kind of media files from your pc ")
lbl6.config(anchor=CENTER,bg="pink")
lbl6.pack()

lbl4 = Label(window, text="  If you are agree with this then to proceed please hit the ok button ")
lbl4.config(anchor=CENTER,bg="pink")
lbl4.pack()


"""
var=StringVar()
print(var)
bt2=Checkbutton(window, text="agree")
bt2.config(anchor=CENTER,bg="pink",variable=var, onvalue = "on", offvalue = "off")
bt2.pack()
"""




#bt1.pack()

bt1 = Button(window, text="  Okay ",command=createNewWindows,pady=10,padx=20)
bt1.config(anchor=CENTER,bg="light blue")
bt1.pack()








#bt1.pack()


"""
if bt2.grab_status() == 0:
    bt1["state"] = DISABLED
else:
    bt1["state"] = NORMAL



if bt2['state']==ACTIVE:
    bt1['state'] =DISABLED
else:
    bt1['state'] = NORMAL
#bt1.pack()"""




lbl3 = Label(window)
lbl3.config(anchor=CENTER, text="******",bg="pink",padx=100,pady=40)
lbl3.pack()

bt3=Button(window, text='Quit', command=window.quit)
bt3.config(anchor=CENTER,bg="light blue",pady=10,padx=20)
bt3.pack()


"""
buttonExample = Button(app,
              text="Create new window",
              command=createNewWindow)
buttonExample.pack()"""

"""
def var_states():
   print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))


var1 = IntVar()
Checkbutton(window, text="male", variable=var1)
var2 = IntVar()
Checkbutton(window, text="female", variable=var2)
Button(window, text='Quit', command=window.quit)
Button(window, text='Show', command=var_states)
"""

canvas = Canvas(window, bd=0, scrollregion=(0, 0, 1000, 1000))
canvas.config(scrollregion=canvas.bbox(ALL))





lbl3 = Label(window)
lbl3.config(anchor=CENTER, text="*************************************************************************************************************************************************",bg="pink",padx=100,pady=40,font="none 22 bold")
lbl3.pack()


window.mainloop()




