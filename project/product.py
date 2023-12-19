from readline import insert_text
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog as fd
import calendar, time, threading
from time import strftime
import tkinter.messagebox as tmsg

#importing necessay requirements
from tkinter import *
from tkinter import messagebox as ms
import sqlite3

with sqlite3.connect('user.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY,password TEX NOT NULL);')
db.commit()
db.close()

class main:
    def __init__(my,master):

        my.master = master
     
        my.account = StringVar()
        my.passcode = StringVar()
        my.new_account = StringVar()
        my.new_passcode = StringVar()
        #development of windows
        my.widgets()

    #sign in abilities
    def login(my):
    	#enabling a database relationship
        with sqlite3.connect('user.db') as db:
            c = db.cursor()

        #identify exisitng username in database
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(my.account.get()),(my.passcode.get())])
        result = c.fetchall()
        if result:
            my.frame.pack_forget()
            my.head['pady'] = 180
            my.head['padx'] = 20
            my.head['text'] = my.account.get() + '\n Close window to continue'

        else:
            ms.showerror('Uh oh!' 'Username not identified.')
            
    def new_user(my):
    	#enabling a database relationship
        with sqlite3.connect('user.db') as db:
            c = db.cursor()

        #attempt to scan for existing account within a database
        find_user = ('SELECT username FROM user WHERE username = ?')
        c.execute(find_user,[(my.new_account.get())])        
        if c.fetchall():
            ms.showerror('Username is in use, input new name')
        else:
            ms.showinfo('Congrats!','Account has been Created!')
            my.log()
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(my.new_account.get()),(my.new_passcode.get())])
        db.commit()

        #login and account creation windown creation process:
    def log(my):
        my.account.set('')
        my.passcode.set('')
        my.frame2.pack_forget()
        my.head['text'] = 'LOGIN'
        my.frame.pack()
    def cr(my):
        my.new_account.set('')
        my.new_passcode.set('')
        my.frame.pack_forget()
        my.head['text'] = 'Create Account'
        my.frame2.pack()
        
    #programming the dimensions and locaions of buttons in window:
    def widgets(my):
        my.head = Label(my.master,text = 'MinimaList',font = ("arial",35, 'bold'), fg= 'dark blue' ,pady = 12)
        my.head.pack()
        my.frame = Frame(my.master,padx =62,pady = 62)
        Label(my.frame,text = 'Username: ',font = ('arial',22),pady=6,padx=6).grid(sticky = W)
        Entry(my.frame,textvariable = my.account,bd = 6,font = ('arial',16)).grid(row=0,column=1)
        Label(my.frame,text = 'Password: ',font = ('arial',22),pady=6,padx=6).grid(sticky = W)
        Entry(my.frame,textvariable = my.passcode,bd = 6,font = ('arial',16),show = '*').grid(row=1,column=1)
        Button(my.frame,text = ' Login ',bd = 4 ,font = ('arial',16),bg= 'light grey', fg= 'dark blue', padx=6,pady=6,command=my.login).grid()
        Button(my.frame,text = ' Create Account ',bd = 4 ,font = ('arial',16),bg= 'light grey',fg= 'dark blue', padx=6,pady=6,command=my.cr).grid(row=2,column=1)
        my.frame.pack()
        
        my.frame2 = Frame(my.master,padx =62,pady = 62)
        Label(my.frame2,text = 'Username: ',font = ('arial',22),pady=6,padx=6).grid(sticky = W)
        Entry(my.frame2,textvariable = my.new_account,bd = 6,font = ('arial',16)).grid(row=0,column=1)
        Label(my.frame2,text = 'Password: ',font = ('',22),pady=6,padx=6).grid(sticky = W)
        Entry(my.frame2,textvariable = my.new_passcode,bd = 6,font = ('arial',16),show = '*').grid(row=1,column=1)
        Button(my.frame2,text = 'Create Account',bd = 4 ,font = ('arial',16),padx=6,pady=6,command=my.new_user).grid()
        Button(my.frame2,text = 'Go to Login',bd = 4 ,font = ('arial',16),padx=6,pady=6,command=my.log).grid(row=2,column=1)

