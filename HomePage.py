from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from ttkthemes import themed_tk
from tkcalendar import *

# from tkinter import Phot
# from try_search import SearchAndReportFilterStudentWidget
# import guest
import cx_Oracle as cx
import datetime
import Queries
# from PIL import Image, ImageTk

link='hr/hr@//localhost:1521/xe'

# global gobalroot

# def Toggle(val=1):
#     if(val==0):
#         root1 = Tk()
#         globalroot=root1
#         root1.title('Search manage and report')
#         root1.state("zoomed")
#         widget = SearchAndReportFilterStudentWidget(root1)
#         widget.pack(expand=True, fill='both')
#         root1.mainloop()
#     else:
#         print('comming')
#         root = Tk()
#         globalroot=root
#         root.title('Home')
#         root.state("zoomed")
#         widget = HomeNewStudentWidget(root)
#         widget.pack(expand=True, fill='both')
#         root.mainloop()


    #global variables
current_time = datetime.datetime.now()
# Date=str(current_time.day)+'/'+str(current_time.month)+'/'+str(current_time.year)
Date=str(current_time.month)+'/'+str(current_time.day)+'/'+str(current_time.year)[2:]


class HomeNewStudentWidget(Frame):
    def __init__(self,master=None, **kw):   #the initial code after running home page new->staff
        Frame.__init__(self,master, **kw)
        self.owner=''
        self.MainLogin()

    
    def MainLogin(self):
        self.MainHomeScreenToggel = Frame(self)
        self.ProjectNameLabel = Label(self.MainHomeScreenToggel)
        self.ProjectNameLabel.config(anchor='center',background='#808080', cursor='arrow')
        self.ProjectNameLabel.config(foreground="white",text='Student-Staff Healthcare Management system',font=("times new roman",40,"bold"))
        self.ProjectNameLabel.pack(anchor='n', expand='true', fill='x', ipady='20', pady='20', side='top')
        self.LoginFrame = Frame(self.MainHomeScreenToggel)
        self.LoginLabel = Label(self.LoginFrame)
        self.LoginLabel.config(foreground="white",background="#804000",justify='center', text='Login',font=("times new roman",20))
        self.LoginLabel.pack( expand='true', fill='x', ipadx='10', pady='0', side='top')
        self.UserNameLabel = Label(self.LoginFrame)
        self.UserNameLabel.config(foreground="white",background="#804000",justify='center', text=' Username',font=("times new roman",18,"bold"))
        self.UserNameLabel.pack(anchor='n', expand='true', ipady='1',pady=("30","0") ,padx='25', side='left')
        self.UsernameEntry = Entry(self.LoginFrame)
        self.UsernameEntry.config(background="white",border="0",borderwidth='5', justify='center', relief='sunken',font=("times new roman",10,"bold"))
        self.UsernameEntry.pack(anchor='center', expand='true', ipady='5',ipadx="15", padx='20', pady='15', side='top')
        self.PasswordLabel = Label(self.LoginFrame)
        self.PasswordLabel.config(foreground="white",background="#804000",text='Password',font=("times new roman",18,"bold"))
        self.PasswordLabel.place(anchor='nw', relx='0.08', rely='0.6', x='0', y='0')
        self.UsernamePassword =Entry(self.LoginFrame)
        self.UsernamePassword.config(background="white",borderwidth='5',justify='left', show='•', relief='sunken',font=("times new roman",10,"bold"))
        self.UsernamePassword.pack(anchor='center', expand='true', ipady='5',ipadx="25", padx='25', pady='15', side='top')
        self.SubmitButton = Button(self.LoginFrame)
        self.SubmitButton.config(justify='center',borderwidth="3",relief='raised', text=' Submit',command=self.LSubmit,font=("times new roman",10,"bold"))
        self.SubmitButton.pack(ipadx='30', side='top')
        self.RegisterButton = Button(self.LoginFrame)
        self.RegisterButton.config(justify='center',borderwidth="3",relief='raised',text='Register',command=self.LRegister,font=("times new roman",10,"bold"))
        self.RegisterButton.pack(ipadx='28', pady='5', side='top')
        self.LoginFrame.config(background="#804000",borderwidth='10', height='350',relief='groove', width='400')
        self.LoginFrame.place(anchor='center', relx='0.5', rely='0.5',relheight="0.5",relwidth="0.3", x='0', y='0')
        self.MainHomeScreenToggel.config(height='200', width='200')
        self.MainHomeScreenToggel.place(anchor='nw', relheight='1.0', relwidth='1.0', x='0', y='0')


    def LRegister(self):
        self.LoginFrame = Frame(self.MainHomeScreenToggel)
        self.LoginLabel = Label(self.LoginFrame)
        self.LoginLabel.config(foreground="white",background="#804000",justify='center', text='Register',font=("times new roman",20,"bold"))
        self.LoginLabel.pack( expand='true', fill='x', ipadx='10', pady='0', side='top')
        self.UserNameLabel = Label(self.LoginFrame)
        self.UserNameLabel.config(foreground="white",background="#804000",justify='center', text=' Username',font=("times new roman",18,"bold"))
        self.UserNameLabel.pack(anchor='n', expand='true', ipady='1',pady=("30","0") ,padx='25', side='left')
        self.UsernameEntry = Entry(self.LoginFrame)
        self.UsernameEntry.config(background="white",border="0",borderwidth='5', justify='center', relief='sunken',font=("times new roman",10,"bold"))
        self.UsernameEntry.pack(anchor='center', expand='true', ipady='5',ipadx="15", padx='20', pady='15', side='top')
        self.PasswordLabel = Label(self.LoginFrame)
        self.PasswordLabel.config(foreground="white",background="#804000",text='Password',font=("times new roman",18,"bold"))
        self.PasswordLabel.place(anchor='nw', relx='0.08', rely='0.6', x='0', y='0')
        self.UsernamePassword = Entry(self.LoginFrame)
        self.UsernamePassword.config(background="white",borderwidth='5',justify='left', show='•', relief='sunken',font=("times new roman",10,"bold"))
        self.UsernamePassword.pack(anchor='center', expand='true', ipady='5',ipadx="25", padx='25', pady='15', side='top')
        self.SubmitButton = Button(self.LoginFrame)
        self.SubmitButton.config(justify='center',borderwidth="3",relief='raised', text='Register',command=self.Lregister,font=("times new roman",10,"bold"))
        self.SubmitButton.pack(ipadx='30', side='top')
        self.RegisterButton = Button(self.LoginFrame)
        self.RegisterButton.config(justify='center',borderwidth="3",relief='raised',text=' <--Login ',command=self.Lback,font=("times new roman",10,"bold"))
        self.RegisterButton.pack(ipadx='28', pady='5', side='top')
        self.LoginFrame.config(background="#804000",borderwidth='10', height='350',relief='groove', width='400')
        self.LoginFrame.place(anchor='center', relx='0.5', rely='0.5',relheight="0.5",relwidth="0.3", x='0', y='0')

    # #show status to user
    # def showerror(self,err,color='#ff0000'):
    #     # self.status = Label(self.LoginFrame)
    #     # self.status.config(background=color,text=err)
    #     # self.status.place(anchor='nw', relwidth='1.0', relx='0.14', rely='0.14', x='0', y='0')
    #     messagebox.showinfo("Server says",err)
    
    def Lregister(self):
        try:
            conn = cx.connect(link)
            cur = conn.cursor()
            username=str(self.UsernameEntry.get())
            password=self.UsernamePassword.get()
            if(username and password):
                print(username,password)
                try:
                    cur.execute('''
                    insert into Admin values(:username,:password)
                    ''',{
                        'username':username,
                        'password':password
                    })
                    conn.commit()
                    messagebox.showinfo('Server Says','Registerd sucessfully')
                    self.Lback()
                except Exception as err:
                    messagebox.showerror('Server says','user name already exisits')
            else:
                messagebox.showerror('Server says','Username and password required')
            
        except Exception as err:
            self.showerror('Poor Connection')

    def Lback(self):
        self.LoginFrame = Frame(self.MainHomeScreenToggel)
        self.LoginLabel = Label(self.LoginFrame)
        self.LoginLabel.config(foreground="white",background="#804000",justify='center', text='Login',font=("times new roman",20,"bold"))
        self.LoginLabel.pack( expand='true', fill='x', ipadx='10', pady='0', side='top')
        self.UserNameLabel = Label(self.LoginFrame)
        self.UserNameLabel.config(foreground="white",background="#804000",justify='center', text=' Username',font=("times new roman",18,"bold"))
        self.UserNameLabel.pack(anchor='n', expand='true', ipady='1',pady=("30","0") ,padx='25', side='left')
        self.UsernameEntry = Entry(self.LoginFrame)
        self.UsernameEntry.config(background="white",border="0",borderwidth='5', justify='center', relief='sunken',font=("times new roman",10,"bold"))
        self.UsernameEntry.pack(anchor='center', expand='true', ipady='5',ipadx="15", padx='20', pady='15', side='top')
        self.PasswordLabel = Label(self.LoginFrame)
        self.PasswordLabel.config(foreground="white",background="#804000",text='Password',font=("times new roman",18,"bold"))
        self.PasswordLabel.place(anchor='nw', relx='0.08', rely='0.6', x='0', y='0')
        self.UsernamePassword = Entry(self.LoginFrame)
        self.UsernamePassword.config(background="white",borderwidth='5',justify='left', show='•', relief='sunken',font=("times new roman",10,"bold"))
        self.UsernamePassword.pack(anchor='center', expand='true', ipady='5',ipadx="25", padx='25', pady='15', side='top')
        self.SubmitButton = Button(self.LoginFrame)
        self.SubmitButton.config(justify='center',borderwidth="3",relief='raised', text=' Submit',command=self.LSubmit,font=("times new roman",10,"bold"))
        self.SubmitButton.pack(ipadx='30', side='top')
        self.RegisterButton = Button(self.LoginFrame)
        self.RegisterButton.config(justify='center',borderwidth="3",relief='raised',text='Register',command=self.LRegister,font=("times new roman",10,"bold"))
        self.RegisterButton.pack(ipadx='28', pady='5', side='top')
        self.LoginFrame.config(background="#804000",borderwidth='10', height='350',relief='groove', width='400')
        self.LoginFrame.place(anchor='center', relx='0.5', rely='0.5',relheight="0.5",relwidth="0.3", x='0', y='0')


    def MainHomePage(self):
        self.MainHomeScreenToggel = Frame(self)
        self.HomeFrame = Frame(self.MainHomeScreenToggel)
        self.HeaderFrame = Frame(self.HomeFrame)
        self.HeadingLabel = Label(self.HeaderFrame)
        self.HeadingLabel.config(background='#808080',foreground='#ffff80', height='5', text='Student-Staff healthcare Management system',font=("times new roman",20,"bold"))
        self.HeadingLabel.pack(anchor='center', expand='true', fill='x', side='top')
        #navigation bar frame
        self.NavFrame = Frame(self.HeaderFrame)
        #buttom to add new student and staff
        self.New_Student_Staff_Add_Button = Button(self.NavFrame)
        self.New_Student_Staff_Add_Button.config(height='10', text='New', width='15')
        self.New_Student_Staff_Add_Button.pack(anchor='center', padx='3', pady='2', side='left')
        self.New_Student_Staff_Add_Button.configure(command=self.New_student_staff_info)
        #button to add guest info
        self.button_2 = Button(self.NavFrame)
        self.button_2.config(height='10', text='Guest', width='15')
        self.button_2.pack(ipady='1', padx='3', pady='3', side='left')
        self.button_2.configure(command=self.Guest)
        #button to add student and staff health status
        self.student_staff_status_update = Button(self.NavFrame)
        self.student_staff_status_update.config(height='10', text='Status_Update', width='15')
        self.student_staff_status_update.pack(ipady='1', padx='3', pady='3', side='left')
        self.student_staff_status_update.configure(command=self.status_update)
        #button for report genration
        self.Report_Generation = Button(self.NavFrame)
        self.Report_Generation.config(height='10', text='Report', width='15')
        self.Report_Generation.pack(ipady='1', padx='3', pady='3', side='left')
        self.Report_Generation.configure(command=self.Report)
        #update student staff information in databse
        self.Update = Button(self.NavFrame)
        self.Update.config(height='10', text='Logout', width='15')
        self.Update.pack(ipady='1', padx='3', pady='3', side='left')
        self.Update.configure(command=self.Logout)
        #admin name with login date
        self.AdminNameLable = Label(self.NavFrame)
        self.AdminNameLable.config(text='Admin:'+self.owner+'\nDate:'+Date, width='50')
        self.AdminNameLable.pack(ipadx='70', ipady='5', padx='70', side='left')
        self.NavFrame.config(background='#000000', height='60', highlightcolor='#000000', width='200')
        self.NavFrame.pack(anchor='center', expand='true', fill='x', side='top')
        self.NavFrame.pack_propagate(0)
        self.HeaderFrame.config(background='#808080', height='230', width='200')
        self.HeaderFrame.pack(anchor='n', expand='true', fill='x', side='top')
        self.HeaderFrame.pack_propagate(0)
        self.BodyFrame = Frame(self.HomeFrame)
        self.innerNavFrame = Frame(self.BodyFrame)
        self.Student_Info_Button = Button(self.innerNavFrame)
        self.Student_Info_Button.config(borderwidth='4', justify='center', relief='raised', text='Student')
        self.Student_Info_Button.config(width='6')
        self.Student_Info_Button.grid(columnspan='2', ipady='20', padx='8', pady='10')
        self.Student_Info_Button.configure(command=self.student_Info)
        self.Staff_info_button = Button(self.innerNavFrame)
        self.Staff_info_button.config(borderwidth='4', justify='center', relief='raised', text='Staff')
        self.Staff_info_button.config(width='6')
        self.Staff_info_button.grid(column='0', columnspan='2', ipady='20', padx='8', pady='10', row='1')
        self.Staff_info_button.configure(command=self.satff_info)
        self.innerNavFrame.config(background='#808080', borderwidth='5', height='200', relief='ridge')
        self.innerNavFrame.config(takefocus=True, width='100')
        self.innerNavFrame.grid(ipady='90', padx='15', pady='13')
        self.innerNavFrame.grid_propagate(0)
        self.innerNavFrame.rowconfigure('0', pad='0')
        self.FormFrame = Frame(self.BodyFrame)
        self.Student_label_form = LabelFrame(self.FormFrame)
        self.Student_ID_Label = Label(self.Student_label_form)
        self.Student_ID_Label.config(text='Student ID*')
        self.Student_ID_Label.grid(padx='20', pady='2')
        self.Student_ID_entry = Entry(self.Student_label_form)
        self.Student_ID_entry.config(justify='center')
        self.Student_ID_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='0')
        self.student_name_label = Label(self.Student_label_form)
        self.student_name_label.config(text='Student FullName')
        self.student_name_label.grid(column='0', padx='20', pady='2', row='1')
        self.Student_name_entry = Entry(self.Student_label_form)
        self.Student_name_entry.config(justify='center')
        self.Student_name_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='1')
        self.student_branch_label = Label(self.Student_label_form)
        self.student_branch_label.config(text='Branch')
        self.student_branch_label.grid(column='0', padx='20', pady='2', row='2')

        self.Dept_rad_frame = Frame(self.Student_label_form)
        self.Dept_rad_frame.config(height='200', width='200')
        self.Dept_rad_frame.grid(column='1', row='2',padx='20',pady='2',ipadx='30',ipady='6')
        Dept = StringVar('')
        self.Branch=Dept
        self.IS_rad = Radiobutton(self.Dept_rad_frame)
        self.IS_rad.config(text='IS', value='1', variable=Dept)
        self.IS_rad.grid(column='1',row='2',padx='10',pady='2')
        self.IS_rad.deselect()
        self.CS_rad = Radiobutton(self.Dept_rad_frame)
        self.CS_rad.config(text='CS', value='2', variable=Dept)
        self.CS_rad.grid(column='2', row='2',padx='10',pady='2')
        self.CS_rad.deselect()
        self.ME_rad = Radiobutton(self.Dept_rad_frame)
        self.ME_rad.config(text='ME', value='3', variable=Dept)
        self.ME_rad.grid(column='3', row='2',padx='10',pady='2')
        self.ME_rad.deselect()
        self.CV_rad = Radiobutton(self.Dept_rad_frame)
        self.CV_rad.config(text='CV', value='4', variable=Dept)
        self.CV_rad.grid(column='4', row='2',padx='10',pady='2')
        self.CV_rad.deselect()
        self.EC_rad = Radiobutton(self.Dept_rad_frame)
        self.EC_rad.config(text='EC', value='5', variable=Dept)
        self.EC_rad.grid(column='5', row='2',padx='10',pady='2')
        self.EC_rad.deselect()
        self.IS_rad.select()
        self.Student_phoneno_label = Label(self.Student_label_form)
        self.Student_phoneno_label.config(text='PhoneNumber')
        self.Student_phoneno_label.grid(column='0', padx='20', pady='2', row='4')
        self.student_phoneno_entry = Entry(self.Student_label_form)
        self.student_phoneno_entry.config(justify='center')
        self.student_phoneno_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='4')
        self.Student_adress_label = Label(self.Student_label_form)
        self.Student_adress_label.config(text='Adress')
        self.Student_adress_label.grid(column='0', padx='20', pady='2', row='5')
        self.student_adress_entry = Entry(self.Student_label_form)
        self.student_adress_entry.config(justify='center')
        self.student_adress_entry.grid(column='1', ipadx='40', ipady='20', padx='25', pady='2', row='5')
        self.Add_to_DB_BUTTON = Button(self.Student_label_form)
        self.Add_to_DB_BUTTON.config(text='Add')
        self.Add_to_DB_BUTTON.grid(column='0', ipadx='35', padx='20', pady='10', row='7')
        self.Add_to_DB_BUTTON.configure(command=lambda:self.Insert_to_database('student'))
        self.Clear_button = Button(self.Student_label_form)
        self.Clear_button.config(text='Clear')
        self.Clear_button.grid(column='1', ipadx='35', padx='20', pady='10', row='7')
        self.Clear_button.configure(command=lambda:self.clear('student'))
        self.Student_label_form.config(height='400', text='Student', width='800')
        self.Student_label_form.pack(expand='true', fill='both', side='top')
        self.Student_label_form.pack_propagate(0)
        self.FormFrame.config(height='200', width='200')
        self.FormFrame.place(anchor='center', height='20', relheight='0.9', relwidth='0.7', relx='0.5', rely='0.5', width='100', x='0', y='0')
        self.BodyFrame.config(background='#c0c0c0', borderwidth='10', height='200', relief='ridge')
        self.BodyFrame.config(width='200')
        self.BodyFrame.place(anchor='center', relheight='0.6', relwidth='1', relx='0.5', rely='0.65', x='0', y='0')
        self.HomeFrame.config(height='200', width='200')
        self.HomeFrame.pack(anchor='center', expand='true', fill='both', side='top')
        self.HomeFrame.pack_propagate(0)
        self.MainHomeScreenToggel.config(height='200', width='200')
        self.MainHomeScreenToggel.place(anchor='nw', relheight='1.0', relwidth='1.0', x='0', y='0')

    #username and password vaidation
    def LSubmit(self):
        username=str(self.UsernameEntry.get())
        password=str(self.UsernamePassword.get())
        if username and password:
            try:
                conn=cx.connect(link)
                cur=conn.cursor()
                try:
                    cur.execute('select * from Admin where username=:username and password=:password',{
                        'username':username,
                        'password':password
                    })
                    print(cur.fetchall())
                    if(cur.rowcount):
                        messagebox.showinfo('Server Says','Login SucessFull')
                        try:
                            self.owner=username
                            self.MainHomePage()
                        except Exception as err:
                            print(err)
                    else:
                        messagebox.showerror('Server says',' incorrect Username/password ')
                except Exception as err:
                    print(err)
            except Exception as err:
                print(err)
        else:
            messagebox.showerror('Server says','Username and password required')





        # self.IS_rad.deselect()
        # self.CS_rad.deselect()
        # self.ME_rad.deselect()
        # self.CV_rad.deselect()
        # self.EC_rad.deselect()

        # self.Student_Section_Label = Label(self.Student_label_form)
        # self.Student_Section_Label.config(text='Section')
        # self.Student_Section_Label.grid(column='0', padx='20', pady='2', row='3')
        # self.student_section_entry = Entry(self.Student_label_form)
        # self.student_section_entry.config(justify='center')
        # self.student_section_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='3')


    
    def showerror(self,err,color='#ff0000'):
        messagebox.showinfo("Server says",err)

    #UI for staff student info
    def New_student_staff_info(self):
        root.title('Home/New')
        self.BodyFrame = Frame(self.HomeFrame)
        self.innerNavFrame = Frame(self.BodyFrame)
        self.Student_Info_Button = Button(self.innerNavFrame)
        self.Student_Info_Button.config(borderwidth='4', justify='center', relief='raised', text='Student')
        self.Student_Info_Button.config(width='6')
        self.Student_Info_Button.grid(columnspan='2', ipady='20', padx='8', pady='10')
        self.Student_Info_Button.configure(command=self.student_Info)
        self.Staff_info_button = Button(self.innerNavFrame)
        self.Staff_info_button.config(borderwidth='4', justify='center', relief='raised', text='Staff')
        self.Staff_info_button.config(width='6')
        self.Staff_info_button.grid(column='0', columnspan='2', ipady='20', padx='8', pady='10', row='1')
        self.Staff_info_button.configure(command=self.satff_info)
        self.innerNavFrame.config(background='#808080', borderwidth='5', height='200', relief='ridge')
        self.innerNavFrame.config(takefocus=True, width='100')
        self.innerNavFrame.grid(ipady='90', padx='15', pady='13')
        self.innerNavFrame.grid_propagate(0)
        self.innerNavFrame.rowconfigure('0', pad='0')
        self.FormFrame = Frame(self.BodyFrame)
        self.Student_label_form = LabelFrame(self.FormFrame)
        self.Student_ID_Label = Label(self.Student_label_form)
        self.Student_ID_Label.config(text='Student ID*')
        self.Student_ID_Label.grid(padx='20', pady='2')
        self.Student_ID_entry = Entry(self.Student_label_form)
        self.Student_ID_entry.config(justify='center')
        self.Student_ID_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='0')
        self.student_name_label = Label(self.Student_label_form)
        self.student_name_label.config(text='Student FullName')
        self.student_name_label.grid(column='0', padx='20', pady='2', row='1')
        self.Student_name_entry = Entry(self.Student_label_form)
        self.Student_name_entry.config(justify='center')
        self.Student_name_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='1')
        self.student_branch_label = Label(self.Student_label_form)
        self.student_branch_label.config(text='Branch')
        self.student_branch_label.grid(column='0', padx='20', pady='2', row='2')
        
        # self.Student_Section_Label = Label(self.Student_label_form)
        # self.Student_Section_Label.config(text='Section')
        # self.Student_Section_Label.grid(column='0', padx='20', pady='2', row='3')

        self.Dept_rad_frame = Frame(self.Student_label_form)
        self.Dept_rad_frame.config(height='200', width='200')
        self.Dept_rad_frame.grid(column='1', row='2',padx='20',pady='2',ipadx='30',ipady='6')
        Dept = StringVar('')
        self.Branch=Dept
        self.IS_rad = Radiobutton(self.Dept_rad_frame)
        self.IS_rad.config(text='IS', value='1', variable=Dept)
        self.IS_rad.grid(column='1',row='2',padx='10',pady='2')
        self.CS_rad = Radiobutton(self.Dept_rad_frame)
        self.CS_rad.config(text='CS', value='2', variable=Dept)
        self.CS_rad.grid(column='2', row='2',padx='10',pady='2')
        self.ME_rad = Radiobutton(self.Dept_rad_frame)
        self.ME_rad.config(text='ME', value='3', variable=Dept)
        self.ME_rad.grid(column='3', row='2',padx='10',pady='2')
        self.CV_rad = Radiobutton(self.Dept_rad_frame)
        self.CV_rad.config(text='CV', value='4', variable=Dept)
        self.CV_rad.grid(column='4', row='2',padx='10',pady='2')
        self.EC_rad = Radiobutton(self.Dept_rad_frame)
        self.EC_rad.config(text='EC', value='5', variable=Dept)
        self.EC_rad.grid(column='5', row='2',padx='10',pady='2')
        self.IS_rad.select()

        self.Student_phoneno_label = Label(self.Student_label_form)
        self.Student_phoneno_label.config(text='PhoneNumber')
        self.Student_phoneno_label.grid(column='0', padx='20', pady='2', row='4')
        self.student_phoneno_entry = Entry(self.Student_label_form)
        self.student_phoneno_entry.config(justify='center')
        self.student_phoneno_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='4')
        self.Student_adress_label = Label(self.Student_label_form)
        self.Student_adress_label.config(text='Adress')
        self.Student_adress_label.grid(column='0', padx='20', pady='2', row='5')
        self.student_adress_entry = Entry(self.Student_label_form)
        self.student_adress_entry.config(justify='center')
        self.student_adress_entry.grid(column='1', ipadx='40', ipady='20', padx='25', pady='2', row='5')
        self.Add_to_DB_BUTTON = Button(self.Student_label_form)
        self.Add_to_DB_BUTTON.config(text='Add')
        self.Add_to_DB_BUTTON.grid(column='0', ipadx='35', padx='20', pady='10', row='7')
        self.Add_to_DB_BUTTON.configure(command=lambda:self.Insert_to_database('student'))
        self.Clear_button = Button(self.Student_label_form)
        self.Clear_button.config(text='Clear')
        self.Clear_button.grid(column='1', ipadx='35', padx='20', pady='10', row='7')
        self.Clear_button.configure(command=lambda:self.clear('student'))
        self.Student_label_form.config(height='400', text='Student', width='800')
        self.Student_label_form.pack(expand='true', fill='both', side='top')
        self.Student_label_form.pack_propagate(0)
        self.FormFrame.config(height='200', width='200')
        self.FormFrame.place(anchor='center', height='20', relheight='0.9', relwidth='0.7', relx='0.5', rely='0.5', width='100', x='0', y='0')
        self.BodyFrame.config(background='#c0c0c0', borderwidth='10', height='200', relief='ridge')
        self.BodyFrame.config(width='200')
        self.BodyFrame.place(anchor='center', relheight='0.6', relwidth='1', relx='0.5', rely='0.65', x='0', y='0')
    #UI end of staff student info
    
    #UI for guest
    def Guest(self):
        root.title('Home/Guest')
        self.FormFrame = Frame(self.BodyFrame)
        self.Guest_label_form = LabelFrame(self.FormFrame)
        self.Guest_Name_Label = Label(self.Guest_label_form)
        self.Guest_Name_Label.config(text='Guest Full Name')
        self.Guest_Name_Label.grid(padx='20', pady='2')
        self.Guest_Name_entry = Entry(self.Guest_label_form)
        self.Guest_Name_entry.config(justify='center')
        self.Guest_Name_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='0')
        self.Guest_Phone_label = Label(self.Guest_label_form)
        self.Guest_Phone_label.config(text='Phone Number*')
        self.Guest_Phone_label.grid(column='0', padx='20', pady='2', row='1')
        self.Add_to_DB_BUTTON = Button(self.Guest_label_form)
        self.Add_to_DB_BUTTON.config(text='Add')
        self.Add_to_DB_BUTTON.grid(column='0', ipadx='35', padx='20', pady='10', row='12')
        self.Add_to_DB_BUTTON.configure(command=lambda:self.Insert_to_database('Guest'))
        self.Clear_button = Button(self.Guest_label_form)
        self.Clear_button.config(text='Clear')
        self.Clear_button.grid(column='1', ipadx='35', padx='20', pady='10', row='12')
        self.Clear_button.configure(command=lambda:self.clear('Guest'))
        self.Guest_Phone_Entry = Entry(self.Guest_label_form)
        self.Guest_Phone_Entry.config(justify='center')
        self.Guest_Phone_Entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='1')
        self.Acadamics_CB = Checkbutton(self.Guest_label_form)
        Acadamics = StringVar('')
        self.Acadamics=Acadamics
        self.Acadamics_CB.config(offvalue='No', onvalue='Acadamics', state='normal', text='Acadamics')
        self.Acadamics_CB.config(variable=Acadamics, width='10')
        self.Acadamics_CB.grid(column='0', padx='20', pady='2', row='4')
        self.Acadamics_CB.deselect()
        self.Admission_CB = Checkbutton(self.Guest_label_form)
        Admission = StringVar('')
        self.Admission=Admission
        self.Admission_CB.config(offvalue='No', onvalue='Admission', text='Admission', variable=Admission)
        self.Admission_CB.config(width='10')
        self.Admission_CB.grid(column='0', padx='20', pady='2', row='5')
        self.Admission_CB.deselect()
        self.Placement_cb = Checkbutton(self.Guest_label_form)
        placement = StringVar('')
        self.placement=placement
        self.Placement_cb.config(offvalue='No', onvalue='placement', text='Placement', variable=placement)
        self.Placement_cb.config(width='10')
        self.Placement_cb.grid(column='0', padx='20', pady='2', row='6')
        self.Placement_cb.deselect()
        self.Finance_cb = Checkbutton(self.Guest_label_form)
        Finance = StringVar('')
        self.Finace=Finance
        self.Finance_cb.config(offvalue='No', onvalue='Finance', text='   Finance ', variable=Finance,width='20')
        self.Finance_cb.config(width='20')
        self.Finance_cb.grid(column='0', padx='20', pady='2', row='7')
        self.Finance_cb.deselect()
        self.Guest_update_button = Button(self.Guest_label_form)
        self.Guest_update_button.config(text='Update')
        self.Guest_update_button.grid(column='2', ipadx='35', padx='20', pady='10', row='12')
        self.Guest_update_button.configure(command=self.Update_guest)

        self.Guest_Check_button = Button(self.Guest_label_form)
        self.Guest_Check_button.config(text='Check')
        self.Guest_Check_button.grid(column='3', ipadx='35', padx='20', pady='10', row='1')
        self.Guest_Check_button.configure(command=self.Check_guest)

        self.Visited_label = Label(self.Guest_label_form)
        self.Visited_label.config(borderwidth='3', justify='center', relief='groove', text='Visited')
        self.Visited_label.config(width='75')
        self.Visited_label.grid(column='0', columnspan='5', padx='20', pady='5', row='2')
        self.Guest_label_form.config(height='400',text='Guest', width='800')
        self.Guest_label_form.pack(anchor='center', expand='true', fill='both', side='top')
        self.Guest_label_form.pack_propagate(0)
        self.FormFrame.config(height='200', width='200')
        self.FormFrame.place(anchor='center', height='20', relheight='0.9', relwidth='0.7', relx='0.5', rely='0.5', width='100', x='0', y='0')
        self.Guest_update_button['state']='disabled'

    def Check_guest(self):
        self.Acadamics_CB.deselect()
        self.Acadamics_CB.deselect()
        self.Acadamics_CB.deselect()
        self.Acadamics_CB.deselect()
        self.Guest_name=self.Guest_Name_entry.get()
        Phone_number=self.Guest_Phone_Entry.get()
        if(self.Guest_name and Phone_number):
            self.Phone_number=int(Phone_number)
            print(self.Guest_name,self.Phone_number)
            guest_visited_from_db=Queries.guest_visited_info_form_db(self.Guest_name,self.Phone_number)
            if(guest_visited_from_db==0):
                messagebox.showerror('Server Says','Guest Not Exsits')
            else:
                self.Guest_update_button['state']='active'
                self.guues_visited_from_db=guest_visited_from_db
                print(guest_visited_from_db)
                #retrive the visited info from database from guest table
                # guest_visited_from_db=['','Admission','placement','Finance']
                if(guest_visited_from_db[0]!='Acadamics'):
                    guest_visited_from_db[0]=self.Acadamics.get()
                else:
                    self.Acadamics_CB.select()
                if(guest_visited_from_db[1]!='Admission'):
                    guest_visited_from_db[1]=self.Admission.get()
                else:
                    self.Admission_CB.select()
                if(guest_visited_from_db[2]!='placement'):
                    guest_visited_from_db[2]=self.placement.get()
                else:
                    self.Placement_cb.select()
                if(guest_visited_from_db[3]!='Finance'):
                    guest_visited_from_db[3]=self.Finace.get()
                else:
                    self.Finance_cb.select()
        else:
            self.showerror('Enter Requeried Field')

    #update guest information
    def Update_guest(self):
        if(self.Guest_name and self.Phone_number):
            Guest_ID=Queries.getGuestIdandUpdateGuestInFO(self.Guest_name,self.Phone_number)
            #Updated values
            Guest=[]
            Guest.append(self.Guest_Name_entry.get())
            Guest.append(int(self.Guest_Phone_Entry.get()))
            Guest.append(Guest_ID)
            guest_visit_Update_db=[]
            guest_visit_Update_db.append(self.Acadamics.get())
            guest_visit_Update_db.append(self.Admission.get())
            guest_visit_Update_db.append(self.placement.get())
            guest_visit_Update_db.append(self.Finace.get())
            print(Guest,guest_visit_Update_db,self.guues_visited_from_db)
            Indicate=[]
            a=guest_visit_Update_db
            b=self.guues_visited_from_db
            if(a[0]==b[0]):
                Indicate.append(0)
            else:
                Indicate.append(1)
            if(a[1]==b[1]):
                Indicate.append(0)
            else:
                Indicate.append(1)
                
            if(a[2]==b[2]):
                Indicate.append(0)
            else:
                Indicate.append(1)
                
            if(a[3]==b[3]):
                Indicate.append(0)
            else:
                Indicate.append(1)
            print(Indicate)
            I=Indicate

            k=0
            for i in Indicate:
                if(i==0):
                    I[k]='No'
                if(i==1):
                    if(a[k]=='No'):
                        I[k]='Delete'
                    else:
                        I[k]='Insert'
                k=k+1
            print(I)
            #end of Updated values
            k=0
            for i in guest_visit_Update_db:
                if(i == 'No' or i==''):
                    k=k+1
            if(k != 4):
                #Update guest visited information
                # print(Guest)
                I.append(Guest_ID)
                Sucess=Queries.updateGuest(Guest)
                Sucess1=Queries.Guest_visited_up_proc(I)
                if(Sucess and Sucess1):
                    messagebox.showinfo('Server says','Guest updated Sucessfully')
                else:
                    messagebox.showerror('Server says','Error')
                print(Sucess)
                self.clear('Guest')
            else:
                self.showerror('Enter any section visited')
        else:
            self.showerror('Enter required field')
        self.Guest_update_button['state']='disabled'


        #end of guest functions

    def status_update(self):
        root.title('Home/HealthStatusUpdate')
        self.FormFrame = Frame(self.BodyFrame)
        self.Status_update_label_form = LabelFrame(self.FormFrame)
        self.Date_Label = Label(self.Status_update_label_form)
        self.Date_Label.config(text='Date')
        self.Date_Label.grid(padx='20', pady='2')
        self.Date_entry = DateEntry(self.Status_update_label_form)
        self.Date_entry.config(justify='center')
        self.Date_entry.delete('0', 'end')
        self.Date_entry.insert('0', Date)
        self.Date_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='0')
        self.Student_or_staff_id_label = Label(self.Status_update_label_form)
        self.Student_or_staff_id_label.config(text='Student/staff ID')
        self.Student_or_staff_id_label.grid(column='0', padx='20', pady='2', row='1')
        self.Add_to_DB_BUTTON = Button(self.Status_update_label_form)
        self.Add_to_DB_BUTTON.config(text='Add')
        self.Add_to_DB_BUTTON.grid(column='0', ipadx='35', padx='20', pady='10', row='12')
        self.Add_to_DB_BUTTON.configure(command=lambda:self.Insert_to_database('HealthStatusUpdate'))
        self.Clear_button = Button(self.Status_update_label_form)
        self.Clear_button.config(text='Clear')
        self.Clear_button.grid(column='1', ipadx='35', padx='20', pady='10', row='12')
        self.Clear_button.configure(command=lambda:self.clear('HealthStatusUpdate'))
        self.Student_or_staff_id_Entry = Entry(self.Status_update_label_form)
        self.Student_or_staff_id_Entry.config(justify='center')
        self.Student_or_staff_id_Entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='1')
        self.Health_status_update_button = Button(self.Status_update_label_form)
        self.Health_status_update_button.config(text='Check & Update')
        self.Health_status_update_button.grid(column='2', ipadx='35', padx='20', pady='10', row='12')
        self.Health_status_update_button.configure(command=self.Update_health_status)

        self.Health_status_check_button = Button(self.Status_update_label_form)
        self.Health_status_check_button.config(text='Check')
        self.Health_status_check_button.grid(column='3', ipadx='35', padx='20', pady='10', row='1')
        self.Health_status_check_button.configure(command=self.Check_health_status)

        self.BodyTemp_label = Label(self.Status_update_label_form)
        self.BodyTemp_label.config(text='Body Temp(F)')
        self.BodyTemp_label.grid(column='0', padx='20', pady='2', row='2')
        self.BodyTemp_Entery = Entry(self.Status_update_label_form)
        self.BodyTemp_Entery.config(justify='center')
        self.BodyTemp_Entery.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='2')
        self.symptoms_label = Label(self.Status_update_label_form)
        self.symptoms_label.config(text='Symptoms')
        self.symptoms_label.grid(column='0', padx='20', pady='8', row='3')
        self.symptoms_rad_Frame = Frame(self.Status_update_label_form)
        self.Yes_rad = Radiobutton(self.symptoms_rad_Frame)
        symptoms = StringVar('')
        self.symptoms=symptoms
        self.Yes_rad.config(text='Yes', value='Yes', variable=symptoms)
        self.Yes_rad.grid(padx='25', pady='8')
        self.No_rad = Radiobutton(self.symptoms_rad_Frame)
        self.No_rad.config(text='No', value='No', variable=symptoms)
        self.No_rad.grid(column='1', padx='25', pady='8', row='0')
        self.No_rad.select()
        self.symptoms_rad_Frame.config(height='200', width='200')
        self.symptoms_rad_Frame.grid(column='1', row='3')
        self.Status_update_label_form.config(height='400',text='Health status update', width='800')
        self.Status_update_label_form.pack(anchor='center', expand='true', fill='both', side='top')
        self.Status_update_label_form.pack_propagate(0)
        self.FormFrame.config(height='200', width='200')
        self.FormFrame.place(anchor='center', height='20', relheight='0.9', relwidth='0.7', relx='0.5', rely='0.5', width='100', x='0', y='0')
        self.Health_status_update_button['state']='disabled'


    def Check_health_status(self):
        date=self.Date_entry.get()
        student_or_staff_id=self.Student_or_staff_id_Entry.get()
        if(date and student_or_staff_id):
            Month=['','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
            date=self.Date_entry.get()
            date=date.split('/')
            Mon=int(date[0])
            dbdate=date[1]+'-'+Month[Mon]+'-'+date[2]
            print(dbdate)
            #using dbdate and student or staff id retrive already exsisting information query
            health_status_from_DB=Queries.getHealthDetailsfromDB(dbdate,student_or_staff_id)
            if(len(health_status_from_DB)==0):
                messagebox.showerror('Server Says','Data on this ID not exsits')
            else:
                # health_status_from_DB=['','',52.2,'True']
                self.BodyTemp_Entery.delete('0', 'end')
                self.BodyTemp_Entery.insert("0",str(health_status_from_DB[0]))
                if(health_status_from_DB[1]=='Yes'):
                    self.Yes_rad.select()
                else:
                    self.No_rad.select()
                self.Date_entry['state']='disabled'
                self.Student_or_staff_id_Entry['state']='disabled'
                self.Health_status_update_button['state']='active'
                
        else:
            self.showerror("Enter Required Fied")

    def Update_health_status(self):
        HealthStatusUpdate=[]
        date=self.Date_entry.get()
        student_or_staff_id=self.Student_or_staff_id_Entry.get()
        BodyTemp=self.BodyTemp_Entery.get()
        symptoms=self.symptoms.get()
        if(date and student_or_staff_id and BodyTemp and symptoms):
            Month=['','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
            date=self.Date_entry.get()
            date=date.split('/')
            Mon=int(date[0])
            dbdate=date[1]+'-'+Month[Mon]+'-'+date[2]
            HealthStatusUpdate.append(dbdate)
            HealthStatusUpdate.append(student_or_staff_id)
            HealthStatusUpdate.append(float(BodyTemp))
            HealthStatusUpdate.append(symptoms)
            Sucess=Queries.updateHealthInfo(HealthStatusUpdate)
            if(Sucess):
                HealthStatusUpdate[2]=((HealthStatusUpdate[2]-32)*5)/9
                Sucess=Queries.updateC(HealthStatusUpdate)
                if(Sucess):
                    messagebox.showinfo('Sever Says','Updation SucessFull')
                else:
                    messagebox.showinfo('Server says','Data entered not exsists')
            #insert the values into HealthStatusUpdate table
            print(HealthStatusUpdate)
            self.clear('HealthStatusUpdate')
        else:
            self.showerror("Enter Required Fied")
        self.Date_entry['state']='normal'
        self.Student_or_staff_id_Entry['state']='normal'
        self.Health_status_update_button['state']='disabled'
        
        



    def Report(self):
        self.SearchandManage()
        
        

    def Logout(self):
        self.owner=''
        self.MainLogin()
    
    #UI for studentinfo
    def student_Info(self):
        root.title('Home/New/Student')
        self.FormFrame = Frame(self.BodyFrame)
        self.Student_label_form = LabelFrame(self.FormFrame)
        self.Student_ID_Label = Label(self.Student_label_form)
        self.Student_ID_Label.config(text='Student ID*')
        self.Student_ID_Label.grid(padx='20', pady='2')
        self.Student_ID_entry = Entry(self.Student_label_form)
        self.Student_ID_entry.config(justify='center')
        self.Student_ID_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='0')
        self.student_name_label = Label(self.Student_label_form)
        self.student_name_label.config(text='Student FullName')
        self.student_name_label.grid(column='0', padx='20', pady='2', row='1')
        self.Student_name_entry = Entry(self.Student_label_form)
        self.Student_name_entry.config(justify='center')
        self.Student_name_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='1')
        self.student_branch_label = Label(self.Student_label_form)
        self.student_branch_label.config(text='Branch')
        self.student_branch_label.grid(column='0', padx='20', pady='2', row='2')

        self.Dept_rad_frame = Frame(self.Student_label_form)
        self.Dept_rad_frame.config(height='200', width='200')
        self.Dept_rad_frame.grid(column='1', row='2',padx='20',pady='2',ipadx='30',ipady='6')
        Dept = StringVar('')
        self.Branch=Dept
        self.IS_rad = Radiobutton(self.Dept_rad_frame)
        self.IS_rad.config(text='IS', value='1', variable=Dept)
        self.IS_rad.grid(column='1',row='2',padx='10',pady='2')
        self.CS_rad = Radiobutton(self.Dept_rad_frame)
        self.CS_rad.config(text='CS', value='2', variable=Dept)
        self.CS_rad.grid(column='2', row='2',padx='10',pady='2')
        self.ME_rad = Radiobutton(self.Dept_rad_frame)
        self.ME_rad.config(text='ME', value='3', variable=Dept)
        self.ME_rad.grid(column='3', row='2',padx='10',pady='2')
        self.CV_rad = Radiobutton(self.Dept_rad_frame)
        self.CV_rad.config(text='CV', value='4', variable=Dept)
        self.CV_rad.grid(column='4', row='2',padx='10',pady='2')
        self.EC_rad = Radiobutton(self.Dept_rad_frame)
        self.EC_rad.config(text='EC', value='5', variable=Dept)
        self.EC_rad.grid(column='5', row='2',padx='10',pady='2')
        self.IS_rad.select()

        # self.Student_Section_Label = Label(self.Student_label_form)
        # self.Student_Section_Label.config(text='Section')
        # self.Student_Section_Label.grid(column='0', padx='20', pady='2', row='3')
        # self.student_section_entry = Entry(self.Student_label_form)
        # self.student_section_entry.config(justify='center')
        # self.student_section_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='3')

        self.Student_phoneno_label = Label(self.Student_label_form)
        self.Student_phoneno_label.config(text='PhoneNumber')
        self.Student_phoneno_label.grid(column='0', padx='20', pady='2', row='4')
        self.student_phoneno_entry = Entry(self.Student_label_form)
        self.student_phoneno_entry.config(justify='center')
        self.student_phoneno_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='4')
        self.Student_adress_label = Label(self.Student_label_form)
        self.Student_adress_label.config(text='Adress')
        self.Student_adress_label.grid(column='0', padx='20', pady='2', row='5')
        self.student_adress_entry = Entry(self.Student_label_form)
        self.student_adress_entry.config(justify='center')
        self.student_adress_entry.grid(column='1', ipadx='40', ipady='20', padx='25', pady='2', row='5')
        self.Add_to_DB_BUTTON = Button(self.Student_label_form)
        self.Add_to_DB_BUTTON.config(text='Add')
        self.Add_to_DB_BUTTON.grid(column='0', ipadx='35', padx='20', pady='10', row='7')
        self.Add_to_DB_BUTTON.configure(command=lambda:self.Insert_to_database('student'))
        self.Clear_button = Button(self.Student_label_form)
        self.Clear_button.config(text='Clear')
        self.Clear_button.grid(column='1', ipadx='35', padx='20', pady='10', row='7')
        self.Clear_button.configure(command=lambda:self.clear('student'))
        self.Student_label_form.config(height='400', text='Student', width='800')
        self.Student_label_form.pack(expand='true', fill='both', side='top')
        self.Student_label_form.pack_propagate(0)
        self.FormFrame.config(height='200', width='200')
        self.FormFrame.place(anchor='center', height='20', relheight='0.9', relwidth='0.7', relx='0.5', rely='0.5', width='100', x='0', y='0')
    #end of student ui


    #UI FOR STAFF
    def satff_info(self):
        root.title('Home/New/Staff')
        self.FormFrame = Frame(self.BodyFrame)
        self.Staff_label_form = LabelFrame(self.FormFrame)
        self.Staff_ID_Label = Label(self.Staff_label_form)
        self.Staff_ID_Label.config(text='Staff ID')
        self.Staff_ID_Label.grid(padx='20', pady='2')
        self.Staff_ID_entry = Entry(self.Staff_label_form)
        self.Staff_ID_entry.config(justify='center')
        self.Staff_ID_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='0')
        self.staff_name_label = Label(self.Staff_label_form)
        self.staff_name_label.config(text='Staff FullName')
        self.staff_name_label.grid(column='0', padx='20', pady='2', row='1')
        self.Staff_name_entry = Entry(self.Staff_label_form)
        self.Staff_name_entry.config(justify='center')
        self.Staff_name_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='1')
        self.staff_dept_label = Label(self.Staff_label_form)
        self.staff_dept_label.config(text='Dept')
        self.staff_dept_label.grid(column='0', padx='20', pady='2', row='2')

        self.Dept_rad_frame = Frame(self.Staff_label_form)
        self.Dept_rad_frame.config(height='200', width='200')
        self.Dept_rad_frame.grid(column='1', row='2',padx='20',pady='2',ipadx='30',ipady='6')
        Dept = StringVar('')
        self.Dept=Dept
        self.IS_rad = Radiobutton(self.Dept_rad_frame)
        self.IS_rad.config(text='IS', value='1', variable=Dept)
        self.IS_rad.grid(column='1',row='2',padx='10',pady='2')
        self.CS_rad = Radiobutton(self.Dept_rad_frame)
        self.CS_rad.config(text='CS', value='2', variable=Dept)
        self.CS_rad.grid(column='2', row='2',padx='10',pady='2')
        self.ME_rad = Radiobutton(self.Dept_rad_frame)
        self.ME_rad.config(text='ME', value='3', variable=Dept)
        self.ME_rad.grid(column='3', row='2',padx='10',pady='2')
        self.CV_rad = Radiobutton(self.Dept_rad_frame)
        self.CV_rad.config(text='CV', value='4', variable=Dept)
        self.CV_rad.grid(column='4', row='2',padx='10',pady='2')
        self.EC_rad = Radiobutton(self.Dept_rad_frame)
        self.EC_rad.config(text='EC', value='5', variable=Dept)
        self.EC_rad.grid(column='5', row='2',padx='10',pady='2')


        self.Staff_Section_Label = Label(self.Staff_label_form)
        self.Staff_Section_Label.config(text='Section')
        self.Staff_Section_Label.grid(column='0', padx='20', pady='2', row='3')

        self.Section_rad_frame = Frame(self.Staff_label_form)
        self.Section_rad_frame.config(height='200', width='200')
        self.Section_rad_frame.grid(column='1', row='3',padx='20',pady='2',ipadx='30',ipady='6')
        Section = StringVar('')
        self.Section=Section
        self.Acadamics_rad = Radiobutton(self.Section_rad_frame)
        self.Acadamics_rad.config(text='Acadamics', value='1', variable=Section)
        self.Acadamics_rad.grid(column='1',row='2',padx='10',pady='2')
        self.Admission_rad = Radiobutton(self.Section_rad_frame)
        self.Admission_rad.config(text='Admission', value='2', variable=Section)
        self.Admission_rad.grid(column='2', row='2',padx='10',pady='2')
        self.Placement_rad = Radiobutton(self.Section_rad_frame)
        self.Placement_rad.config(text='Placement', value='3', variable=Section)
        self.Placement_rad.grid(column='3', row='2',padx='10',pady='2')
        self.Finace_rad = Radiobutton(self.Section_rad_frame)
        self.Finace_rad.config(text='Finace', value='4', variable=Section)
        self.Finace_rad.grid(column='4', row='2',padx='10',pady='2')
        self.Maintance_rad = Radiobutton(self.Section_rad_frame)
        self.Maintance_rad.config(text='Maintance', value='5', variable=Section)
        self.Maintance_rad.grid(column='5', row='2',padx='10',pady='2')

        self.Staff_phoneno_label = Label(self.Staff_label_form)
        self.Staff_phoneno_label.config(text='PhoneNumber')
        self.Staff_phoneno_label.grid(column='0', padx='20', pady='2', row='4')
        self.staff_phoneno_entry = Entry(self.Staff_label_form)
        self.staff_phoneno_entry.config(justify='center')
        self.staff_phoneno_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='4')
        self.Staff_adress_label = Label(self.Staff_label_form)
        self.Staff_adress_label.config(text='Adress')
        self.Staff_adress_label.grid(column='0', padx='20', pady='0', row='5')
        self.staff_adress_entry = Entry(self.Staff_label_form)
        self.staff_adress_entry.config(justify='center')
        self.staff_adress_entry.grid(column='1', ipadx='40', ipady='20', padx='25', pady='0', row='5')
        self.Add_to_DB_BUTTON = Button(self.Staff_label_form)
        self.Add_to_DB_BUTTON.config(text='Add')
        self.Add_to_DB_BUTTON.grid(column='0', ipadx='35', padx='20', pady='0', row='7')
        self.Add_to_DB_BUTTON.configure(command=lambda:self.Insert_to_database('staff'))
        self.Clear_button = Button(self.Staff_label_form)
        self.Clear_button.config(text='Clear')
        self.Clear_button.grid(column='1', ipadx='35', padx='20', pady='0', row='7')
        self.Clear_button.configure(command=lambda:self.clear('staff'))
        self.Staff_type_label = Label(self.Staff_label_form)
        self.Staff_type_label.config(text='Staff Type')
        self.Staff_type_label.grid(column='0', padx='20', pady='2', row='6')

        self.StaffType_rad_frame = Frame(self.Staff_label_form)
        self.StaffType_rad_frame.config(height='200', width='200')
        self.StaffType_rad_frame.grid(column='1', row='6',padx='20',pady='0',ipadx='30',ipady='6')
        self.Teaching_staff_label = Radiobutton(self.StaffType_rad_frame)
        stafftype = StringVar('')
        self.stafftype=stafftype
        self.Teaching_staff_label.config(text='Teaching',value='T', variable=stafftype)
        self.Teaching_staff_label.grid(column='1', ipadx='40', ipady='20', padx='25', pady='0', row='6')
        self.Non_Teaching_staff_label = Radiobutton(self.StaffType_rad_frame)
        self.Non_Teaching_staff_label.config(text='Non-Teaching', value='N', variable=stafftype)
        self.Non_Teaching_staff_label.grid(column='2', ipadx='40', ipady='20', padx='25', pady='0', row='6')

        self.Staff_label_form.config(height='400', text='Staff', width='800')
        self.Staff_label_form.pack(expand='true', fill='both', side='top')
        self.Staff_label_form.pack_propagate(0)
        self.FormFrame.config(height='200', width='200')
        self.FormFrame.place(anchor='center', height='20', relheight='0.9', relwidth='0.7', relx='0.5', rely='0.5', width='100', x='0', y='0')
        self.IS_rad.select()
        self.Admission_rad.select()
        self.Teaching_staff_label.select()
        
        #end of satff ui

    #function to fetch all the details from the form new->student and staff
    def Insert_to_database(self,value_of):
        #insert student info
        if(value_of=='student'):
            student=[]
            if(self.Student_ID_entry.get() and self.Student_name_entry.get() and self.Branch.get() and  self.student_phoneno_entry.get()):
                student.append(self.Student_ID_entry.get())
                student.append(self.Student_name_entry.get())
                student.append(int(self.Branch.get()))
                # student.append(self.student_section_entry.get())
                student.append(int(self.student_phoneno_entry.get()))
                student.append(self.student_adress_entry.get())
                #passing student info to Quires
                Sucess=Queries.InsertStudent(student)
                # print(student)
                if(Sucess):
                    messagebox.showinfo('Server Says','Added SucessFully')
                else:
                    messagebox.showerror('Server Says','Student Already Exsits')
                self.clear('student')
            else:
                self.showerror("Enter required field")
        #insert staff info    
        elif(value_of=='staff'):
            staff=[]
            Staff_ID=self.Staff_ID_entry.get()
            Staff_Name=self.Staff_name_entry.get()
            Staff_Dept=(self.Dept.get())
            Staff_Section=(self.Section.get())
            Staff_phone=(self.staff_phoneno_entry.get())
            Staff_adress=self.staff_adress_entry.get()
            Staff_type=self.stafftype.get()
            if(Staff_ID and Staff_Name and Staff_Dept and Staff_Section and Staff_phone and Staff_type):
                staff.append(Staff_ID)
                staff.append(Staff_Name)
                staff.append(int(Staff_Dept))
                staff.append(int(Staff_Section))
                staff.append(int(Staff_phone))
                staff.append(Staff_adress)
                staff.append(Staff_type)
                #INSERT STAFF VALUE TO DATABASE
                Sucess=Queries.InsertStaff(staff)
                if(Sucess):
                    messagebox.showinfo('Server Says',' Staff Added sucessfully')
                else:
                    messagebox.showerror('Server Says','Staff Already Exsits')
                self.clear('staff')
            else:
                self.showerror("Enter the reuired field")
        #insert guest info
        #function to fetch all info from guest ui and pass to database
        elif(value_of=='Guest'):
            Guest=[]
            guest_visited=[]
            Guest_name=self.Guest_Name_entry.get()
            Phone_number=self.Guest_Phone_Entry.get()
            guest_visited.append(self.Acadamics.get())
            guest_visited.append(self.Admission.get())
            guest_visited.append(self.placement.get())
            guest_visited.append(self.Finace.get())
            if(Guest_name and Phone_number):
                k=0
                for i in guest_visited:
                    if(i == 'No' or i==''):
                        k=k+1
                if(k != 4):
                    Guest.append(Guest_name)
                    Guest.append(int(Phone_number))
                    Guest.append(guest_visited)
                    #insert value to Guest table in database
                    #pass value to guest table
                    Sucess=Queries.InsertGuest([Guest[0],Guest[1]],Guest[2])
                    if(Sucess):
                        #pass value to guest_visited Table
                        guest_visited.append(Sucess)
                        Sucess=Queries.Guest_visited_insert_proc(guest_visited)
                        if(Sucess):
                            messagebox.showinfo('Server Says','Added SucessFully')
                        else:
                            messagebox.showerror('Server Says','Guest Already Exsits')
                    else:
                            messagebox.showerror('Server Says','Guest Already Exsit')
                    
                    self.clear('Guest')
                else:
                    self.showerror('Enter any section visited')
            else:
                self.showerror('Enter Requeried Field')

        elif(value_of=='HealthStatusUpdate'):
            Month=['','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
            HealthStatusUpdate=[]
            date=self.Date_entry.get()
            date=date.split('/')
            Mon=int(date[0])
            dbdate=date[1]+'-'+Month[Mon]+'-'+date[2]
            # print(dbdate)
            student_or_staff_id=self.Student_or_staff_id_Entry.get()
            BodyTemp=self.BodyTemp_Entery.get()
            symptoms=self.symptoms.get()
            if(date and student_or_staff_id and BodyTemp and symptoms):
                HealthStatusUpdate.append(dbdate)
                HealthStatusUpdate.append(student_or_staff_id)
                HealthStatusUpdate.append(float(BodyTemp))
                HealthStatusUpdate.append(symptoms)
                #insert the values into HealthStatusUpdate table
                print(HealthStatusUpdate)
                Sucess=Queries.InsertHealthStatusInfo(HealthStatusUpdate)
                if(Sucess==1):
                    messagebox.showinfo('Server Says','Added SucessFully')
                elif(Sucess==2):
                    pass
                else:
                    messagebox.showerror('Server Says','Health info Already Exsits')
                self.clear('HealthStatusUpdate')
            else:
                self.showerror("Enter Required Fied")
                

        
    def clear(self,value_of):
        #clear student field
        if(value_of=='student'):
            self.Student_ID_entry.delete("0",END)
            #self.student_section_entry.delete("0",END)
            self.Student_name_entry.delete("0",END)
            self.student_adress_entry.delete("0",END)
            self.student_phoneno_entry.delete("0",END)
            self.IS_rad.select()
        elif(value_of=='staff'):
            self.Staff_ID_entry.delete("0",END)
            self.staff_adress_entry.delete("0",END)
            self.Staff_name_entry.delete("0",END)
            self.staff_phoneno_entry.delete("0",END)
            self.IS_rad.select()
            self.Teaching_staff_label.select()
            self.Acadamics_rad.select()
        elif(value_of=='Guest'):
            self.Guest_Name_entry.delete("0",END)
            self.Guest_Phone_Entry.delete("0",END)
            self.Acadamics_CB.deselect()
            self.Admission_CB.deselect()
            self.Finance_cb.deselect()
            self.Placement_cb.deselect()
            self.Guest_update_button['state']='disabled'
        #clear status update page
        elif(value_of=='HealthStatusUpdate'):
            self.Date_entry.delete('0', 'end')
            self.Date_entry.insert('0', Date)
            self.Student_or_staff_id_Entry.delete('0',END)
            self.BodyTemp_Entery.delete("0",END)
            self.No_rad.select()

# root = Tk()
# root.title('Home')
# root.state("zoomed")
# widget = HomeNewStudentWidget(root)
# widget.pack(expand=True, fill='both')
# root.mainloop()

    def SearchandManage(self):
        root.title("Home/Search And Manage and get Report")
        self.MainHomeScreenToggel = Frame(self)
        self.SearchAndReporFrame = Frame(self.MainHomeScreenToggel)
        self.NavFrame = Frame(self.SearchAndReporFrame)
        self.SearchField_Entery = Entry(self.NavFrame)
        self.SearchField_Entery.grid(column='3', ipadx='30', padx='0', pady='10')
        self.SearchField_Entery.grid_propagate(0)
        self.SearchButton = Button(self.NavFrame)
        self.SearchButton.config(text='SearchID')
        self.SearchButton.grid(column='4', row='0')
        self.SearchButton.configure(command=self.Search)

        self.close = Button(self.NavFrame)
        self.close.config(text='close',background="red")
        self.close.grid(column='5', row='0')
        self.close.configure(command=self.close1)

        self.TableNameSelect = Combobox(self.NavFrame)
        self.TableNameSelect.config(values=("Student","Staff","HealthStatus","Guest"))
        self.TableNameSelect.grid(column='1', padx='10', row='0')
        self.ShowAllButton = Button(self.NavFrame)
        self.ShowAllButton.config(text='ShowAll')
        self.ShowAllButton.grid(column='2', padx='5', row='0')
        self.ShowAllButton.configure(command=self.ShowAll)

        # self.ShowGraph = Button(self.NavFrame)
        # self.ShowGraph.config(text='ShowGraph')
        # self.ShowGraph.grid(column='5', padx='5', row='0')
        # self.ShowGraph.configure(command=self.ShowGraphval)

        self.NavFrame.config(background='#000000', height='125', width='200')
        self.NavFrame.pack(anchor='n', expand='true', fill='x', ipady='0', side='bottom')
        self.NavFrame.pack_propagate(0)
        self.TitleFrame = Frame(self.SearchAndReporFrame)
        self.Title_Frame = Label(self.TitleFrame)
        self.Title_Frame.config(background='#808080',foreground='#ffff80', text='Search and Report and Manage',font=("times new roman",20,"bold"))
        self.Title_Frame.pack(expand='true', fill='both', side='top')
        self.TitleFrame.config(height='100', width='200')
        self.TitleFrame.pack(anchor='n', expand='false', fill='x', side='top')
        self.TitleFrame.pack_propagate(0)

        self.TableFrame = LabelFrame(self.SearchAndReporFrame)
        self.TableFrame.config(borderwidth='5', height='300', text='Student')
        self.TableFrame.config(width='200')
        self.TableFrame.place(anchor='nw', height='500', relwidth='1.0', rely='0.3', width='0', x='0', y='0')




        self.studentTableRender(
              '''
                    select * from student order by studentid
                    '''
        )

        self.SearchAndReporFrame.config(background='#c0c0c0', height='200', width='200')
        self.SearchAndReporFrame.pack(expand='true', fill='both', side='top')
        self.SearchAndReporFrame.pack_propagate(0)
        self.MainHomeScreenToggel.config(height='200', width='200')
        self.MainHomeScreenToggel.place(anchor='nw', relheight='1.0', relwidth='1.0', x='0', y='0')
    
    def ShowGraphval(self):
        Table=self.TableNameSelect.get()
        ID=self.SearchField_Entery.get()
        if(Table):
            if(Table=='Student'):
                Sucess=Queries.RunQueryWithValue(
                '''
                select studentfullname,bodytemp,dates from student,health_status where ids=:1 and student.studentid=health_status.ids
                ''',{
                    '1':ID
                })
                if(not Sucess):
                    messagebox.showerror('Server says','ID invalid')
                else:
                    Name=Sucess[0][0]
                    Date=[]
                    BodyTemp=[]
                    Xcor=[]
                    i=1
                    for row in Sucess:
                        t=row[2]
                        Xcor.append(i)
                        BodyTemp.append(float(row[1]))
                        Date.append(t.strftime('%d-%m-%Y'))
                        i=i+1
                    try:
                        Queries.graph(Name,BodyTemp,Date,Xcor)
                    except Exception as err:
                        print(err)
            
                print('in student health')
            elif(Table=='Staff'):
                Sucess=Queries.RunQueryWithValue(
                '''
                select stafffullname,bodytemp,dates from staff,health_status where ids=:1 and staff.staffid=health_status.ids
                ''',{
                    '1':ID
                })
                if(not Sucess):
                    messagebox.showerror('Server says','ID invalid')
                else:
                    Name=Sucess[0][0]
                    Date=[]
                    BodyTemp=[]
                    Xcor=[]
                    i=1
                    for row in Sucess:
                        t=row[2]
                        Xcor.append(i)
                        BodyTemp.append(float(row[1]))
                        Date.append(t.strftime('%d-%m-%Y'))
                        i=i+1
                    try:
                        Queries.graph(Name,BodyTemp,Date,Xcor)
                    except Exception as err:
                        print(err)
        else:
            messagebox.showinfo('Server says','Enter student/staff Table')



    def close1(self):
        root.title("Home")
        self.MainHomeScreenToggel = Frame(self)
        self.HomeFrame = Frame(self.MainHomeScreenToggel)
        self.HeaderFrame = Frame(self.HomeFrame)
        self.HeadingLabel = Label(self.HeaderFrame)
        self.HeadingLabel.config(background='#808080', foreground='#ffff80', height='5', text='Student-Staff healthcare Management system',font=("times new roman",20,"bold"))
        self.HeadingLabel.pack(anchor='center', expand='true', fill='x', side='top')
        #navigation bar frame
        self.NavFrame = Frame(self.HeaderFrame)
        #buttom to add new student and staff
        self.New_Student_Staff_Add_Button = Button(self.NavFrame)
        self.New_Student_Staff_Add_Button.config(height='10', text='New', width='15')
        self.New_Student_Staff_Add_Button.pack(anchor='center', padx='3', pady='2', side='left')
        self.New_Student_Staff_Add_Button.configure(command=self.New_student_staff_info)
        #button to add guest info
        self.button_2 = Button(self.NavFrame)
        self.button_2.config(height='10', text='Guest', width='15')
        self.button_2.pack(ipady='1', padx='3', pady='3', side='left')
        self.button_2.configure(command=self.Guest)
        #button to add student and staff health status
        self.student_staff_status_update = Button(self.NavFrame)
        self.student_staff_status_update.config(height='10', text='Status_Update', width='15')
        self.student_staff_status_update.pack(ipady='1', padx='3', pady='3', side='left')
        self.student_staff_status_update.configure(command=self.status_update)
        #button for report genration
        self.Report_Generation = Button(self.NavFrame)
        self.Report_Generation.config(height='10', text='Report', width='15')
        self.Report_Generation.pack(ipady='1', padx='3', pady='3', side='left')
        self.Report_Generation.configure(command=self.Report)
        #update student staff information in databse
        self.Update = Button(self.NavFrame)
        self.Update.config(height='10', text='Logout', width='15')
        self.Update.pack(ipady='1', padx='3', pady='3', side='left')
        self.Update.configure(command=self.Logout)
        #admin name with login date
        self.AdminNameLable = Label(self.NavFrame)
        self.AdminNameLable.config(text='Admin:'+self.owner+'\nDate:'+Date, width='50')
        self.AdminNameLable.pack(ipadx='70', ipady='5', padx='70', side='left')
        self.NavFrame.config(background='#000000', height='60', highlightcolor='#000000', width='200')
        self.NavFrame.pack(anchor='center', expand='true', fill='x', side='top')
        self.NavFrame.pack_propagate(0)
        self.HeaderFrame.config(background='#808080', height='230', width='200')
        self.HeaderFrame.pack(anchor='n', expand='true', fill='x', side='top')
        self.HeaderFrame.pack_propagate(0)
        self.BodyFrame = Frame(self.HomeFrame)
        self.innerNavFrame = Frame(self.BodyFrame)
        self.Student_Info_Button = Button(self.innerNavFrame)
        self.Student_Info_Button.config(borderwidth='4', justify='center', relief='raised', text='Student')
        self.Student_Info_Button.config(width='6')
        self.Student_Info_Button.grid(columnspan='2', ipady='20', padx='8', pady='10')
        self.Student_Info_Button.configure(command=self.student_Info)
        self.Staff_info_button = Button(self.innerNavFrame)
        self.Staff_info_button.config(borderwidth='4', justify='center', relief='raised', text='Staff')
        self.Staff_info_button.config(width='6')
        self.Staff_info_button.grid(column='0', columnspan='2', ipady='20', padx='8', pady='10', row='1')
        self.Staff_info_button.configure(command=self.satff_info)
        self.innerNavFrame.config(background='#808080', borderwidth='5', height='200', relief='ridge')
        self.innerNavFrame.config(takefocus=True, width='100')
        self.innerNavFrame.grid(ipady='90', padx='15', pady='13')
        self.innerNavFrame.grid_propagate(0)
        self.innerNavFrame.rowconfigure('0', pad='0')
        self.FormFrame = Frame(self.BodyFrame)
        self.Student_label_form = LabelFrame(self.FormFrame)
        self.Student_ID_Label = Label(self.Student_label_form)
        self.Student_ID_Label.config(text='Student ID*')
        self.Student_ID_Label.grid(padx='20', pady='2')
        self.Student_ID_entry = Entry(self.Student_label_form)
        self.Student_ID_entry.config(justify='center')
        self.Student_ID_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='0')
        self.student_name_label = Label(self.Student_label_form)
        self.student_name_label.config(text='Student FullName')
        self.student_name_label.grid(column='0', padx='20', pady='2', row='1')
        self.Student_name_entry = Entry(self.Student_label_form)
        self.Student_name_entry.config(justify='center')
        self.Student_name_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='1')
        self.student_branch_label = Label(self.Student_label_form)
        self.student_branch_label.config(text='Branch')
        self.student_branch_label.grid(column='0', padx='20', pady='2', row='2')

        self.Dept_rad_frame = Frame(self.Student_label_form)
        self.Dept_rad_frame.config(height='200', width='200')
        self.Dept_rad_frame.grid(column='1', row='2',padx='20',pady='2',ipadx='30',ipady='6')
        Dept = StringVar('')
        self.Branch=Dept
        self.IS_rad = Radiobutton(self.Dept_rad_frame)
        self.IS_rad.config(text='IS', value='1', variable=Dept)
        self.IS_rad.grid(column='1',row='2',padx='10',pady='2')
        self.IS_rad.deselect()
        self.CS_rad = Radiobutton(self.Dept_rad_frame)
        self.CS_rad.config(text='CS', value='2', variable=Dept)
        self.CS_rad.grid(column='2', row='2',padx='10',pady='2')
        self.CS_rad.deselect()
        self.ME_rad = Radiobutton(self.Dept_rad_frame)
        self.ME_rad.config(text='ME', value='3', variable=Dept)
        self.ME_rad.grid(column='3', row='2',padx='10',pady='2')
        self.ME_rad.deselect()
        self.CV_rad = Radiobutton(self.Dept_rad_frame)
        self.CV_rad.config(text='CV', value='4', variable=Dept)
        self.CV_rad.grid(column='4', row='2',padx='10',pady='2')
        self.CV_rad.deselect()
        self.EC_rad = Radiobutton(self.Dept_rad_frame)
        self.EC_rad.config(text='EC', value='5', variable=Dept)
        self.EC_rad.grid(column='5', row='2',padx='10',pady='2')
        self.EC_rad.deselect()
        self.IS_rad.select()


        # self.IS_rad.deselect()
        # self.CS_rad.deselect()
        # self.ME_rad.deselect()
        # self.CV_rad.deselect()
        # self.EC_rad.deselect()

        # self.Student_Section_Label = Label(self.Student_label_form)
        # self.Student_Section_Label.config(text='Section')
        # self.Student_Section_Label.grid(column='0', padx='20', pady='2', row='3')
        # self.student_section_entry = Entry(self.Student_label_form)
        # self.student_section_entry.config(justify='center')
        # self.student_section_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='3')

        self.Student_phoneno_label = Label(self.Student_label_form)
        self.Student_phoneno_label.config(text='PhoneNumber')
        self.Student_phoneno_label.grid(column='0', padx='20', pady='2', row='4')
        self.student_phoneno_entry = Entry(self.Student_label_form)
        self.student_phoneno_entry.config(justify='center')
        self.student_phoneno_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='4')
        self.Student_adress_label = Label(self.Student_label_form)
        self.Student_adress_label.config(text='Adress')
        self.Student_adress_label.grid(column='0', padx='20', pady='2', row='5')
        self.student_adress_entry = Entry(self.Student_label_form)
        self.student_adress_entry.config(justify='center')
        self.student_adress_entry.grid(column='1', ipadx='40', ipady='20', padx='25', pady='2', row='5')
        self.Add_to_DB_BUTTON = Button(self.Student_label_form)
        self.Add_to_DB_BUTTON.config(text='Add')
        self.Add_to_DB_BUTTON.grid(column='0', ipadx='35', padx='20', pady='10', row='7')
        self.Add_to_DB_BUTTON.configure(command=lambda:self.Insert_to_database('student'))
        self.Clear_button = Button(self.Student_label_form)
        self.Clear_button.config(text='Clear')
        self.Clear_button.grid(column='1', ipadx='35', padx='20', pady='10', row='7')
        self.Clear_button.configure(command=lambda:self.clear('student'))
        self.Student_label_form.config(height='400', text='Student', width='800')
        self.Student_label_form.pack(expand='true', fill='both', side='top')
        self.Student_label_form.pack_propagate(0)
        self.FormFrame.config(height='200', width='200')
        self.FormFrame.place(anchor='center', height='20', relheight='0.9', relwidth='0.7', relx='0.5', rely='0.5', width='100', x='0', y='0')
        self.BodyFrame.config(background='#c0c0c0', borderwidth='10', height='200', relief='ridge')
        self.BodyFrame.config(width='200')
        self.BodyFrame.place(anchor='center', relheight='0.6', relwidth='1', relx='0.5', rely='0.65', x='0', y='0')
        self.HomeFrame.config(height='200', width='200')
        self.HomeFrame.pack(anchor='center', expand='true', fill='both', side='top')
        self.HomeFrame.pack_propagate(0)
        self.MainHomeScreenToggel.config(height='200', width='200')
        self.MainHomeScreenToggel.place(anchor='nw', relheight='1.0', relwidth='1.0', x='0', y='0')
    
        
    
    #============student table functions==============
    def studentTableRender(self,Query,Values=0):#Query
        #creating scroll bar for table
        self.TableFrame = LabelFrame(self.SearchAndReporFrame)
        self.TableFrame.config(borderwidth='5', height='300', text='Student')
        self.TableFrame.config(width='200')
        self.TableFrame.place(anchor='nw', height='500', relwidth='1.0', rely='0.3', width='0', x='0', y='0')
        self.scorl_x=Scrollbar(self.TableFrame,orient='horizontal')
        self.scorl_y=Scrollbar(self.TableFrame,orient='vertical')

        #creating table tree 
        self.Student_Table = Treeview(self.TableFrame,columns=("student_id","student_name","Branch","phoneno","Adress"),xscrollcommand=self.scorl_x,yscrollcommand=self.scorl_y)
        self.scorl_x.pack(side='bottom',fill='x')
        self.scorl_y.pack(side='right',fill='y')
        self.scorl_x.config(command=self.Student_Table.xview)
        self.scorl_y.config(command=self.Student_Table.yview)
        self.Student_Table.heading('student_id',text="student_id")
        self.Student_Table.heading('student_name',text="student_name")
        self.Student_Table.heading('Branch',text="Branch")
        self.Student_Table.heading('phoneno',text="phone Number")
        self.Student_Table.heading('Adress',text="Adress")
        self.Student_Table['show']='headings'
        self.fetchStudentData(Query,Values)
        self.Student_Table.column('student_id',width=100)
        self.Student_Table.column('student_name',width=100)
        self.Student_Table.column('Branch',width=100)
        self.Student_Table.column('student_name',width=100)
        self.Student_Table.column('Adress',width=100)
        self.Student_Table.pack(fill='both',expand=1)
        self.Student_Table.bind("<ButtonRelease-1>",self.get_student_cursor)

    def fetchStudentData(self,Query,Values=0):
        # rows=[('1','Rajath M R','IS','962547898','bangalore'),('2','Rajath M R','IS','962547898','bangalore'),('2','Rajath M R','IS','962547898','bangalore'),('1','Rajath M R','IS','962547898','bangalore'),('2','Rajath M R','IS','962547898','bangalore'),('1','Rajath M R','IS','962547898','bangalore'),('2','Rajath M R','IS','962547898','bangalore'),('1','Rajath M R','IS','962547898','bangalore'),('2','Rajath M R','IS','962547898','bangalore'),('1','Rajath M R','IS','962547898','bangalore'),('2','Rajath M R','IS','962547898','bangalore'),('1','Rajath M R','IS','962547898','bangalore'),('2','Rajath M R','IS','962547898','bangalore'),('1','Rajath M R','IS','962547898','bangalore'),('2','Rajath M R','IS','962547898','bangalore'),('2','Rajath M R','IS','962547898','bangalore'),('1','Rajath M R','IS','962547898','bangalore'),('2','Rajath M R','IS','962547898','bangalore'),('1','Rajath M R','IS','962547898','bangalore'),('2','Rajath M R','IS','962547898','bangalore'),('1','Rajath M R','IS','962547898','bangalore'),('2','Rajath M R','IS','962547898','bangalore'),('1','Rajath M R','IS','962547898','bangalore'),('2','Rajath M R','IS','962547898','bangalore'),('1','Rajath M R','IS','962547898','bangalore'),('1','Rajath M R','IS','962547898','bangalore'),('2','Rajath M R','IS','962547898','bangalore'),('2','Rajath M R','IS','962547898','bangalore'),('1','Rajath M R','IS','962547898','bangalore'),('2','Rajath M R','IS','962547898','bangalore'),('1','Rajath M R','IS','962547898','bangalore'),('2','Rajath M R','IS','962547898','bangalore')]
        if(Values==0):
            rows=Queries.RunQueryWithNoValue(Query)
        else:
            rows=Queries.RunQueryWithValue(Query,Values)
        if (len(rows)!=0):
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('',END,values=row)
            # conn.commit()
        # conn.close()
        else:
            messagebox.showinfo('Server Says','No Data')
        #===============end of student table functions==================

    #====================staff table functions==================================
    def staffTableRender(self,Query,Values=0):#Query
        #creating scroll bar for table
        self.TableFrame = LabelFrame(self.SearchAndReporFrame)
        self.TableFrame.config(borderwidth='5', height='300', text='Staff')
        self.TableFrame.config(width='200')
        self.TableFrame.place(anchor='nw', height='500', relwidth='1.0', rely='0.3', width='0', x='0', y='0')
        self.scorl_x=Scrollbar(self.TableFrame,orient='horizontal')
        self.scorl_y=Scrollbar(self.TableFrame,orient='vertical')

        #creating table tree 
        self.Staff_Table = Treeview(self.TableFrame,columns=("staff_id","staff_name","Dept","Section","phonenumber","Adress","StaffType"),xscrollcommand=self.scorl_x,yscrollcommand=self.scorl_y)
        self.scorl_x.pack(side='bottom',fill='x')
        self.scorl_y.pack(side='right',fill='y')
        self.scorl_x.config(command=self.Staff_Table.xview)
        self.scorl_y.config(command=self.Staff_Table.yview)
        self.Staff_Table.heading('staff_id',text="staff_id")
        self.Staff_Table.heading('staff_name',text="staff_name")
        self.Staff_Table.heading('Dept',text="Departmwnt")
        self.Staff_Table.heading('Section',text="Section")
        self.Staff_Table.heading('phonenumber',text="phone Number")
        self.Staff_Table.heading('Adress',text="Adress")
        self.Staff_Table.heading('StaffType',text="StaffType")

        self.Staff_Table['show']='headings'
        self.fetchStaffData(Query,Values)
        self.Staff_Table.column('staff_id',width=100)
        self.Staff_Table.column('staff_name',width=100)
        self.Staff_Table.column('Dept',width=100)
        self.Staff_Table.column('Section',width=100)
        self.Staff_Table.column('phonenumber',width=100)
        self.Staff_Table.column('Adress',width=100)
        self.Staff_Table.column('StaffType',width=100)
        self.Staff_Table.pack(fill='both',expand=1)
        self.Staff_Table.bind("<ButtonRelease-1>",self.get_staff_cursor)


    def fetchStaffData(self,Query,Values=0):#Query
        if(Values==0):
            rows=Queries.RunQueryWithNoValue(Query)
        else:
            rows=Queries.RunQueryWithValue(Query,Values)
        # rows=[('1','Ganaraj k','IS','Acadamics','963564272','Mangalore','T')]
        if (len(rows)!=0):
            self.Staff_Table.delete(*self.Staff_Table.get_children())
            for row in rows:
                self.Staff_Table.insert('',END,values=row)
            # conn.commit()
        # conn.close()
        else:
            messagebox.showinfo('Server Says','No Data')
    #======================end of student table functions=========================================================



    #====================HealthStatus table functions==================================
    def HealthStatusjoinStudentTableRender(self,Query,Values=0):#Query
        #creating scroll bar for table
        self.TableFrame = LabelFrame(self.SearchAndReporFrame)
        self.TableFrame.config(borderwidth='5', height='300', text='Students HealthStatus')
        self.TableFrame.config(width='200')
        self.TableFrame.place(anchor='nw', height='500', relwidth='1.0', rely='0.3', width='0', x='0', y='0')
        self.scorl_x=Scrollbar(self.TableFrame,orient='horizontal')
        self.scorl_y=Scrollbar(self.TableFrame,orient='vertical')

        #creating table tree 
        self.HealthStatusjoinStudent_Table = Treeview(self.TableFrame,columns=("student_id","student_name","Branch","Date","BodyTemp","Symtomps","Celsius"),xscrollcommand=self.scorl_x,yscrollcommand=self.scorl_y)
        self.scorl_x.pack(side='bottom',fill='x')
        self.scorl_y.pack(side='right',fill='y')
        self.scorl_x.config(command=self.HealthStatusjoinStudent_Table.xview)
        self.scorl_y.config(command=self.HealthStatusjoinStudent_Table.yview)
        self.HealthStatusjoinStudent_Table.heading('student_id',text="student_id")
        self.HealthStatusjoinStudent_Table.heading('student_name',text="student_name")
        self.HealthStatusjoinStudent_Table.heading('Branch',text="Branch")
        self.HealthStatusjoinStudent_Table.heading('Date',text="Date")
        self.HealthStatusjoinStudent_Table.heading('BodyTemp',text="BodyTemprature")
        self.HealthStatusjoinStudent_Table.heading('Symtomps',text="Symtompsess")
        self.HealthStatusjoinStudent_Table.heading('Celsius',text="Celsius")


        self.HealthStatusjoinStudent_Table['show']='headings'
        self.fetchHealthStatusjoinStudentData(Query,Values)
        self.HealthStatusjoinStudent_Table.column('student_id',width=100)
        self.HealthStatusjoinStudent_Table.column('student_name',width=100)
        self.HealthStatusjoinStudent_Table.column('Branch',width=100)
        self.HealthStatusjoinStudent_Table.column('Date',width=100)
        self.HealthStatusjoinStudent_Table.column('BodyTemp',width=100)
        self.HealthStatusjoinStudent_Table.column('Symtomps',width=100)
        self.HealthStatusjoinStudent_Table.column('Celsius',width=100)
        self.HealthStatusjoinStudent_Table.pack(fill='both',expand=1)
        self.HealthStatusjoinStudent_Table.bind("<ButtonRelease-1>",self.get_HealthStatusjoinStudent_cursor)

    def fetchHealthStatusjoinStudentData(self,Query,Values=0):#Query
        if(Values==0):
            rows=Queries.RunQueryWithNoValue(Query)
        else:
            rows=Queries.RunQueryWithValue(Query,Values)
        # rows=[('1','Rajath M R','IS','2020-12-24','52.2','Yes')]
        if (len(rows)!=0):
            self.HealthStatusjoinStudent_Table.delete(*self.HealthStatusjoinStudent_Table.get_children())
            formatdate=[]
            for i in rows:
                k=list(i)
                m=k[3]
                Date=str(m.month)+'/'+str(m.day)+'/'+str(m.year)
                k[3]=Date
                formatdate.append(tuple(k))
            for row in formatdate:
                self.HealthStatusjoinStudent_Table.insert('',END,values=row)
            # conn.commit()
        # conn.close()
        else:
            messagebox.showinfo('Server Says','No Data')


    def HealthStatusjoinStaffTableRender(self,Query,Values=0):#Query
        #creating scroll bar for table
        self.TableFrame = LabelFrame(self.SearchAndReporFrame)
        self.TableFrame.config(borderwidth='5', height='300', text='Staffs HealthStatus')
        self.TableFrame.config(width='200')
        self.TableFrame.place(anchor='nw', height='500', relwidth='1.0', rely='0.3', width='0', x='0', y='0')
        self.scorl_x=Scrollbar(self.TableFrame,orient='horizontal')
        self.scorl_y=Scrollbar(self.TableFrame,orient='vertical')

        #creating table tree 
        self.HealthStatusjoinStaff_Table = Treeview(self.TableFrame,columns=("staff_id","staff_name","Dept","Section","StaffType","Date","BodyTemp","Symtomps","Celsius"),xscrollcommand=self.scorl_x,yscrollcommand=self.scorl_y)
        self.scorl_x.pack(side='bottom',fill='x')
        self.scorl_y.pack(side='right',fill='y')
        self.scorl_x.config(command=self.HealthStatusjoinStaff_Table.xview)
        self.scorl_y.config(command=self.HealthStatusjoinStaff_Table.yview)
        self.HealthStatusjoinStaff_Table.heading('staff_id',text="staff_id")
        self.HealthStatusjoinStaff_Table.heading('staff_name',text="staff_name")
        self.HealthStatusjoinStaff_Table.heading('Dept',text="Dept")
        self.HealthStatusjoinStaff_Table.heading('Section',text="Section")
        self.HealthStatusjoinStaff_Table.heading('StaffType',text="StaffType")
        self.HealthStatusjoinStaff_Table.heading('Date',text="Date")
        self.HealthStatusjoinStaff_Table.heading('BodyTemp',text="BodyTemprature")
        self.HealthStatusjoinStaff_Table.heading('Symtomps',text="Symtompsess")
        self.HealthStatusjoinStaff_Table.heading('Celsius',text="Celsius")


        self.HealthStatusjoinStaff_Table['show']='headings'
        self.fetchHealthStatusjoinStaffData(Query,Values)
        self.HealthStatusjoinStaff_Table.column('staff_id',width=100)
        self.HealthStatusjoinStaff_Table.column('staff_name',width=100)
        self.HealthStatusjoinStaff_Table.column('Dept',width=100)
        self.HealthStatusjoinStaff_Table.column('Section',width=100)
        self.HealthStatusjoinStaff_Table.column('StaffType',width=100)
        self.HealthStatusjoinStaff_Table.column('Date',width=100)
        self.HealthStatusjoinStaff_Table.column('BodyTemp',width=100)
        self.HealthStatusjoinStaff_Table.column('Symtomps',width=100)
        self.HealthStatusjoinStaff_Table.column('Celsius',width=100)
        self.HealthStatusjoinStaff_Table.pack(fill='both',expand=1)
        self.HealthStatusjoinStaff_Table.bind("<ButtonRelease-1>",self.get_HealthStatusjoinStaff_cursor)

    def fetchHealthStatusjoinStaffData(self,Query,Values=0):
        if(Values==0):
            rows=Queries.RunQueryWithNoValue(Query)
        else:
            rows=Queries.RunQueryWithValue(Query,Values)
        # rows=[('1','Ganaraj K','IS','Acadamics','T','2020-12-24','52.2','Yes')]
        if (len(rows)!=0):
            self.HealthStatusjoinStaff_Table.delete(*self.HealthStatusjoinStaff_Table.get_children())
            formatdate=[]
            for i in rows:
                k=list(i)
                m=k[5]
                Date=str(m.month)+'/'+str(m.day)+'/'+str(m.year)
                k[5]=Date
                formatdate.append(tuple(k))
            for row in formatdate:
                self.HealthStatusjoinStaff_Table.insert('',END,values=row)
            # conn.commit()
        # conn.close()
        else:
            messagebox.showinfo('Server Says','No Data')
    #======================end of HealthStatus table functions=========================================================


