#importing modules
from tkinter import *
import sqlite3
import time
import datetime
import matplotlib
import os
from os import chdir, close, error, system
from pathlib import Path
import platform
import tkinter.font as tkfont
import urllib.request
from matplotlib.pyplot import autoscale, text
import webbrowser
from PIL import Image, ImageColor

print('program started')

#main start program function
def initialise():
    definingDefaultVariables()
    findOS()
    if path_seperator != None: #basically if the device is running on an accepted OS
        if fileCreation() == 'Correct Files Created':
            convertAssetColor(primary,secondry)
            ### This allows me to access specific pages without having to go via the terms and conditions -> login -> menu etc
            #loginPage()
            ###
            displayTCs()

#setting up key bindings for quickly exciting the program (mainly useful for developing)
def escapeProgram(event):
    root.destroy()

def invalidOSRunning():
    InvalidOSRoot = Tk()
    InvalidOSRoot.title('Property managment system')
    InvalidOSRoot.geometry('500x500')
    InvalidOSRoot.resizable(width=False, height=False)
    InvalidOSRoot.configure(background=primary)
    IVOSTitle = Label(InvalidOSRoot, font=(font,'20','underline'), text='Operating System not supported', justify='center', width='71', bg=primary,fg=secondry).place(relx=0.5, rely=0.1, anchor=CENTER)
    IVOOperatingSystem = Label(InvalidOSRoot, font=(font,'12'), text='We have detected your device is running an unsupported\noperating system. '+platform.system()+' operating system is not supported\nby this software', justify='center', width='71', bg=primary,fg=secondry).place(relx=0.5, rely=0.5, anchor=CENTER)    
    IVOSMainMessage = Label(InvalidOSRoot, font=(font,'12'), text='Sorry, but only Windows and MAC OS operating\nsystems are supported by this software', justify='center', width='71', bg=primary,fg=secondry).place(relx=0.5, rely=0.8, anchor=CENTER)
    IVOSEmail = Label(InvalidOSRoot, font=(font,'12'), text='For more information please email\nmburton22@norwich-school.org.uk', justify='center', width='71', bg=primary,fg=secondry).place(relx=0.5, rely=0.9, anchor=CENTER)
    InvalidOSRoot.mainloop()
 
#defining certain default variables
def definingDefaultVariables():
    global primary, secondry, tertiary, bannedColours, font, listOfIdealTables, databaseName, listOfIdealAssests, listOfIdealAssestsMutable ,connectionError
    primary = '#373f51'
    secondry = '#ffffff'
    tertiary = '#a9a9a9'
    bannedColours = {'errorRed':'#','warningYellow':'#','activeTextColor':'dark grey'}
    font = 'Bahnschrift SemiLight'
    listOfIdealTables = ['Accounts', 'Complaints', 'Loan_table', 'Refinance', 'Sold_Units', "Tenant's_Entity", "Unit's_Monthly", 'Units']
    databaseName = 'Property Managment System Database.db'
    listOfIdealAssests = ['Long-Fat.PNG','Long-Normal.PNG','Long-Skinny.PNG','Short-Fat.PNG','Short-Normal.PNG','House.ico']
    connectionError = Tk()
    connectionError.destroy()

#intialising page
def initialiseWindow():
    closeMainPage()
    global root
    root = Tk()
    root.title('Property managment system')
    root.geometry('1250x850')
    root.configure(background=primary)
    root.resizable(width=False, height=False) #Makes the window not be reziable becuase that mucks up the asthetics
    chdir(f'.{path_seperator}Assests')
    root.iconbitmap("House.ico")
    root.bind("`", escapeProgram)

#Finding out what OS the device runs on and setting the path seperator approrialtly
def findOS():
    if platform.system() == 'Windows': #Windows (for me to develope the program)
        global path_seperator
        path_seperator = '\\'
    elif platform.system() == 'Darwin': #MAC OS (for my end user to run the program)
        path_seperator = '/'
    else:
        path_seperator = None
        invalidOSRunning()

def fileCreation():
    createFolder('Assests')
    configureDatabase()
    if addAssests() == 'Correct Assests Obtained':
        return 'Correct Files Created'
    else:
        return 'Incorrect Files Created'
    
