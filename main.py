#importing modules
from tkinter import *
import sqlite3
import time
import datetime
import matplotlib
import os
from os import chdir, close, error
import pathlib
import platform
import tkinter.font as tkfont
import urllib.request
from matplotlib.pyplot import autoscale

print('program started')

def initialise():
    definingDefaultVariables()
    findOS()
    setCWD()
    if path_seperator != None: #basically if the device is running on an accepted OS
        fileCreation()
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
    global primary, secondry, tertiary, bannedColours, font, listOfIdealTables, databaseName, listOfIdealAssests, connectionError
    primary = '#373f51'
    secondry = '#ffffff'
    tertiary = '#a9a9a9'
    bannedColours = {'errorRed':'#','warningYellow':'#'}
    font = 'Bahnschrift SemiLight'
    listOfIdealTables = ['Accounts', 'Complaints', 'Loan_table', 'Refinance', 'Sold_Units', "Tenant's_Entity", "Unit's_Monthly", 'Units']
    databaseName = 'Property Managment System Database.db'
    listOfIdealAssests = ['Long-Fat.PNG','Long-Normal.PNG','Long-Skinny.PNG','Short-Fat.PNG','Short-Normal.PNG']
    connectionError = 0

#intialising page
def initialiseWindow():
    global root
    root = Tk()
    root.title('Property managment system')
    root.geometry('1250x850')
    root.configure(background=primary)
    root.resizable(width=False, height=False) #Makes the window not be reziable becuase that mucks up the asthetics
    root.bind("`", escapeProgram)
    # ######### testing
    # chdir(f'.{path_seperator}Assests')
    # print(os.getcwd())
    # print(os.listdir(os.getcwd()))
    # global black_Short_SVG
    # black_Short_SVG = PhotoImage(file=os.listdir(os.getcwd())[0])
    # entryBackground_Test = Label(root, image = black_Short_SVG,background=None).place(x = 100, y = 100) 
    # chdir('..')
    # ######### testing
    # root.mainloop()

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
    addAssests()
    
def createFolder(folderName):
    listOfFilesInDirectory = os.listdir(os.getcwd())
    if str(folderName) not in listOfFilesInDirectory:
        os.makedirs(folderName)

def createFile(fileName):
    listOfFilesInDirectory = os.listdir(cwd)
    if fileName not in listOfFilesInDirectory:
        f = open(fileName,'w')
        f.close()

def addAssests():
    chdir(f'.{path_seperator}Assests')
    listOfAssets = os.listdir(os.getcwd())
    for asset in listOfIdealAssests:
        if asset not in listOfAssets:
            try:
                urllib.request.urlretrieve(f"https://emuxmatt.github.io/NEA/{asset}",f'{asset}')
            except OSError: #if there is a connection error
                if checkPageOpen(connectionError) == 'Not Open':
                    displayConnectionError()
    chdir('..')

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

def setCWD():
    global cwd
    cwd = pathlib.Path(__file__).parent.absolute() 
    chdir(cwd)

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

def checkPageOpen(page_root):
    if page_root == 0: #this means a page of this root has never been made. It is only defined in the default_Variables
        return 'Not Open'
    else:
        if page_root.state() == 'open':
            return 'Open'
        else:
            print (page_root.state())
            return 'Not Open'

# def endPageLoop():
#     root.mainloop()

def displayTCs():
    initialiseWindow()
    root.title('Property managment system - Terms and Condtions')
    tCsTitle = Label(root, font=(font,'25'), text='TERMS & CONDITIONS', justify='center', width='71', bg=primary,fg=secondry).place(relx=0.5, rely=0.1, anchor=CENTER)
    tCsSubTitle = Label(root,font=(font,'15'), text='By accepting the terms and condtions you agree to the following', justify='center', width='71', bg=primary,fg=secondry).place(relx=0.5, rely=0.15, anchor=CENTER)
    tCsBP1 = Label(root,font=(font,'13'), text= '○ I will only enter personal data into this system when the person whom the data belongs to has given consent for their data to be stored', anchor='w',width='125', bg=primary,fg=secondry).place(relx=0.025, rely=0.25)
    tCsBP2 = Label(root,font=(font,'13'), text= '○ I will keep all data stored accurate and upto date', width='125', bg=primary,fg=secondry, justify='left',anchor='w').place(relx=0.025, rely=0.3)
    tCsBP3 = Label(root,font=(font,'13'), text= '○ I will not share of the data stored on this system with any unauthorised person or an organisation', anchor='w',width='125', bg=primary,fg=secondry).place(relx=0.025, rely=0.35)
    tCsBP4 = Label(root,font=(font,'13'), text= '○ I will not use this system to store data about a tenant that has left a unit', width='125', bg=primary,fg=secondry, justify='left',anchor='w').place(relx=0.025, rely=0.4)
    tCsBP5 = Label(root,font=(font,'13'), text= '○ I will delete personal data on anyone as soon as it becomes unnecessary', width='125', bg=primary,fg=secondry, justify='left',anchor='w').place(relx=0.025, rely=0.45)
    tCsBP6 = Label(root,font=(font,'13'), text= '○ I will not share my pasword anywhere or with anyone who is unauthorised to access the data stored by this system', width='125', bg=primary,fg=secondry, justify='left',anchor='w').place(relx=0.025, rely=0.5)
    tCsBP6 = Label(root,font=(font,'13'), text= '○ h', width='125', bg=primary,fg=secondry, justify='left',anchor='w').place(relx=0.025, rely=0.55)
    tCsBP7 = Label(root,font=(font,'13'), text= '○ h', width='125', bg=primary,fg=secondry, justify='left',anchor='w').place(relx=0.025, rely=0.55)

    root.mainloop()

initialise()