#=======================================Guest Table Render functions==================================================
    def GuestTableRender(self,Query,Values=0):#Query
        #creating scroll bar for table
        self.TableFrame = LabelFrame(self.SearchAndReporFrame)
        self.TableFrame.config(borderwidth='5', height='300', text='Guest')
        self.TableFrame.config(width='200')
        self.TableFrame.place(anchor='nw', height='500', relwidth='1.0', rely='0.3', width='0', x='0', y='0')
        self.scorl_x=Scrollbar(self.TableFrame,orient='horizontal')
        self.scorl_y=Scrollbar(self.TableFrame,orient='vertical')

        #creating table tree 
        self.Guest_Table = Treeview(self.TableFrame,columns=("guest_name","phonenumber","Visited"),xscrollcommand=self.scorl_x,yscrollcommand=self.scorl_y)
        self.scorl_x.pack(side='bottom',fill='x')
        self.scorl_y.pack(side='right',fill='y')
        self.scorl_x.config(command=self.Guest_Table.xview)
        self.scorl_y.config(command=self.Guest_Table.yview)
        self.Guest_Table.heading('guest_name',text="Guest Name")
        self.Guest_Table.heading('phonenumber',text="Phone Number")
        self.Guest_Table.heading('Visited',text="Visited")


        self.Guest_Table['show']='headings'
        self.fetchGuestData(Query,Values)
        self.Guest_Table.column('guest_name',width=100)
        self.Guest_Table.column('phonenumber',width=100)
        self.Guest_Table.column('Visited',width=100)
        self.Guest_Table.pack(fill='both',expand=1)
        self.Guest_Table.bind("<ButtonRelease-1>",self.get_Guest_cursor)

    def fetchGuestData(self,Query,Values=0):#Query
        if(Values==0):
            rows=Queries.RunQueryWithNoValue(Query)
        else:
            rows=Queries.RunQueryWithValue(Query,Values)
        # rows=[('Rajath M R','789456123','Acadamics'),('Rajath M R','789456123','Admission'),('Rajath M R','789456123','Placement')]
        if (len(rows)!=0):
            self.Guest_Table.delete(*self.Guest_Table.get_children())
            for row in rows:
                self.Guest_Table.insert('',END,values=row)
            # conn.commit()
        # conn.close()
        else:
            messagebox.showinfo('Server Says','No Data')







