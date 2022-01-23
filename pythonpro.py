from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import pandas as pd
import matplotlib.pyplot as plt
import socket 
import requests
import bs4 

#design of root Window
root = Tk()
root.title("sms")
root.geometry("1200x700+20+20")
root.configure(background = "LIGHT GREEN")

def f1() :
	adst.deiconify()
	root.withdraw()
	aentrno.focus()
	
		
def f2() :
	root.deiconify()
	adst.withdraw() 
def f3() :
	stdata.delete(1.0 , END)
	
	vist.deiconify()
	root.withdraw() 

	con = None
	try:
		con = connect("student.db")
		print("Connected")

		cursor = con.cursor()
		sql = "Select * from stu"
		cursor.execute(sql)
		
		data = cursor.fetchall()
		
		info = " "
		for d in data :
			info  = info + " Roll no :"  + str(d[0]) + " Name :" + str(d[1]) + " Marks :" + str(d[2]) + "\n"
			
				
		stdata.insert(INSERT,info)
		
	except Exception as e:
		showerror("View Issue!" , str(e))

	finally:
		if con is not None :
			con.close()
			print("Disconnected")

def f4() :
	root.deiconify()
	vist.withdraw() 

def f5() :
	udst.deiconify()
	root.withdraw() 

def f6() :
	root.deiconify()
	udst.withdraw() 

def f7() :
	ddst.deiconify()
	root.withdraw() 

def f8() :
	root.deiconify()
	ddst.withdraw() 

def f9() :
	con = None
	try :
		con = connect("student.db")
		print("Connected")

		rno = int(aentrno.get())
		name = aentname.get()
		marks = int(aentmarks.get())
		args=(rno,name,marks)

		cursor = con.cursor()
		cursor.execute("CREATE TABLE if not exists stu (rno integer PRIMARY KEY , name text , marks real)")
		sql = "insert into stu values('%d' , '%s' , '%d')"
		cursor.execute(sql%args)

		if (rno < 0) or (len(str(rno)) == 0)  :
			showerror("Mistake!","Invalid Roll no !")
		
		elif (len(name) < 2) or (False == name.isalpha()) or (len(name) == 0):		
			showerror("Mistake","Invalid name !")
		elif (marks < 0 or marks > 100):
			showerror("Mistake","Invalid marks !");
		else :

			con.commit()
			showinfo("Success" , "Record added !")

		aentrno.delete(0,END)
		aentname.delete(0,END)
		aentmarks.delete(0,END)

		


		
		

	except Exception as e:
		showerror("Mistake" , "Insert issue!" +str(e))
		con.rollback()

	

	finally :
		if con is not None :
			con.close()
			print("Disconnected")

def f10() :
	
	con = None
	
	try :
		con = connect("student.db")
		print("Connected")
		
		rno = int(dentrno.get())
		args = (rno)
		cursor = con.cursor()

		sql = "delete from stu where rno = '%d'  "
		cursor.execute(sql % args)

		if cursor.rowcount >= 1:
			con.commit()
			showinfo("Success!","Record Deleted!")
			
		else :
			showerror("Delete Error" , "Roll No does not exists!")
		dentrno.delete(0 , END)

			

	except Exception as e :
		showerror("Delete issue!", str(e))
		con.rollback()
	finally :
		if con is not None :
			con.close()
			print("Disconnected")
				

def f11() :
	
	con = None
	try :
		con = connect("student.db")
		print("Connected")

		rno = int(uentrno.get())
		name = uentname.get()
		marks = int(uentmarks.get())
		args = (name,marks,rno)

		cursor = con.cursor()
		sql = "Update stu set name = '%s' , marks = '%d' where rno = '%d' "
		cursor.execute(sql % args)

		
		if (len(name) < 2) or (False == name.isalpha()) or (len(name) == 0):		
			showerror("Mistake","Invalid name !")
		elif (marks < 0 or marks > 100):
			showerror("Mistake","Invalid marks !")
		elif cursor.rowcount >=1 :
			con.commit()
			showinfo("Success !" ,"Record Updated Successfully!")
		else :
			showerror("Update Issue!" , "Record doesnt exists!")
		uentrno.delete(0,END)
		uentname.delete(0,END)
		uentmarks.delete(0,END)

	except Exception as e :
		showerror("Issue!" , str(e))
		con.rollback()

	finally :
		if con is not None :
			con.close()
			print("Disconnected")

def f12() :
	
	con = None 
	try :
		con = connect("student.db")
		print("Connected")

		cursor = con.cursor()
		sql =  "Select * from stu order by marks desc limit 5"
		cursor.execute(sql)
		
		data = cursor.fetchall()
		print(data)
		
		names = [ ]
		marks = [ ]
		for row in data :
			names.append(row[1])
			marks.append(row[2])
		plt.bar(names,marks,color = 'red',label = 'Marks of top 5 students')
		plt.title("Batch Information")
		plt.xlabel("NAMES")
		plt.ylabel("MARKS")
		plt.legend()
		plt.show()
		
		




	except Exception as e :
		showerror("Issue!",str(e))
		
	finally :
		if con is not None :
			con.close()
			print("Disconnected")


def f13() :
	try :
		socket.create_connection(("www.google.com" , 80))

		lblCity = Label(root, text = "City : Mumbai " , font = ("arial" , 18 , "bold"))
		lblCity.place(x = 20 , y = 320)

		
		city = 'Mumbai'
		
		a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
		a2 = "&q=" + city
		a3 = "&appid=c6e315d09197cec231495138183954bd"
		api_address = a1 + a2 + a3

		res = requests.get(api_address)
		#print(res)

		data = res.json()
		#print(data)
	
		#wpc to get temp
		tempdata = data['main']
		print(tempdata)
		temp = tempdata['temp']
		print("temperature = " , temp)

		#temp2 = data['main']['temp'] ; print("temp2 = ",temp2)

		lblTemplb = Label(root, text = "Temp : ", font = ("arial" , 18 , "bold"))
		lblTemplb.place(x = 20 , y = 400)

		
		lblTemp = Label(root, text = temp , font = ("arial" , 18 , "bold"))
		lblTemp.place(x = 100 , y = 400 )
		
		



	


	except OSError as e :
		print("issue" , e)
	

