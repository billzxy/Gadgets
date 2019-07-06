"""
Good stuff m8!
Because this thing has a GUI!
"""

from tkinter import *  

def timeStampToSec(t):
    return t[0]*60*60 + t[1]*60 + t[2]

def secToTimeStamp(sec):
    h = sec//3600
    tmp=sec-h*3600
    m = (tmp)//60
    s = (tmp-m*60)
    return (h,m,s)

def mapVal(var):
    return int(var.get()) if not var.get()=="" else 0

def allZero(li):
    for i in li:
        if not i==0:
            return False
    return True

def calculate(times,delay):
    lt = list(map(list, (map(mapVal, t) for t in times)))
    if allZero(lt[0]) or allZero(lt[1]) or allZero(lt[2]):
        return "First/Second Clip Cannot Be Empty!"
    ins = ""
    c1s = timeStampToSec(lt[0])
    c1e = timeStampToSec(lt[1])
    c2s = timeStampToSec(lt[2])
    c2e = timeStampToSec(lt[3])
    c3s = timeStampToSec(lt[4])

    c1i = secToTimeStamp(c1s-delay.get() if c1s>=delay.get() else 0)
    ins+="Set Clip 1 to: %i:%i:%i\n" %(c1i[0],c1i[1],c1i[2])
    c2i = secToTimeStamp(c2s-(c1e-c1s)-delay.get() if c2s>=c1e-c1s+delay.get() else 0)
    ins+="Set Clip 2 to: %i:%i:%i\n" %(c2i[0],c2i[1],c2i[2])

    if not allZero(lt[3]) and not allZero(lt[4]):
        c3i = secToTimeStamp(c3s-(c1e-c1s)-(c2e-c2s)-delay.get() if c3s>=(c1e-c1s)+(c2e-c2s)+delay.get() else 0)
        ins += "Set Clip 3 to: %i:%i:%i\n" %(c3i[0],c3i[1],c3i[2])
    return ins


def goButton(times,msg,buffer_delay):
    text = calculate(times,buffer_delay)
    msg.set(text)

def autoFill(start,end):
    for i in range(0,3):
        end[i].set(start[i].get())
  