#=======================================end of Guest Table Render functions=============================================




    def Search(self):
        ID=self.SearchField_Entery.get()
        Table=self.TableNameSelect.get()
        try:
            self.FiltetrNavFrame.destroy()
        except Exception:
            print(Exception)
        if(ID and Table!='Guest'):
            #select from Table where id=ID
            if(Table=='Student'):
                #Query=select * from student where Student_ID=Id
                self.studentTableRender(
                                        '''
                    select studentid,studentfullname,branchname,phonenumber,adress
                    from student,branch
                    where student.branchid=branch.branchid and studentid=:1
                    order by studentid
                    ''',{
                        '1':ID
                    }
                )
                print(ID,Table)

            
            elif(Table=='Staff'):
                #Query= select * from Staff where Staff_id=Id
                self.staffTableRender(
                    '''
                    select staffid,stafffullname,branchname,sectionname,phonenumber,adress,stafftype
                    from branch,staff,section where branch.branchid=staff.deptid and staff.deptid=section.sectionid and staffid=:1
                    order by staffid
                    ''',{
                        '1':ID
                    }
                )
        else:
            messagebox.showerror('Server says','Select Table exept guest and ID')


    def ShowAll(self,Table=''):
        try:
            self.SearchButton['state']='disabled'
        except Exception:
            print(Exception)
        Table=self.TableNameSelect.get()
        self.Filter_()
        if(Table):
            #select from table Table with no condtion
            if(Table=='Student'):
                self.SearchButton['state']='active'
                # Query='select * from Student'
                self.studentTableRender(
                    '''
                    select studentid,studentfullname,branchname,phonenumber,adress
                    from student,branch
                    where student.branchid=branch.branchid
                    order by studentid
                    '''
                )
            elif(Table=='Staff'):
                self.SearchButton['state']='active'
                # Query='select * from Staff'
                self.staffTableRender(
                    '''
                    select staffid,stafffullname,branchname,sectionname,phonenumber,adress,stafftype
                    from branch,staff,section where branch.branchid=staff.deptid and staff.sectionid=section.sectionid
                    order by staffid
                    '''
                )
            elif(Table=='HealthStatus'):
                #Query='select student_id,Name,Branch,Date,ID,BodyTemp,Symtomps from student,HealthStatus where student_id=ID
                self.HealthStatusjoinStudentTableRender(
                    '''
select DISTINCT studentid,student.studentfullname,branch.branchname,health_status.dates,health_status.bodytemp,health_status.symtoms,in_cto_temperature.cel FROM
student,health_status,branch,in_cto_temperature where student.studentid=health_status.ids and branch.branchid=student.branchid and 
in_cto_temperature.ids=health_status.ids and in_cto_temperature.dates=health_status.dates
order by studentid

                    '''
                )
            elif(Table=='Guest'):
                #Query=select * from Guest,Guest_Visited where guest_id=GID
                self.GuestTableRender(
                    '''
                    select guestname,phonenumber,sectionname from guest,guest_visited,section
                    where guest.guestid=guest_visited.guestid and guest_visited.sectionid=section.sectionid
                    '''
                )
        else:
            messagebox.showerror('Server says','Select Table')

    def FilterStudent(self):
        BranchSelected=self.BranchWiseSearchcombo.get()
        if(BranchSelected):
            #search from table student where branch=branchselected and render the student table
            #Query=select * from student where branch=BranchSelected
            self.studentTableRender(
                    '''
                    select studentid,studentfullname,branchname,phonenumber,adress
                    from student,branch
                    where student.branchid=branch.branchid and branchname=:1
                    order by studentid
                    ''',
                    {
                        '1':BranchSelected
                    }
            )
        else:
            messagebox.showerror('Server says','Select Any branch')

    def FilterStaff(self):
        BranchSelected=self.BranchWiseSearchcombo.get()
        SectionSelected=self.Sectionwise.get()
        stafftypeSelected=self.StaffTypeCombo.get()
        if(BranchSelected or SectionSelected or stafftypeSelected):
            if(stafftypeSelected=='Teaching'):
                stafftypeSelected='T'
            elif(stafftypeSelected=='NonTeaching'):
                stafftypeSelected='N'
            print(BranchSelected,SectionSelected,stafftypeSelected)
            if(BranchSelected and SectionSelected=='' and stafftypeSelected==''):
                #select from table staff where branch=branchselected selected
                #Query=select * from staff where Branch=BranchSelected
                self.staffTableRender(
                    '''
                    select staffid,stafffullname,branchname,sectionname,phonenumber,adress,stafftype
                    from branch,staff,section where branch.branchid=staff.deptid and staff.sectionid=section.sectionid and branchname=:1
                    order by staffid
                    ''',{
                        '1':BranchSelected
                    }
                )

            elif(BranchSelected=='' and SectionSelected and stafftypeSelected==''):
                #select from table staff where section=SectionSelected selected
                #Query=select * from staff where Section=SectionSelected
                self.staffTableRender(
                    '''
                    select staffid,stafffullname,branchname,sectionname,phonenumber,adress,stafftype
                    from branch,staff,section where branch.branchid=staff.deptid and staff.sectionid=section.sectionid and sectionname=:1
                    order by staffid
                    ''',{
                        '1':SectionSelected
                    }
                )

            elif(BranchSelected=='' and SectionSelected=='' and stafftypeSelected):
                #select from table staff where stafftype=stafftypeSelected selected
                #Query=select * from staff where StaffType=stafftypeSelected
                self.staffTableRender(
                    '''
                    select staffid,stafffullname,branchname,sectionname,phonenumber,adress,stafftype
                    from branch,staff,section where branch.branchid=staff.deptid and staff.sectionid=section.sectionid and stafftype=:1
                    order by staffid
                    ''',{
                        '1':stafftypeSelected
                    }
                )
    
            elif(BranchSelected and SectionSelected and stafftypeSelected==''):
                #select from table staff where branch=branchselected and section=SectionSelected selected
                #Query=select * from staff where Branch=BranchSelected and Section=SectionSelected
                self.staffTableRender(
                    '''
                    select staffid,stafffullname,branchname,sectionname,phonenumber,adress,stafftype
                    from branch,staff,section where branch.branchid=staff.deptid and staff.sectionid=section.sectionid and branchname=:1 and sectionname=:2
                    order by staffid
                    ''',{
                        '1':BranchSelected,
                        '2':SectionSelected
                    }
                )

            
            elif(BranchSelected=='' and SectionSelected and stafftypeSelected):
                #select from table staff where section=SectionSelected and stafftype=stafftypeSelected selected
                #Query=select * from staff where StaffType=stafftypeSelected and Section=SectionSelected
                self.staffTableRender(
                                        '''
                    select staffid,stafffullname,branchname,sectionname,phonenumber,adress,stafftype
                    from branch,staff,section where branch.branchid=staff.deptid and staff.sectionid=section.sectionid and stafftype=:1 and sectionname=:2
                    order by staffid
                    ''',{
                        '1':stafftypeSelected,
                        '2':SectionSelected
                    }
                )


            elif(BranchSelected and SectionSelected=='' and stafftypeSelected):
                #select from table staff where branch=branchselected and stafftype=stafftypeSelected selected
                #Query=select * from staff where StaffType=stafftypeSelected and Branch=BranchSelected
                self.staffTableRender(
                                                          '''
                    select staffid,stafffullname,branchname,sectionname,phonenumber,adress,stafftype
                    from branch,staff,section where branch.branchid=staff.deptid and staff.sectionid=section.sectionid and branchname=:1 and stafftype=:2
                    order by staffid
                    ''',{
                        '1':BranchSelected,
                        '2':stafftypeSelected
                    }
                )
            

            elif(BranchSelected and SectionSelected and stafftypeSelected):
                #select using all variables from satff table
                #Query=select * from staff where StaffType=stafftypeSelected and Branch=BranchSelected and Section=SectionSelected
                self.staffTableRender(
                    '''
                    select staffid,stafffullname,branchname,sectionname,phonenumber,adress,stafftype
                    from branch,staff,section where branch.branchid=staff.deptid and staff.sectionid=section.sectionid and branchname=:1 and stafftype=:2 and sectionname=:3
                    order by staffid
                    ''',{
                        '1':BranchSelected,
                        '2':stafftypeSelected,
                        '3':SectionSelected
                    }
                )


        else:
            messagebox.showerror('Server says','Select Any one Field')

    def FilterHealthStatus(self):
        Table_to_join=self.Student_or_staff_Combo.get()
        Date=str(self.DateEntery.get())
        print(Date)
        ID=self.SearchField_Entery.get()
        if(Date):
            Month=['','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
            Date=Date.split('/')
            Mon=int(Date[0])
            dbdate=Date[1]+'-'+Month[Mon]+'-'+Date[2]
            print(dbdate)
        if(Table_to_join and Date=='' and ID==''):
            ##Query=select (clm) from HealthStatus H,Table_to_join D where D.ID=H.ID
            if(Table_to_join=='Student'):
                #Query=Select (clm) from Student,HealthStatus where Student_id=ID
                self.HealthStatusjoinStudentTableRender(
                                '''
select DISTINCT studentid,student.studentfullname,branch.branchname,health_status.dates,health_status.bodytemp,health_status.symtoms,in_cto_temperature.cel FROM
student,health_status,branch,in_cto_temperature where student.studentid=health_status.ids and branch.branchid=student.branchid and 
in_cto_temperature.ids=health_status.ids and in_cto_temperature.dates=health_status.dates
                    '''
                )
            elif(Table_to_join=='Staff'):
                #Query=Select (clm) from Student,HealthStatus where Staff_id=ID
                self.HealthStatusjoinStaffTableRender('''
select DISTINCT staffid,staff.stafffullname,branch.branchname,section.sectionname,
staff.stafftype,health_status.dates,health_status.bodytemp,health_status.symtoms,in_cto_temperature.cel
from staff,branch,section,health_status,in_cto_temperature
where staff.staffid=health_status.ids and staff.deptid=branch.branchid and staff.sectionid=section.sectionid
and health_status.ids=in_cto_temperature.ids and health_status.dates=in_cto_temperature.dates
''')

        elif(Table_to_join and Date and ID==''):
            #first join the table healthstatus and table_to_join then select based on Date
            #Query=select (clms) from HealthStatus,Table_to_join where Date=Date and staff_id=ID
            if(Table_to_join=='Student'):
                #Query=Select (clm) from Student,HealthStatus where Student_id=ID and Dtae=Date
                self.HealthStatusjoinStudentTableRender('''
select DISTINCT studentid,student.studentfullname,branch.branchname,health_status.dates,health_status.bodytemp,health_status.symtoms,in_cto_temperature.cel FROM
student,health_status,branch,in_cto_temperature where student.studentid=health_status.ids and branch.branchid=student.branchid and 
in_cto_temperature.ids=health_status.ids and in_cto_temperature.dates=health_status.dates and health_status.dates=:1''',{
                        '1':dbdate
                    })
            elif(Table_to_join=='Staff'):
                #Query=Select (clm) from Student,HealthStatus where Staff_id=ID and Dtae=Date
                self.HealthStatusjoinStaffTableRender('''
select DISTINCT staffid,staff.stafffullname,branch.branchname,section.sectionname,
staff.stafftype,health_status.dates,health_status.bodytemp,health_status.symtoms,in_cto_temperature.cel
from staff,branch,section,health_status,in_cto_temperature
where staff.staffid=health_status.ids and staff.deptid=branch.branchid and staff.sectionid=section.sectionid
and health_status.ids=in_cto_temperature.ids and health_status.dates=in_cto_temperature.dates and health_status.dates=:1
''',{
                        '1':dbdate
    }
                )
            print(Table_to_join,Date)

        elif(Table_to_join and Date=='' and ID):
            #first join the table healthstatus and table_to_join then select based on ID for all date
            #Query=select (clms) from HealthStatus,Table_to_join where ID=ID and Staff_id=ID
            if(Table_to_join=='Student'):
                #Query=Select (clm) from Student,HealthStatus where Student_id=ID and ID=ID
                self.HealthStatusjoinStudentTableRender('''
select DISTINCT studentid,student.studentfullname,branch.branchname,health_status.dates,health_status.bodytemp,health_status.symtoms,in_cto_temperature.cel FROM
student,health_status,branch,in_cto_temperature where student.studentid=health_status.ids and branch.branchid=student.branchid and 
in_cto_temperature.ids=health_status.ids and in_cto_temperature.dates=health_status.dates and health_status.ids=:1''',{
                        '1':ID
                    })
            elif(Table_to_join=='Staff'):
                #Query=Select (clm) from Student,HealthStatus where Staff_id=ID and ID=ID
                self.HealthStatusjoinStaffTableRender('''
select DISTINCT staffid,staff.stafffullname,branch.branchname,section.sectionname,
staff.stafftype,health_status.dates,health_status.bodytemp,health_status.symtoms,in_cto_temperature.cel
from staff,branch,section,health_status,in_cto_temperature
where staff.staffid=health_status.ids and staff.deptid=branch.branchid and staff.sectionid=section.sectionid
and health_status.ids=in_cto_temperature.ids and health_status.dates=in_cto_temperature.dates and health_status.ids=:1
''',{
                        '1':ID
    }
               
                )
            print(Table_to_join,ID)

        elif(Table_to_join and Date and ID):
            #first join the table healthstatus and table_to_join then select based on Date and ID
            #Query=select (clms) from HealthStatus,Table_to_join where ID=ID and Date=Date and staff_id=ID
            if(Table_to_join=='Student'):
                #Query=Select (clm) from Student,HealthStatus where Student_id=ID and ID=ID and Date=Date
                self.HealthStatusjoinStudentTableRender('''
select DISTINCT studentid,student.studentfullname,branch.branchname,health_status.dates,health_status.bodytemp,health_status.symtoms,in_cto_temperature.cel FROM
student,health_status,branch,in_cto_temperature where student.studentid=health_status.ids and branch.branchid=student.branchid and 
in_cto_temperature.ids=health_status.ids and in_cto_temperature.dates=health_status.dates and health_status.ids=:1 and health_status.dates=:2 ''',{
                        '1':ID,
                        '2':dbdate
                    }
                )
            elif(Table_to_join=='Staff'):
                #Query=Select (clm) from Student,HealthStatus where Staff_id=ID and ID=ID and Date=Date
                self.HealthStatusjoinStaffTableRender('''
select DISTINCT staffid,staff.stafffullname,branch.branchname,section.sectionname,
staff.stafftype,health_status.dates,health_status.bodytemp,health_status.symtoms,in_cto_temperature.cel
from staff,branch,section,health_status,in_cto_temperature
where staff.staffid=health_status.ids and staff.deptid=branch.branchid and staff.sectionid=section.sectionid
and health_status.ids=in_cto_temperature.ids and health_status.dates=in_cto_temperature.dates and health_status.ids=:1 and health_status.dates=:2
''',{
                        '1':ID,
                        '2':dbdate
    })
            print(Table_to_join,Date,ID)
            pass 
        else:
            messagebox.showerror('server says','Enter student/staff')

        

    def Filter_(self):
        Table=self.TableNameSelect.get()
        if(Table=='Student'):
            self.FiltetrNavFrame = Frame(self.SearchAndReporFrame)
            self.BranchWiseSearchcombo = Combobox(self.FiltetrNavFrame)
            self.BranchWiseSearchcombo.config(values=("IS","CS","ME","CV","EC"))
            self.BranchWiseSearchcombo.grid(column='1')
            self.BranchWiseLabel = Label(self.FiltetrNavFrame)
            self.BranchWiseLabel.config(text='BranchWiseSearch')
            self.BranchWiseLabel.grid(column='0', row='0')
            self.Filter = Button(self.FiltetrNavFrame)
            self.Filter.config(text='Search')
            self.Filter.grid(column='2', row='0')
            self.Filter.configure(command=self.FilterStudent)
            self.FiltetrNavFrame.config(background='#000000', height='200', width='200')
            self.FiltetrNavFrame.place(anchor='nw', relwidth='1.0', rely='0.2', x='0', y='0')
            self.ShowGraph = Button(self.FiltetrNavFrame)
            self.ShowGraph.config(text='ShowGraph')
            self.ShowGraph.grid(column='5', padx='5', row='0')
            self.ShowGraph.configure(command=self.ShowGraphval)
            try:
                self.SearchField_Entery['state']='active'
            except Exception:
                pass
        elif(Table=='Staff'):
            self.FiltetrNavFrame = Frame(self.SearchAndReporFrame)
            self.BranchWiseSearchcombo = Combobox(self.FiltetrNavFrame)
            self.BranchWiseSearchcombo.config(values=("IS","CS","ME","CV","EC"))
            self.BranchWiseSearchcombo.grid(column='1')
            self.BranchWiseLabel = Label(self.FiltetrNavFrame)
            self.BranchWiseLabel.config(text='BranchWiseSearch')
            self.BranchWiseLabel.grid(column='0', row='0')
            self.Filter = Button(self.FiltetrNavFrame)
            self.Filter.config(text='Search')
            self.Filter.grid(column='6', row='0')
            self.Filter.configure(command=self.FilterStaff)
            self.SectionwiseLabel = Label(self.FiltetrNavFrame)
            self.SectionwiseLabel.config(text='Sectionwise')
            self.SectionwiseLabel.grid(column='2', row='0')
            self.Sectionwise = Combobox(self.FiltetrNavFrame)
            self.Sectionwise.config(values=("Acadamics","Admission","placement","Finance","Maintance"))
            self.Sectionwise.grid(column='3', row='0')
            self.StaffTypeLabel = Label(self.FiltetrNavFrame)
            self.StaffTypeLabel.config(text='Staff Type')
            self.StaffTypeLabel.grid(column='4', row='0')
            self.StaffTypeCombo = Combobox(self.FiltetrNavFrame)
            self.StaffTypeCombo.config(values=("Teaching","NonTeaching"))
            self.StaffTypeCombo.grid(column='5', row='0')
            self.FiltetrNavFrame.config(background='#000000', height='200', width='200')
            self.FiltetrNavFrame.place(anchor='nw', relwidth='1.0', rely='0.2', x='0', y='0')
            self.ShowGraph = Button(self.FiltetrNavFrame)
            self.ShowGraph.config(text='ShowGraph')
            self.ShowGraph.grid(column='10', padx='5', row='0')
            self.ShowGraph.configure(command=self.ShowGraphval)
            try:
                self.SearchField_Entery['state']='normal'
            except Exception:
                pass
        elif(Table=='HealthStatus'):
            self.FiltetrNavFrame = Frame(self.SearchAndReporFrame)
            self.DateLabel = Label(self.FiltetrNavFrame)
            self.DateLabel.config(text='Date(YYYY-MM-DD)')
            self.DateLabel.grid(column='0', row='0')
            self.Filter = Button(self.FiltetrNavFrame)
            self.Filter.config(text='Search')
            self.Filter.grid(column='6', row='0')
            self.Filter.configure(command=self.FilterHealthStatus)
            self.Student_or_staff_Label = Label(self.FiltetrNavFrame)
            self.Student_or_staff_Label.config(text='Student/Staff')
            self.Student_or_staff_Label.grid(column='4', row='0')
            self.Student_or_staff_Combo = Combobox(self.FiltetrNavFrame)
            self.Student_or_staff_Combo.config(values=("Student","Staff"))
            self.Student_or_staff_Combo.grid(column='5', row='0')
            self.DateEntery = DateEntry(self.FiltetrNavFrame)
            self.DateEntery.delete('0', 'end')
            self.DateEntery.insert("0",Date)
            self.DateEntery.config(justify='center')
            self.DateEntery.grid(column='1', row='0')
            self.FiltetrNavFrame.config(background='#000000',height='200', width='200')
            self.FiltetrNavFrame.place(anchor='nw', relwidth='1.0', rely='0.2', x='0', y='0')
            try:
                self.SearchField_Entery['state']='normal'
            except Exception:
                pass
        elif(Table=='Guest'):
            self.FiltetrNavFrame = Frame(self.SearchAndReporFrame)
            self.FiltetrNavFrame.config(background='#c0c0c0',height='200', width='200')
            self.FiltetrNavFrame.place(anchor='nw', relwidth='1.0', rely='0.2', x='0', y='0')
            try:
                self.SearchButton['state']='disabled'
                self.SearchField_Entery['state']='disabled'
            except Exception:
                pass


#=====================================Managing DataBase Update/Delete operation==================================
        #=============================Managing Student Database=================================
    #UI for Student
    def popUpStudent(self):
        self.FormFrame = Frame(self.SearchAndReporFrame)
        self.Student_label_form = LabelFrame(self.FormFrame)
        self.Student_ID_Label = Label(self.Student_label_form)
        self.Student_ID_Label.config(text='Student ID*')
        self.Student_ID_Label.grid(padx='20', pady='2')
        self.Student_ID_entry1 = Entry(self.Student_label_form)
        self.Student_ID_entry1.config(justify='center')
        self.Student_ID_entry1.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='0')
        self.student_name_label = Label(self.Student_label_form)
        self.student_name_label.config(text='Student FullName')
        self.student_name_label.grid(column='0', padx='20', pady='2', row='1')
        self.Student_name_entry1 = Entry(self.Student_label_form)
        self.Student_name_entry1.config(justify='center')
        self.Student_name_entry1.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='1')
        self.student_branch_label = Label(self.Student_label_form)
        self.student_branch_label.config(text='Branch')
        self.student_branch_label.grid(column='0', padx='20', pady='2', row='2')

        self.Dept_rad_frame = Frame(self.Student_label_form)
        self.Dept_rad_frame.config(height='200', width='200')
        self.Dept_rad_frame.grid(column='1', row='2',padx='20',pady='2',ipadx='30',ipady='6')
        Dept = StringVar('')
        self.Branchh=Dept
        self.IS_rad = Radiobutton(self.Dept_rad_frame)
        self.IS_rad.config(text='IS', value='1', variable=Dept)
        self.IS_rad.grid(column='1',row='2',padx='10',pady='2')
        self.CS_rad = Radiobutton(self.Dept_rad_frame)
        self.CS_rad.config(text='CS', value='2', variable=Dept)
        self.CS_rad.grid(column='2', row='2',padx='10',pady='2')
        self.ME_rad = Radiobutton(self.Dept_rad_frame)
        self.ME_rad.config(text='ME', value='3', variable=Dept)
        self.ME_rad.grid(column='3', row='2',padx='10',pady='2')
        self.CV_rad = Radiobutton(self.Dept_rad_frame)
        self.CV_rad.config(text='CV', value='4', variable=Dept)
        self.CV_rad.grid(column='4', row='2',padx='10',pady='2')
        self.EC_rad = Radiobutton(self.Dept_rad_frame)
        self.EC_rad.config(text='EC', value='5', variable=Dept)
        self.EC_rad.grid(column='5', row='2',padx='10',pady='2')
        self.IS_rad.select()

    # self.Student_Section_Label = Label(self.Student_label_form)
    # self.Student_Section_Label.config(text='Section')
    # self.Student_Section_Label.grid(column='0', padx='20', pady='2', row='3')
    # self.student_section_entry = Entry(self.Student_label_form)
    # self.student_section_entry.config(justify='center')
    # self.student_section_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='3')

        self.Student_phoneno_label = Label(self.Student_label_form)
        self.Student_phoneno_label.config(text='PhoneNumber')
        self.Student_phoneno_label.grid(column='0', padx='20', pady='2', row='4')
        self.student_phoneno_entry1 = Entry(self.Student_label_form)
        self.student_phoneno_entry1.config(justify='center')
        self.student_phoneno_entry1.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='4')
        self.Student_adress_label = Label(self.Student_label_form)
        self.Student_adress_label.config(text='Adress')
        self.Student_adress_label.grid(column='0', padx='20', pady='2', row='5')
        self.student_adress_entry1 = Entry(self.Student_label_form)
        self.student_adress_entry1.config(justify='center')
        self.student_adress_entry1.grid(column='1', ipadx='40', ipady='20', padx='25', pady='2', row='5')

        self.ButtonFrame = Frame(self.Student_label_form)
        self.ButtonFrame.config(height='200', width='200')
        self.ButtonFrame.grid(column='0', columnspan='5', padx='2', pady='2', row='6')

        self.Update_to_DB_BUTTON = Button(self.ButtonFrame)
        self.Update_to_DB_BUTTON.config(text='Update')
        self.Update_to_DB_BUTTON.grid(column='0', ipadx='35', padx='10', pady='10', row='0')
        self.Update_to_DB_BUTTON.configure(command=lambda:self.UpdateRow('Student'))

        self.Delete_button = Button(self.ButtonFrame)
        self.Delete_button.config(text='Delete')
        self.Delete_button.grid(column='1', ipadx='35', padx='10', pady='10', row='0')
        self.Delete_button.configure(command=lambda:self.DeleteRow('Student'))

        # self.Clear_button = Button(self.ButtonFrame)
        # self.Clear_button.config(text='Clear')
        # self.Clear_button.grid(column='2', ipadx='35', padx='10', pady='10', row='0')
        # self.Clear_button.configure(command=lambda:self.clear('student'))

        self.Close_button = Button(self.ButtonFrame)
        self.Close_button.config(text='Close')
        self.Close_button.grid(column='3', ipadx='35', padx='10', pady='10', row='0')
        self.Close_button.configure(command=lambda:self.close24('Student'))

        self.Student_label_form.config(height='400', text='Student', width='800')
        self.Student_label_form.pack(expand='true', fill='both', side='top')
        self.Student_label_form.pack_propagate(0)
        self.FormFrame.config(height='200', width='200')
        self.FormFrame.place(anchor='center', height='20', relheight='0.4', relwidth='0.4', relx='0.5', rely='0.5', width='100', x='0', y='0')
    #end of student ui


    def get_student_cursor(self,evn):
        Cursor_row=self.Student_Table.focus()
        Content=self.Student_Table.item(Cursor_row)
        row=Content['values']
        if(len(row)!=0):
            self.popUpStudent()
            self.Student_ID_entry1.insert("0",row[0])
            self.Student_name_entry1.insert("0",row[1])
            if(row[2]=='IS'):
                self.IS_rad.select()
            elif(row[2]=='CS'):
                self.CS_rad.select()
            elif(row[2]=='ME'):
                self.ME_rad.select()
            elif(row[2]=='CV'):
                self.CV_rad.select()
            elif(row[2]=='EC'):
                self.EC_rad.select()
            self.student_phoneno_entry1.insert("0",row[3])
            self.student_adress_entry1.insert("0",row[4])
        print(row)


