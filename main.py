#importing modules
from sqlite3.dbapi2 import Connection
from tkinter import *
from tkinter import ttk
import sqlite3
import time
import datetime
import tkinter
import matplotlib
import os
from os import chdir, close, error, getcwd, name, system, terminal_size
from pathlib import Path
import platform
import tkinter.font as tkfont
import urllib.request
from matplotlib.pyplot import autoscale, flag, get, text
import webbrowser
from PIL import Image, ImageColor, ImageFilter
import random
import string

print('program started')

#main start program function
def initialise():
    definingDefaultVariables()
    findOS()
    if path_seperator != None: #basically if the device is running on an accepted OS
        if fileCreation() == 'Correct Files Created':
            convertAssetColor(primary,secondry)
            ## This allows me to access specific pages without having to go via the terms and conditions -> login -> menu etc
            createAccountPage()  
            #displayTCs()

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
    global primary, secondry, tertiary, bannedColours, font, listOfIdealTables, databaseName, listOfIdealAssets, listOfIdealAssetsMutable ,connectionError, previousPage
    global incPA, bIncTR, hIncTR, aIncTR, bCapGainsAllowence, bIncCutOff, hIncCutOff, corpTR, corpCapGainsTR, bCapGainsTR, hCapGainsTR, aCapGainsTR, normalSet, mappingSet, numericalMappingSet
    primary = '#373f51'
    secondry = '#ffffff'
    tertiary = '#a9a9a9'
    bannedColours = {'errorRed':'#','warningYellow':'#','activeTextColor':'dark grey'}
    font = 'Bahnschrift SemiLight'
    listOfIdealTables = ['accounts', 'complaints', 'loan', 'refinance', 'sold_Units', "tenants", "units_Monthly", 'units']
    databaseName = 'Property Managment System Database.db'
    listOfIdealAssets = ['Long-Fat.PNG','Long-Normal.PNG','Long-Skinny.PNG','Short-Fat.PNG','Short-Normal.PNG','House.ico']
    connectionError = Tk()
    connectionError.destroy()
    previousPage = None
    incPA = 12500.0
    bIncTR = 20.0
    hIncTR = 40.0
    aIncTR = 45.0
    bCapGainsAllowence = 12300.0
    bIncCutOff = 50000.0
    hIncCutOff = 150000.0
    corpTR = 19
    corpCapGainsTR = 20
    bCapGainsTR = 18
    hCapGainsTR = 28
    aCapGainsTR = 28
    normalSet = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','`','¬','!','"','£','$','%','^','&','*','(',')','_','-','=','+',';',':','@',"'",' ','#',',','.','?','/']
    mappingSet = ['m', '3', '4', 'A', 'e', 'b', 'o', 'B', 'u', 'w', 'C', 'a', '2', 'i', 'D', 'E', 'F', '9', "G", 'g', 'H', 'I', '7', 'J', 'h', 'K', '6', 'L', 'M', 'x', 's', 'N', 'O', 'p', 'P', '5', 'r','Q', '0', 'c', 'R', 't', 'd', 'q', 'f', 'S', 'z', 'k', 'T', 'y', 'j', 'U', 'V', 'n', 'W', '8', 'l', 'X', 'Y', 'Z', '1', 'v']
    numericalMappingSet = ['7','1','5','2','3','8','4','6','0','9']

#intialising page
def initialiseWindow():
    closeMainPage()
    global root
    root = Tk()
    root.title('Property managment system')
    root.geometry('1250x850')
    root.configure(background=primary)
    root.resizable(width=False, height=False) #Makes the window not be reziable becuase that mucks up the asthetics
    if ((os.getcwd()).split(path_seperator))[len(os.getcwd().split(path_seperator))-1] != 'Assets':
        chdir(f'.{path_seperator}Assets')
    root.iconbitmap("House.ico")
    root.bind("=", escapeProgram)

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
    if ((os.getcwd()).split(path_seperator))[len(os.getcwd().split(path_seperator))-1] != 'Assets':
        createFolder('Assets')
    configureDatabase()
    if addAssets() == 'Correct Assets Obtained':
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

def addAssets():
    if ((os.getcwd()).split(path_seperator))[len(os.getcwd().split(path_seperator))-1] != 'Assets':
        chdir(f'.{path_seperator}Assets')
    listOfAssets = os.listdir(os.getcwd())
    i = 0
    while i in range(len(listOfIdealAssets)):
        asset = listOfIdealAssets[i]
        if asset not in listOfAssets:
            try:
                urllib.request.urlretrieve(f"https://matt-jl-burton.github.io/NEA/{asset}",f'{asset}')
            except OSError: #if there is a connection error
                if connectionError.state != 'normal':
                    i = len(listOfIdealAssets) + 1 #to exit while loop so as not to try and get more Assets resulting in 
                    #loads of connection error's being displayed
                    displayConnectionError()
        i = i + 1

    #sorting list
    listOfIdealAssetsSorted = (listOfIdealAssets).sort()
    listOfObtainedAssetsSorted =  ((os.listdir(os.getcwd())).sort())
    chdir('..')

    if listOfObtainedAssetsSorted == listOfIdealAssetsSorted:
        return 'Correct Assets Obtained'
    else:
        print('Correct Assets Not Obtained')
        return 'Correct Assets Not Obtained'

def configureDatabase():
    if ((os.getcwd()).split(path_seperator))[len(os.getcwd().split(path_seperator))-1] != 'Assets':
        chdir(f'.{path_seperator}Assets')
    createFile(databaseName)
    if checkTableExsistance() == False: #Deletes all tables if the all tables dont exsist - this is to uphold referentail integrity and becasue it is easier to add all tables again instead of working out which ones are gone and trying to restich the database together
        openDatabase()
        for table in listOfTables:
            cursor.execute('DROP TABLE ' + table)
        closeDatabase()
        createTables()
    chdir('..')

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
    CREATE TABLE accounts(
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
    global listOfTables
    listOfTables = []
    for line in cursor.execute('SELECT name from sqlite_master WHERE type = "table"'):
        listOfTables.append(line[0])
    closeDatabase()
    if sorted(listOfTables) == sorted(listOfIdealTables):
        return True #all tables are present
    else:
        return False #not all tables are present

def openDatabase():
    global connection, cursor
    if ((os.getcwd()).split(path_seperator))[len(os.getcwd().split(path_seperator))-1] != 'Assets':
        chdir(f'.{path_seperator}Assets')
    connection = sqlite3.connect(databaseName)
    cursor = connection.cursor()

def closeDatabase():
    connection.commit()
    connection.close()
    #chdir('..')

def restartFromConnectionError():
    connectionError.destroy()
    initialise()

def displayTCs():
    initialiseWindow()
    global previousPage
    previousPage = 'Terms and Conditions'
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
        webbrowser.open_new('https://Matt-JL-Burton.github.io/NEA/Terms-Condtions.pdf')
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
    displayBackButton()
    global previousPage
    previousPage = 'Login'
    root.title ('Property managment system - Login')
    headerL = Label(root,text='Login',font=((font,'40')),fg=secondry,bg=primary).place(relx=0.5,rely=0.1, anchor=CENTER)
    #username input
    usernameHeaderL = Label(root,text='Username',font=((font,'15')),fg=secondry,bg=primary).place(relx=0.5,rely=0.28, anchor=CENTER)
    longNormal = PhotoImage(file = "Long-Normal.PNG")
    longNormalLabelU = Label(image = longNormal, border = 0).place(relx=0.5,rely=0.37,anchor=CENTER)
    usernameEntry = Entry(root, bg=primary, fg=secondry, width=42, font=(font,24),justify='center',relief='flat').place(relx=0.5,rely=0.37,anchor=CENTER)
    #password input
    passwordHeaderL = Label(root,text='Password',font=((font,'15')),fg=secondry,bg=primary).place(relx=0.5,rely=0.55, anchor=CENTER)
    longNormalLabelP = Label(image = longNormal, border = 0).place(relx=0.5,rely=0.64,anchor=CENTER)
    passwordEntry = Entry(root, bg=primary,fg=secondry, width=42, font=(font,24),justify='center',relief='flat').place(relx=0.5,rely=0.64,anchor=CENTER)
    hidePasswordLoginPageB = Button(root, text='Hide', font=(font,'15','underline'),fg=secondry,bg=primary,activeforeground=bannedColours['activeTextColor'],activebackground=primary,border=0,command=hidePasswordLoginPage).place(relx=0.15, rely=0.64, anchor=CENTER)
    createAccountPageB = Button(root, text='Create Account', font=(font,'15','underline'),fg=secondry,bg=primary,activeforeground=bannedColours['activeTextColor'],activebackground=primary,border=0,command=createAccountPage).place(relx=0.2, rely=0.9, anchor=CENTER)
    ForgottenPageB = Button(root, text='Forgotten Password?', font=(font,'15','underline'),fg=secondry,bg=primary,activeforeground=bannedColours['activeTextColor'],activebackground=primary,border=0,command=forgottenPasswordPageOne).place(relx=0.8, rely=0.9, anchor=CENTER)
    submitLoginDetailsB = Button(root, text='L O G I N', font=(font,'20','underline','bold'),fg=secondry,bg=primary,activeforeground=bannedColours['activeTextColor'],activebackground=primary,border=0,command=login).place(relx=0.5, rely=0.9, anchor=CENTER)
    root.mainloop()

def convertAssetColor(primaryHex,secondryHex):
    if ((os.getcwd()).split(path_seperator))[len(os.getcwd().split(path_seperator))-1] != 'Assets':
        chdir(f'.{path_seperator}Assets')
    listOfAssets = os.listdir(os.getcwd())
    testAsset = listOfAssets[1]
    img = Image.open(testAsset)
    newPrimary = list(ImageColor.getcolor(primaryHex, "RGBA"))
    newSecondry = list(ImageColor.getcolor(secondryHex, "RGBA"))
    if testAsset == 'Long-Fat.PNG' and (newPrimary != list(img.getpixel((0,0))) or newSecondry != list(img.getpixel((9,112)))): #check to see if assets are already in the correct colours and so we shoudl not bother changing them
        for asset in listOfAssets:
            if (asset.split('.')[1]).lower() == 'png':
                img = Image.open(asset)
                x = 0
                y = 0
                # listOfPixelsInForeground = {}
                for x in range(img.size[0]):
                    if [x,y] == [0,0]:
                        oldPrimary = list(img.getpixel((x,y)))
                        newPrimary =  list(ImageColor.getcolor(primaryHex, "RGBA"))
                    for y in range(img.size[1]):
                        r,g,b,a = img.getpixel((x,y))
                        if [r,g,b,a] == oldPrimary:
                            img.putpixel((x,y),(newPrimary[0],newPrimary[1],newPrimary[2]))
                        else:
                            # print(x,y)
                            # time.sleep(1000)
                            # listOfPixelsInForeground[x,y] = 0
                            newSecondry = list(ImageColor.getcolor(secondryHex, "RGBA"))
                            img.putpixel((x,y),(newSecondry[0],newSecondry[1],newSecondry[2]))
                # for pixel in list(listOfPixelsInForeground.keys()):
                #     x,y = list(pixel)[0],list(pixel)[1]
                #     count = 1
                #     for i in range(3):
                #         for ii in range (3):
                #             r,g,b,a = img.getpixel(((x-1)+i,(y-1)+ii))
                #             if [r,g,b,a] == oldPrimary:
                #                 count = count + 1
                #     listOfPixelsInForeground[(x,y)] = count
                # img.save(asset)
                # img.close()
                # img = Image.open(asset)
                # for pixel in list(listOfPixelsInForeground.keys()):
                #     x,y = list(pixel)[0],list(pixel)[1]
                #     img.putpixel(pixel,(newSecondry[0]//listOfPixelsInForeground[(x,y)],newSecondry[1]//listOfPixelsInForeground[(x,y)],newSecondry[2]//listOfPixelsInForeground[(x,y)]))
                img.save(asset)
                img.close()
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

def createAccountPage():
    initialiseWindow()
    displayBackButton()
    global previousPage
    previousPage = 'Create Account'
    root.title('Property managment system - Create Account')
    headerL = Label(root,text='Create Account',font=((font,'40')),fg=secondry,bg=primary).place(relx=0.5,rely=0.1, anchor=CENTER)
    shortNormal = PhotoImage(file = "Short-Normal.PNG")
    
    emailEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.25,rely=0.25,anchor=CENTER)
    global emailEntryBox
    emailEntryBox = Entry(root, bg=primary,fg=secondry, width=23, font=(font,18),justify='center',relief='flat')
    emailEntryBox.place(relx=0.25,rely=0.25,anchor=CENTER)
    emailLabel = Label(root, text='Email',bg=primary, fg=secondry, width=23, font=(font,18), justify='center',relief='flat').place(relx=0.25,rely=0.17,anchor=CENTER)
    emailSubLabel = Label(root, text='This will be used as your username, so make sure you can access it',bg=primary, fg=secondry, width=60, font=(font,7), justify='center',relief='flat').place(relx=0.25,rely=0.315,anchor=CENTER)

    firstNameEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.25,rely=0.43,anchor=CENTER)
    global firstNameEntryBox
    firstNameEntryBox = Entry(root, bg=primary,fg=secondry, width=23, font=(font,18),justify='center',relief='flat')
    firstNameEntryBox.place(relx=0.25,rely=0.43,anchor=CENTER)
    firstNameLabel = Label(root, text='First Name',bg=primary, fg=secondry, width=23, font=(font,18), justify='center',relief='flat').place(relx=0.25,rely=0.35,anchor=CENTER)
    
    operationTypeEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.25,rely=0.61,anchor=CENTER)
    global operationTypeOptions
    operationTypeOptions = ['Business','Personal']
    global operationTypeMenu
    operationTypeMenu = ttk.Combobox(root, value=operationTypeOptions, justify=tkinter.CENTER, font=(font,18))
    operationTypeMenu.current(1)
    operationTypeMenu.place(relx=0.25,rely=0.61,anchor=CENTER)
    root.option_add('*TCombobox*Listbox.font', (font,14)) 
    operationTypeLabel = Label(root, text='Operation Type',bg=primary, fg=secondry, width=23, font=(font,18), justify='center',relief='flat').place(relx=0.25,rely=0.53,anchor=CENTER)
    
    otherIncomeEstimateEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.25,rely=0.79,anchor=CENTER)
    global otherIncomeEntryBox
    otherIncomeEntryBox = Entry(root, bg=primary,fg=secondry, width=23, font=(font,18),justify='center',relief='flat')
    otherIncomeEntryBox.place(relx=0.25,rely=0.79,anchor=CENTER)
    otherIncomeLabel = Label(root, text='Other Income (Estimate in £)',bg=primary, fg=secondry, width=23, font=(font,15), justify='center',relief='flat').place(relx=0.25,rely=0.71,anchor=CENTER)
    otherIncomeSubLabel = Label(root, text='This data is used for calcualting tax estiamtes, it is kept private and secure',bg=primary, fg=secondry, width=60, font=(font,7), justify='center',relief='flat').place(relx=0.25,rely=0.855,anchor=CENTER)

    passwordEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.75,rely=0.25,anchor=CENTER)
    global passwordEntryBox
    passwordEntryBox = Entry(root, bg=primary,fg=secondry, width=23, font=(font,18),justify='center',relief='flat')
    passwordEntryBox.place(relx=0.75,rely=0.25,anchor=CENTER)
    passwordLabel = Label(root, text='Password',bg=primary, fg=secondry, width=23, font=(font,18), justify='center',relief='flat').place(relx=0.75,rely=0.17,anchor=CENTER)
    passwordSubLabel = Label(root, text='As with all user data input, the password is none case sensative',bg=primary, fg=secondry, width=60, font=(font,7), justify='center',relief='flat').place(relx=0.75,rely=0.315,anchor=CENTER)

    surnameEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.75,rely=0.43,anchor=CENTER)
    global surnameEntryBox
    surnameEntryBox = Entry(root, bg=primary,fg=secondry, width=23, font=(font,18),justify='center',relief='flat')
    surnameEntryBox.place(relx=0.75,rely=0.43,anchor=CENTER)
    surnameEntryLabel = Label(root, text='Surname',bg=primary, fg=secondry, width=23, font=(font,18), justify='center',relief='flat').place(relx=0.75,rely=0.35,anchor=CENTER)

    titleEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.75,rely=0.61,anchor=CENTER)
    global titleEntryBox
    titleEntryBox = Entry(root, bg=primary,fg=secondry, width=23, font=(font,18),justify='center',relief='flat')
    titleEntryBox.place(relx=0.75,rely=0.61,anchor=CENTER)
    titleeEntryLabel = Label(root, text='Title',bg=primary, fg=secondry, width=23, font=(font,18), justify='center',relief='flat').place(relx=0.75,rely=0.53,anchor=CENTER)

    nationalInsuranceEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.75,rely=0.79,anchor=CENTER)
    global nationalInsuranceEntryBox
    nationalInsuranceEntryBox = Entry(root, bg=primary,fg=secondry, width=23, font=(font,18),justify='center',relief='flat')
    nationalInsuranceEntryBox.place(relx=0.75,rely=0.79,anchor=CENTER)
    nationalInsuranceLabel = Label(root, text='National Insurance Tax Due (£)',bg=primary, fg=secondry, width=25, font=(font,15), justify='center',relief='flat').place(relx=0.75,rely=0.71,anchor=CENTER)
    nationalInsuranceSubLabel = Label(root, text="Don't know how much to pay? - ",bg=primary, fg=secondry, width=60, font=(font,7), justify='center',relief='flat').place(relx=0.735,rely=0.855,anchor=CENTER)
    nationalInsuranceClickHereB = Button(root, text='Click Here', font=(font,'7','underline'),fg=secondry,bg=primary,activeforeground=bannedColours['activeTextColor'],activebackground=primary,border=0,command=displayGovermentNationalInsurancePage).place(relx=0.805, rely=0.855, anchor=CENTER)

    submitLoginDetailsB = Button(root, text='C R E A T E   A C C O U N T ', font=(font,'20','underline','bold'),fg=secondry,bg=primary,activeforeground=bannedColours['activeTextColor'],activebackground=primary,border=0,command=createAccount).place(relx=0.5, rely=0.93, anchor=CENTER)
    root.mainloop()

def forgottenPasswordPageOne():
    initialiseWindow()
    global previousPage
    previousPage = 'Forgotten Password Page 1'
    root.title('Property managment system - Forgotten Password (Page 1 of 3)')
    root.mainloop()

def login():
    print('attempt login')
    root.mainloop()

def hidePasswordLoginPage():
    #TODO: hide the password 
    #TODO: replace the hide button with a show button and then code show button
    pass

def createAccount():
    email = emailEntryBox.get()
    firstName = firstNameEntryBox.get()
    operationType = operationTypeMenu.get()
    otherIncomeEstimate = otherIncomeEntryBox.get()
    password = passwordEntryBox.get()
    surname = surnameEntryBox.get()
    title = titleEntryBox.get()
    natInsuranceDue = nationalInsuranceEntryBox.get()

    characters = (string.ascii_uppercase)+(string.digits)
    account_ID =  (''.join(random.choice(characters) for i in range(10)))

    createAccountArray = [account_ID,password,email,firstName,surname, operationType, title, getTaxRate(account_ID),otherIncomeEstimate,bIncTR, hIncTR, aIncTR, bIncCutOff, hIncCutOff, corpTR, bCapGainsTR, bCapGainsAllowence, hCapGainsTR, aCapGainsTR, corpCapGainsTR,natInsuranceDue, primary, secondry, tertiary, font]
    accountFields = ['account_ID', 'password', 'recovery_Email', 'first_Name', 'last_Name', 'operation_Type', 'title', 'tax_Rate', 'other_Income_Estimate', 'basic_Income_Rate', 'high_Income_Rate', 'additional_Income_Rate', 'basic_Income_Cut_Off', 'high_Income_Cut_Off', 'corporation_Rate', 'basic_Capital_Gains_Rate', 'basic_Capital_Gains_Allowence', 'high_Capital_Gains_Rate', 'additional_Capital_Gains_Rate', 'corporation_Capital_Gains_Rate', 'national_Insurance_Due', 'primary_Colour', 'secondry_Colour', 'tertiary_Colour','font']
        
    for i in range(len(createAccountArray)):
        createAccountArray[i] = scramble(createAccountArray[i])

    listOfDataValidationResults = dict.fromkeys(accountFields)


    #TODO: entry validation
    #TODO: run SQL command to add data to database
    openDatabase()
    global accountsInsertionCommand
    accountsInsertionCommand = """INSERT INTO accounts(account_ID, password, recovery_Email, first_Name, last_Name, operation_Type, title, tax_Rate, other_Income_Estimate, basic_Income_Rate, high_Income_Rate, additional_Income_Rate, basic_Income_Cut_Off, high_Income_Cut_Off, corporation_Rate, basic_Capital_Gains_Rate, basic_Capital_Gains_Allowence, high_Capital_Gains_Rate, additional_Capital_Gains_Rate, corporation_Capital_Gains_Rate, national_Insurance_Due, primary_Colour, secondry_Colour, tertiary_Colour, font)
    Values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
    cursor.execute(accountsInsertionCommand,createAccountArray)
    closeDatabase()
    pass

def displayBackButton():
    if previousPage == None:
        pass
    elif previousPage == 'Login':
        backButton = Button(root, text='BACK', font=(font,'15','underline','bold'),fg=tertiary,bg=primary,activeforeground=bannedColours['activeTextColor'],activebackground=primary,border=0,command=loginPage).place(relx=0.05, rely=0.05, anchor=CENTER)
    elif previousPage == 'Create Account':
        backButton = Button(root, text='BACK', font=(font,'15','underline','bold'),fg=tertiary,bg=primary,activeforeground=bannedColours['activeTextColor'],activebackground=primary,border=0,command=createAccountPage).place(relx=0.05, rely=0.05, anchor=CENTER)
    elif previousPage == 'Terms and Conditions':
        backButton = Button(root, text='BACK', font=(font,'15','underline','bold'),fg=tertiary,bg=primary,activeforeground=bannedColours['activeTextColor'],activebackground=primary,border=0,command=displayTCs).place(relx=0.05, rely=0.05, anchor=CENTER)
    elif previousPage == 'Forgotten Password Page 1':
        backButton = Button(root, text='BACK', font=(font,'15','underline','bold'),fg=tertiary,bg=primary,activeforeground=bannedColours['activeTextColor'],activebackground=primary,border=0,command=forgottenPasswordPageOne).place(relx=0.05, rely=0.05, anchor=CENTER)

def displayGovermentNationalInsurancePage():
    try:
        webbrowser.open_new('https://www.gov.uk/government/collections/how-to-manually-check-your-payroll-calculations ')
    except OSError:
        if connectionError.state() != 'Normal':
                displayConnectionError()

def getTaxRate(accountID):
    # openDatabase()
    # otherIncome = cursor.execute('SELECT other_Income_Estimate FROM accounts WHERE account_ID ='+str(accountID))
    # closeDatabase()
    # #TODO: need to find other income streams
    tax_Rate = 'b'
    return(tax_Rate)

def scramble(data):
    if type(data) == list:
        for i in range(len(data)):
            if type(data[i]) == str: 
                data[i] = data[i].lower()
                data[i] = list(data[i])
                for i in range(len(data[i])):
                    data[i][i] = mappingSet[normalSet.index(data[i][i])]
                data[i] = listToString(data[i])
                data[i] = data[i][::-1]
            elif type(data[i]) == int:
                data[i] = str(data[i])
                data[i] = data[i].replace(',','')
                data[i] = list(data[i])
                for i in range(len(data[i])):
                    data[i][i] = numericalMappingSet[normalSet.index(data[i][i])]
                data[i] = data[i][::-1]
                data[i] = listToInt(data[i])
            elif type(data[i]) == float:
                data[i] = str(data[i])
                data[i] = data[i].replace(',','')
                data[i] = list(data[i])
                for i in range(len(data[i])):
                    if data[i][i] != '.':
                        data[i][i] = numericalMappingSet[normalSet.index(data[i][i])]
                data[i] = data[i][::-1]
                data[i] = listToFloat(data[i])
            else:
                print(data[i],' unrecognised data type in string scrambling func')
    else:
        if type(data) == str: 
            data = data.lower()
            data = list(data)
            for i in range(len(data)):
                data[i] = mappingSet[normalSet.index(data[i])]
            data = listToString(data)
            data = data[::-1]
        elif type(data) == int:
            data = str(data)
            data = list(data)
            for i in range(len(data)):
                data[i] = numericalMappingSet[normalSet.index(data[i])]
            data = data[::-1]
            data = listToInt(data)
        elif type(data) == float:
            data = str(data)
            data = list(data)
            for i in range(len(data)):
                if data[i] != '.':
                    data[i] = numericalMappingSet[normalSet.index(data[i])]
            data = data[::-1]
            data = listToFloat(data)
        else:
            print(data,' unrecognised data type in string descrambling func')
    return(data)

def deScramble(data):
    if type(data) == list:
        for i in range(len(data)):
            if type(data[i]) == str: 
                data[i] = data[i].lower()
                data[i] = list(data[i])
                for i in range(len(data[i])):
                    data[i][i] = normalSet[mappingSet.index(data[i][i])]
                data[i] = listToString(data[i])
                data[i] = data[i][::-1]
            elif type(data[i]) == int:
                data[i] = str(data[i])
                data[i] = data[i].replace(',','')
                data[i] = list(data[i])
                for i in range(len(data[i])):
                    data[i][i] = normalSet[numericalMappingSet.index(data[i][i])]
                data[i] = data[i][::-1]
                data[i] = listToInt(data[i])
            elif type(data[i]) == float:
                data[i] = str(data[i])
                data[i] = data[i].replace(',','')
                data[i] = list(data[i])
                for i in range(len(data[i])):
                    if data[i][i] != '.':
                        data[i][i] = normalSet[numericalMappingSet.index(data[i][i])]
                data[i] = data[i][::-1]
                data[i] = listToFloat(data[i])
            else:
                print(data[i],' unrecognised data type in string scrambling func')
    else:
        if type(data) == str: 
            data = data.lower()
            data = list(data)
            for i in range(len(data)):
                data[i] = normalSet[mappingSet.index(data[i])]
            data = listToString(data)
            data = data[::-1]
        elif type(data) == int:
            data = str(data)
            data = list(data)
            for i in range(len(data)):
                data[i] = normalSet[numericalMappingSet.index(data[i])]
            data = data[::-1]
            data = listToInt(data)
        elif type(data) == float:
            data = str(data)
            data = list(data)
            for i in range(len(data)):
                if data[i] != '.':
                    data[i] = normalSet[numericalMappingSet.index(data[i])]
            data = data[::-1]
            data = listToFloat(data)
        else:
            print(data,' unrecognised data type in string descrambling func')
    return data

def listToString(list):
    word = ''
    for letter in list:
        word = word + str(letter)
    return word

def listToInt(list):
    word = ''
    for letter in list:
        word = word + str(letter)
    integer = int(word)
    return integer

def listToFloat(list):
    word = ''
    for letter in list:
        word = word + str(letter)
    floater = float(word)
    return floater

#data validation
def menuOptionCheck(entry,globalMenuList):
    if entry in globalMenuList:
        return True
    else:
        return False 

def castingTypeCheckFunc(dataInput,preferredType):
    if preferredType == str:
        if type(dataInput) == str:
            return dataInput
        else:
            return False
    try:
        dataInput = preferredType(dataInput)
        return dataInput
    except:
        return False

def uniqueDataCheck(dataValue,fieldName,table):
    returnedValue = []
    openDatabase()
    for line in cursor.execute('SELECT '+str(fieldName) + ' FROM ' + str(table) + ' WHERE ' + str(fieldName) + " = '" +str(dataValue)+str("'")):
        returnedValue.append(line[0])
    closeDatabase()
    if returnedValue == None or returnedValue == []:
        return True
    else:
        return False

def basicPictureCheck(data,mustContain):
    print(mustContain)
    if type(mustContain) == list:
        for i in range (len(mustContain)):
            mustContain[i] = str(mustContain[i])
        listOfContainResults = []
        for i in range(len(mustContain)):
            if (mustContain[i]) in data:
                listOfContainResults.append(True)
            else:
                listOfContainResults.append(False)
        if False in listOfContainResults:
            return False
        else:
            return True
    else:
        mustContain = str(mustContain)
        if mustContain in data:
            return True
        else:
            return False

def rangeCheck(data,lowerBound,upperBound):
    #inclusive of bounds - this func can be used for length checking aswell by using the len method on data as an argument for the func
    if (type(lowerBound) == float or type(lowerBound) == int or type(lowerBound) == None) and (type(upperBound) == float or type(upperBound) == int or type(upperBound) == None):
        if lowerBound == None and upperBound != None:
            if data <= upperBound:
                return True
            else:
                return False
        elif upperBound == None and lowerBound != None:
            if data >= lowerBound:
                return True
            else:
                return False
        elif upperBound == None and lowerBound == None:
            raise TypeError('Both Bounds cannot be None')
        else:
            if data >= lowerBound and data <= upperBound:
                return True
            else:
                return False
    else:
        raise TypeError('Bounds where the incorrect data type') 

def presenceCheck(data):
    if data != None:
        return True
    else:
        return False

initialise()