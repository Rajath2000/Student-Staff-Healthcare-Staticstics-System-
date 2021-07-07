import cx_Oracle as cx
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox

#link to connect to DataBase
link='hr/hr@//localhost:1521/xe'

#Quires like create table
def initializeDataBae():
    try:
        conn=cx.connect(link)
        cur=conn.cursor()
        try:
            cur.execute("""
            CREATE TABLE BRANCH(
            BranchID NUMBER(2),
            BranchName VARCHAR(2),
            CONSTRAINT BRANCH_PK PRIMARY KEY(BranchID)
            );""")
            cur.execute("""
            CREATE TABLE STUDENT(
            StudentID VARCHAR(10),
            StudentFullName VARCHAR(20),
            BranchID NUMBER(2),
            PhoneNumber NUMBER(10),
            Adress VARCHAR(20),
            CONSTRAINT STUDENT_PK PRIMARY KEY(StudentID),
            CONSTRAINT STUDENT_FK FOREIGN KEY(BranchID) REFERENCES Branch(BranchID)
            ON DELETE CASCADE
            );
            """)
            cur.execute("""
            CREATE TABLE SECTION(
            SectionID NUMBER(2),
            SectionName VARCHAR(10),
            CONSTRAINT SECTION_PK PRIMARY KEY(SectionID)
            );""")
            cur.execute("""
            CREATE TABLE STAFF(
            StaffID VARCHAR(10),
            StaffFullName VARCHAR(20),
            DeptID NUMBER(2),
            SectionID NUMBER(2),
            PhoneNumber NUMBER(10),
            Adress VARCHAR(20),
            StaffType VARCHAR(1),
            CONSTRAINT STAFF_CK CHECK(StaffType IN('T','N')),
            CONSTRAINT STAFF_PK PRIMARY KEY(StaffID),
            CONSTRAINT STAFF_FK1 FOREIGN KEY(SectionID)REFERENCES SECTION(SectionID) ON DELETE CASCADE,
            CONSTRAINT STAFF_FK2 FOREIGN KEY(DeptID)REFERENCES BRANCH(BranchID) ON DELETE CASCADE
            );
            """)
            cur.execute("""
            CREATE SEQUENCE customer_id minvalue 1 start with 1 cache 10;           
            """)
            cur.execute("""
            CREATE TABLE GUEST(
            GuestID INT NOT NULL,
            GuestName VARCHAR(20),
            PhoneNumber NUMBER(10),
            CONSTRAINT GUEST_UQ UNIQUE(GuestName,PhoneNumber)
            CONSTRAINT GUEST_PK PRIMARY KEY(GuestID)
            );
            """)
            cur.execute("""
            CREATE TABLE HEALTH_STATUS(
            Dates DATE,
            Ids VARCHAR(10),
            BodyTemp FLOAT(62),
            Symtoms VARCHAR(3),
            CONSTRAINT HEALTH_STATUS_CK CHECK(Symtoms IN('Yes','No'))
            );
            """)
            cur.execute("""
            CREATE TABLE GUEST_VISITED(
            GUESTID NUMBER(2),
            SECTIONID NUMBER(2),
            CONSTRAINT GUEST_VISITED_UQ UNIQUE(GUESTID,SECTIONID),
            CONSTRAINT GUEST_VISITED_FK1 FOREIGN KEY(GUESTID) REFERENCES GUEST(GUESTID) ON DELETE CASCADE,
            CONSTRAINT GUEST_VISITED_FK2 FOREIGN KEY(SECTIONID) REFERENCES SECTION(SECTIONID)
            );
            """)
            cur.execute("""
            CREATE TABLE IN_CTO_TEMPERATURE(
            Dates DATE,
            IDS VARCHAR(10),
            CEL FLOAT(62),
            UNIQUE(IDS),
            FOREIGN key(IDS,Dates)REFERENCES HEALTH_STATUS(Ids,Dates) ON DELETE CASCADE
            );
            """)
        except Exception as err:
            pass
    except Exception as err:
            pass
            

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
         


