from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
import pymysql


root = Tk()
root.title("College-Fest Management System")
root.geometry("500x400+400+200")
root.configure(background = "maroon")

def f1() :
	adst.deiconify()
	root.withdraw()
def f2() :
	root.deiconify()
	adst.withdraw()
def f3() :
	sdst.deiconify()
	root.withdraw()
def f4() :
	root.deiconify()
	sdst.withdraw()
def f5() :
	ap.deiconify()
	adst.withdraw()
def f6() :
	adst.deiconify()
	ap.withdraw()
def f7() :
	up.deiconify()
	adst.withdraw()
def f8() :
	adst.deiconify()
	up.withdraw()
def f9() :
	dp.deiconify()
	adst.withdraw()
def f10() :
	adst.deiconify()
	dp.withdraw()
def f11() :

	vpdata.delete(1.0 , END)
	vp.deiconify()
	adst.withdraw()
	
	con = None
	try :
		con = pymysql.connect("localhost","root","abc456","mypro")
		print("Connected")

		cursor = con.cursor()
		sql = "Select * from student"
		cursor.execute(sql)

		data = cursor.fetchall()
		
		info = " "
		for d in data :
			info  = info + " ID:"  + str(d[0]) + " Name :" + str(d[1]) + " College:" + str(d[2]) + " Year :" +str(d[3]) +" Event :" + str(d[4]) + "\n" + "----------------------------------------------------------------------"
		
		vpdata.insert(INSERT , info)

	except Exception as e:
		showerror("View Issue!" , str(e))

	finally:
		if con is not None :
			con.close()
			print("Disconnected")

		
	

	

	
def f12() :
	adst.deiconify()
	vp.withdraw()	
def f13() :
	ae.deiconify()
	adst.withdraw()
def f14() :
	adst.deiconify()
	ae.withdraw()
def f15() :
	aw.deiconify()
	adst.withdraw()
def f16() :
	adst.deiconify()
	aw.withdraw()
def f17() :

	vwdata.delete(1.0 , END)
	vw.deiconify()
	adst.withdraw()

	con = None
	try :
		con = pymysql.connect("localhost","root","abc456","mypro")
		print("Connected")

		cursor = con.cursor()
		sql = "Select * from winner"
		cursor.execute(sql)

		data = cursor.fetchall()

		info = " "
		for d in data :
			info  = info + " ID:"  + str(d[0]) + " Winner :" + str(d[1]) + " Event:" + str(d[2]) + "\n" + "--------------------------------------------------"


		vwdata.insert(INSERT,info)

	except Exception as e :
		showerror("View Issue!" , str(e))

	finally :
		if con is not None :
			con.close()
			print("Disconnected")
def f18() :
	adst.deiconify()
	vw.withdraw()	

def f19() :
	con = None
	try :
		con = pymysql.connect("localhost","root","abc456","mypro")
		print("Connected")

		
		
		id = int(sentstudentid.get())
		name = sentname.get()
		college = sentcollege.get()
		year = sentyear.get()
		event = sentevent.get()
		
		args=(id,name,college,year,event)

		cursor = con.cursor()
		cursor.execute("CREATE TABLE if not exists student (id int primary key ,name varchar(20) , college varchar(20),year enum('FE','SE','TE','BE'),event varchar(20))")
		sql = "insert into student values('%d' , '%s' , '%s' , '%s' , '%s')"
		cursor.execute(sql%args)
		con.commit()
		showinfo("Success" , "Record added !")

		f25()
		f28()


		
	
	except Exception as e:
		showerror("Mistake" , "Insert issue!" +str(e))
		con.rollback()
	finally :
		if con is not None :
			con.close()
			print("Disconnected")