#======================================end of Managing Student Database=================================

#=========================================Managing Staff DataBase==============================================
 #Staff Ui
    def popUpStaff(self):
        self.FormFrame = Frame(self.SearchAndReporFrame)
        self.Staff_label_form = LabelFrame(self.FormFrame)
        self.Staff_ID_Label = Label(self.Staff_label_form)
        self.Staff_ID_Label.config(text='Staff ID')
        self.Staff_ID_Label.grid(padx='20', pady='2')
        self.Staff_ID_entry = Entry(self.Staff_label_form)
        self.Staff_ID_entry.config(justify='center')
        self.Staff_ID_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='0')
        self.staff_name_label = Label(self.Staff_label_form)
        self.staff_name_label.config(text='Staff FullName')
        self.staff_name_label.grid(column='0', padx='20', pady='2', row='1')
        self.Staff_name_entry = Entry(self.Staff_label_form)
        self.Staff_name_entry.config(justify='center')
        self.Staff_name_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='1')
        self.staff_dept_label = Label(self.Staff_label_form)
        self.staff_dept_label.config(text='Dept')
        self.staff_dept_label.grid(column='0', padx='20', pady='2', row='2')

        self.Dept_rad_frame = Frame(self.Staff_label_form)
        self.Dept_rad_frame.config(height='200', width='200')
        self.Dept_rad_frame.grid(column='1', row='2',padx='20',pady='2',ipadx='30',ipady='6')
        Dept = StringVar('')
        self.Dept=Dept
        self.IS_rad = Radiobutton(self.Dept_rad_frame)
        self.IS_rad.config(text='IS', value='1', variable=Dept)
        self.IS_rad.grid(column='1',row='2',padx='10',pady='2')
        self.CS_rad = Radiobutton(self.Dept_rad_frame)
        self.CS_rad.config(text='CS', value='2', variable=Dept)
        self.CS_rad.grid(column='2', row='2',padx='10',pady='2')
        self.ME_rad = Radiobutton(self.Dept_rad_frame)
        self.ME_rad.config(text='ME', value='3', variable=Dept)
        self.ME_rad.grid(column='3', row='2',padx='10',pady='2')
        self.CV_rad = Radiobutton(self.Dept_rad_frame)
        self.CV_rad.config(text='CV', value='4', variable=Dept)
        self.CV_rad.grid(column='4', row='2',padx='10',pady='2')
        self.EC_rad = Radiobutton(self.Dept_rad_frame)
        self.EC_rad.config(text='EC', value='5', variable=Dept)
        self.EC_rad.grid(column='5', row='2',padx='10',pady='2')


        self.Staff_Section_Label = Label(self.Staff_label_form)
        self.Staff_Section_Label.config(text='Section')
        self.Staff_Section_Label.grid(column='0', padx='20', pady='2', row='3')

        self.Section_rad_frame = Frame(self.Staff_label_form)
        self.Section_rad_frame.config(height='200', width='200')
        self.Section_rad_frame.grid(column='1', row='3',padx='20',pady='2',ipadx='30',ipady='6')
        Section = StringVar('')
        self.Section=Section
        self.Acadamics_rad = Radiobutton(self.Section_rad_frame)
        self.Acadamics_rad.config(text='Acadamics', value='1', variable=Section)
        self.Acadamics_rad.grid(column='1',row='2',padx='10',pady='2')
        self.Admission_rad = Radiobutton(self.Section_rad_frame)
        self.Admission_rad.config(text='Admission', value='2', variable=Section)
        self.Admission_rad.grid(column='2', row='2',padx='10',pady='2')
        self.Placement_rad = Radiobutton(self.Section_rad_frame)
        self.Placement_rad.config(text='Placement', value='3', variable=Section)
        self.Placement_rad.grid(column='3', row='2',padx='10',pady='2')
        self.Finace_rad = Radiobutton(self.Section_rad_frame)
        self.Finace_rad.config(text='Finace', value='4', variable=Section)
        self.Finace_rad.grid(column='4', row='2',padx='10',pady='2')
        self.Maintance_rad = Radiobutton(self.Section_rad_frame)
        self.Maintance_rad.config(text='Maintance', value='5', variable=Section)
        self.Maintance_rad.grid(column='5', row='2',padx='10',pady='2')

        self.Staff_phoneno_label = Label(self.Staff_label_form)
        self.Staff_phoneno_label.config(text='PhoneNumber')
        self.Staff_phoneno_label.grid(column='0', padx='20', pady='2', row='4')
        self.staff_phoneno_entry = Entry(self.Staff_label_form)
        self.staff_phoneno_entry.config(justify='center')
        self.staff_phoneno_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='4')
        self.Staff_adress_label = Label(self.Staff_label_form)
        self.Staff_adress_label.config(text='Adress')
        self.Staff_adress_label.grid(column='0', padx='20', pady='2', row='5')
        self.staff_adress_entry = Entry(self.Staff_label_form)
        self.staff_adress_entry.config(justify='center')
        self.staff_adress_entry.grid(column='1', ipadx='40', ipady='20', padx='25', pady='2', row='5')


        self.ButtonFrame = Frame(self.Staff_label_form)
        self.ButtonFrame.config(height='200', width='200')
        self.ButtonFrame.grid(column='0', columnspan='5', padx='2', pady='2', row='8')

        self.Update_to_DB_BUTTON = Button(self.ButtonFrame)
        self.Update_to_DB_BUTTON.config(text='Update')
        self.Update_to_DB_BUTTON.grid(column='0', ipadx='35', padx='10', pady='10', row='0')
        self.Update_to_DB_BUTTON.configure(command=lambda:self.UpdateRow('Staff'))

        self.Delete_button = Button(self.ButtonFrame)
        self.Delete_button.config(text='Delete')
        self.Delete_button.grid(column='1', ipadx='35', padx='10', pady='10', row='0')
        self.Delete_button.configure(command=lambda:self.DeleteRow('Staff'))

        # self.Clear_button = Button(self.ButtonFrame)
        # self.Clear_button.config(text='Clear')
        # self.Clear_button.grid(column='2', ipadx='35', padx='10', pady='10', row='0')
        # self.Clear_button.configure(command=lambda:self.clear('Staff'))

        self.Close_button = Button(self.ButtonFrame)
        self.Close_button.config(text='Close')
        self.Close_button.grid(column='3', ipadx='35', padx='10', pady='10', row='0')
        self.Close_button.configure(command=lambda:self.close24('Staff'))


        self.Staff_type_label = Label(self.Staff_label_form)
        self.Staff_type_label.config(text='Staff Type')
        self.Staff_type_label.grid(column='0', padx='20', pady='2', row='6')

        self.StaffType_rad_frame = Frame(self.Staff_label_form)
        self.StaffType_rad_frame.config(height='200', width='200')
        self.StaffType_rad_frame.grid(column='1', row='6',padx='20',pady='2',ipadx='30',ipady='6')
        self.Teaching_staff_label = Radiobutton(self.StaffType_rad_frame)
        stafftype = StringVar('')
        self.stafftype=stafftype
        self.Teaching_staff_label.config(text='Teaching',value='T', variable=stafftype)
        self.Teaching_staff_label.grid(column='1', ipadx='40', ipady='20', padx='25', pady='2', row='6')
        self.Non_Teaching_staff_label = Radiobutton(self.StaffType_rad_frame)
        self.Non_Teaching_staff_label.config(text='Non-Teaching', value='N', variable=stafftype)
        self.Non_Teaching_staff_label.grid(column='2', ipadx='40', ipady='20', padx='25', pady='2', row='6')

        self.Staff_label_form.config(height='400', text='Staff', width='800')
        self.Staff_label_form.pack(expand='true', fill='both', side='top')
        self.Staff_label_form.pack_propagate(0)
        self.FormFrame.config(height='200', width='200')
        self.FormFrame.place(anchor='center', height='20',relheight='0.55', relwidth='0.5', relx='0.5', rely='0.4', width='100', x='0', y='0')
        self.CS_rad.select()
        self.Admission_rad.select()
        self.Teaching_staff_label.select()
 #end of Staff Ui

    def get_staff_cursor(self,evn):
        Cursor_row=self.Staff_Table.focus()
        Content=self.Staff_Table.item(Cursor_row)
        row=Content['values']
        if(len(row)!=0):
            self.popUpStaff()
            self.Staff_ID_entry.insert("0",row[0])
            self.Staff_name_entry.insert("0",row[1])
            if(row[2]=='IS'):
                self.IS_rad.select()
            elif(row[2]=='CS'):
                self.CS_rad.select()
            elif(row[2]=='ME'):
                self.ME_rad.select()
            elif(row[2]=='CV'):
                self.CV_rad.select()
            elif(row[2]=='EC'):
                self.EC_rad.select()
            
            if(row[3]=='Acadamics'):
                self.Acadamics_rad.select()
            elif(row[3]=='Admission'):
                self.Admission_rad.select()
            elif(row[3]=='Placement'):
                self.Placement_rad.select()
            elif(row[3]=='Finance'):
                self.Finace_rad.select()
            elif(row[3]=='Maintance'):
                self.Maintance_rad.select()
            
            self.staff_phoneno_entry.insert("0",row[4])
            self.staff_adress_entry.insert("0",row[5])

            if(row[6]=='T'):
                self.Teaching_staff_label.select()
            elif(row[6]=='N'):
                self.Non_Teaching_staff_label.select()

        print(row)