#Quries to create procedures
def InsertStudent(Values):
    try:
        conn=cx.connect(link)
        cur=conn.cursor()
        #Create procedure to 
        studentprocedure='''
        create or replace PROCEDURE Add_student_info(STUDENTID VARCHAR,STUDENTFULLNAME VARCHAR,BRANCHID NUMBER,PHONENUMBER NUMBER,ADRESS VARCHAR)
        IS
        BEGIN
            INSERT INTO STUDENT VALUES(STUDENTID,STUDENTFULLNAME,BRANCHID,PHONENUMBER,ADRESS);
            COMMIT;
        END;
        '''
        try:
            #Execute procedure
            # cur.execute(studentprocedure)
            #calling Procedure
            cur.callproc('Add_student_info',Values)
            return cur.rowcount
        except Exception:
            pass
    except Exception:
        pass
    finally:
        conn.close()
        
#Quries to add staffinfo
def InsertStaff(Values):
    try:
        conn=cx.connect(link)
        cur=conn.cursor()
        staffprocedure='''
        create or replace PROCEDURE Add_staff_info(STAFFID VARCHAR,STAFFFULLNAME VARCHAR,DEPTID NUMBER,SECTIONID NUMBER,PHONENUMBER NUMBER,ADRESS VARCHAR,STAFFTYPE VARCHAR)
        IS
        BEGIN
            INSERT INTO STAFF VALUES(STAFFID,STAFFFULLNAME,DEPTID,SECTIONID,PHONENUMBER,ADRESS,STAFFTYPE);
            COMMIT;
        END;
        '''
        try:
            # cur.execute(staffprocedure)
            cur.callproc('Add_staff_info',Values)
            return cur.rowcount
        except Exception as err:
            print(err)
    except Exception as err:
        print(err)
    finally:
        conn.close()

#Quries to add Guest info
def InsertGuest(Values,Visited_info):
    val=0
    try:
        conn=cx.connect(link)
        cur=conn.cursor()
        Guestprocedure='''
        create or replace PROCEDURE Add_Guest_info(GUESTNAME VARCHAR,PHONENUMBER NUMBER)
        IS
        BEGIN
            INSERT INTO GUEST VALUES(CUSTOMER_ID.nextval,GUESTNAME,PHONENUMBER);
            COMMIT;
        END;
        '''
        try:
            cur.execute(Guestprocedure)
            cur.callproc('Add_Guest_info',Values)
            val=1
            try:
                cur.execute('select GUESTID from GUEST')
                row=cur.fetchall()
                newrow=[]
                for i in row:
                    newrow.append(i[0])
                newrow.sort()
                if(val==1 and cur.rowcount):
                    return newrow[-1]
            except Exception as err:
                print(err)
                return val
        except Exception as err:
            print(err)
            return val
    except Exception as err:
        print(err)
        return val
    finally:
        conn.close()

#Quries to add Guest info with procedure
def Guest_visited_insert_proc(Visited_info):
    try:
        conn=cx.connect(link)
        cur=conn.cursor()
        Guest_visit_insert_procedure='''
create or replace PROCEDURE GUESTVISIT_IN_PRO 
(
 Acadamics IN VARCHAR2 
, Admission IN VARCHAR2 
, Placement IN VARCHAR2 
, Finance IN VARCHAR2 
,GuestID IN NUMBER
) AS 
BEGIN
  IF(Acadamics = 'Acadamics')
  THEN
  INSERT INTO guest_visited VALUES(GuestID,1);
  END IF;
  IF(Admission = 'Admission')
  THEN
  INSERT INTO guest_visited VALUES(GuestID,2);
  END IF; 
  IF(Placement = 'placement')
  THEN
  INSERT INTO guest_visited VALUES(GuestID,3);
  END
  IF;  IF(Finance = 'Finance')
  THEN
  INSERT INTO guest_visited VALUES(GuestID,4);
  END IF;
  commit;
END GUESTVISIT_IN_PRO;

        '''
        try:
            # cur.execute(Guest_visit_insert_procedure)
            print(Visited_info)
            cur.callproc('GUESTVISIT_IN_PRO',Visited_info)
            return cur.rowcount
        except Exception as err:
            print(err)
    except Exception as err:
        print(err)
    finally:
        conn.close()