def f20() :
	con = None
	try :
		con = pymysql.connect("localhost","root","abc456","mypro")
		print("Connected")

		
		
		id = int(apentstudentid.get())
		name = apentname.get()
		college = apentcollege.get()
		year = apentyear.get()
		event = apentevent.get()
		
		args=(id,name,college,year,event)

		cursor = con.cursor()
		cursor.execute("CREATE TABLE if not exists student ( id int primary key ,name varchar(20) , college varchar(20),year enum('FE','SE','TE','BE'),event varchar(20))")
		sql = "insert into student values('%d' , '%s' , '%s' , '%s' , '%s')"
		cursor.execute(sql%args)
		con.commit()
		showinfo("Success" , "Record added !")

		f25()
		f28()
	
	except Exception as e:
		showerror("Mistake" , "Insert issue!" +str(e))
		con.rollback()
	finally :
		if con is not None :
			con.close()
			print("Disconnected")
		
def f21() :
	con = None
	try :
		con = pymysql.connect("localhost","root","abc456","mypro")
		print("Connected")

		
		id = int(upentstudentid.get())
		name = upentname.get()
		college = upentcollege.get()
		year = upentyear.get()
		event = upentevent.get()

		args = (name , college , year , event, id)

		cursor = con.cursor()
		sql = "Update student set name = '%s' , college = '%s' , year = '%s' , event = '%s' where id = '%d' "
		cursor.execute(sql % args)

		
		
		if cursor.rowcount >=1 :
			con.commit()
			showinfo("Success !" ,"Record Updated Successfully!")
		else :
			showerror("Update Issue!" , "Record doesnt exists!")

		f26()
		

	except Exception as e :
		showerror("Issue!" , str(e))
		con.rollback()

	finally :
		if con is not None :
			con.close()
			print("Disconnected")

def f22() :
	con = None
	
	try :
		con = pymysql.connect("localhost","root","abc456","mypro")
		print("Connected")
		
		id = int(dpentstudentid.get())
		args = (id)
		cursor = con.cursor()

		sql = "delete from student where id = '%d'  "
		cursor.execute(sql % args)

		if cursor.rowcount >= 1:
			con.commit()
			showinfo("Success!","Record Deleted!")
			
		else :
			showerror("Delete Error" , "Roll No does not exists!")

		f27()
		dpentstudentid.delete(0 , END)

			

	except Exception as e :
		showerror("Delete issue!", str(e))
		con.rollback()
	finally :
		if con is not None :
			con.close()
			print("Disconnected")

def f23() :
	con = None
	try :
		con = pymysql.connect("localhost","root","abc456","mypro")
		print("Connected")

		eid = int(aeenteid.get())
		ename = aeentename.get()

		args = (eid,ename)

		cursor = con.cursor()
		cursor.execute("CREATE TABLE if not exists event ( eid int primary key ,ename varchar(20))")
		sql = "insert into event values('%d' , '%s' )"
		cursor.execute(sql%args)
		con.commit()
		showinfo("Success" , "Event added !")

	except Exception as e:
		showerror("Mistake" , "Insert issue!" +str(e))
		con.rollback()
	finally :
		if con is not None :
			con.close()
			print("Disconnected")
	
def f24() :
	con = None
	try :
		con = pymysql.connect("localhost","root","abc456","mypro")
		print("Connected")

		wid = int(awentstudentid.get())
		wname = awentname.get()
		wevent = awentename.get()

		args = (wid,wname,wevent)

		cursor = con.cursor()
		cursor.execute("CREATE TABLE if not exists winner ( wid int primary key ,wname varchar(20) ,wevent varchar(20))")
		sql = "insert into winner values('%d' , '%s' , '%s' )"
		cursor.execute(sql%args)
		con.commit()
		showinfo("Success" , "Winner added !")

		f29()

	except Exception as e:
		showerror("Mistake" , "Insert issue!" +str(e))
		con.rollback()
	finally :
		if con is not None :
			con.close()
			print("Disconnected")

