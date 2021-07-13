from tkinter import *
import numpy
import statistics
import pandas as pd
from tkinter import messagebox
import collections

import matplotlib.pyplot as plt

root = Tk()

frame = Frame(root,bg="blue",height=175)
farmec = Frame(root,bg="blue",width=300,height=650)
farmet = Frame(root,bg="pink",width=300,height=30)
framel = Frame(root, bg="pink",width=30,height=30)
framer = Frame(root, bg="pink",width=30,height=30)
farmeb = Frame(root,bg="pink",width=300,height=30)

farmet.pack(side=TOP,fill=X)
framer.pack(fill=Y, side=RIGHT)
framel.pack(fill=Y, side=LEFT)
farmec.pack(fill=X)
frame.pack(side=BOTTOM,fill=X)
farmeb.pack(side=BOTTOM,fill=X)

button1 = Button(farmec, text="Mean",font=("courier new",10, "bold"), fg="black",bg="pink",width=20)
button1.grid(row=1,column=0)
list2 = Listbox(farmec,width=10, height=1)
list2.grid(row=1,column=1)

button2 = Button(farmec, text="Median",font=("courier new",10, "bold"), fg="black", bg="pink",width=20)
button2.grid(row=1,column=3)
list3 = Listbox(farmec,width=10, height=1)
list3.grid(row=1,column=4)

button3 = Button(farmec, text="Mode",font=("courier new",10, "bold"), fg="black", bg="pink",width=20)
button3.grid(row=2,column=0)
list4 = Listbox(farmec,width=10, height=1)
list4.grid(row=2,column=1)

button4 = Button(farmec, text="Standard deviation",font=("courier new",10, "bold"), fg="black", bg="pink",width=20)
button4.grid(row=2,column=3)
list5 = Listbox(farmec,width=10, height=1)
list5.grid(row=2,column=4)

button5 = Button(farmec, text="Variance",font=("courier new",10, "bold"), fg="black", bg="pink",width=20)
button5.grid(row=3,column=0)
list6 = Listbox(farmec,width=10, height=1)
list6.grid(row=3,column=1)

button6 = Button(farmec, text="IQR",font=("courier new",10, "bold"), fg="black", bg="pink",width=20)
button6.grid(row=3,column=3)
list7 = Listbox(farmec,width=10, height=1)
list7.grid(row=3,column=4)

button7 = Button(farmec, text="Maximum",font=("courier new",10, "bold"), fg="black", bg="pink",width=20)
button7.grid(row=4,column=0)
list8 = Listbox(farmec,width=10, height=1)
list8.grid(row=4,column=1)

button8 = Button(farmec, text="minimum",font=("courier new",10, "bold"), fg="black", bg="pink",width=20)
button8.grid(row=4,column=3)
list9 = Listbox(farmec,width=10, height=1)
list9.grid(row=4,column=4)


button9 = Button(farmec, text="Range",font=("courier new",10, "bold"), fg="black", bg="pink",width=20)
button9.grid(row=5,column=0)
list10 = Listbox(farmec,width=10, height=1)
list10.grid(row=5,column=1)

button10 = Button(farmec, text="Correlation", font=("courier new", 10, "bold") , fg="black" , bg="pink" , width=20)
button10.grid(row=5,column=3)
list11 = Listbox(farmec,width=50, height=2)
list11.grid(row=5,column=4)

buttonent1 = Button(farmec, text="add to another List",font=("courier new",10, "bold"), fg="black", bg="pink",width=20)
buttonent1.grid(row=1,column=5)

buttonent = Button(farmec, text="Okay",font=("courier new",10, "bold"), fg="black", bg="pink",width=10)
buttonent.grid(row=0,column=5)
list1 = Listbox(farmec,width=30,height=15)
list1.grid(row=3,column=5)



label3 = Label(farmec,text="  you Entered: ",font=("courier new",10, "bold"), fg="white",bg="blue")
label3.grid(row=2, column=5)

label1 = Label(farmec,text="            Enter Your Values!",font=("courier new",20, "bold"), fg="white",bg="blue")
label1.grid(row=0,column=3)


