import mysql.connector
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from tkinter.messagebox import showinfo


def newHotelWindow():
    nhw = tk.Tk()
    nhw.title("Insert a new hotel")
    nhw.geometry('800x600')
    nhw.iconbitmap("./resources/db3.ico")

    nhw.columnconfigure(0, weight=1)
    nhw.columnconfigure(1, weight=3)

    c = 0
    r = 0

    # name
    name_label = ttk.Label(nhw, text="Hotel name:")
    name_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    name_entry = ttk.Entry(nhw)
    name_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # standard
    standard_label = ttk.Label(nhw, text="Hotel standard (stars):")
    standard_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    standard_entry = ttk.Entry(nhw)
    standard_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # address
    # country
    country_label = ttk.Label(nhw, text="Country:")
    country_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    country_entry = ttk.Entry(nhw)
    country_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # region
    region_label = ttk.Label(nhw, text="Region:")
    region_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    region_entry = ttk.Entry(nhw)
    region_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # city
    city_label = ttk.Label(nhw, text="City:")
    city_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    city_entry = ttk.Entry(nhw)
    city_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # postal_code
    postal_code_label = ttk.Label(nhw, text="Postal code (XX-XXX):")
    postal_code_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    postal_code_entry = ttk.Entry(nhw)
    postal_code_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # street
    street_label = ttk.Label(nhw, text="Street:")
    street_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    street_entry = ttk.Entry(nhw)
    street_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # building_no
    building_no_label = ttk.Label(nhw, text="Building number:")
    building_no_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    building_no_entry = ttk.Entry(nhw)
    building_no_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # concatenation
    # hotels_input = name.get() + ", " + standard.get()
    # address_input = country.get() + ", " + region.get() + ", " + city.get() + ", " + postal_code.get() + ", " + street.get() + ", " + building_no.get()

    # print(hotels_input)
    # print(address_input)

    add_button = ttk.Button(nhw, text="Add",
                            command=lambda: addHotel("'" + name_entry.get() + "', " + standard_entry.get(),
                                                     "'" + country_entry.get() + "', '" + region_entry.get() + "', '" + city_entry.get() + "', '" + postal_code_entry.get() + "', '" + street_entry.get() + "', '" + building_no_entry.get() + "'"))
    add_button.grid(column=1, row=r, sticky=tk.E, padx=5, pady=5)

    showWindow(nhw)


def newReservationWindow():
    nrw = tk.Tk()
    nrw.title("New reservation")
    nrw.geometry('800x600')
    nrw.iconbitmap("./resources/db3.ico")

    nrw.columnconfigure(0, weight=1)
    nrw.columnconfigure(1, weight=3)

    c = 0
    r = 0

    # name
    name_label = ttk.Label(nrw, text="Hotel name:")
    name_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    name_entry = ttk.Entry(nrw)
    name_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)

    r += 1
    c = 0

    # room_no
    room_no_label = ttk.Label(nrw, text="Room number:")
    room_no_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    room_no_entry = ttk.Entry(nrw)
    room_no_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # standard
    f_name_label = ttk.Label(nrw, text="Client first name")
    f_name_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    f_name_entry = ttk.Entry(nrw)
    f_name_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # country
    l_name_label = ttk.Label(nrw, text="Client last name:")
    l_name_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    l_name_entry = ttk.Entry(nrw)
    l_name_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # address
    # country
    country_label = ttk.Label(nrw, text="Client country:")
    country_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    country_entry = ttk.Entry(nrw)
    country_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # region
    region_label = ttk.Label(nrw, text="Client region:")
    region_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    region_entry = ttk.Entry(nrw)
    region_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # city
    city_label = ttk.Label(nrw, text="Client city:")
    city_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    city_entry = ttk.Entry(nrw)
    city_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # postal_code
    postal_code_label = ttk.Label(nrw, text="Client postal code (XX-XXX):")
    postal_code_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    postal_code_entry = ttk.Entry(nrw)
    postal_code_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # street
    street_label = ttk.Label(nrw, text="Client street:")
    street_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    street_entry = ttk.Entry(nrw)
    street_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # building_no
    building_no_label = ttk.Label(nrw, text="Client building number:")
    building_no_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    building_no_entry = ttk.Entry(nrw)
    building_no_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # apartment_no
    apartment_no_label = ttk.Label(nrw, text="Client apartment number:")
    apartment_no_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    apartment_no_entry = ttk.Entry(nrw)
    apartment_no_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    add_button = ttk.Button(nrw, text="Add",
                            command=lambda: addReservation(room_no_entry.get(),
                                                           "'" + country_entry.get() + "', '" + region_entry.get() + "', '" + city_entry.get() + "', '" + postal_code_entry.get() + "', '" + street_entry.get() + "', '" + building_no_entry.get() + "', '" + apartment_no_entry.get() + "'",
                                                           "'" + f_name_entry.get() + "', '" + l_name_entry.get() + "'",
                                                           "'" + name_entry.get() + "'"))
    add_button.grid(column=1, row=r, sticky=tk.E, padx=5, pady=5)

    showWindow(nrw)