def createFolder(folderName):
    listOfFilesInDirectory = os.listdir(os.getcwd())
    if str(folderName) not in listOfFilesInDirectory:
        os.makedirs(folderName)

def createFile(fileName):
    listOfFilesInDirectory = os.listdir(os.getcwd())
    if fileName not in listOfFilesInDirectory:
        f = open(fileName,'w')
        f.close()

def addAssests():
    chdir(f'.{path_seperator}Assests')
    listOfAssets = os.listdir(os.getcwd())
    i = 0
    while i in range(len(listOfIdealAssests)):
        asset = listOfIdealAssests[i]
        if asset not in listOfAssets:
            try:
                urllib.request.urlretrieve(f"https://emuxmatt.github.io/NEA/{asset}",f'{asset}')
            except OSError: #if there is a connection error
                if connectionError.state != 'normal':
                    i = len(listOfIdealAssests) + 1 #to exit while loop so as not to try and get more assests resulting in 
                    #loads of connection error's being displayed
                    displayConnectionError()
        i = i + 1

    #sorting list
    listOfIdealAssestsSorted = (listOfIdealAssests).sort()
    listOfObtainedAssestsSorted =  ((os.listdir(os.getcwd())).sort())
    chdir('..')

    if listOfObtainedAssestsSorted == listOfIdealAssestsSorted:
        return 'Correct Assests Obtained'
    else:
        print('Correct Assests Not Obtained')
        return 'Correct Assests Not Obtained'

def configureDatabase():
    createFile(databaseName)
    if checkTableExsistance() == False: #Deletes all tables if the all tables dont exsist - this is to uphold referentail integrity and becasue it is easier to add all tables again instead of working out which ones are gone and trying to restich the database together
        openDatabase()
        for table in listOfTables:
            cursor.execute('DROP TABLE ' + table)
        closeDatabase()
    createTables()

def displayConnectionError():
    global connectionError
    connectionError = Tk()
    connectionError.title('Property managment system')
    connectionError.geometry('500x500')
    connectionError.resizable(width=False, height=False)
    connectionError.configure(background=primary)
    connectionErrorTitle = Label(connectionError, font=(font,'20','underline'), text='Connection Error', justify='center', width='71', bg=primary,fg=secondry).place(relx=0.5, rely=0.1, anchor=CENTER)
    connectionErrorMessage = Label(connectionError, font=(font,'12'), text='we found a internet connection error, please check your \n connection and click restart program when you have a \n stable connection', justify='center', width='71', bg=primary,fg=secondry).place(relx=0.5, rely=0.5, anchor=CENTER)    
    restart = Button(connectionError, font=(font,'12','underline'), text = 'restart program', command=restartFromConnectionError, bg = primary, fg = secondry, borderwidth=0, activeforeground=tertiary, activebackground=primary).place(relx=0.5, rely=0.8, anchor=CENTER)
    connectionError.mainloop()