entryval = Entry(farmec,width=10)
entryval.grid(row=0,column=4)





value = []
value2 = []






def copying1(event):
    val = entryval.get()
    list1.insert(END, "list two :")
    value2.append(int(val))
    list1.insert(END,value2)
    print(value2)



def copying(event):

    val = entryval.get()
    list1.insert(END,"list one :")
    value.append(int(val))
    list1.insert(END,value)
    print(value)


data = {'List_1':value,'List_2':value2}


def corrfun(event):
    df = pd.DataFrame(data,columns=['List_1','List_2'])
    list11.insert(END,df.corr())
    print(data)


def meanfun(event):
   x=statistics.mean(value)
   list2.insert(END,x)



def medfun(event):
   x=statistics.median(value)
   list3.insert(END,x)



def modfun(event):
 x = statistics.mode(value)
 list4.insert(END,x)


def stdfun(event):
  x = statistics.stdev(value)
  list5.insert(END,x)



def varfun(event):
  x = statistics.variance(value)
  list6.insert(END,x)
  print(x)



def iqrfun(event):
    x = numpy.array(value)
    q1_x = numpy.percentile(x, 25, interpolation='midpoint')
    q3_x = numpy.percentile(x, 75, interpolation='midpoint')
    interrange = q3_x - q1_x
    list7.insert(END,interrange)
    print(interrange)



def maxfun(event):
    x = max(value)
    list8.insert(END, x)


def minfun(event):
    x = min(value)
    list9.insert(END, x)


def rangefun(event):
    x = min(value)
    x2 = max(value)
    rang = x2-x
    list10.insert(END,rang)



buttonent.bind("<Button-1>",copying)
button1.bind("<Button-1>",meanfun)
button2.bind("<Button-1>",medfun)
button3.bind("<Button-1>",modfun)
button4.bind("<Button-1>",stdfun)
button5.bind("<Button-1>",varfun)
button6.bind("<Button-1>",iqrfun)
button7.bind("<Button-1>",maxfun)
button8.bind("<Button-1>",minfun)
button9.bind("<Button-1>",rangefun)
buttonent1.bind("<Button-1>",copying1)
button10.bind("<Button-1>",corrfun)


#graphical part



def scatfun(event):
   try:
     plt.scatter(value,value2)
     plt.show()
   except:
     messagebox.showerror("Erorr", "ya ")


def histofun(event):
    try:
        plt.hist2d(value,value2)
        plt.show()
    except:
        messagebox.showerror("Erorr","ya ")




def barfun(event):
    try:
        plt.bar(value,value2)
        plt.show()
    except:
        messagebox.showerror("Erorr","ya ")


def piefun(event):
    try:
     plt.pie(collections.Counter(value).values(),labels=collections.Counter(value).keys(),startangle=180,radius=1.2,autopct='%1.1f%%')
     plt.legend()
     plt.title("Pie Char")
     plt.show()
    except:
        messagebox.showerror("Erorr","ya ")


def boxfun(event):
  try:
    plt.boxplot(value)
    plt.show()
  except:
      messagebox.showerror("Erorr" , "ya ")




button_scatter = Button(frame,text="scatter Plot",bg="pink",fg="black",width=15)
button_scatter.bind("<Button-1>",scatfun)

button_histo = Button(frame,text="Histogram",bg="pink",fg="black",width=15)
button_histo.bind("<Button-1>",histofun)

button_bar = Button(frame,text="bar Chart",bg="pink",fg="black",width=15)
button_bar.bind("<Button-1>",barfun)

button_pie = Button(frame,text="pie Chart",bg="pink",fg="black",width=15)
button_pie.bind("<Button-1>",piefun)

button_box = Button(frame,text="Box Plot",bg="pink",fg="black",width=15)
button_box.bind("<Button-1>",boxfun)



button_scatter.grid()
button_histo.grid()
button_bar.grid()
button_pie.grid(row=0,column=2)
button_box.grid(row=1,column=2)











root.mainloop()