def f25() : # trigger after insert
	

	con = None
	try :
		con = pymysql.connect("localhost","root","abc456","mypro")
		print("Connected")

	
		cursor = con.cursor()
		cursor.execute("drop trigger if exists t1")
		#cursor.execute("CREATE TABLE if not exists student_trigger ( id int ,name varchar(20) , college varchar(20),year enum('FE','SE','TE','BE'),event varchar(20))")

		sql = "create trigger t1 after insert on student for each row begin insert into student_trigger values(new.id , new.name , new.college , new.year , new.event);end"

		cursor.execute(sql)
		con.commit()
		showinfo("Success" , "Trigger added ! :)")

	except Exception as e:
		showerror("Mistake" , "Insert issue!" +str(e))
		con.rollback()
	finally :
		if con is not None :
			con.close()
			print("Disconnected")

def f26() : #trigger after update

	con = None
	try :
		con = pymysql.connect("localhost","root","abc456","mypro")
		print("Connected")

	
		cursor = con.cursor()
		cursor.execute("drop trigger if exists t2")
		#cursor.execute("create table  if not exists student_afupdate(id int  , name varchar(20) , college varchar(20) , year enum('FE' , 'SE' , 'TE' , 'BE') , event varchar(20))")

		sql = "create trigger t2 after update on student for each row begin insert into student_afupdate values(new.id , new.name , new.college , new.year , new.event);end"

		cursor.execute(sql)
		con.commit()
		showinfo("Success" , "Trigger added for after update! :)")

	except Exception as e:
		showerror("Mistake" , "Insert issue!" +str(e))
		con.rollback()
	finally :
		if con is not None :
			con.close()
			print("Disconnected")

def f27() : # trigger b4 delete

	con = None
	try :
		con = pymysql.connect("localhost","root","abc456","mypro")
		print("Connected")

	
		cursor = con.cursor()
		cursor.execute("drop trigger if exists t3")
		#cursor.execute("create table  if not exists student_b4delete(id int  , name varchar(20) , college varchar(20) , year enum('FE' , 'SE' , 'TE' , 'BE') , event varchar(20))")

		sql = "create trigger t3 before delete on student for each row begin insert into student_b4delete values(old.id , old.name , old.college , old.year , old.event);end"

		cursor.execute(sql)
		con.commit()
		showinfo("Success" , "Trigger added for before delete! :)")

	except Exception as e:
		showerror("Mistake" , "Insert issue!" +str(e))
		con.rollback()
	finally :
		if con is not None :
			con.close()
			print("Disconnected")

def f28() : #event on student	

	con = None
	try :
		con = pymysql.connect("localhost","root","abc456","mypro")
		print("Connected")

	
		cursor = con.cursor()
		cursor.execute("drop event if exists e1")
		#cursor.execute("create table if not exists student_bkup like student")

		sql = "create event e1 ON SCHEDULE every 5 second do begin delete from student_bkup ;insert into student_bkup select * from student ;end"

		cursor.execute(sql)
		con.commit()
		showinfo("Success" , "Event updated successfully! :)")

	except Exception as e:
		showerror("Mistake" , "Insert issue!" +str(e))
		con.rollback()
	finally :
		if con is not None :
			con.close()
			print("Disconnected")

def f29() : #event for winner

	con = None
	try :
		con = pymysql.connect("localhost","root","abc456","mypro")
		print("Connected")

	
		cursor = con.cursor()
		cursor.execute("drop event if exists e2")
		#cursor.execute("create table if not exists winner_bkup like winner")

		sql = "create event e2 ON SCHEDULE every 5 second do begin delete from winner_bkup ;insert into winner_bkup select * from winner ;end"

		cursor.execute(sql)
		con.commit()
		showinfo("Success" , "Event updated successfully! :)")

	except Exception as e:
		showerror("Mistake" , "Insert issue!" +str(e))
		con.rollback()
	finally :
		if con is not None :
			con.close()
			print("Disconnected")
	
		

	

















	










btnAdmin = Button(root, text = "Admin" , font = ("arial" , 20 , "bold" ,),fg = "Red" , width = 15,command = f1 , bg = "Green")
btnStudent = Button(root,text = "Participant" , font = ("arial" , 20 , "bold") , fg = "Orange" , width = 15,command = f3 , bg = "Blue")
btnStudent.pack(pady=15)
btnAdmin.pack(pady = 15)