BGCOLOR = "#282923"
BUFFER_DELAY = 25
C1Y = 100
C2Y = 220
C3Y = 340

  
# Driver code 
if __name__ == "__main__": 
    # create a GUI window 
    gui = Tk()  
    gui.configure(background=BGCOLOR) 
    gui.title("Video Clip Binge-watching Calculator") 
    gui.geometry("480x640") 

    buffer_time = IntVar()
    buffer_time.set(45)
    
    lb = Label(gui, text="Set Buffer Time", fg='White', bg=BGCOLOR)
    lb.place(x=20, y=20)
    buf = Entry(gui, textvariable=buffer_time, justify="center",bg="grey69")
    buf.place(x=170,y=20,height=30,width=50)
    
    c1_h = StringVar()
    c1_m = StringVar() 
    c1_s = StringVar()
    
    c1l = Label(gui, text="Clip 1", fg='White', bg=BGCOLOR)
    c1l.place(x=20, y=C1Y-30)
    c1l = Label(gui, text="Start", fg='White', bg=BGCOLOR)
    c1l.place(x=20, y=C1Y)
    c1hl = Label(gui, text="Hour", fg='White', bg=BGCOLOR)
    c1hl.place(x=70, y=C1Y, height=30, width=50)
    c1ml = Label(gui, text="Minute", fg='White', bg=BGCOLOR)
    c1ml.place(x=170, y=C1Y, height=30, width=50)
    c1sl = Label(gui, text="Second", fg='White', bg=BGCOLOR)
    c1sl.place(x=270, y=C1Y, height=30, width=50)

    c1_hour = Entry(gui, textvariable=c1_h, justify="center",bg="grey69")
    c1_hour.place(x=120,y=C1Y,height=30,width=50)
    c1_min = Entry(gui, textvariable=c1_m, justify="center",bg="grey69")
    c1_min.place(x=220,y=C1Y,height=30,width=50)
    c1_sec = Entry(gui, textvariable=c1_s, justify="center",bg="grey69")
    c1_sec.place(x=320,y=C1Y,height=30,width=50)

    c1e_h = StringVar()
    c1e_m = StringVar()
    c1e_s = StringVar()
    lc1e = (c1e_h,c1e_m,c1e_s)
    lc1s = (c1_h,c1_m,c1_s)

    fill_c1e_button = Button(gui, command=lambda: autoFill(lc1s,lc1e), 
        text='AutoFill', fg='White', bg='AntiqueWhite4') 
    fill_c1e_button.place(x=380,y=C1Y,height=30,width=50)


    c1el = Label(gui, text="End", fg='White', bg=BGCOLOR)
    c1el.place(x=20, y=C1Y+35)
    c1ehl = Label(gui, text="Hour", fg='White', bg=BGCOLOR)
    c1ehl.place(x=70, y=C1Y+35, height=30, width=50)
    c1eml = Label(gui, text="Minute", fg='White', bg=BGCOLOR)
    c1eml.place(x=170, y=C1Y+35, height=30, width=50)
    c1esl = Label(gui, text="Second", fg='White', bg=BGCOLOR)
    c1esl.place(x=270, y=C1Y+35, height=30, width=50)
    
    c1e_hour = Entry(gui, textvariable=c1e_h, justify="center",bg="grey69")
    c1e_hour.place(x=120,y=C1Y+35,height=30,width=50)
    c1e_min = Entry(gui, textvariable=c1e_m, justify="center",bg="grey69")
    c1e_min.place(x=220,y=C1Y+35,height=30,width=50)
    c1e_sec = Entry(gui, textvariable=c1e_s, justify="center",bg="grey69")
    c1e_sec.place(x=320,y=C1Y+35,height=30,width=50)

    c2_h = StringVar()
    c2_m = StringVar() 
    c2_s = StringVar()
    
    c2l = Label(gui, text="Clip 2", fg='White', bg=BGCOLOR)
    c2l.place(x=20, y=C2Y-30)
    c2l = Label(gui, text="Start", fg='White', bg=BGCOLOR)
    c2l.place(x=20, y=C2Y)
    c2hl = Label(gui, text="Hour", fg='White', bg=BGCOLOR)
    c2hl.place(x=70, y=C2Y, height=30, width=50)
    c2ml = Label(gui, text="Minute", fg='White', bg=BGCOLOR)
    c2ml.place(x=170, y=C2Y, height=30, width=50)
    c2sl = Label(gui, text="Second", fg='White', bg=BGCOLOR)
    c2sl.place(x=270, y=C2Y, height=30, width=50)

    c2_hour = Entry(gui, textvariable=c2_h, justify="center",bg="grey69")
    c2_hour.place(x=120,y=C2Y,height=30,width=50)
    c2_min = Entry(gui, textvariable=c2_m, justify="center",bg="grey69")
    c2_min.place(x=220,y=C2Y,height=30,width=50)
    c2_sec = Entry(gui, textvariable=c2_s, justify="center",bg="grey69")
    c2_sec.place(x=320,y=C2Y,height=30,width=50)

    c2e_h = StringVar()
    c2e_m = StringVar() 
    c2e_s = StringVar()

    lc2e = (c2e_h,c2e_m,c2e_s)
    lc2s = (c2_h,c2_m,c2_s)
    fill_c2e_button = Button(gui, command=lambda: autoFill(lc2s,lc2e), 
        text='AutoFill', fg='White', bg='AntiqueWhite4') 
    fill_c2e_button.place(x=380,y=C2Y,height=30,width=50)

    c2el = Label(gui, text="End", fg='White', bg=BGCOLOR)
    c2el.place(x=20, y=C2Y+35)
    c2ehl = Label(gui, text="Hour", fg='White', bg=BGCOLOR)
    c2ehl.place(x=70, y=C2Y+35, height=30, width=50)
    c2eml = Label(gui, text="Minute", fg='White', bg=BGCOLOR)
    c2eml.place(x=170, y=C2Y+35, height=30, width=50)
    c2esl = Label(gui, text="Second", fg='White', bg=BGCOLOR)
    c2esl.place(x=270, y=C2Y+35, height=30, width=50)

    c2e_hour = Entry(gui, textvariable=c2e_h, justify="center",bg="grey69")
    c2e_hour.place(x=120,y=C2Y+35,height=30,width=50)
    c2e_min = Entry(gui, textvariable=c2e_m, justify="center",bg="grey69")
    c2e_min.place(x=220,y=C2Y+35,height=30,width=50)
    c2e_sec = Entry(gui, textvariable=c2e_s, justify="center",bg="grey69")
    c2e_sec.place(x=320,y=C2Y+35,height=30,width=50)


    c3_h = StringVar()
    c3_m = StringVar() 
    c3_s = StringVar()
    
    c3l = Label(gui, text="Clip 3", fg='White', bg=BGCOLOR)
    c3l.place(x=20, y=C3Y-30)
    c3l = Label(gui, text="Start", fg='White', bg=BGCOLOR)
    c3l.place(x=20, y=C3Y)
    c3hl = Label(gui, text="Hour", fg='White', bg=BGCOLOR)
    c3hl.place(x=70, y=C3Y, height=30, width=50)
    c3ml = Label(gui, text="Minute", fg='White', bg=BGCOLOR)
    c3ml.place(x=170, y=C3Y, height=30, width=50)
    c3sl = Label(gui, text="Second", fg='White', bg=BGCOLOR)
    c3sl.place(x=270, y=C3Y, height=30, width=50)

    c3_hour = Entry(gui, textvariable=c3_h, justify="center",bg="grey69")
    c3_hour.place(x=120,y=C3Y,height=30,width=50)
    c3_min = Entry(gui, textvariable=c3_m, justify="center",bg="grey69")
    c3_min.place(x=220,y=C3Y,height=30,width=50)
    c3_sec = Entry(gui, textvariable=c3_s, justify="center",bg="grey69")
    c3_sec.place(x=320,y=C3Y,height=30,width=50)

    msg = StringVar()    
    msgbox = Message(gui, textvariable=msg, anchor="nw", aspect=2000)
    msgbox.place(x=30, y=500,height=100,width=300)

    all_time_stamps = (
        (c1_h,c1_m,c1_s),
        (c1e_h,c1e_m,c1e_s),
        (c2_h,c2_m,c2_s),
        (c2e_h,c2e_m,c2e_s),
        (c3_h,c3_m,c3_s)
    )

    go_button = Button(gui, command=lambda: goButton(all_time_stamps,msg,buffer_time), text=' GO! ', fg='White', bg='AntiqueWhite4') 
    go_button.place(x=50,y=400,height=70,width=200)


    gui.mainloop()

    
  
    
    