def Guest_visited_up_proc(Visited_info):
    try:
        conn=cx.connect(link)
        cur=conn.cursor()
        Guest_visit_up_procedure='''
        CREATE OR REPLACE PROCEDURE GUEST_VISIT_UP_PRO 
        (
        
        Acadamics IN VARCHAR2 , Admission IN VARCHAR2 , Placement IN VARCHAR2 , Finance IN VARCHAR2 ,
        Guest IN NUMBER
        ) AS 
        BEGIN
        IF(Acadamics='Delete')
        THEN
            DELETE FROM guest_visited WHERE GUESTID=Guest AND SECTIONID=1;
        ELSIF(Acadamics='Insert')
        THEN
            INSERT INTO guest_visited VALUES(Guest,1);
        END IF;
        
            IF(Admission='Delete')
        THEN
            DELETE FROM guest_visited WHERE GUESTID=Guest AND SECTIONID=2;
        ELSIF(Admission='Insert')
        THEN
            INSERT INTO guest_visited VALUES(Guest,2);
        END IF;
        
            IF(Placement='Delete')
        THEN
            DELETE FROM guest_visited WHERE GUESTID=Guest AND SECTIONID=3;
        ELSIF(Placement='Insert')
        THEN
            INSERT INTO guest_visited VALUES(Guest,3);
        END IF;
        
            IF(Finance='Delete')
        THEN
            DELETE FROM guest_visited WHERE GUESTID=Guest AND SECTIONID=4;
        ELSIF(Finance='Insert')
        THEN
            INSERT INTO guest_visited VALUES(Guest,4);
        END IF;
        commit;
        END GUEST_VISIT_UP_PRO;
        
        '''
        try:
            cur.execute(Guest_visit_up_procedure)
            cur.callproc('GUEST_VISIT_UP_PRO',Visited_info)
            return 1
        except Exception as err:
            print(err)
    except Exception as err:
        print(err)
    finally:
        conn.close()
    


def guest_visited_info_form_db(Gname,Gphone):
    val=0
    try:
        conn=cx.connect(link)
        cur=conn.cursor()
        try:
            #QUERY TO FETCH VISITED INFO FROM DATABASE
            # SELECT S.SECTIONNAME FROM
            # SECTION S,GUEST  G,guest_visited V
            # WHERE G.GUESTID=V.GUESTID AND V.SECTIONID=S.SECTIONID AND G.GUESTNAME='rama' 
            # AND G.PHONENUMBER=963214587;
            cur.execute("""select section.sectionname from guest,guest_visited,section where
             guest.guestid=guest_visited.guestid and 
             section.sectionid=guest_visited.sectionid and guestname=:val1 and phonenumber=:val2""",
            {
                'val1':Gname,
                'val2':Gphone
            })
            newrow=[]
            send=['No','No','No','No']
            rows=cur.fetchall()
            for row in rows:
                newrow.append(row[0])
            for i in newrow:
                if(i=='Acadamics'):
                    send[0]='Acadamics'
                else:
                    pass
                if(i=='Admission'):
                    send[1]='Admission'
                else:
                    pass
                if(i=='placement'):
                    send[2]='placement'
                else:
                    pass
                if(i=='Finance'):
                    send[3]='Finance'
                else:
                    pass
            if(cur.rowcount):
                return send
            else:
                return val
        except Exception as err:
            pass
    finally:
        conn.close()

def getGuestIdandUpdateGuestInFO(guestname,phonenumber):
    try:
        conn=cx.connect(link)
        cur=conn.cursor()
        try:
            cur.execute('select guestid from guest where guestname=:guestname and phonenumber=:phonenumber',[guestname,phonenumber])
            val=cur.fetchone()
            print(val[0])
            guestid=val[0]
            print(type(guestid))
            # cur.execute('Update guest set guestname=:guestname,phonenumber=:phonenumber where guestid=:guestid',[guestname,phonenumber,guestid])
            conn.commit()
            return guestid
        except Exception:
            print(Exception)
    except Exception:
        pass
    finally:
        conn.close()