#design of student window

sdst = Toplevel(root)
sdst.title("Participnt Registration")
sdst.geometry("700x700+450+40")
sdst.configure(background = "orange")
sdst.withdraw()



slblname = Label(sdst , text = "Name : " , font = ("arial",18 , "bold"))
sentname = Entry(sdst , bd = 5 , font = ("arial",18,"bold"))
slblname.place(x=20 , y = 100)
sentname.place(x = 170 , y = 100)

slblstudentid = Label(sdst , text = "Student Id :" , font = ("arial" ,18, "bold" ))
sentstudentid = Entry(sdst , bd = 5 , font = ("arial" , 18 , "bold"))
slblstudentid.place(x = 20 , y = 20)
sentstudentid.place(x = 170 , y = 20)

slblcollege = Label(sdst , text = "College : " , font = ("arial" , 18 , "bold"))
sentcollege = Entry(sdst , bd = 5 , font = ("arial" , 18 , "bold"))
slblcollege.place(x = 20 , y = 180)
sentcollege.place(x = 170 , y = 180)

slblyear = Label(sdst , text = "Year : " , font = ("arial" , 18 , "bold"))
sentyear =  Entry(sdst , bd = 5 , font = ("arial" , 18 , "bold"))
slblyear.place(x = 20 , y = 260)
sentyear.place(x = 170 , y = 260)

slblevent = Label(sdst , text = "Event : " , font = ("arial" , 18 , "bold"))
sentevent = Entry(sdst , bd = 5 , font = ("arial" , 18 , "bold"))
slblevent.place(x = 20 , y = 340)
sentevent.place(x = 170 , y = 340)

btnRegister = Button(sdst , text = "Register" , font = ("arial" , 18 , "bold") , width = 18 , command = f19)
btnRegister.place(x = 100 , y = 420)
btnBack = Button(sdst , text = "Back" , font = ("arial" , 18 , "bold") , width = 18,command = f4)
btnBack.place(x = 100 , y = 500)


#design of admin window

adst = Toplevel(root)
adst.title("Admin")
adst.geometry("900x700+450+20")
adst.configure(background = "Dark blue")
adst.withdraw()

btnAdd = Button(adst,text = "Add Participant" , font = ("calibri" , 18 , "bold") , width = 18 ,command = f5)
btnAdd.place(x = 40 , y = 20)
btnUpdate = Button(adst,text = "Update Participant" , font = ("calibri" , 18 , "bold") , width = 18 , command = f7 )
btnUpdate.place(x = 40 , y = 100)
btnDelete = Button(adst,text = "Delete Participant" , font = ("calibri" , 18 , "bold") , width = 18 , command = f9)
btnDelete.place(x = 40 , y = 180)
btnView = Button(adst,text = "View All Participants" , font = ("calibri" , 18 , "bold") , width = 18 , command = f11 )
btnView.place(x = 40 , y = 260)
btnAddEvent = Button(adst,text = "Add Event" , font = ("calibri" , 18 , "bold") , width = 18 , command = f13 )
btnAddEvent.place(x=40,y=340)
btnAddWinners = Button(adst,text = "Add Winners" , font = ("calibri" , 18 , "bold") , width = 18 , command = f15 )
btnAddWinners.place(x=40,y=420)
btnViewWinners = Button(adst,text = "View Winners" , font = ("calibri" , 18 , "bold") , width = 18 , command = f17 )
btnViewWinners.place(x=40,y=500)

btnBack = Button(adst,text = "Back" , font = ("calibri" , 18 , "bold") , width = 18 ,command = f2)
btnBack.place(x=500,y=260)

#design of add participant
ap = Toplevel(adst)
ap.title("Add Participant")
ap.geometry("900x700+450+20")
ap.configure(background = "Pink")
ap.withdraw()