def createTables(): 
    openDatabase()
    #### accounts
    create_Accounts_Entity = """
    CREATE TABLE accounts (
        account_ID varchar(16) NOT NULL,
        password varchar(16) NOT NULL,
        recovery_Email varchar(32) NOT NULL,
        first_Name varchar(16) NOT NULL,
        last_Name varchar(16) NOT NULL,
        operation_Type varchar(1) NOT NULL,
        title varchar(4) NOT NULL,
        tax_Rate char(1) NOT NULL,
        other_Income_Estimate float(5) NOT NULL,
        basic_Income_Rate float(1) NOT NULL,
        high_Income_Rate float(1) NOT NULL,
        additional_Income_Rate float(1) NOT NULL,
        basic_Income_Cut_Off float(4) NOT NULL,
        high_Income_Cut_Off float(4) NOT NULL,
        corporation_Rate float(1) NOT NULL,
        basic_Capital_Gains_Rate float(1) NOT NULL,
        basic_Capital_Gains_Allowence float(4) NOT NULL,
        high_Capital_Gains_Rate float(1) NOT NULL,
        additional_Capital_Gains_Rate float(1) NOT NULL,
        corporation_Capital_Gains_Rate float(1) NOT NULL,
        national_Insurance_Due float(5) NOT NULL,
        primary_Colour char(7) NOT NULL,
        secondry_Colour char(7) NOT NULL,
        tertiary_Colour char(7) NOT NULL,
        font varchar(30) NOT NULL,
        PRIMARY KEY (account_ID)
    )
    """
    cursor.execute(create_Accounts_Entity)
    ###
    ### sold_Units
    create_Sold_Units_Entity = """
    CREATE TABLE sold_Units (
        unit_ID varchar(16) NOT NULL,
        account_ID varchar(16) NOT NULL,
        buy_Price float NOT NULL,
        sell_Price float NOT NULL,
        sell_Month integar NOT NULL,
        sell_Year integar NOT NULL,
        tax_Due float NOT NULL,
        tax_Paid boolean NOT NULL,
        PRIMARY KEY (unit_ID),
        FOREIGN KEY (account_ID) REFERENCES accounts(account_ID) 
    )
    """
    cursor.execute(create_Sold_Units_Entity)
    ###
    ### tenants
    create_Tenants_Entity = """
    CREATE TABLE tenants (
        tenant_ID varchar(16) NOT NULL,
        account_ID varchar(16) NOT NULL,
        tenant_Email varchar(32) NOT NULL,
        first_Name varchar(16) NOT NULL,
        title varchar(4) NOT NULL,
        date_Of_Birth char(10) NOT NULL,
        score float NOT NULL,
        total_Residents integar NOT NULL,
        start_Date char(10) NOT NULL,
        deposit float NOT NULL,
        gerneral_Notes varchar(1024) NOT NULL,
        PRIMARY KEY (tenant_ID),
        FOREIGN KEY (account_ID) REFERENCES accounts(account_ID)
    )
    """
    cursor.execute(create_Tenants_Entity)
    ###
    ### complaints
    create_Complaints_Entity = """
    CREATE TABLE complaints (
        complaint_ID varchar(16) NOT NULL,
        tenant_ID varchar(16) NOT NULL,
        month integar NOT NULL,
        year integar NOT NULL,
        complaint_Nature varchar(1024) NOT NULL,
        resoltion varchar(1024),
        PRIMARY KEY (complaint_ID),
        FOREIGN KEY (tenant_ID) REFERENCES tenants(tenant_ID) 
    )
    """ 
    cursor.execute(create_Complaints_Entity)
    ###
    ### units
    create_Units_Entity = """
    CREATE TABLE units (
        unit_ID varchar(16) NOT NULL,
        account_ID varchar(16) NOT NULL,
        tenant_ID varchar(16) NOT NULL,
        most_Recent_Valuation float NOT NULL,
        buy_Price float NOT NULL,
        address varchar(512) NOT NULL,
        postcode varchar(8) NOT NULL,
        buy_Month integar NOT NULL,
        buy_Year integar NOT NULL,
        property_Equity float NOT NULL,
        rent float NOT NULL,
        general_Notes varchar(1024),
        PRIMARY KEY (unit_ID),
        FOREIGN KEY (account_ID) REFERENCES accounts(accounts_ID),
        FOREIGN KEY (tenant_ID) REFERENCES tenants(tenant_ID)
    )
    """
    cursor.execute(create_Units_Entity)
    ###
    ### units_Monthly
    create_Units_Monthly_Entity = """
    CREATE TABLE units_Monthly (
        year integar NOT NULL,
        month integar NOT NULL,
        unit_ID varchar(16) NOT NULL,
        tenant_ID varchar(16) NOT NULL,
        rent_Paid boolean NOT NULL,
        rent_Late boolean NOT NULL,
        income float NOT NULL,
        non_Taxable_Expenses float NOT NULL,
        taxable_Expenses float NOT NULL,
        suspected_Property_Value float NOT NULL,
        equity_In_Property float NOT NULL,
        money_Taken_From_Deposit float NOT NULL,
        PRIMARY KEY (year, month, unit_ID),
        FOREIGN KEY (unit_ID) REFERENCES units(unit_ID),
        FOREIGN KEY (tenant_ID) REFERENCES tenants(tenant_ID)
    )
    """
    cursor.execute(create_Units_Monthly_Entity)
    ###
    ### refinance
    create_Refinance_Entity = """
    CREATE TABLE refinance (
        unit_ID varchar(16) NOT NULL,
        month integar NOT NULL,
        year integar NOT NULL,
        equity_Withdrawn float NOT NULL,
        PRIMARY KEY (unit_ID, month, year)
        FOREIGN KEY (unit_ID) REFERENCES units(unit_ID)
    )
    """
    cursor.execute(create_Refinance_Entity)
    ###
    ### loan
    create_Loan_Entity = """
    CREATE TABLE loan (
        loan_ID varchar(16) NOT NULL,
        unit_ID varchar(16) NOT NULL,
        interest_Rate float NOT NULL,
        instalments float NOT NULL,
        capital_Owed float NOT NULL,
        PRIMARY KEY (loan_ID)
        FOREIGN KEY (unit_ID) REFERENCES units(unit_ID)
    )
    """
    cursor.execute(create_Loan_Entity)
    closeDatabase()