def newClientWindow():
    ncw = tk.Tk()
    ncw.title("New client")
    ncw.geometry('800x600')
    ncw.iconbitmap("./resources/db3.ico")

    ncw.columnconfigure(0, weight=1)
    ncw.columnconfigure(1, weight=3)

    c = 0
    r = 0

    f_name_label = ttk.Label(ncw, text="First name:")
    f_name_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    f_name_entry = ttk.Entry(ncw)
    f_name_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    l_name_label = ttk.Label(ncw, text="Last name:")
    l_name_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    l_name_entry = ttk.Entry(ncw)
    l_name_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # address
    # country
    country_label = ttk.Label(ncw, text="Country:")
    country_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    country_entry = ttk.Entry(ncw)
    country_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # region
    region_label = ttk.Label(ncw, text="Region:")
    region_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    region_entry = ttk.Entry(ncw)
    region_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # city
    city_label = ttk.Label(ncw, text="City:")
    city_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    city_entry = ttk.Entry(ncw)
    city_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # postal_code
    postal_code_label = ttk.Label(ncw, text="Postal code (XX-XXX):")
    postal_code_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    postal_code_entry = ttk.Entry(ncw)
    postal_code_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # street
    street_label = ttk.Label(ncw, text="Street:")
    street_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    street_entry = ttk.Entry(ncw)
    street_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # building_no
    building_no_label = ttk.Label(ncw, text="Building number:")
    building_no_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    building_no_entry = ttk.Entry(ncw)
    building_no_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # apartment_no
    apartment_no_label = ttk.Label(ncw, text="Apartment number:")
    apartment_no_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    apartment_no_entry = ttk.Entry(ncw)
    apartment_no_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    add_button = ttk.Button(ncw, text="Add",
                            command=lambda: addClient("'" + f_name_entry.get() + "', " + l_name_entry.get(),
                                                      "'" + country_entry.get() + "', '" + region_entry.get() + "', '" + city_entry.get() + "', '" + postal_code_entry.get() + "', '" + street_entry.get() + "', '" + building_no_entry.get() + "', '" + apartment_no_entry.get() + "'"))
    add_button.grid(column=1, row=r, sticky=tk.E, padx=5, pady=5)

    showWindow(ncw)


def newEmployeeWindow():
    new = tk.Tk()
    new.title("New employee")
    new.geometry('800x600')
    new.iconbitmap("./resources/db3.ico")

    new.columnconfigure(0, weight=1)
    new.columnconfigure(1, weight=3)

    c = 0
    r = 0

    f_name_label = ttk.Label(new, text="First name:")
    f_name_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    f_name_entry = ttk.Entry(new)
    f_name_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    l_name_label = ttk.Label(new, text="Last name:")
    l_name_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    l_name_entry = ttk.Entry(new)
    l_name_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    hotel_id_label = ttk.Label(new, text="Hotel ID:")
    hotel_id_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    hotel_id_entry = ttk.Entry(new)
    hotel_id_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    salary_label = ttk.Label(new, text="Salary:")
    salary_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    salary_entry = ttk.Entry(new)
    salary_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # address
    # country
    country_label = ttk.Label(new, text="Country:")
    country_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    country_entry = ttk.Entry(new)
    country_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # region
    region_label = ttk.Label(new, text="Region:")
    region_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    region_entry = ttk.Entry(new)
    region_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # city
    city_label = ttk.Label(new, text="City:")
    city_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    city_entry = ttk.Entry(new)
    city_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # postal_code
    postal_code_label = ttk.Label(new, text="Postal code (XX-XXX):")
    postal_code_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    postal_code_entry = ttk.Entry(new)
    postal_code_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # street
    street_label = ttk.Label(new, text="Street:")
    street_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    street_entry = ttk.Entry(new)
    street_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # building_no
    building_no_label = ttk.Label(new, text="Building number:")
    building_no_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    building_no_entry = ttk.Entry(new)
    building_no_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    # apartment_no
    apartment_no_label = ttk.Label(new, text="Apartment number:")
    apartment_no_label.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    c += 1
    apartment_no_entry = ttk.Entry(new)
    apartment_no_entry.grid(column=c, row=r, sticky=tk.EW, padx=5, pady=5)
    r += 1
    c = 0

    add_button = ttk.Button(new, text="Add",
                            command=lambda: addEmployee(
                                "'" + f_name_entry.get() + "', '" + l_name_entry.get() + ", " + salary_entry.get() + ", '" + hotel_id_entry.get() + "'",
                                "'" + country_entry.get() + "', '" + region_entry.get() + "', '" + city_entry.get() + "', '" + postal_code_entry.get() + "', '" + street_entry.get() + "', '" + building_no_entry.get() + "', '" + apartment_no_entry.get() + "'"))
    add_button.grid(column=1, row=r, sticky=tk.E, padx=5, pady=5)

    showWindow(new)