aplblname = Label(ap , text = "Name : " , font = ("arial",18 , "bold"))
apentname = Entry(ap , bd = 5 , font = ("arial",18,"bold"))
aplblname.place(x=20 , y = 100)
apentname.place(x = 170 , y = 100)

aplblstudentid = Label(ap , text = "Student Id :" , font = ("arial" ,18, "bold" ))
apentstudentid = Entry(ap , bd = 5 , font = ("arial" , 18 , "bold"))
aplblstudentid.place(x = 20 , y = 20)
apentstudentid.place(x = 170 , y = 20)

aplblcollege = Label(ap , text = "College : " , font = ("arial" , 18 , "bold"))
apentcollege = Entry(ap , bd = 5 , font = ("arial" , 18 , "bold"))
aplblcollege.place(x = 20 , y = 180)
apentcollege.place(x = 170 , y = 180)

aplblyear = Label(ap , text = "Year : " , font = ("arial" , 18 , "bold"))
apentyear =  Entry(ap , bd = 5 , font = ("arial" , 18 , "bold"))
aplblyear.place(x = 20 , y = 260)
apentyear.place(x = 170 , y = 260)

aplblevent = Label(ap , text = "Event : " , font = ("arial" , 18 , "bold"))
apentevent = Entry(ap , bd = 5 , font = ("arial" , 18 , "bold"))
aplblevent.place(x = 20 , y = 340)
apentevent.place(x = 170 , y = 340)

btnRegister = Button(ap , text = "Register" , font = ("arial" , 18 , "bold") , width = 18 , command = f20 )
btnRegister.place(x = 100 , y = 420)
btnBack = Button(ap , text = "Back" , font = ("arial" , 18 , "bold") , width = 18,command = f6)
btnBack.place(x = 100 , y = 500)

#design of update participant
up = Toplevel(adst)
up.title("Update Participant")
up.geometry("900x700+450+20")
up.configure(background = "purple")
up.withdraw()

uplblstudentid = Label(up , text = "Student Id :" , font = ("arial" ,18, "bold" ))
upentstudentid = Entry(up , bd = 5 , font = ("arial" , 18 , "bold"))
uplblstudentid.place(x = 20 , y = 20)
upentstudentid.place(x = 170 , y = 20)

uplblname = Label(up , text = "Name : " , font = ("arial",18 , "bold"))
upentname = Entry(up , bd = 5 , font = ("arial",18,"bold"))
uplblname.place(x=20 , y = 100)
upentname.place(x = 170 , y = 100)

uplblcollege = Label(up , text = "College : " , font = ("arial" , 18 , "bold"))
upentcollege = Entry(up , bd = 5 , font = ("arial" , 18 , "bold"))
uplblcollege.place(x = 20 , y = 180)
upentcollege.place(x = 170 , y = 180)

uplblyear = Label(up , text = "Year : " , font = ("arial" , 18 , "bold") )
upentyear =  Entry(up , bd = 5 , font = ("arial" , 18 , "bold"))
uplblyear.place(x = 20 , y = 260)
upentyear.place(x = 170 , y = 260)

uplblevent = Label(up , text = "Event : " , font = ("arial" , 18 , "bold"))
upentevent = Entry(up , bd = 5 , font = ("arial" , 18 , "bold"))
uplblevent.place(x = 20 , y = 340)
upentevent.place(x = 170 , y = 340)

btnUpdate = Button(up , text = "Update" , font =  ("arial" , 18 , "bold") , width = 18 , command = f21)
btnUpdate.place(x = 100 , y = 420)
btnBack = Button(up , text = "Back" , font = ("arial" , 18 , "bold") , width = 18 , command = f8)
btnBack.place(x = 100 , y = 500)

#design of delete window
dp = Toplevel(adst)
dp.title("Delete Participant")
dp.geometry("500x400+400+200")
dp.configure(background = "Violet")
dp.withdraw()