#=========================================end of Managing Staff DataBase========================================


#=============================================Managing Guest DataBase============================================
#UI for Guest
    def popUpGuest(self):
        self.FormFrame = Frame(self.SearchAndReporFrame)
        self.Guest_label_form = LabelFrame(self.FormFrame)
        self.Guest_Name_Label = Label(self.Guest_label_form)
        self.Guest_Name_Label.config(text='Guest Full Name')
        self.Guest_Name_Label.grid(padx='20', pady='2')
        self.Guest_Name_entry = Entry(self.Guest_label_form)
        self.Guest_Name_entry.config(justify='center')
        self.Guest_Name_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='0')
        self.Guest_Phone_label = Label(self.Guest_label_form)
        self.Guest_Phone_label.config(text='Phone Number*')
        self.Guest_Phone_label.grid(column='0', padx='20', pady='2', row='1')
        self.Guest_Phone_Entry = Entry(self.Guest_label_form)
        self.Guest_Phone_Entry.config(justify='center')
        self.Guest_Phone_Entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='1')
        self.Visited_label = Label(self.Guest_label_form)
        self.Visited_label.config(borderwidth='3', justify='center', relief='groove', text='Are You sure?Want to delete?')
        self.Visited_label.config(width='75')
        self.Visited_label.grid(column='0', columnspan='5', padx='20', pady='5', row='2')

        self.ButtonFrame = Frame(self.Guest_label_form)
        self.ButtonFrame.config(height='200', width='200')
        self.ButtonFrame.grid(column='0', columnspan='5', padx='2', pady='2', row='10')

        # self.Update_to_DB_BUTTON = Button(self.ButtonFrame)
        # self.Update_to_DB_BUTTON.config(text='Update')
        # self.Update_to_DB_BUTTON.grid(column='0', ipadx='35', padx='10', pady='10', row='0')
        # self.Update_to_DB_BUTTON.configure(command=lambda:self.UpdateRow('Guest'))

        self.Delete_button = Button(self.ButtonFrame)
        self.Delete_button.config(text='Delete')
        self.Delete_button.grid(column='1', ipadx='35', padx='10', pady='10', row='0')
        self.Delete_button.configure(command=lambda:self.DeleteRow('Guest'))

        # self.Clear_button = Button(self.ButtonFrame)
        # self.Clear_button.config(text='Clear')
        # self.Clear_button.grid(column='2', ipadx='35', padx='10', pady='10', row='0')
        # self.Clear_button.configure(command=lambda:self.clear('Guest'))

        self.Close_button = Button(self.ButtonFrame)
        self.Close_button.config(text='Close')
        self.Close_button.grid(column='3', ipadx='35', padx='10', pady='10', row='0')
        self.Close_button.configure(command=lambda:self.close24('Guest'))


        self.Guest_label_form.config(height='400',text='Guest', width='800')
        self.Guest_label_form.pack(anchor='center', expand='true', fill='both', side='top')
        self.Guest_label_form.pack_propagate(0)
        self.FormFrame.config(height='200', width='200')
        self.FormFrame.place(anchor='center', height='20', relheight='0.4', relwidth='0.4', relx='0.5', rely='0.5', width='100', x='0', y='0')