def f14() :
	
	res = requests.get("https://www.brainyquote.com/quote_of_the_day")
	#print(res)

	soup = bs4.BeautifulSoup(res.text , "lxml")
	#print(soup)

	data = soup.find("img" , {"class" : "p-qotd"})
	#print(data)

	text1 = data['alt']
	print(text1)

	
	lblqotd1 = Label(root, text = "Quote of the Day : " , font = ("arial" , 18 , "bold"))
	lblqotd1.place(x = 20 , y = 450)
	lblqotd = Label(root, text = text1 , font = ("arial" , 18 , "bold"))
	lblqotd.place(x = 20 , y = 500)

	

btnAdd = Button(root, text = "Add" , font = ("arial", 18 , "bold"),width = 10 , command = f1)
btnView = Button(root, text = "View" , font = ("arial", 18 , "bold"),width = 10 , command = f3 )
btnUpdate=Button(root,text = "Update" , font = ("arial",18 , "bold"),width = 10,command = f5)
btnDelete = Button(root,text = "Delete" , font = ("arial" , 18 , "bold"),width = 10,command = f7)
btnCharts = Button(root,text = "Charts" , font = ("arial" , 18 , "bold"),width = 10,command = f12)

btnAdd .pack(pady = 10)
btnView.pack(pady = 10)
btnUpdate.pack(pady = 10)
btnDelete.pack(pady = 10)
btnCharts.pack(pady = 10)

f13 ()
f14 ()

#design of Add Window

adst = Toplevel(root)
adst.title("Add Student.")
adst.geometry("500x400+400+200")
adst.withdraw()
adst.configure(background = "LIGHT BLUE")


alblrno = Label(adst, text = "Enter rno :" , font = ("arial" , 18 , "bold"))
aentrno = Entry(adst, bd = 5 , font = ("arial" , 18 , "bold"))

alblname = Label(adst, text = "Enter name :" , font = ("arial" , 18 , "bold"))
aentname = Entry(adst, bd = 5 , font = ("arial" , 18 , "bold"))

alblmarks = Label(adst, text = "Enter marks :" , font = ("arial" , 18 , "bold"))
aentmarks = Entry(adst, bd = 5 , font = ("arial" , 18 , "bold"))

abtnSave = Button(adst, text = "Save" , font = ("arial" , 18 , "bold"),command = f9)
abtnBack = Button(adst, text = "Back" , font = ("arial" , 18 , "bold"), command = f2 )

alblrno.pack(pady = 5)
aentrno.pack(pady = 5)
alblname.pack(pady = 5)
aentname.pack(pady = 5)
alblmarks.pack(pady = 5)
aentmarks.pack(pady = 5)
abtnSave.pack(pady = 5)
abtnBack.pack(pady = 5)


#design of view window

vist = Toplevel(root)
vist.title("View Student")
vist.geometry("900x700+400+200")
vist.withdraw()
vist.configure(background = "RED")
stdata = ScrolledText(vist, width=50 , height = 30)
vbtnvback = Button(vist , text = "Back", font = ("arial", 18 , "bold") , command = f4)

stdata.pack(pady=10)
vbtnvback.pack(pady = 10)


#design of udst window

udst = Toplevel(root)
udst.title("Update Student.")
udst.geometry("500x400+400+200")
udst.withdraw()
udst.configure(background = "LIGHT PINK")

ulblrno = Label(udst, text = "Enter rno :" , font = ("arial" , 18 , "bold"))
uentrno = Entry(udst, bd = 5 , font = ("arial" , 18 , "bold"))

ulblname = Label(udst, text = "Enter name :" , font = ("arial" , 18 , "bold"))
uentname = Entry(udst, bd = 5 , font = ("arial" , 18 , "bold"))

ulblmarks = Label(udst, text = "Enter marks :" , font = ("arial" , 18 , "bold"))
uentmarks = Entry(udst, bd = 5 , font = ("arial" , 18 , "bold"))

ubtnSave = Button(udst, text = "Save" , font = ("arial" , 18 , "bold"),command = f11 )
ubtnBack = Button(udst, text = "Back" , font = ("arial" , 18 , "bold"),command = f6 )

ulblrno.pack(pady = 5)
uentrno.pack(pady = 5)
ulblname.pack(pady = 5)
uentname.pack(pady = 5)
ulblmarks.pack(pady = 5)
uentmarks.pack(pady = 5)
ubtnSave.pack(pady = 5)
ubtnBack.pack(pady = 5)

#design of delete student 

ddst = Toplevel(root)
ddst.title("Delete Student")
ddst.geometry("500x400+400+200")
ddst.withdraw()
ddst.configure(background = "Yellow")

dlblrno = Label(ddst , text = "Enter rno :" , font = ("arial" , 18 , "bold"))
dentrno = Entry(ddst , bd = 7 , font = ("arial" , 18 , "bold"))
dentrno.focus()

dbtnSave = Button(ddst , text = "Save" , font = ("arial" , 18 , "bold"),command = f10)
dbtnBack = Button(ddst , text = "Back" , font = ("arial" , 18 , "bold"),command = f8)

dlblrno.pack(pady = 5)
dentrno.pack(pady = 5)
dbtnSave.pack(pady = 5)
dbtnBack.pack(pady = 5)












root.mainloop()