import tkinter as tk
from tkinter import ttk

win_1 = tk.Tk()
win_1.geometry("500x400+0+0")
win_1.title("Login")

lb_login= tk.Label(win_1, text= "Please enter Email and Password to login",
font=("Arial", 13), border=7)
lb_login.pack(side=tk.TOP)

def show_password():
	if en_pass.cget('show')=="*":
		en_pass.config(show="")
	else:
		en_pass.config(show="*")
lb_user= tk.Label(win_1, text= "Username",font=("Arial", 13), border=7)
lb_user.pack()
en_user=tk.Entry(win_1, bd =3,font=("Arial", 17))
en_user.pack()
lb_pass= tk.Label(win_1, text= "Password",font=("Arial", 13), border=7)
lb_pass.pack()
en_pass=tk.Entry(win_1, bd =3,font=("Arial", 17),show="*")
en_pass.pack()
btn_show_pass = tk.Checkbutton(win_1, text="Show password",command=show_password)
btn_show_pass.pack()

btn_login = tk.Button(win_1, text = "Login", bd = 7, font=("Arial", 13), width=17)
btn_login.pack()




username = "phu97"
password = "khongkhong123"
def check_login(event):
	input_username = en_user.get()
	input_password = en_pass.get()
	if input_username == None or input_username.strip() =="":
		lb_login.config(text="You entered missing information")
	elif input_username==username and input_password==password:
		lb_login.config(text="OK")
		win = tk.Tk()
		win.geometry("1500x700+0+0")
		win.title("Apartment Management")

		data = []
		# def add_client(event):
		#     with open("myfile.csv","w",newline="") as file:
		#         wt=csv.writer(file,delimiter=',')
		#         room_csv=room.get()
		#         name_csv=name.get()
		#         client_csv=client_number.get()
		#         phone_csv=phone.get()
		#         water_csv=water_meter.get()
		#         electric_csv=electric_meter.get()
		#         room_rate_csv=room_rates.get()
		#         internet_csv=internet_fee.get()
		        
		#         wt.writerow(["Room", "Name", "Client number", "Phone","Water meter", "Electric meter", "Room rates", "Internet fee"])
		#         wt.writerow([room_csv,name_csv,client_csv,phone_csv,water_csv,electric_csv,room_rate_csv,internet_csv])
		#         print("Record has been inserted!")
		#     file.close()

		global count
		count =0
		# Create striped row tags


		for record in data:
		    data_table.insert(parent='', index='end',iid=count,text="",value=(room_entry.get(),name_entry.get(),client_num_entry.get(),phone_entry.get(),water_meter_entry.get(),electric_meter_entry.get(),room_rates_entry.get(),internet_fee_entry.get(),tot_pay))
		    count+=1
		def clear_box():
		    room_entry.delete(0, tk.END)
		    name_entry.delete(0, tk.END)
		    client_num_entry.delete(0, tk.END)
		    phone_entry.delete(0, tk.END)
		    water_meter_entry.delete(0, tk.END)
		    electric_meter_entry.delete(0, tk.END)
		    room_rates_entry.delete(0, tk.END)
		    internet_fee_entry.delete(0, tk.END)
		def Total_paying():
		    tot_paying = int(room_rates_entry.get()) + int(water_meter_entry.get())*5000 + int(electric_meter_entry.get())*3000 + int(internet_fee_entry.get())*int(client_num_entry.get())
		    return tot_paying
		def add_client():
		    global count
		    tot_pay = Total_paying()
		    data_table.insert(parent='', index='end',iid=count,text="",value=(room_entry.get(),name_entry.get(),client_num_entry.get(),phone_entry.get(),water_meter_entry.get(),electric_meter_entry.get(),room_rates_entry.get(),internet_fee_entry.get(),tot_pay))
		    count+=1

		# clear boxes
		    clear_box()



		title_label = tk.Label(win, text= "Apartment Management",
		font=("Arial", 25), border=12, relief= tk.GROOVE)
		title_label.pack(side=tk.TOP,fill= tk.X)

		detail_frame = tk.LabelFrame(win, text= "Enter Detail",
		font=("Arial", 25), border=12, relief= tk.GROOVE)
		detail_frame.place(relx = 0.01, rely= 0.53, relwidth=0.3, relheight=0.85, anchor = "w")

		data_frame = tk.LabelFrame(win, text= "Data",
		font=("Arial", 25), border=12, relief= tk.GROOVE)
		data_frame.place(relx = 0.35, rely= 0.53, relwidth=0.63, relheight=0.85, anchor = "w")


		def update_client():
		    # Grab record number
		    selected = data_table.focus()
		    # Save new data
		    tot_pay = Total_paying()
		    data_table.item(selected, text="", values=(room_entry.get(),name_entry.get(),client_num_entry.get(),phone_entry.get(),water_meter_entry.get(),electric_meter_entry.get(),room_rates_entry.get(),internet_fee_entry.get(),tot_pay))
		    clear_box()
		    print("update")
		def delete_client():
		    x = data_table.selection()[0]
		    data_table.delete(x)
		    clear_box()
		    print("delete")
		def clear_client():
		    for record in data_table.get_children():
		        data_table.delete(record)
		    clear_box()
		    print("Clear")

		def select_record():
		    # Clear entry boxes
		    clear_box()

		    # Grab record number
		    selected = data_table.focus()
		    # Grab record values
		    values = data_table.item(selected, 'values')

		    #temp_label.config(text=values[0])

		    # output to entry boxes
		    room_entry.insert(0, values[0])
		    name_entry.insert(0, values[1])
		    client_num_entry.insert(0, values[2])
		    phone_entry.insert(0, values[3])
		    water_meter_entry.insert(0, values[4])
		    electric_meter_entry.insert(0, values[5])
		    room_rates_entry.insert(0, values[6])
		    internet_fee_entry.insert(0, values[7])


		def search_client():
		    print("search")
		def showall_client():
		    print("show all")       


		# Variables
		# room = tk.StringVar()
		# name = tk.StringVar()
		# client_number = tk.StringVar()
		# phone = tk.StringVar()
		# water_meter = tk.StringVar()
		# electric_meter = tk.StringVar()
		# room_rates = tk.StringVar()
		# internet_fee = tk.StringVar()

		# search_by = tk.StringVar()

		# Into detail frame
		room_label = tk.Label(detail_frame, text= "Room",font=("Arial", 17),)
		room_label.grid(column = 0, row= 0 ,padx=2, pady=2)
		room_entry = tk.Entry(detail_frame, bd =3,font=("Arial", 17))
		room_entry.grid(column = 1, row= 0,sticky=tk.E,padx=2, pady=2)

		name_label = tk.Label(detail_frame, text= "Name",font=("Arial", 17))
		name_label.grid(column = 0, row= 2 ,padx=2, pady=2)
		name_entry = tk.Entry(detail_frame, bd =3,font=("Arial", 17))
		name_entry.grid(column = 1, row= 2,sticky=tk.E,padx=2, pady=2)

		client_num_label = tk.Label(detail_frame, text= "Client number",font=("Arial", 17))
		client_num_label.grid(column = 0, row= 3 ,padx=2, pady=2)
		client_num_entry = tk.Entry(detail_frame, bd =3,font=("Arial", 17))
		client_num_entry.grid(column = 1, row= 3,sticky=tk.E,padx=2, pady=2)

		phone_label = tk.Label(detail_frame, text= "Phone",font=("Arial", 17))
		phone_label.grid(column = 0, row= 4 ,padx=2, pady=2)
		phone_entry = tk.Entry(detail_frame, bd =3,font=("Arial", 17))
		phone_entry.grid(column = 1, row= 4,sticky=tk.E,padx=2, pady=2)

		water_meter_label = tk.Label(detail_frame, text= "Water meter",font=("Arial", 17))
		water_meter_label.grid(column = 0, row= 5 ,padx=2, pady=2)
		water_meter_entry = tk.Entry(detail_frame, bd =3,font=("Arial", 17))
		water_meter_entry.grid(column = 1, row= 5,sticky=tk.E,padx=2, pady=2)

		electric_meter_label = tk.Label(detail_frame, text= "Electric meter",font=("Arial", 17))
		electric_meter_label.grid(column = 0, row= 6 ,padx=2, pady=2)
		electric_meter_entry = tk.Entry(detail_frame, bd =3,font=("Arial", 17))
		electric_meter_entry.grid(column = 1, row= 6,sticky=tk.E,padx=2, pady=2)

		room_rates_label = tk.Label(detail_frame, text= "Room rates",font=("Arial", 17))
		room_rates_label.grid(column = 0, row= 7 ,padx=2, pady=2)
		room_rates_entry = tk.Entry(detail_frame, bd =3,font=("Arial", 17))
		room_rates_entry.grid(column = 1, row= 7,sticky=tk.E,padx=2, pady=2)

		internet_fee_label = tk.Label(detail_frame, text= "Internet fee",font=("Arial", 17))
		internet_fee_label.grid(column = 0, row= 8 ,padx=2, pady=2)
		internet_fee_entry = tk.Entry(detail_frame, bd =3,font=("Arial", 17))
		internet_fee_entry.grid(column = 1, row= 8,sticky=tk.E,padx=2, pady=2)

		# buttons
		btn_frame = tk.Frame(detail_frame, bd= 10, relief= tk.GROOVE)
		btn_frame.place(relx = 0.05, rely= 0.8, relwidth=0.9, relheight=0.23, anchor = "w")

		add_btn = tk.Button(btn_frame, text = "Add", bd = 7, font=("Arial", 13), width=17, command=add_client)
		add_btn.grid(column = 0, row= 1 ,padx=2, pady=2)
		update_btn = tk.Button(btn_frame, text = "Update", bd = 7, font=("Arial", 13), width=17,command=update_client)
		update_btn.grid(column = 1, row= 1 ,padx=2, pady=2)
		delete_btn = tk.Button(btn_frame, text = "Delete", bd = 7, font=("Arial", 13), width=17,command=delete_client)
		delete_btn.grid(column = 0, row= 2 ,padx=2, pady=2)
		clear_btn = tk.Button(btn_frame, text = "Clear", bd = 7, font=("Arial", 13), width=17,command=clear_client)
		clear_btn.grid(column = 1, row=2 ,padx=2, pady=2)

		# search
		search_frame = tk.Frame(data_frame, bd=10, relief=tk.GROOVE)
		search_frame.pack(side=tk.TOP, fill= tk.X)

		search_label = tk.Label(search_frame, text = "Search", font=("Arial", 14))
		search_label.grid(column = 0, row= 0 ,padx=12, pady=2)

		search_in = ttk.Combobox(search_frame, font=("Arial", 14), state = "readonly")
		search_in["values"] = ("Name", "Room", "Client number", "Phone" )
		search_in.grid(column = 1, row=0 ,padx=12, pady=2)

		search_btn = tk.Button(search_frame, text = "Search", bd = 9, font=("Arial", 13), width=17,command=search_client)
		search_btn.grid(column = 2, row= 0 ,padx=12, pady=2)

		showall_btn = tk.Button(search_frame, text = "Show all", bd = 9, font=("Arial", 13), width=17,command=showall_client)
		showall_btn.grid(column = 3, row= 0 ,padx=12, pady=2)

		#data frame
		# main_frame = tk.Frame(data_frame, bd=11, relief = tk.GROOVE)
		# main_frame.pack(fill=tk.BOTH, expand = True)

		y_scroll = tk.Scrollbar(data_frame, orient= tk.VERTICAL)
		x_scroll = tk.Scrollbar(data_frame, orient= tk.HORIZONTAL)

		data_table = ttk.Treeview(data_frame, columns=("Room", "Name", "Client number", "Phone","Water meter", "Electric meter", "Room rates", "Internet fee","Total paying"),
		    yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set, show="headings")

		y_scroll.config(command = data_table.yview)
		x_scroll.config(command = data_table.xview)

		y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
		x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

		data_table.heading("Room",text="Room")
		data_table.heading("Name",text="Name")
		data_table.heading("Client number",text="Client number")
		data_table.heading("Phone",text="Phone")
		data_table.heading("Water meter",text="Water meter")
		data_table.heading("Electric meter",text="Electric meter")
		data_table.heading("Room rates",text="Room rates")
		data_table.heading("Internet fee",text="Internet fee")  
		data_table.heading("Total paying",text="Total paying")  

		data_table.column("Room",width="50")
		data_table.column("Name",width="150")
		data_table.column("Client number",width="100")
		data_table.column("Phone",width="100")
		data_table.column("Water meter",width="100")
		data_table.column("Electric meter",width="100")
		data_table.column("Room rates",width="100")
		data_table.column("Internet fee",width="100")
		data_table.column("Total paying",width="100")

		data_table.pack(fill= tk.BOTH, expand= True)

		data_table.insert(parent='',index='end',text='00001')

		def clicker(e):
		    select_record()
		# Bindings
		#my_tree.bind("<Double-1>", clicker)
		data_table.bind("<ButtonRelease-1>", clicker)

		win.mainloop()
	else:
		lb_login.config(text="you entered wrong")

btn_login.bind("<Button-1>", check_login)
win_1.mainloop()