#End of Guest UI
    def get_Guest_cursor(self,evn):
        Cursor_row=self.Guest_Table.focus()
        Content=self.Guest_Table.item(Cursor_row)
        row=Content['values']
        if(len(row)!=0):
            self.popUpGuest()
            self.Guest_Name_entry.insert("0",row[0])
            self.Guest_Phone_Entry.insert("0",row[1])
            #select Visited from Guest,Guest_Visited where GuestPhone=row[1]
            #render_cb=[]
            #for i in rows:
                #for row in rows:
                    #render_cb.append(row)
            #for cb in render_cb:
                #if(cb=='Acadamics):
                    #self.Acadamics_rad.select()
                    #same for all


#============================================= end of Managing Guest DataBase============================================
#=============================================Managing Health StatusTable=======================================

    def popUpHealthStatus(self):
        self.FormFrame = Frame(self.SearchAndReporFrame)
        self.Status_update_label_form = LabelFrame(self.FormFrame)
        self.Date_Label = Label(self.Status_update_label_form)
        self.Date_Label.config(text='Date')
        self.Date_Label.grid(padx='20', pady='2')
        self.Date_entry = DateEntry(self.Status_update_label_form)
        self.Date_entry.config(justify='center')
        self.Date_entry.delete('0', 'end')
        self.Date_entry.insert('0', Date)
        self.Date_entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='0')
        self.Student_or_staff_id_label = Label(self.Status_update_label_form)
        self.Student_or_staff_id_label.config(text='Student/staff ID')
        self.Student_or_staff_id_label.grid(column='0', padx='20', pady='2', row='1')
        self.Student_or_staff_id_Entry = Entry(self.Status_update_label_form)
        self.Student_or_staff_id_Entry.config(justify='center')
        self.Student_or_staff_id_Entry.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='1')
        self.BodyTemp_label = Label(self.Status_update_label_form)
        self.BodyTemp_label.config(text='Body Temp(F)')
        self.BodyTemp_label.grid(column='0', padx='20', pady='2', row='2')
        self.BodyTemp_Entery = Entry(self.Status_update_label_form)
        self.BodyTemp_Entery.config(justify='center')
        self.BodyTemp_Entery.grid(column='1', ipadx='30', ipady='6', padx='20', pady='2', row='2')
        self.symptoms_label = Label(self.Status_update_label_form)
        self.symptoms_label.config(text='Symptoms')
        self.symptoms_label.grid(column='0', padx='20', pady='8', row='3')
        self.symptoms_rad_Frame = Frame(self.Status_update_label_form)
        self.Yes_rad = Radiobutton(self.symptoms_rad_Frame)
        symptoms = StringVar('')
        self.symptoms=symptoms
        self.Yes_rad.config(text='Yes', value='Yes', variable=symptoms)
        self.Yes_rad.grid(padx='25', pady='8')
        self.No_rad = Radiobutton(self.symptoms_rad_Frame)
        self.No_rad.config(text='No', value='No', variable=symptoms)
        self.No_rad.grid(column='1', padx='25', pady='8', row='0')
        self.symptoms_rad_Frame.config(height='200', width='200')
        self.symptoms_rad_Frame.grid(column='1', row='3')

        self.ButtonFrame = Frame(self.Status_update_label_form)
        self.ButtonFrame.config(height='200', width='200')
        self.ButtonFrame.grid(column='0', columnspan='5', padx='2', pady='2', row='10')

        # self.Update_to_DB_BUTTON = Button(self.ButtonFrame)
        # self.Update_to_DB_BUTTON.config(text='Update')
        # self.Update_to_DB_BUTTON.grid(column='0', ipadx='35', padx='10', pady='10', row='0')
        # self.Update_to_DB_BUTTON.configure(command=lambda:self.UpdateRow('HealthStatus'))

        self.Delete_button = Button(self.ButtonFrame)
        self.Delete_button.config(text='Delete')
        self.Delete_button.grid(column='1', ipadx='35', padx='10', pady='10', row='0')
        self.Delete_button.configure(command=lambda:self.DeleteRow('HealthStatus'))

        # self.Clear_button = Button(self.ButtonFrame)
        # self.Clear_button.config(text='Clear')
        # self.Clear_button.grid(column='2', ipadx='35', padx='10', pady='10', row='0')
        # self.Clear_button.configure(command=lambda:self.clear('HealthStatus'))

        self.Close_button = Button(self.ButtonFrame)
        self.Close_button.config(text='Close')
        self.Close_button.grid(column='3', ipadx='35', padx='10', pady='10', row='0')
        self.Close_button.configure(command=lambda:self.close24('HealthStatus'))

        self.Status_update_label_form.config(height='400',text='Health status update', width='800')
        self.Status_update_label_form.pack(anchor='center', expand='true', fill='both', side='top')
        self.Status_update_label_form.pack_propagate(0)
        self.FormFrame.config(height='200', width='200')
        self.FormFrame.place(anchor='center', height='20', relheight='0.3', relwidth='0.4', relx='0.5', rely='0.5', width='100', x='0', y='0')