def updateGuest(values):
    # print(values)
    try:
        conn=cx.connect(link)
        cur=conn.cursor()
        try:
            cur.execute('update guest set guestname=:name,phonenumber=:phone where guestid=:id',{
                'name':values[0],
                'phone':values[1],
                'id':values[2]
            })
            # cur.execute('Update guest set guestname=:guestname,phonenumber=:phonenumber where guestid=:guestid',[guestname,phonenumber,guestid])
            conn.commit()
            return cur.rowcount
        except Exception:
            print(Exception)
    except Exception:
        pass
    finally:
        conn.close()


def InsertHealthStatusInfo(Values):
    print(Values)
    try:
        conn=cx.connect(link)
        cur=conn.cursor()
        #Create procedure to 
        HealthStatusprocedure='''
        CREATE OR REPLACE PROCEDURE INSERT_HEALTH_STAT_PROC 
        (
        DATES IN DATE 
        , IDS IN VARCHAR 
        , BODYTEMP IN FLOAT
        , SYMTOMS IN VARCHAR
        ) AS 
        BEGIN
        INSERT INTO health_status VALUES(DATES,IDS,BODYTEMP,SYMTOMS);
        commit;
        END INSERT_HEALTH_STAT_PROC;
        '''
        try:
            #Execute procedure
            cur.execute('select * from student where studentid=:1',
            {
                '1':Values[1]
            })
            cur.fetchall()
            countstudent=cur.rowcount
            cur.execute('select * from staff where staffid=:1',
            {
                '1':Values[1]
            })
            cur.fetchall()
            countstaff=cur.rowcount
            if(countstudent or countstaff):
                # cur.execute(HealthStatusprocedure)
                #calling Procedure
                cur.callproc('INSERT_HEALTH_STAT_PROC',Values)
                conn.commit()
                return 1
            else:
                messagebox.showerror('Server says','Student/staff not exsits')
                return 2

        except Exception as err:
            print(err)
    except Exception:
        pass
    finally:
        conn.close()


def Triggers():
    try:
        conn=cx.connect(link)
        cur=conn.cursor()
        try:
            CALCUATE_celsius_on_INSERT='''
            create or replace TRIGGER CALCUATE_C_ON_INSERT 
            AFTER INSERT ON HEALTH_STATUS 
            REFERENCING OLD AS OLD NEW AS NEW 
            FOR EACH ROW
            DECLARE
            Dates DATE;
            Celi FLOAT(62);
            IDSS VARCHAR(10);
            BEGIN
            Dates:=:new.Dates;
            idss:=:new.IDS;
            Celi:=((:new.BODYTEMP-32)*5)/9;
            INSERT INTO IN_CTO_TEMPERATURE VALUES(Dates,idss,Celi);
            END;
            '''
            CALCUATE_celsius_on_UPDATE='''
            create or replace TRIGGER CALCUATE_C_ON_Update
            AFTER UPDATE ON HEALTH_STATUS 
            REFERENCING OLD AS OLD NEW AS NEW 
            FOR EACH ROW
            DECLARE
            Dates DATE;
            Celi FLOAT(62);
            IDSS VARCHAR(10);
            BEGIN
            Dates:=:new.Dates;
            idss:=:new.IDS;
            Celi:=((:new.BODYTEMP-32)*5)/9;
            UPDATE IN_CTO_TEMPERATURE SET cel=Celi WHERE dates=dates and ids=idss;
            END;
            '''
            cur.execute(CALCUATE_celsius_on_INSERT)
            cur.execute(CALCUATE_celsius_on_UPDATE)
            # cur.execute('Update guest set guestname=:guestname,phonenumber=:phonenumber where guestid=:guestid',[guestname,phonenumber,guestid])
            conn.commit()
            return 1
        except Exception:
            print(Exception)
    except Exception:
        pass
    finally:
        conn.close()