def checkTableExsistance():
    openDatabase()
    cursor.execute('SELECT name from sqlite_master WHERE type = "table"')
    listOfTablesTuples = cursor.fetchall()
    closeDatabase()
    global listOfTables
    listOfTables = []
    for tableTuple in listOfTablesTuples:
        listOfTables.append(listOfTablesTuples[listOfTablesTuples.index(tableTuple)][0])
    if sorted(listOfTables) == listOfIdealTables:
        return True #all tables are present
    else:
        return False #not all tables are present

def openDatabase():
    global connection, cursor
    connection = sqlite3.connect(databaseName)
    cursor = connection.cursor()

def closeDatabase():
    connection.commit()
    connection.close()

def restartFromConnectionError():
    connectionError.destroy()
    initialise()

def displayTCs():
    initialiseWindow()
    root.title('Property managment system - Terms and Condtions')
    tCsTitle = Label(root, font=(font,'25'), text='TERMS & CONDITIONS', justify='center', width='71', bg=primary,fg=secondry).place(relx=0.5, rely=0.1, anchor=CENTER)
    tCsSubTitle = Label(root,font=(font,'15'), text='By accepting the terms and condtions you agree to the following', justify='center', width='71', bg=primary,fg=secondry).place(relx=0.5, rely=0.15, anchor=CENTER)
    tCsBP1 = Label(root,font=(font,'13'), text= '○ I will only enter personal data into this system when the person whom the data belongs to has given consent for their data to be stored', anchor='w',width='125', bg=primary,fg=secondry).place(relx=0.025, rely=0.25)
    tCsBP2 = Label(root,font=(font,'13'), text= '○ I will keep all data stored accurate and upto date', width='125', bg=primary,fg=secondry, justify='left',anchor='w').place(relx=0.025, rely=0.3)
    tCsBP3 = Label(root,font=(font,'13'), text= '○ I will not share the data stored on this system with any unauthorised person or an organisation', anchor='w',width='125', bg=primary,fg=secondry).place(relx=0.025, rely=0.35)
    tCsBP4 = Label(root,font=(font,'13'), text= '○ I will not use this system to store data about a tenant that has left a unit', width='125', bg=primary,fg=secondry, justify='left',anchor='w').place(relx=0.025, rely=0.4)
    tCsBP5 = Label(root,font=(font,'13'), text= '○ I will delete personal data on anyone as soon as it becomes unnecessary', width='125', bg=primary,fg=secondry, justify='left',anchor='w').place(relx=0.025, rely=0.45)
    tCsBP6 = Label(root,font=(font,'13'), text= '○ I will not alter any files relating to this system except through this system', width='125', bg=primary,fg=secondry, justify='left',anchor='w').place(relx=0.025, rely=0.5)
    tCsBP6 = Label(root,font=(font,'13'), text= '○ I understand that the creator of this system is not responsible for the security of any data stored in this system', width='125', bg=primary,fg=secondry, justify='left',anchor='w').place(relx=0.025, rely=0.55)
    tCsBP7 = Label(root,font=(font,'13'), text= '○ I have read, understand and accept the full terms and conditions of this system', width='125', bg=primary,fg=secondry, justify='left',anchor='w').place(relx=0.025, rely=0.6)
    viewFullTCsB = Button(root, text='View Full Terms & conditions', font=(font,'15','underline'),fg=secondry,bg=primary,activeforeground=bannedColours['activeTextColor'],activebackground=primary,border=0,command=viewFullTCs).place(relx=0.5, rely=0.7, anchor=CENTER)
    acceptTCsB = Button(root, text='Accept', font=(font,'50','underline'),fg=secondry,bg=primary,activeforeground=bannedColours['activeTextColor'],activebackground=primary,border=0,command=loginPage).place(relx=0.5, rely=0.8, anchor=CENTER)
    declineTCsB = Button(root, text='Decline', font=(font,'11','underline'),fg=secondry,bg=primary,activeforeground=bannedColours['activeTextColor'],activebackground=primary,border=0,command=declineTCs).place(relx=0.5, rely=0.9, anchor=CENTER)
    root.mainloop()