#End of HealthStatus UI

    def get_HealthStatusjoinStaff_cursor(self,evn):
        Cursor_row=self.HealthStatusjoinStaff_Table.focus()
        Content=self.HealthStatusjoinStaff_Table.item(Cursor_row)
        row=Content['values']
        if(len(row)!=0):
            self.popUpHealthStatus()
            self.Student_or_staff_id_Entry.insert("0",row[0])
            self.Date_entry.delete("0",END)
            self.Date_entry.insert("0",row[5])
            self.BodyTemp_Entery.insert("0",row[6])
            if(row[7]=='Yes'):
                self.Yes_rad.select()
            if(row[7]=='No'):
                self.No_rad.select()
        print(row)

    
    def get_HealthStatusjoinStudent_cursor(self,evn):
        Cursor_row=self.HealthStatusjoinStudent_Table.focus()
        Content=self.HealthStatusjoinStudent_Table.item(Cursor_row)
        row=Content['values']
        if(len(row)!=0):
            self.popUpHealthStatus()
            self.Student_or_staff_id_Entry.insert("0",row[0])
            self.Date_entry.delete("0",END)
            self.Date_entry.insert("0",row[3])
            self.BodyTemp_Entery.insert("0",row[4])
            if(row[5]=='Yes'):
                self.Yes_rad.select()
            if(row[5]=='No'):
                self.No_rad.select()
        print(row)