# InsertHealthStatusInfo(['28-FEB-2018','7',98.6,'Yes'])

def getHealthDetailsfromDB(Date,ID):
    try:
        conn=cx.connect(link)
        cur=conn.cursor()
        try:
            cur.execute('select bodytemp,symtoms from health_status where dates=:1 and ids=:2',{
              '1':Date,
              '2':ID
            })
            # cur.execute('Update guest set guestname=:guestname,phonenumber=:phonenumber where guestid=:guestid',[guestname,phonenumber,guestid])
            rows=cur.fetchall()
            send=[]
            for row in rows:
                send.append(row[0])
                send.append(row[1])
            return send
        except Exception as err:
            return 0
    except Exception:
        pass
    finally:
        conn.close()

def updateHealthInfo(Values):
    try:
        conn=cx.connect(link)
        cur=conn.cursor()
        try:
            print(Values)
            cur.execute('update health_status set bodytemp=:3,symtoms=:4 where ids=:2 and dates=:1',{
              '1':Values[0],
              '2':Values[1],
              '3':Values[2],
              '4':Values[3],
            })
            # cur.execute('Update guest set guestname=:guestname,phonenumber=:phonenumber where guestid=:guestid',[guestname,phonenumber,guestid])
            conn.commit()
            return cur.rowcount
        except Exception as err:
            print(err)
    except Exception:
        pass
    finally:
        conn.close()
        
def updateC(Values):
    try:
        conn=cx.connect(link)
        cur=conn.cursor()
        #Create procedure to 
        try:
            cur.execute("""
            update IN_CTO_TEMPERATURE set cel=:1 where ids=:2 and dates=:3
            """,{
                '1':Values[2],
                '2':Values[1],
                '3':Values[0]
            })
            conn.commit()
            return cur.rowcount
        except Exception as err:
            print(err)
    except Exception as err:
        print(err)
    finally:
        conn.close()



####===================================Search Quires==========================================================
#=====================================student table searching functions=======================================
def RunQueryWithNoValue(Query):
    try:
        conn=cx.connect(link)
        cur=conn.cursor()
        try:
            cur.execute(Query)
            # cur.execute('Update guest set guestname=:guestname,phonenumber=:phonenumber where guestid=:guestid',[guestname,phonenumber,guestid])
            return cur.fetchall()
        except Exception as err:
            print(err)
    except Exception:
        pass
    finally:
        conn.close()

def RunQueryWithValue(Query,value):
    try:
        conn=cx.connect(link)
        cur=conn.cursor()
        try:
            cur.execute(Query,value)
            # cur.execute('Update guest set guestname=:guestname,phonenumber=:phonenumber where guestid=:guestid',[guestname,phonenumber,guestid])
            return cur.fetchall()
        except Exception as err:
            print(err)
    except Exception:
        pass
    finally:
        conn.close()

def RunUpdateFunction(Query,value):
    try:
        conn=cx.connect(link)
        cur=conn.cursor()
        try:
            cur.execute(Query,value)
            conn.commit()
            return cur.rowcount
        except Exception as err:
            print(err)
    except Exception:
        pass
    finally:
        conn.close()

#=====================================end of student table searching functions=======================================

    
#=====================================DATA ANALYSIS==============================================
def graph(Name,bodytemp,Dates,Xcor):
    # x-coordinates of left sides of bars  
    print(Name,bodytemp,Dates)
    left = Xcor

    
    # heights of bars 

    height =bodytemp

    
    # labels for bars 

    tick_label = Dates

    
    # plotting a bar chart 

    plt.bar(left, height, tick_label = tick_label, 

            width = 0.5, color = ['#bebebe']) 

    
    # naming the x-axis 

    plt.xlabel('DATE') 
    # naming the y-axis 

    plt.ylabel('BODYTEMP IN (F)') 
    # plot title 

    plt.title(Name) 

    
    # function to show the plot 
    plt.show()
# graph('Rajath',['28-12-2020', '20-02-2020'],[98.3, 96.3])