def viewFullTCs():
    try:
        webbrowser.open_new('https://emuxmatt.github.io/NEA/Terms-Condtions.pdf')
    except OSError:
        if connectionError.state() != 'Normal':
                displayConnectionError()

def closeMainPage():
    try:
        if root.state() == 'normal':
            root.destroy()
            chdir('..')
    except NameError: #this means that the page is not defined and thus there is no previous page
        pass 

def loginPage():
    initialiseWindow()
    root.title ('Property managment system - Login')
    headerL = Label(root,text='Login',font=((font,'40')),fg=secondry,bg=primary).place(relx=0.5,rely=0.1, anchor=CENTER)
    #username input
    logo = PhotoImage(file = "Long-Normal.PNG")
    logoLabel = Label(image = logo, border = 0).place(relx=0.5,rely=0.4,anchor=CENTER)
    usernameHeaderL = Label(root,text='Username',font=((font,'15')),fg=secondry,bg=primary).place(relx=0.5,rely=0.28, anchor=CENTER)
    #password input
    root.mainloop()

def convertAssetColor(primary,secondry):
    chdir(f'.{path_seperator}Assests')
    listOfAssets = os.listdir(os.getcwd())
    for asset in listOfAssets:
        if (asset.split('.')[1]).lower() == 'png':
            print(asset) 
            img = Image.open(asset)
            x = 0
            y = 0
            count = 0
            for x in range(img.size[0]):
                if [x,y] == [0,0]:
                    oldPrimary = img.getpixel((x,y))
                    print('Old Primary = ',oldPrimary)  
                for y in range(img.size[1]):
                    r,g,b,a = img.getpixel((x,y))
                    if (r,g,b,a) == oldPrimary:
                        img.putpixel((x,y),(r,g,b))
                    else:
                        r,g,b,a = ImageColor.getcolor(secondry, "RGBA")
                        img.putpixel((x,y),(r,g,b))
            img.save(asset)
            # img.show()
    chdir('..')

def declineTCs():
    initialiseWindow()
    root.title('Property managment system - Terms and Condtions declined')
    root.geometry('500x500')
    headerDTC = Label(root,text='You must accept the terms and\nconditions to use this system',font=((font,'20')),fg=secondry,bg=primary).place(relx=0.5,rely=0.1, anchor=CENTER)
    messageDTC = Label(root,text='Unfortunatly you cannot use this system unless you have\naccept the terms and conditions of this system',font=((font,'12')),fg=secondry,bg=primary).place(relx=0.5,rely=0.3, anchor=CENTER)
    returnToTCPageB = Button(root,text='Go Back To Terms And Conditions',font=((font,'12','underline')),activeforeground=bannedColours['activeTextColor'],activebackground=primary,fg=secondry,bg=primary,border=0,command=displayTCs).place(relx=0.5,rely=0.5, anchor=CENTER)
    confirmDeclineB = Button(root,text='Confrim Decline',font=((font,'12','underline')),activeforeground=bannedColours['activeTextColor'],activebackground=primary,fg=secondry,bg=primary,border=0,command=closeMainPage).place(relx=0.5,rely=0.7, anchor=CENTER)
    acceptTCsB = Button(root, text='Accept Terms and Conditions', font=(font,'12','underline'),fg=secondry,bg=primary,activeforeground=bannedColours['activeTextColor'],activebackground=primary,border=0,command=loginPage).place(relx=0.5, rely=0.9, anchor=CENTER)
    root.mainloop()

initialise()