#=============================================Managing Health StatusTable=======================================




    #===========================All Button Functions Handling===============================================
    # def RunQuery(self,Values,Query):
    #     conn=cx.connect(link)
    #     cur=conn.cursor()
    #     cur.execute(Query,Values)
    #     conn.commit()
    #     conn.close()

    def FetchStudentValues(self):
        Values=[]
        StudentID=self.Student_ID_entry1.get() 
        StudentName=self.Student_name_entry1.get() 
        Branch=self.Branchh.get()
        PhoneNumber=self.student_phoneno_entry1.get() 
        Adress=self.student_adress_entry1.get()
        if(StudentID and StudentName and Branch and PhoneNumber and Adress):
            Values.append(StudentID)
            Values.append(StudentName)
            Values.append(int(Branch))
            Values.append(int(PhoneNumber))
            Values.append(Adress)
        else:
            messagebox.showerror('Server Says','Enter Required Fields')
        return Values

    def FetchStaffValues(self):
        Values=[]
        StaffID=self.Staff_ID_entry.get()
        satffNmae=self.Staff_name_entry.get()
        Dept=self.Dept.get()
        Section=self.Section.get()
        PhoneNumber=self.staff_phoneno_entry.get()
        Adress=self.staff_adress_entry.get()
        StaffType=self.stafftype.get()
        if(StaffID and satffNmae and Dept and Section and PhoneNumber and Adress and StaffType):
            Values.append(StaffID)
            Values.append(satffNmae)
            Values.append(int(Dept))
            Values.append(int(Section))
            Values.append(int(PhoneNumber))
            Values.append(Adress)
            Values.append(StaffType)
        else:
            messagebox.showerror('Server Says','Enter Required Fields')
        return Values

    def FetchHealthValues(self):
        Month=['','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
        Values=[]
        date=self.Date_entry.get()
        # date=date[0:10]
        # date=date.split('-')
        # dates=[]
        # for i in date[::-1]:
        #     dates.append(i)
        date=date.split('/')
        Mon=int(date[0])
        date=date[1]+'-'+Month[Mon]+'-'+date[2]
        ID=self.Student_or_staff_id_Entry.get()
        BodyTemp=self.BodyTemp_Entery.get()
        Symptopms=self.symptoms.get()
        if(date and ID and BodyTemp and Symptopms):
            Values.append(date)
            Values.append(ID)
            Values.append(BodyTemp)
            Values.append(Symptopms)
            print(Values)
        else:
            messagebox.showerror('Server Says','Enter Required Fields')
        return Values
    
    def FetchGuestValues(self):
        Values=[]
        Guest_name=self.Guest_Name_entry.get()
        Phone_number=self.Guest_Phone_Entry.get()
        if(Guest_name and Phone_number):
            # guest_visited_from_db=[]
            # guest_visited_from_db.append(self.Acadamics.get())
            # guest_visited_from_db.append(self.Admission.get())
            # guest_visited_from_db.append(self.placement.get())
            # guest_visited_from_db.append(self.Finace.get())
            # k=0
            # for i in guest_visited_from_db:
            #     if(i == 'No' or i==''):
            #         k=k+1
            # if(k != 4):
            Values.append(Guest_name)
            Values.append(int(Phone_number))
                #Update guest visited information
                # print(Values)
            # else:
            #     messagebox.showerror('Server Says','Enter any section visited')
        else:
            messagebox.showerror('Server Says','Enter Required Fields')
        return Values



    def UpdateRow(self,Value_of):
        if(Value_of=='Student'):
            # #Query=Update student Query
            Values=self.FetchStudentValues()
            Sucess=Queries.RunUpdateFunction(
                '''
                update student set studentfullname=:1,branchid=:2,phonenumber=:3,adress=:4
                where studentid=:5
                ''',
                {
                    '1':Values[1],
                    '2':Values[2],
                    '3':Values[3],
                    '4':Values[4],
                    '5':Values[0]
                }
            )
            if(Sucess):
                messagebox.showinfo('Server Says','Updation SucessFull')
                self.close24('Student')
                self.ShowAll('Student')
            else:
                messagebox.showinfo('Server Says','Error')
            print(Values)
            
            print("Update Student")
        elif(Value_of=='Staff'):
            Values=self.FetchStaffValues()
            Sucess=Queries.RunUpdateFunction(
                '''
                update staff set stafffullname=:1,deptid=:2,sectionid=:3,phonenumber=:4,adress=:5,stafftype=:6
                where staffid=:7
                ''',
                               {
                    '1':Values[1],
                    '2':Values[2],
                    '3':Values[3],
                    '4':Values[4],
                    '5':Values[5],
                    '6':Values[6],
                    '7':Values[0]
                }
            )
            if(Sucess):
                messagebox.showinfo('Server Says','Updation SucessFull')
                self.close24('Staff')
                self.ShowAll('Staff')
            else:
                messagebox.showinfo('Server Says','Error')

            print("Update Staff")
        # elif(Value_of=='HealthStatus'):
        #     Values=self.FetchHealthValues()
        #     print(Values)
        #     #Update Health Status Based on date and ID
        #     print("update HealthStatus")
        # elif(Value_of=='Guest'):
        #     Values=self.FetchGuestValues()
        #     print(Values)
            
        #     print("update Guest")
    def DeleteRow(self,Value_of):
        if(Value_of=='Student'):
            # #Query=DeleteQuery
            Values=self.FetchStudentValues()
            print(Values)
            Sucess=Queries.RunUpdateFunction(
                '''
                delete from student where studentid=:5
                ''',
                {
                    '5':Values[0]
                }
            )
            if(Sucess):
                messagebox.showinfo('Server Says','Deleted')
                self.close24('Student')
                self.ShowAll('Student')
            else:
                messagebox.showerror('Server Says','Error')
            print("Delete Student")
        elif(Value_of=='Staff'):
            Values=self.FetchStaffValues()
            print(Values)
            Sucess=Queries.RunUpdateFunction(
                '''
                delete from staff where staffid=:5
                ''',
                {
                    '5':Values[0]
                }
            )
            if(Sucess):
                messagebox.showinfo('Server Says','Deleted')
                self.close24('Staff')
                self.ShowAll('Staff')
            else:
                messagebox.showerror('Server Says','Error')
            print("Delete Staff")
        elif(Value_of=='HealthStatus'):
            Values=self.FetchHealthValues()
            print(Values)
            Sucess=Queries.RunUpdateFunction(
                '''
                delete from health_status where ids=:1 and dates=:2
                ''',
                {
                    '1':Values[1],
                    '2':Values[0]
                }
            )
            if(Sucess):
                messagebox.showinfo('Server Says','Deleted')
                self.close24('HealthStatus')
                self.ShowAll('HealthStatus')
            else:
                messagebox.showerror('Server Says','Error')
            print("Delete HealthStatus")
        elif(Value_of=='Guest'):
            Values=self.FetchGuestValues()
            print(Values)
            Sucess=Queries.RunUpdateFunction(
                '''
                delete from guest where guestname=:1 and phonenumber=:2
                ''',
                {
                    '1':Values[0],
                    '2':Values[1]
                }
            )
            if(Sucess):
                messagebox.showinfo('Server Says','Deleted')
                self.close24('Guest')
                self.ShowAll('Guest')
            else:
                messagebox.showerror('Server Says','Error')
            print("Delete Guest")
    
    def close24(self,Value_of):
        if(Value_of=='Student' or Value_of=='Staff' or Value_of=='Guest' or Value_of=='HealthStatus'):
            try:
                self.FormFrame.destroy()
            except Exception:
                pass
    #===========================end of All Button Functions Handling===========================================
    

#=====================================end of Managing DataBase Update/Delete operation==================================
# root1 = Tk()
# root1.title('Search manage and report')
# root1.state("zoomed")
# widget = SearchAndReportFilterStudentWidget(root1)
# widget.pack(expand=True, fill='both')
# root1.mainloop()





root = themed_tk.ThemedTk()
root.get_themes()
root.set_theme("radiance")#clearlooks#breeze#black#adapta#radiance
root.title('Home')
root.state("zoomed")
widget = HomeNewStudentWidget(root)
widget.pack(expand=True, fill='both')
root.mainloop()
