import boto3
import botocore
def Save():
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file(s, 'ssr806', s)






def Submit():
    global s
    string1 = e2.get()
    string2 = e3.get()
    string3 = e4.get()
    string4 = e5.get()
    string5 = e6.get()
    string6 = e7.get()
    string7 = e8.get()
    string8 = e9.get()
    string9 = e10.get()
    string10 = e11.get()
    s=string+" "+date+" "+sub
    
    file = open(s,"w") 
    file.write(" Roll no.1     ") 
    file.write(string1+"\n") 
    file.write(" Roll no.2     ") 
    file.write(string2+"\n") 
    file.write(" Roll no.3     ") 
    file.write(string3+"\n") 
    file.write(" Roll no.4     ") 
    file.write(string4+"\n") 
    file.write(" Roll no.5     ") 
    file.write(string5+"\n") 
    file.write(" Roll no.6     ") 
    file.write(string6+"\n")
    file.write(" Roll no.7     ") 
    file.write(string7+"\n")
    file.write(" Roll no.8     ") 
    file.write(string8+"\n")
    file.write(" Roll no.9     ") 
    file.write(string9+"\n")
    file.write(" Roll no.10     ") 
    file.write(string10+"\n")
 
    file.close() 
    d = Button(root,text='Save attendance',command=Save, bg="YELLOW")
    d.grid(row=23, column=1)

def batch():
    global e1
    global et
    global ep
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8
    global e9
    global e10
    global e11
    global string
    global date
    global sub
    string = e1.get() 
    date = et.get()
    sub = ep.get()
    if(string=="CSE-3"):
        #print("world")
        Label(root, text="Roll no. 1", bg="orange").grid(row=10)
        Label(root, text="Roll no. 2", bg="orange").grid(row=11)
        Label(root, text="Roll no. 3", bg="orange").grid(row=12)
        Label(root, text="Roll no. 4", bg="orange").grid(row=13)
        Label(root, text="Roll no. 5", bg="orange").grid(row=14)
        Label(root, text="Roll no. 6", bg="orange").grid(row=15)
        Label(root, text="Roll no. 7", bg="orange").grid(row=16)
        Label(root, text="Roll no. 8", bg="orange").grid(row=17)
        Label(root, text="Roll no. 9", bg="orange").grid(row=18)
        Label(root, text="Roll no. 10", bg="orange").grid(row=19)
        e2 = Entry(root)
        e3 = Entry(root)
        e4 = Entry(root)
        e5 = Entry(root)
        e6 = Entry(root)
        e7 = Entry(root)
        e8 = Entry(root)
        e9 = Entry(root)
        e10 = Entry(root)
        e11 = Entry(root)
        e2.grid(row=10, column=1) 
        e3.grid(row=11, column=1)
        e4.grid(row=12, column=1)
        e5.grid(row=13, column=1)
        e6.grid(row=14, column=1)
        e7.grid(row=15, column=1)
        e8.grid(row=16, column=1)
        e9.grid(row=17, column=1)
        e10.grid(row=18, column=1)
        e11.grid(row=19, column=1)
        C = Button(root,text='Submit',command=Submit, bg="YELLOW")
        C.grid(row=21,column=1)

def view():
    global e1
    global et
    global ep
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8
    global e9
    global e10
    global e11
    global string
    global date
    global sub
    
    string = e1.get() 
    date = et.get()
    sub = ep.get()
    BUCKET_NAME = 'ssr806' 
    KEY = string+" "+date+" "+sub
    s3 = boto3.resource('s3')
    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, "RECEIVED.txt")
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
    

    file = open("RECEIVED.txt", "r") 
    Label(root, text=file.read()).grid(row=10,pady=10,padx=10)
    
 

from Tkinter import *
root = Tk()

C = Canvas(root, bg="black", height=250, width=300)
filename = PhotoImage(file = "/home/sudhanshu/Desktop/3.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.geometry("500x500")
#C.grid(sticky=N+S+E+W)
#background_image=root.PhotoImage(file="/home/sudhanshu/Desktop/download.png")
#background_label = root.Label(parent, image=background_image)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.configure(background='BLUE')

root.title('Cloud Based Attendance System')
Label(root, text="Cloud Based Attendance System",font=20,bg="yellow").grid(row=0,column=1, pady=20)
Label(root, text="Batch", bg="orange").grid(row=2)
Label(root, text="Date", bg="orange").grid(row=4)
Label(root, text="Subject", bg="orange").grid(row=5)

e1 = Entry(root)
et = Entry(root)
ep = Entry(root)

e1.grid(row=2, column=1)
et.grid(row=4, column=1)
ep.grid(row=5, column=1)


#e = Entry(root)
#e2.grid(row=2)

b = Button(root,text='Enter',command = batch,bg="green")
b.grid(row=6,column=1,pady=10)

F = Button(root,text='View Attendance',command = view,bg="yellow")
F.grid(row=8,column=1,pady=10)



root.mainloop()