dplblstudentid = Label(dp , text = "Student Id :" , font = ("arial" ,18, "bold" ))
dpentstudentid = Entry(dp , bd = 5 , font = ("arial" , 18 , "bold"))
dplblstudentid.place(x = 20 , y = 20)
dpentstudentid.place(x = 170 , y = 20)

btnDelete = Button(dp , text = "Delete" , font =  ("arial" , 18 , "bold") , width = 18 , command = f22)
btnDelete.place(x = 100 , y = 100)
btnBack = Button(dp , text = "Back" , font = ("arial" , 18 , "bold") , width = 18,command = f10 )
btnBack.place(x = 100 , y = 180)

#design of view participants
vp = Toplevel(adst)
vp.title("View All Participant")
vp.geometry("900x700+450+20")
vp.configure(background = "Yellow")
vp.withdraw()

vpdata = ScrolledText(vp , width = 70 , height = 30)
btnBack = Button(vp , text = "Back" , font = ("arial" , 18 , "bold") , width = 18 , command = f12 )
vpdata.pack(pady = 10)
btnBack.pack(pady = 10)

#design of add event
ae = Toplevel(adst)
ae.title("Add Event")
ae.geometry("800x600+450+100")
ae.configure(background = "Red")
ae.withdraw()

aelbleid = Label(ae , text = "Enter Event Id :" , font = ("arial" ,18, "bold" ))
aeenteid = Entry(ae , bd = 5 , font = ("arial" , 18 , "bold"))
aelbleid.place(x = 20 , y = 20)
aeenteid.place(x = 260 , y = 20)

aelblename = Label(ae , text = " Enter Event Name :" , font = ("arial" ,18, "bold" ))
aeentename = Entry(ae , bd = 5 , font = ("arial" , 18 , "bold"))
aelblename.place(x = 20 , y = 100)
aeentename.place(x = 260 , y = 100)

btnSave = Button(ae , text = "Save" , font =  ("arial" , 18 , "bold") , width = 18 , command = f23)
btnSave.place(x = 100 , y = 180)
btnBack = Button(ae , text = "Back" , font = ("arial" , 18 , "bold") , width = 18  , command = f14)
btnBack.place(x = 100 , y =260)

#design of add winner window
aw = Toplevel(adst)
aw.title("Add Winner")
aw.geometry("800x600+450+100")
aw.configure(background = "Green")
aw.withdraw()

awlblname = Label(aw , text = "Name : " , font = ("arial",18 , "bold"))
awentname = Entry(aw , bd = 5 , font = ("arial",18,"bold"))
awlblname.place(x=20 , y = 100)
awentname.place(x = 190 , y = 100)

awlblstudentid = Label(aw , text = "Student Id :" , font = ("arial" ,18, "bold" ))
awentstudentid = Entry(aw , bd = 5 , font = ("arial" , 18 , "bold"))
awlblstudentid.place(x = 20 , y = 20)
awentstudentid.place(x = 190 , y = 20)

awlblename = Label(aw , text = "Event Name:" , font = ("arial" ,18, "bold" ))
awentename = Entry(aw , bd = 5 , font = ("arial" , 18 , "bold"))
awlblename.place(x = 20 , y = 180)
awentename.place(x = 190 , y = 180)

btnSave = Button(aw , text = "Save" , font =  ("arial" , 18 , "bold") , width = 18,command = f24)
btnSave.place(x = 100 , y = 260)
btnBack = Button(aw , text = "Back" , font = ("arial" , 18 , "bold") , width = 18 , command = f16)
btnBack.place(x = 100 , y =340)

#design of view winners window
vw = Toplevel(adst)
vw.title("View All Participant")
vw.geometry("900x700+450+20")
vw.configure(background = "Orange")
vw.withdraw()

vwdata = ScrolledText(vw , width = 50 , height = 30 )
btnBack = Button(vw , text = "Back" , font = ("arial" , 18 , "bold") , width = 18  , command = f18)
vwdata.pack(pady = 10)
btnBack.pack(pady = 10)


























root.mainloop()