if __name__ == '__main__':
        root = Tk()
        root.title('Login page')
        
        main(root)
        root.mainloop()

class GUI(Tk):

    def __init__(self):
        super().__init__()
        app_width = 595
        app_height = 390
        self.title("MinimaList: Student Organisation")
        self.configure(bg='#082b63')

        s_width = self.winfo_screenwidth()
        s_height = self.winfo_screenheight()

        x  = (s_width/2) - (app_width/2)
        x = int(x)
        y  = (s_height/2) - (app_height/2)
        y = int(y)

        self.geometry(f'{app_width}x{app_height}+{x}+{y}')
        self.maxsize(app_width, app_height)
        self.minsize(app_width, app_height)

        notebook = ttk.Notebook(self)
        notebook.grid(row=0, column=0, sticky=N, padx=10, pady=8)

        notes = Frame(notebook, bg='white')
        notebook.add(notes, text="Notes")

        notesave = Frame(notebook, bg='white')
        notebook.add(notes, text="Notes")

        calculator = Frame(notebook, bg='white')
        notebook.add(calculator, text="Calculator")
        
        calendar = Frame(notebook, bg='white')
        notebook.add(calendar, text="Calendar", padding=1)

        stop_watch = Frame(notebook, bg='white')
        notebook.add(stop_watch, text="Stop Watch")

        flip_clock = Frame(notebook, bg='white')
        notebook.add(flip_clock, text="Flip Clock")

        alarm_clock = Frame(notebook, bg='white')
        notebook.add(alarm_clock, text="Alarm Clock")

        # notes --------------------------------------
        self.notes_textarea = ScrolledText(notes, height=22, width=70) 
        self.notes_textarea.grid(row=0, column=0)

        self.notes_textarea.grid = insert_text ('e')

        menubar = Menu(notes)
        file = Menu(menubar, tearoff = 0)
        file.add_command(label="New",command=self.new_notes)
        file.add_command(label="Open",command=self.open_notes)
        file.add_command(label="Save",command=self.save_notes)
       
        menubar.add_cascade(label="Note-functions",menu=file,font=('verdana',300,'bold'))
        self.config(menu=menubar)

        # calculator --------------------------------
        #Entry Widgets to show calculations
        self.calc_input = Entry(calculator, width=34, borderwidth=2, relief=RIDGE, font=("helvetica", 18, 'bold'))
        self.calc_input.grid(row=0,sticky="n",padx=10, pady=10)

        # <============= Button Design Code starts here.. ==================>
        # using lambda instead of functions to make the use of buttons more clear
        calc_clear = Button(calculator,text="C",width=7,command=lambda:self.calc_input.delete(0,"end"), bg="#082b63", fg="black", relief=RIDGE)
        calc_clear.grid(row=0, column=1, sticky="n", pady=13)

        calc_frame_btns = Frame(calculator, bg='white')
        calc_frame_btns.grid(row=1, column=0)

        calc_nine = Button(calc_frame_btns, text="9",width=12, height=2, font=("helvetica", 12, 'bold'), command=lambda:self.calc_input.insert("end","9"), borderwidth=3, relief=RIDGE)
        calc_nine.grid(row=0, column=0, sticky="n", padx=5, pady=10)

        calc_eight = Button(calc_frame_btns, text="8",width=12, height = 2, font=("helvetica", 12, 'bold'),command=lambda:self.calc_input.insert("end","8"),borderwidth=3,relief=RIDGE)
        calc_eight.grid(row=0, column=1, sticky="n",padx=5, pady=10)

        calc_seven = Button(calc_frame_btns,text="7",width=12, height = 2, font=("helvetica", 12, 'bold'),command=lambda:self.calc_input.insert("end","7"),borderwidth=3,relief=RIDGE)
        calc_seven.grid(row=0, column=2, sticky="n", padx=5, pady=10)

        calc_plus = Button(calc_frame_btns, text="+",width=12, height = 2, font=("helvetica", 12, 'bold'), command=lambda:self.calc_input.insert("end","+"),borderwidth=3,relief=RIDGE)
        calc_plus.grid(row=0, column=3, sticky="n", padx=5, pady=10)


        calc_six = Button(calc_frame_btns, text="6",width=12, height = 2, font=("helvetica", 12, 'bold'),command=lambda:self.calc_input.insert("end","6"),borderwidth=3,relief=RIDGE)
        calc_six.grid(row=1, column=0, sticky="n",padx=5,pady=10)

        calc_five = Button(calc_frame_btns, text="5",width=12, height = 2, font=("helvetica", 12, 'bold'),command=lambda:self.calc_input.insert("end","5"),borderwidth=3,relief=RIDGE)
        calc_five.grid(row=1, column=1, sticky="n",padx=5,pady=10)

        calc_four = Button(calc_frame_btns, text="4",width=12, height = 2, font=("helvetica", 12, 'bold'),command=lambda:self.calc_input.insert("end","4"),borderwidth=3,relief=RIDGE)
        calc_four.grid(row=1, column=2, sticky="n",padx=5,pady=10)

        calc_minus = Button(calc_frame_btns, text="-",width=12, height = 2, font=("helvetica", 12, 'bold'),command=lambda:self.calc_input.insert("end","-"),borderwidth=3,relief=RIDGE)
        calc_minus.grid(row=1, column=3, sticky="n",padx=5,pady=10)



        calc_three = Button(calc_frame_btns, text="3",width=12, height = 2, font=("helvetica", 12, 'bold'),command=lambda:self.calc_input.insert("end","3"),borderwidth=3,relief=RIDGE)
        calc_three.grid(row=3, column=0, sticky="n",padx=5,pady=10)

        calc_two = Button(calc_frame_btns, text="2",width=12, height = 2, font=("helvetica", 12, 'bold'),command=lambda:self.calc_input.insert("end","2"),borderwidth=3,relief=RIDGE)
        calc_two.grid(row=3, column=1, sticky="n",padx=5,pady=10)

        calc_one = Button(calc_frame_btns,text="1",width=12, height = 2, font=("helvetica", 12, 'bold'),command=lambda:self.calc_input.insert("end","1"),borderwidth=3,relief=RIDGE)
        calc_one.grid(row=3, column=2, sticky="n",padx=5,pady=10)

        calc_multiply = Button(calc_frame_btns,text="*",width=12, height = 2, font=("helvetica", 12, 'bold'),command=lambda:self.calc_input.insert("end","*"),borderwidth=3,relief=RIDGE)
        calc_multiply.grid(row=3, column=3, sticky="n",padx=5,pady=10)


        calc_zero = Button(calc_frame_btns, text="0",width=12, height = 2, font=("helvetica", 12, 'bold'),command=lambda:self.calc_input.insert("end","0"),borderwidth=3,relief=RIDGE)
        calc_zero.grid(row=4,column=0, sticky="n",padx=5,pady=10)

        calc_double_zero = Button(calc_frame_btns, text="00",width=12, height = 2, font=("helvetica", 12, 'bold'),command=lambda:self.calc_input.insert("end","00"),borderwidth=3,relief=RIDGE)
        calc_double_zero.grid(row=4,column=1, sticky="n",padx=5,pady=10)

        calc_dot = Button(calc_frame_btns, text=".",width=12, height = 2, font=("helvetica", 12, 'bold'),command=lambda:self.calc_input.insert("end","."),borderwidth=3,relief=RIDGE)
        calc_dot.grid(row=4,column=2, sticky="n",padx=5,pady=10)

        calc_divide = Button(calc_frame_btns,text="/",width=12, height = 2, font=("helvetica", 12, 'bold'),command=lambda:self.calc_input.insert("end","/"),borderwidth=3,relief=RIDGE)
        calc_divide.grid(row=4,column=3, sticky="n",padx=5,pady=10)

        calc_result = Button(calc_frame_btns,text="=",width=12, height = 2, font=("helvetica", 12, 'bold'),command=self.calc_result,bg="#082b63",fg="black",borderwidth=3,relief=RIDGE)
        calc_result.grid(row=5, column=0, sticky="n",padx=5,pady=10)

        calc_modulus = Button(calc_frame_btns,text="%",width=12, height = 2, font=("helvetica", 12, 'bold'),command=lambda:self.calc_input.insert("end","%"),borderwidth=3,relief=RIDGE)
        calc_modulus.grid(row=5, column=1, sticky="n",padx=5,pady=10)

        # -----------------------------------------
        # calendar 
        calendar_top_frame = Frame(calendar, bg='white')
        calendar_top_frame.grid(row=0,column=0, padx=10, pady=10)

        m_label = Label(calendar_top_frame, text="Month",font=('verdana','10','bold'), bg='white')
        m_label.grid(row=0, column=0, padx=5) 

        self.month = Spinbox(calendar_top_frame, from_= 1, to = 12,width="18") 
        self.month.grid(row=0, column=1, padx=5) 
        
        y_label = Label(calendar_top_frame, text="Year",font=('verdana','10','bold'), bg='white')
        y_label.grid(row=0, column=2, padx=5) 

        self.year = Spinbox(calendar_top_frame, from_= 2020, to = 3000,width="18") 
        self.year.grid(row=0, column=3, padx=5) 

        calendar_middle_frame = Frame(calendar, bg='white')
        calendar_middle_frame.grid(row=1,column=0, padx=10, pady=10)
        self.cal = Text(calendar_middle_frame, width=23,height=8,relief=RIDGE,borderwidth=4)
        self.cal.grid(row=0, column=0, padx=20, pady=10)

        calendar_last_frame = Frame(calendar, bg='white')
        calendar_last_frame.grid(row=2,column=0, padx=10, pady=10)

        show = Button(calendar_last_frame,text="Show",font=('verdana',10,'bold'),relief=RIDGE,borderwidth=2, command=self.calendar_show)
        show.grid(row=0, column=0, padx=10, pady=30)

        clear = Button(calendar_last_frame,text="Clear",font=('verdana',10,'bold'),relief=RIDGE,borderwidth=2, command=self.calendar_clear)
        clear.grid(row=0, column=1, padx=10, pady=30)

        # Stop watch ------------------------------------------------
        self.h = 00 
        self.m = 00 
        self.s = 00 
        self.stop_sw = 0 

        self.stopwatch_label = Label(stop_watch, text=f'{self.h}:{self.m}:{self.s}', font= ('verdana', 30, 'bold'), bg='white')
        self.stopwatch_label.grid(row=0, column=0, stick='n', padx=80, pady=40)

        stopwatch_frame_btn = Frame(stop_watch, bg='white')
        stopwatch_frame_btn.grid(row=1, column=0) 

        sw_btn_start = Button(stopwatch_frame_btn, text='Start', width=10, font=('verdana', 20, 'bold'), bg='#082b63', fg='black', command=self.sw_start)
        sw_btn_start.grid(row=0, column=0, padx=10, pady=40, sticky='s')

        sw_btn_pause = Button(stopwatch_frame_btn, text='Pause', width=10, font=('verdana', 20, 'bold'), bg='#082b63', fg='black', command=self.sw_pause)
        sw_btn_pause.grid(row=0, column=1, padx=10, pady=40, sticky='s')
        
        sw_btn_reset = Button(stopwatch_frame_btn, text='Reset', width=10, font=('verdana', 20, 'bold'), bg='#082b63', fg='black', command=self.sw_reset)
        sw_btn_reset.grid(row=0, column=2, padx=10, pady=40, sticky='s')
        
        #  Flip Clock -------------------------------------------
        self.clock_time = Label(flip_clock, text="", font=('verdana', 36, 'bold'), bg='white')
        self.clock_time.grid(row=2, column=50, stick='n', padx=120, pady=80 )
        self.show_flip_clock()

        #  Alarm Clock ------------------------------------------
        # self.set_alarm_clock = Label(alarm_clock, text="00:00:00", font=('verdana', 36, 'bold'), bg='white')
        # self.set_alarm_clock.grid(row=0, column=0, padx=10, pady=10, sticky='n')

        # enter hour 
        alarm_hour_label = Label(alarm_clock, text="Enter Hour(s)", bg='light grey', fg= 'black', font=('verdana', 15))
        alarm_hour_label.grid(row=0, column=0, padx=10, pady=10)
        self.alarm_hour_inp = Spinbox(alarm_clock, from_=0, to=50, font=('verdana', 18))
        self.alarm_hour_inp.grid(row=0, column=1, padx=40, pady=50)

        # enter minutes 
        alarm_min_label = Label(alarm_clock, text="Enter Minutes", bg='light grey', fg= 'black', font=('verdana', 15))
        alarm_min_label.grid(row=1, column=0, padx=10, pady=10)
        self.alarm_min_inp = Spinbox(alarm_clock, from_=0, to=60, font=('verdana', 18))
        self.alarm_min_inp.grid(row=1, column=1, padx=40, pady=50)

        set_alarm_btn = Button(alarm_clock,text='Set Alarm', font=('verdana', 10, "bold"), bg='#082b63', fg='black', command=self.check_inp)
        set_alarm_btn.grid(row=2, column=0, sticky='n')

    # notes related functions
    def new_notes(self):
        self.notes_textarea.delete('1.0','end')
    def open_notes(self):
        filename = fd.askopenfilename(
                initialdir = '/',
                title="Select file",
                filetypes=(("Text files","*.txt"),) )
        file = open(filename)
        self.notes_textarea.insert('end',file.read())
    def save_notes(self):
        filename = fd.asksaveasfile(mode="w",defaultextension='.txt')
        if filename is None:
                return
        file_save =  str(self.notes_textarea.get(1.0,END))
        filename.write(file_save)
        filename.close()

    # calendar related functions 
    def calendar_show(self):
        m = int(self.month.get())
        y = int(self.year.get())
        output = calendar.month(y,m)
        self.cal.insert('end',output)
        return 0
    def calendar_clear(self):
        self.cal.delete(1.0,'end')
        return 0

    # calculator realted functions
    def calc_result(self):
        try:
                
            if self.calc_input.get() == "":
                        self.calc_input.insert("end","error")
            elif self.calc_input.get()[0] == "0":
                        self.calc_input.delete(0,"end")
                        self.calc_input.insert("end","error")

            else:
                res = self.calc_input.get()
                res = eval(res)
                self.calc_input.delete(0,"end")
                self.calc_input.insert("end",res)
        except SyntaxError:
            self.calc_input.insert("end","invalid input")    

    # stop watch funcitons 
    def sw_start(self):
        self.h = int(self.h)
        self.m = int(self.m)
        self.s = int(self.s)
        self.s += 1
        if self.s == 60:
            self.s = 0
            self.m += 1
        if self.m == 60:
            self.m = 0
            self.h += 1
        if self.stop_sw == 0:
            self.stopwatch_label.config(text=f'{self.h}:{self.m}:{self.s}')
            self.stopwatch_label.after(1000, self.sw_start)
    def sw_pause(self):
        self.stop_sw = 1
    def sw_reset(self):
        self.h = 00
        self.m = 00
        self.s = 00
        self.stop_sw = 0
        self.stopwatch_label.config(text=f'{self.h}:{self.m}:{self.s}')
        return 0

    # keep clock running:
    def show_flip_clock(self):  
        current_time = strftime("%H: %M: %S\n %d-%m-%Y ")
        self.clock_time.config(text=current_time)
        self.clock_time.after(100, self.show_flip_clock)

    # alarm functions
    def check_inp(self):
        h = int(self.alarm_hour_inp.get())
        m = int(self.alarm_min_inp.get())
        if h <= 23 and m <=60 :
            self.thread_start(h,m)
            if m < 10:
                m = f"0{m}"
            tmsg.showinfo("Alarm set", f"Alarm has been set for {h} : {m}")
        return 0
    
    def thread_start(self,h,m):
        t = threading.Thread(target=self.set_alarm, args=[h,m])
        t.start()
    
    def set_alarm(self, h, m):
        if m < 10 :
            m = f"0{m}"

        set_alarm = f"{h}:{m}"
        current_time = time.strftime("%H:%M")

        while set_alarm != current_time:
            current_time = time.strftime("%H:%M")
            print(current_time)
        
        if set_alarm == current_time:
            tmsg.showinfo("Exit Alarm", f"Alarm was set at {h} : {m}")

        return 0
# ---- ** End ** ---- 

if __name__ == '__main__':
    win = GUI()
    win.mainloop()