def newGoodWindow():
    pass


def newRoomWindow():
    pass


def viewerWindow():
    vw = tk.Tk()
    vw.title("Data viewer")
    vw.geometry('800x600')
    vw.resizable(False, False)
    vw.iconbitmap("./resources/db3.ico")

    # TODO add entry

    button = ttk.Button(vw, text="Show all rows from Hotels table", command=lambda: showAll(vw, "hotels"),
                        style="my.TButton")
    button.grid(column=0, row=0, padx=5, pady=5)

    showWindow(vw)


def addHotel(hotel_values, addresses_values):
    mycursor = mydb.cursor()
    mycursor.execute(
        f"INSERT INTO addresses (country, region, city, postal_code, street, building_no) VALUES ({addresses_values})")
    mycursor.execute(f"SELECT address_id from addresses where address_id = (select max(address_id) from addresses);")
    address_id = mycursor.fetchone()

    mycursor.execute(f"INSERT INTO hotels (name, standard, address_id) VALUES ({hotel_values}, {address_id[0]})")
    mydb.commit()
    print(f"Succesfully added a new hotel!")


def addClient(client_values, addresses_values):
    mycursor = mydb.cursor()
    mycursor.execute(
        f"INSERT INTO addresses (country, region, city, postal_code, street, building_no, apartment_no) VALUES ({addresses_values})")
    mycursor.execute(f"SELECT address_id from addresses where address_id = (select max(address_id) from addresses);")
    address_id = mycursor.fetchone()

    mycursor.execute(
        f"INSERT INTO clients (first_name, last_name, address_id) VALUES ({client_values}, {address_id[0]})")
    mydb.commit()
    print(f"Succesfully added a new client!")


def addAddress(addresses_values):
    mycursor = mydb.cursor()
    mycursor.execute(
        f"INSERT INTO addresses (country, region, city, postal_code, street, building_no, apartment_no) VALUES ({addresses_values})")
    mydb.commit()
    print(f"Succesfully added a new address!")


def addEmployee(employee_values, addresses_values):
    mycursor = mydb.cursor()
    mycursor.execute(
        f"INSERT INTO addresses (country, region, city, postal_code, street, building_no, apartment_no) VALUES ({addresses_values})")
    mycursor.execute(f"SELECT address_id from addresses where address_id = (select max(address_id) from addresses);")
    address_id = mycursor.fetchone()

    mycursor.execute(
        f"INSERT INTO employees (first_name, last_name, hotel_id, salary, address_id) VALUES ({employee_values}, {address_id[0]})")
    mydb.commit()
    print(f"Succesfully added a new employee!")


def addReservation(room_no, addresses_values, client_values, hotel_name):  # TODO
    mycursor = mydb.cursor()
    mycursor.execute(
        f"INSERT INTO addresses (country, region, city, postal_code, street, building_no, apartment_no) VALUES ({addresses_values})")

    mycursor.execute(f"select max(address_id) from addresses;")
    address_id = mycursor.fetchone()[0]

    mycursor.execute(
        f"INSERT INTO clients (first_name, last_name, address_id) VALUES ({client_values}, {address_id})")
    mycursor.execute(f"select max(client_id) from clients")
    client_id = mycursor.fetchone()[0]

    mycursor.execute(f"select hotel_id from hotels where name = {hotel_name}")
    hotel_id = mycursor.fetchone()[0]

    mycursor.execute(
        f"INSERT INTO reservations (hotel_id, client_id, room_no) VALUES ({hotel_id}, {client_id}, {room_no})")
    mydb.commit()
    print(f"Succesfully added a new reservation!")


def addGood():  # TODO
    print(f"Succesfully added a new good!")


def deleteHotelWindow():
    pass


def deleteReservationWindow():
    pass


def deleteClientWindow():
    pass


def deleteEmployeeWindow():
    pass


def deleteGoodWindow():
    pass


def deleteRoomWindow():
    pass


def createTable(name, columns):
    mycursor = mydb.cursor()
    mycursor.execute(f"CREATE TABLE {name} ({columns})")
    mydb.commit()
    print(f"Succesfully created table {name}")


def showAll(window, table):
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM {table}")
    column = 1
    row = 0
    for x in mycursor:
        ttk.Label(window, text=x).grid(column=column, row=row)
        row += 1


def searchFor(columns, table, column, value):
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT {columns} FROM {table} WHERE {column} = {value}")


def showWindow(root):
    try:
        from ctypes import windll

        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        root.mainloop()  # last line


def styleWindow(window):
    s = ttk.Style(window)
    s.configure("my.TButton", font=('Helvetica', 12))


def main():
    # ****** GUI ******

    # root window
    root = tk.Tk()
    root.title("Hotels")
    root.geometry('800x600')
    root.resizable(False, False)
    root.iconbitmap("./resources/db3.ico")

    styleWindow(root)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    # root.rowconfigure(1, weight=1)

    myFont = font.Font(size=16, weight="bold")
    myFont2 = font.Font(size=14)
    welcome_text = ttk.Label(root, text="Welcome to Hotels database management app!")
    welcome_text['font'] = myFont
    welcome_text.grid(column=0, row=0, columnspan=3, padx=5, pady=20)

    section_text1 = ttk.Label(root, text="Inserting data:")
    section_text1['font'] = myFont2
    section_text1.grid(column=0, row=1, padx=10, pady=10)

    section_text2 = ttk.Label(root, text="Viewing data:")
    section_text2['font'] = myFont2
    section_text2.grid(column=1, row=1, padx=10, pady=10)

    section_text3 = ttk.Label(root, text="Deleting data:")
    section_text3['font'] = myFont2
    section_text3.grid(column=2, row=1, padx=10, pady=10)

    r = 2
    c = 0

    button = ttk.Button(root, text="Add a new hotel", width=20, command=newHotelWindow, style="my.TButton")
    button.grid(column=c, row=r, padx=5, pady=5)
    r += 1
    button = ttk.Button(root, text="Add a new reservation", width=20, command=newReservationWindow, style="my.TButton")
    button.grid(column=c, row=r, padx=5, pady=5)
    r += 1
    button = ttk.Button(root, text="Add a new client", width=20, command=newClientWindow, style="my.TButton")
    button.grid(column=c, row=r, padx=5, pady=5)
    r += 1
    button = ttk.Button(root, text="Add a new employee", width=20, command=newEmployeeWindow, style="my.TButton")
    button.grid(column=c, row=r, padx=5, pady=5)
    r += 1
    button = ttk.Button(root, text="Add a new good", width=20, command=newGoodWindow, style="my.TButton")
    button.grid(column=c, row=r, padx=5, pady=5)
    r += 1
    button = ttk.Button(root, text="Add a new room", width=20, command=newRoomWindow, style="my.TButton")
    button.grid(column=c, row=r, padx=5, pady=5)

    c += 1
    r = 2

    button = ttk.Button(root, text="Open data viewer", width=20, command=viewerWindow, style="my.TButton")
    button.grid(column=c, row=r, padx=5, pady=5)

    c += 1
    r = 2

    button = ttk.Button(root, text="Delete a hotel", width=20, command=deleteHotelWindow, style="my.TButton")
    button.grid(column=c, row=r, padx=5, pady=5)
    r += 1
    button = ttk.Button(root, text="Delete a reservation", width=20, command=deleteReservationWindow,
                        style="my.TButton")
    button.grid(column=c, row=r, padx=5, pady=5)
    r += 1
    button = ttk.Button(root, text="Delete a client", width=20, command=deleteClientWindow, style="my.TButton")
    button.grid(column=c, row=r, padx=5, pady=5)
    r += 1
    button = ttk.Button(root, text="Delete a employee", width=20, command=deleteEmployeeWindow, style="my.TButton")
    button.grid(column=c, row=r, padx=5, pady=5)
    r += 1
    button = ttk.Button(root, text="Delete a good", width=20, command=deleteGoodWindow, style="my.TButton")
    button.grid(column=c, row=r, padx=5, pady=5)
    r += 1
    button = ttk.Button(root, text="Delete a room", width=20, command=deleteRoomWindow, style="my.TButton")
    button.grid(column=c, row=r, padx=5, pady=5)
    r += 1

    showWindow(root)


if __name__ == "__main__":
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admIn4819864",
        database="hotels"
    )
    main()
