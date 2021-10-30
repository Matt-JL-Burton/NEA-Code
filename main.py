#importing modules
from email import message
from http.client import GATEWAY_TIMEOUT
from sqlite3.dbapi2 import Connection, Error
from tkinter import ttk
from tkinter import *
import sqlite3
import time
import datetime
import tkinter
import matplotlib
import os
from os import chdir, close, error, getcwd, name, system, terminal_size
import pathlib
import platform
import tkinter.font as tkfont
import urllib.request
from matplotlib.pyplot import autoscale, fill, flag, get, pink, prism, show, table, text, title
import webbrowser
from PIL import Image, ImageColor, ImageFilter
import random
import string
from dataObjectClass import uInputDataObj

print('program started')

#main start program function
def initialise():
    definingDefaultVariables()
    findOS()
    if path_seperator != None: #basically if the device is running on an accepted OS
        os.chdir(pathlib.Path(__file__).parent.absolute())
        if fileCreation() == 'Correct Files Created':
            convertAssetColor(primary,secondry)
            ## This allows me to access specific pages without having to go via the terms and conditions -> login -> menu -> target page  
            #displayTCs()
            complaintsManagmentPage('TA1')

#setting up key bindings for quickly exciting the program (mainly useful for developing)
def escapeProgram(event):
    root.destroy()

def invalidOSRunning():
    InvalidOSRoot = Tk()
    InvalidOSRoot.title('Property managment system')
    InvalidOSRoot.geometry('500x500')
    InvalidOSRoot.resizable(width=False, height=False)
    InvalidOSRoot.configure(background=primary.data)
    IVOSTitle = Label(InvalidOSRoot, font=(font,'20','underline'), text='Operating System not supported', justify='center', width='71', bg=primary.data,fg=secondry.data).place(relx=0.5, rely=0.1, anchor=CENTER)
    IVOOperatingSystem = Label(InvalidOSRoot, font=(font,'12'), text='We have detected your device is running an unsupported\noperating system. '+platform.system()+' operating system is not supported\nby this software', justify='center', width='71', bg=primary.data,fg=secondry.data).place(relx=0.5, rely=0.5, anchor=CENTER)    
    IVOSMainMessage = Label(InvalidOSRoot, font=(font,'12'), text='Sorry, but only Windows and MAC OS operating\nsystems are supported by this software', justify='center', width='71', bg=primary.data,fg=secondry.data).place(relx=0.5, rely=0.8, anchor=CENTER)
    IVOSEmail = Label(InvalidOSRoot, font=(font,'12'), text='For more information please email\nmburton22@norwich-school.org.uk', justify='center', width='71', bg=primary.data,fg=secondry.data).place(relx=0.5, rely=0.9, anchor=CENTER)
    InvalidOSRoot.mainloop()
 
#defining certain default variables
def definingDefaultVariables():
    global primary, secondry, tertiary, bannedColours, font, listOfIdealTables, databaseName, listOfIdealAssets, listOfIdealAssetsMutable ,connectionError, previousPage
    global incPA, bIncTR, hIncTR, aIncTR, bCapGainsAllowence, bIncCutOff, hIncCutOff, corpTR, corpCapGainsTR, bCapGainsTR, hCapGainsTR, aCapGainsTR, normalSet, mappingSet, numericalMappingSet
    global errorMessgesDict, databaseCurrentAccount_ID, listOfSecondryColourOptions, listOfAcceptedFonts, operation_Type, recovery_Email, first_Name, last_Name, password, title
    global tax_Rate, other_Income_Estimate, national_Insurance_Due, style
    primary = uInputDataObj('#373f51',str)
    secondry = uInputDataObj('#ffffff',str)
    tertiary = uInputDataObj('#a9a9a9',str)
    listOfSecondryColourOptions = ['white','grey','black']
    bannedColours = {'errorRed':'#FF0000','warningYellow':'#FDDA0D','activeTextColor':'dark grey','emaraldGreen':'#50C878'}
    errorMessgesDict = {'presenceCheck':'Please give an input of correct data type','uniqueDataCheck':'Sorry a this data is not unique in the database - it must be unique','lengthCheck':'Sorry the length of this input is not appropriate','pictureCheck':'Sorry the format of this input is invalid','lengthOverSevenCheck':'This input must be more than 7 charcters long','@check':'This input must contain 1 "@" symbol','containsOnlyLetters':'This input should only contain letters','typeCheck':'Sorry the data type of this data is wrong','positiveCheck':'This input must be a positive number','menuOptionCheck':'Please pick and option that is in the menu','noSpaces':'Sorry this input cannot have any spaces in it','dayBetween0/31':'Please enter a day between 0 and 31','monthBetween1/12':'Please enter an integar between 1 and 12','yearBetween1900/2100':'Please enter a year in 1900 and 2100','between0/100':'Please enter number between 0 and 100','mustContainsLetters':'The input must contain atleast one letter','mustContainNumbers':'The input must contain atleast one number','hexCodeCheck':'Please enter a valid hex code','fontCheck':'Sorry this font is not supported please try again','checkPassword':'Incorrect password','matchesNewPassword':'Your new passwords are not matching, please enter matching passwords'}
    font = uInputDataObj('Bahnschrift SemiLight',str)
    operation_Type = uInputDataObj(None,str)
    recovery_Email = uInputDataObj(None,str)
    first_Name = uInputDataObj(None, str)
    last_Name = uInputDataObj(None,str)
    password = uInputDataObj(None,str)
    title = uInputDataObj(None,str)
    listOfIdealTables = ['accounts', 'complaints', 'loan', 'refinance', 'sold_Units', "tenants", "units_Monthly", 'units']
    databaseName = 'Property Managment System Database.db'
    listOfIdealAssets = ['Long-Fat.PNG','Long-Normal.PNG','Long-Skinny.PNG','Short-Fat.PNG','Short-Normal.PNG','House.ico','Long-Normal 2.PNG']
    connectionError = Tk()
    connectionError.destroy()
    previousPage = None
    other_Income_Estimate = uInputDataObj(None,str)
    national_Insurance_Due = uInputDataObj(None,str)
    tax_Rate = uInputDataObj(None,str)
    incPA = uInputDataObj(12500.0,float)
    bIncTR = uInputDataObj(20.0,float)
    hIncTR = uInputDataObj(40.0,float)
    aIncTR =  uInputDataObj(45.0,float)
    bCapGainsAllowence =  uInputDataObj(12300.0,float)
    bIncCutOff =  uInputDataObj(50000.0,float)
    hIncCutOff =  uInputDataObj(150000.0,float)
    corpTR =  uInputDataObj(19,float)
    corpCapGainsTR =  uInputDataObj(20,float)
    bCapGainsTR =  uInputDataObj(18,float)
    hCapGainsTR =  uInputDataObj(28,float)
    aCapGainsTR =  uInputDataObj(28,float)
    databaseCurrentAccount_ID = uInputDataObj('W2V2423OL5',str) #instansaite the current account object - also allows me the developer to access pages using test accoutns without signing in
    listOfAcceptedFonts = ['Bahnschrift Semilight','Georgia','Courier New','Microsoft Sans Serif','Franklin Gothic Medium','Times New Roman','Calibri']
    for i in range(len(listOfAcceptedFonts)):
        listOfAcceptedFonts[i] = listOfAcceptedFonts[i].title()

#intialising page
def initialiseWindow():
    closeMainPage()
    global root
    root = Tk()
    root.title('Property managment system')
    root.geometry('1250x850')
    root.configure(background=primary.data)
    root.resizable(width=False, height=False) #Makes the window not be reziable becuase that mucks up the asthetics
    if ((os.getcwd()).split(path_seperator))[len(os.getcwd().split(path_seperator))-1] != 'Assets':
        chdir(f'.{path_seperator}Assets')
    root.iconbitmap("House.ico")
    root.bind("=", escapeProgram)

#Finding out what OS the device runs on and setting the path seperator approrialtly
def findOS():
    global path_seperator
    if platform.system() == 'Windows': #Windows (for me to develope the program)
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
    connectionError.configure(background=primary.data)
    connectionErrorTitle = Label(connectionError, font=(font.data,'20','underline'), text='Connection Error', justify='center', width='71', bg=primary.data,fg=secondry.data).place(relx=0.5, rely=0.1, anchor=CENTER)
    connectionErrorMessage = Label(connectionError, font=(font.data,'12'), text='we found a internet connection error, please check your \n connection and click restart program when you have a \n stable connection', justify='center', width='71', bg=primary.data,fg=secondry.data).place(relx=0.5, rely=0.5, anchor=CENTER)    
    restart = Button(connectionError, font=(font.data,'12','underline'), text = 'restart program', command=restartFromConnectionError, bg = primary.data, fg = secondry.data, borderwidth=0, activeforeground=tertiary.data, activebackground=primary.data).place(relx=0.5, rely=0.8, anchor=CENTER)
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
        personal_Income_Allowence float(4) NOT NULL,
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
        last_Name varchar(16) NOT NULL,
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
    tCsTitle = Label(root, font=(font.data,'25'), text='TERMS & CONDITIONS', justify='center', width='71', bg=primary.data,fg=secondry.data).place(relx=0.5, rely=0.1, anchor=CENTER)
    tCsSubTitle = Label(root,font=(font.data,'15'), text='By accepting the terms and condtions you agree to the following', justify='center', width='71', bg=primary.data,fg=secondry.data).place(relx=0.5, rely=0.15, anchor=CENTER)
    tCsBP1 = Label(root,font=(font.data,'13'), text= '○ I will only enter personal data into this system when the person whom the data belongs to has given consent for their data to be stored', anchor='w',width='125', bg=primary.data,fg=secondry.data).place(relx=0.025, rely=0.25)
    tCsBP2 = Label(root,font=(font.data,'13'), text= '○ I will keep all data stored accurate and upto date', width='125', bg=primary.data,fg=secondry.data, justify='left',anchor='w').place(relx=0.025, rely=0.3)
    tCsBP3 = Label(root,font=(font.data,'13'), text= '○ I will not share the data stored on this system with any unauthorised person or an organisation', anchor='w',width='125', bg=primary.data,fg=secondry.data).place(relx=0.025, rely=0.35)
    tCsBP4 = Label(root,font=(font.data,'13'), text= '○ I will not use this system to store data about a tenant that has left a unit', width='125', bg=primary.data,fg=secondry.data, justify='left',anchor='w').place(relx=0.025, rely=0.4)
    tCsBP5 = Label(root,font=(font.data,'13'), text= '○ I will delete personal data on anyone as soon as it becomes unnecessary', width='125', bg=primary.data,fg=secondry.data, justify='left',anchor='w').place(relx=0.025, rely=0.45)
    tCsBP6 = Label(root,font=(font.data,'13'), text= '○ I will not alter any files relating to this system except through this system', width='125', bg=primary.data,fg=secondry.data, justify='left',anchor='w').place(relx=0.025, rely=0.5)
    tCsBP6 = Label(root,font=(font.data,'13'), text= '○ I understand that the creator of this system is not responsible for the security of any data stored in this system', width='125', bg=primary.data,fg=secondry.data, justify='left',anchor='w').place(relx=0.025, rely=0.55)
    tCsBP7 = Label(root,font=(font.data,'13'), text= '○ I have read, understand and accept the full terms and conditions of this system', width='125', bg=primary.data,fg=secondry.data, justify='left',anchor='w').place(relx=0.025, rely=0.6)
    viewFullTCsB = Button(root, text='View Full Terms & conditions', font=(font.data,'15','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=viewFullTCs).place(relx=0.5, rely=0.7, anchor=CENTER)
    acceptTCsB = Button(root, text='Accept', font=(font.data,'50','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=loginPage).place(relx=0.5, rely=0.8, anchor=CENTER)
    declineTCsB = Button(root, text='Decline', font=(font.data,'11','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=declineTCs).place(relx=0.5, rely=0.9, anchor=CENTER)
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
            #chdir('..')
    except NameError: #this means that the page is not defined and thus there is no previous page
        pass 

def loginPage():
    initialiseWindow()
    displayBackButton()
    global previousPage
    previousPage = 'Login'
    root.title ('Property managment system - Login')
    headerL = Label(root,text='Login',font=((font.data,'40')),fg=secondry.data,bg=primary.data).place(relx=0.5,rely=0.1, anchor=CENTER)
    #username input
    usernameHeaderL = Label(root,text='Username',font=((font.data,'15')),fg=secondry.data,bg=primary.data).place(relx=0.5,rely=0.28, anchor=CENTER)
    longNormalTwo = PhotoImage(file = "Long-Normal 2.PNG")
    longNormalLabelU = Label(image = longNormalTwo, border = 0).place(relx=0.5,rely=0.37,anchor=CENTER)
    global usernameEntry
    usernameEntry = Entry(root, bg=primary.data, fg=secondry.data, width=42, font=(font.data,24),justify='center',relief='flat')
    usernameEntry.place(relx=0.5,rely=0.37,anchor=CENTER)
    #password input
    passwordHeaderL = Label(root,text='Password',font=((font.data,'15')),fg=secondry.data,bg=primary.data).place(relx=0.5,rely=0.55, anchor=CENTER)
    longNormalLabelP = Label(image = longNormalTwo, border = 0).place(relx=0.5,rely=0.64,anchor=CENTER)
    global passwordEntry 
    passwordEntry = Entry(root, bg=primary.data,fg=secondry.data, width=42, font=(font.data,24),justify='center',relief='flat')
    passwordEntry.place(relx=0.5,rely=0.64,anchor=CENTER)
    hidePasswordLoginPageB = Button(root, text='Hide', font=(font.data,'15','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command= lambda: hideEntryBox(passwordEntry,0.14,0.64)).place(relx=0.14, rely=0.64, anchor=CENTER)
    createAccountPageB = Button(root, text='Create Account', font=(font.data,'15','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=createAccountPage).place(relx=0.2, rely=0.9, anchor=CENTER)
    ForgottenPageB = Button(root, text='Forgotten Password?', font=(font.data,'15','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=forgottenPasswordPageOne).place(relx=0.8, rely=0.9, anchor=CENTER)
    submitLoginDetailsB = Button(root, text='L O G I N', font=(font.data,'20','underline','bold'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=login).place(relx=0.5, rely=0.9, anchor=CENTER)
    timeLabel = Label(root,text="Logging in may take some time please be patient",bg=primary.data,fg=secondry.data, width=75, font=(font.data,12), justify='center',relief='flat').place(relx=0.5, rely=0.95 ,anchor=CENTER)

    root.mainloop()

def convertAssetColor(primaryHex,secondryHex):
    if ((os.getcwd()).split(path_seperator))[len(os.getcwd().split(path_seperator))-1] != 'Assets':
        chdir(f'.{path_seperator}Assets')
    listOfAssets = os.listdir(os.getcwd())
    testAsset = listOfAssets[1]
    img = Image.open(testAsset)
    newPrimary = list(ImageColor.getcolor(str(primaryHex.data), "RGBA"))
    newSecondry = list(ImageColor.getcolor(str(secondryHex.data), "RGBA"))
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
                        newPrimary =  list(ImageColor.getcolor(primaryHex.data, "RGBA"))
                    for y in range(img.size[1]):
                        r,g,b,a = img.getpixel((x,y))
                        if [r,g,b,a] == oldPrimary:
                            img.putpixel((x,y),(newPrimary[0],newPrimary[1],newPrimary[2]))
                        else:
                            # print(x,y)
                            # time.sleep(1000)
                            # listOfPixelsInForeground[x,y] = 0
                            newSecondry = list(ImageColor.getcolor(secondryHex.data, "RGBA"))
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
    headerDTC = Label(root,text='You must accept the terms and\nconditions to use this system',font=((font.data,'20')),fg=secondry.data,bg=primary.data).place(relx=0.5,rely=0.1, anchor=CENTER)
    messageDTC = Label(root,text='Unfortunatly you cannot use this system unless you have\naccept the terms and conditions of this system',font=((font.data,'12')),fg=secondry.data,bg=primary.data).place(relx=0.5,rely=0.3, anchor=CENTER)
    returnToTCPageB = Button(root,text='Go Back To Terms And Conditions',font=((font.data,'12','underline')),activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,fg=secondry.data,bg=primary.data,border=0,command=displayTCs).place(relx=0.5,rely=0.5, anchor=CENTER)
    confirmDeclineB = Button(root,text='Confrim Decline',font=((font.data,'12','underline')),activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,fg=secondry.data,bg=primary.data,border=0,command=closeMainPage).place(relx=0.5,rely=0.7, anchor=CENTER)
    acceptTCsB = Button(root, text='Accept Terms and Conditions', font=(font.data,'12','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=loginPage).place(relx=0.5, rely=0.9, anchor=CENTER)
    root.mainloop()

def createAccountPage():
    initialiseWindow()
    displayBackButton()
    global previousPage
    previousPage = 'Create Account'
    root.title('Property managment system - Create Account')
    headerL = Label(root,text='Create Account',font=((font.data,'40')),fg=secondry.data,bg=primary.data).place(relx=0.5,rely=0.1, anchor=CENTER)
    shortNormal = PhotoImage(file = "Short-Normal.PNG")
    
    emailEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.25,rely=0.25,anchor=CENTER)
    global emailEntryBox
    emailEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    emailEntryBox.place(relx=0.25,rely=0.25,anchor=CENTER)
    emailLabel = Label(root, text='Email',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.25,rely=0.17,anchor=CENTER)
    emailSubLabel = Label(root, text='This will be used as your username, so make sure you can access it',bg=primary.data, fg=secondry.data, width=60, font=(font.data,7), justify='center',relief='flat').place(relx=0.25,rely=0.315,anchor=CENTER)

    firstNameEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.25,rely=0.43,anchor=CENTER)
    global firstNameEntryBox
    firstNameEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    firstNameEntryBox.place(relx=0.25,rely=0.43,anchor=CENTER)
    firstNameLabel = Label(root, text='First Name',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.25,rely=0.35,anchor=CENTER)
    
    operationTypeEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.25,rely=0.61,anchor=CENTER)
    global operationTypeOptions
    operationTypeOptions = ['Business','Personal']
    global operationTypeMenu
    operationTypeMenu = ttk.Combobox(root, value=operationTypeOptions, justify=tkinter.CENTER, font=(font.data,18))
    operationTypeMenu.current(1)
    operationTypeMenu.place(relx=0.25,rely=0.61,anchor=CENTER)
    root.option_add('*TCombobox*Listbox.font', (font.data,14)) 
    operationTypeLabel = Label(root, text='Operation Type',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.25,rely=0.53,anchor=CENTER)
    
    otherIncomeEstimateEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.25,rely=0.79,anchor=CENTER)
    global otherIncomeEntryBox
    otherIncomeEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    otherIncomeEntryBox.place(relx=0.25,rely=0.79,anchor=CENTER)
    otherIncomeLabel = Label(root, text='Other Income (Estimate in £)',bg=primary.data, fg=secondry.data, width=23, font=(font.data,15), justify='center',relief='flat').place(relx=0.25,rely=0.71,anchor=CENTER)
    otherIncomeSubLabel = Label(root, text='This data is used for calcualting tax estiamtes, it is kept private and secure',bg=primary.data, fg=secondry.data, width=60, font=(font.data,7), justify='center',relief='flat').place(relx=0.25,rely=0.855,anchor=CENTER)

    passwordEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.75,rely=0.25,anchor=CENTER)
    global passwordEntryBox
    passwordEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    passwordEntryBox.place(relx=0.75,rely=0.25,anchor=CENTER)
    passwordLabel = Label(root, text='Password',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.75,rely=0.17,anchor=CENTER)
    #passwordSubLabel = Label(root, text='As with all user data input, the password is none case sensative',bg=primary.data, fg=secondry.data, width=60, font=(font.data,7), justify='center',relief='flat').place(relx=0.75,rely=0.315,anchor=CENTER)

    surnameEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.75,rely=0.43,anchor=CENTER)
    global surnameEntryBox
    surnameEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    surnameEntryBox.place(relx=0.75,rely=0.43,anchor=CENTER)
    surnameEntryLabel = Label(root, text='Surname',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.75,rely=0.35,anchor=CENTER)

    titleEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.75,rely=0.61,anchor=CENTER)
    global titleEntryBox
    titleEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    titleEntryBox.place(relx=0.75,rely=0.61,anchor=CENTER)
    titleeEntryLabel = Label(root, text='Title',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.75,rely=0.53,anchor=CENTER)

    nationalInsuranceEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.75,rely=0.79,anchor=CENTER)
    global nationalInsuranceEntryBox
    nationalInsuranceEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    nationalInsuranceEntryBox.place(relx=0.75,rely=0.79,anchor=CENTER)
    nationalInsuranceLabel = Label(root, text='National Insurance Tax Due (£)',bg=primary.data, fg=secondry.data, width=25, font=(font.data,15), justify='center',relief='flat').place(relx=0.75,rely=0.71,anchor=CENTER)
    nationalInsuranceSubLabel = Label(root, text="Don't know how much to pay? - ",bg=primary.data, fg=secondry.data, width=60, font=(font.data,7), justify='center',relief='flat').place(relx=0.735,rely=0.855,anchor=CENTER)
    nationalInsuranceClickHereB = Button(root, text='Click Here', font=(font.data,'7','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=displayGovermentNationalInsurancePage).place(relx=0.805, rely=0.855, anchor=CENTER)

    submitLoginDetailsB = Button(root, text='C R E A T E   A C C O U N T ', font=(font.data,'20','underline','bold'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=createAccount).place(relx=0.5, rely=0.93, anchor=CENTER)
    
    global accountPageEntryMessageBoxCords
    accountPageEntryMessageBoxCords= {'password':{'x':0.75,'y':0.3175},'recovery_Email':{'x':0.25,'y':0.3175},'first_Name':{'x':0.25,'y':0.4975},'last_Name':{'x':0.75,'y':0.4975},'other_Income_Estimate':{'x':0.25,'y':0.8575},'operation_Type':{'x':0.25,'y':0.6775},'title':{'x':0.75,'y':0.6775},'national_Insurance_Due':{'x':0.75,'y':0.8575}}
    root.mainloop()

def forgottenPasswordPageOne():
    initialiseWindow()
    displayBackButton()
    global previousPage
    previousPage = 'Forgotten Password Page 1'
    root.title('Property managment system - Forgotten Password (Page 1 of 3)')
    happyFace = Label(root, text=':)', font=(font.data,'40'),fg=secondry.data,bg=primary.data,justify='center').place(relx=0.5,rely=0.5,anchor=CENTER)
    root.mainloop()

def createAccount():
    recovery_Email = uInputDataObj(emailEntryBox.get(),str)
    first_Name = uInputDataObj(firstNameEntryBox.get(),str)
    global operation_Type
    operation_Type = uInputDataObj(operationTypeMenu.get(),str)
    global other_Income_Estimate
    other_Income_Estimate = uInputDataObj(otherIncomeEntryBox.get(),float)
    password = uInputDataObj(passwordEntryBox.get(),str)
    last_Name = uInputDataObj(surnameEntryBox.get(),str)
    title = uInputDataObj(titleEntryBox.get(),str)
    national_Insurance_Due = uInputDataObj(nationalInsuranceEntryBox.get(),float)

    characters = (string.ascii_uppercase)+(string.digits)
    account_ID =  uInputDataObj(''.join(random.choice(characters) for i in range(10)),str)
    while uniqueDataCheck(account_ID,'account_ID','accounts') == False:
        account_ID =  (''.join(random.choice(characters) for i in range(10)))

    createAccountArray = [account_ID.data,password.data,recovery_Email.data,first_Name.data,last_Name.data, operation_Type.data, title.data, getTaxRate(account_ID.data),incPA.data,other_Income_Estimate.data,bIncTR.data, hIncTR.data, aIncTR.data, bIncCutOff.data, hIncCutOff.data, corpTR.data, bCapGainsTR.data, bCapGainsAllowence.data, hCapGainsTR.data, aCapGainsTR.data, corpCapGainsTR.data,national_Insurance_Due.data, primary.data, secondry.data, tertiary.data, font.data]
    accountFields = ['account_ID', 'password', 'recovery_Email', 'first_Name', 'last_Name', 'operation_Type', 'title', 'tax_Rate','personal_Income_Allowence','other_Income_Estimate', 'basic_Income_Rate', 'high_Income_Rate', 'additional_Income_Rate', 'basic_Income_Cut_Off', 'high_Income_Cut_Off', 'corporation_Rate', 'basic_Capital_Gains_Rate', 'basic_Capital_Gains_Allowence', 'high_Capital_Gains_Rate', 'additional_Capital_Gains_Rate', 'corporation_Capital_Gains_Rate', 'national_Insurance_Due', 'primary_Colour', 'secondry_Colour', 'tertiary_Colour','font']
        

    #running tests
    global dictOfDataValdationResults
    dictOfDataValdationResults = dict.fromkeys(accountFields)
    #dictOfDataValdationResults['account_ID'] = {'presenceCheck':presenceCheck(account_ID),'uniqueDataCheck':uniqueDataCheck(account_ID,'account_ID','accounts')}
    dictOfDataValdationResults['password'] = {'lengthOverSevenCheck':rangeCheck(password,7,None)}
    dictOfDataValdationResults['recovery_Email'] = {'lengthCheck':rangeCheck(recovery_Email,3,None),'@check':pictureCheck(recovery_Email,'@',1,1),'noSpaces':pictureCheck(recovery_Email,'',0,0),'uniqueDataCheck':uniqueDataCheck(recovery_Email,'recovery_Email','accounts')}
    dictOfDataValdationResults['first_Name'] = {'presenceCheck':presenceCheck(first_Name),'containsOnlyLetters':containsOnlyLetters(first_Name)}
    dictOfDataValdationResults['last_Name'] = {'presenceCheck':presenceCheck(last_Name),'containsOnlyLetters':containsOnlyLetters(last_Name)}
    dictOfDataValdationResults['other_Income_Estimate'] = {'presenceCheck':presenceCheck(other_Income_Estimate),'positiveCheck':rangeCheck(other_Income_Estimate,0,1099511628)}
    dictOfDataValdationResults['operation_Type'] = {'menuOptionCheck':menuOptionCheck(operation_Type,operationTypeOptions)}
    dictOfDataValdationResults['title'] = {'presenceCheck':presenceCheck(title),'containsOnlyLetters':containsOnlyLetters(title)}
    dictOfDataValdationResults['national_Insurance_Due'] = {'presenceCheck':presenceCheck(national_Insurance_Due),'positiveCheck':rangeCheck(national_Insurance_Due,0,None)}
    createAccountCoverUpErrorMessage()

    for entryboxData in dictOfDataValdationResults.keys():
        countOfFailedTests = 0
        if dictOfDataValdationResults[entryboxData] != None:
            for test in dictOfDataValdationResults[entryboxData].keys():
                while dictOfDataValdationResults[entryboxData][test] == False and countOfFailedTests == 0:
                    disaplayEM(test,accountPageEntryMessageBoxCords[entryboxData]['x'],accountPageEntryMessageBoxCords[entryboxData]['y'])
                    countOfFailedTests = countOfFailedTests + 1

    countOfFailedTests = 0
    for entryboxData in dictOfDataValdationResults.keys():
        if dictOfDataValdationResults[entryboxData] != None:
            for test in dictOfDataValdationResults[entryboxData].values():
                if test == False:
                    countOfFailedTests = countOfFailedTests +1


    if countOfFailedTests == 0:
        for i in range(len(createAccountArray)):
            createAccountArray[i] = scramble(createAccountArray[i])

        openDatabase()
        global accountsInsertionCommand
        accountsInsertionCommand = """INSERT INTO accounts(account_ID, password, recovery_Email, first_Name, last_Name, operation_Type, title, tax_Rate, personal_Income_Allowence, other_Income_Estimate, basic_Income_Rate, high_Income_Rate, additional_Income_Rate, basic_Income_Cut_Off, high_Income_Cut_Off, corporation_Rate, basic_Capital_Gains_Rate, basic_Capital_Gains_Allowence, high_Capital_Gains_Rate, additional_Capital_Gains_Rate, corporation_Capital_Gains_Rate, national_Insurance_Due, primary_Colour, secondry_Colour, tertiary_Colour, font)
        Values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        cursor.execute(accountsInsertionCommand,createAccountArray)
        closeDatabase()

        displayConfirmation('Login')

def displayMenuButton():
    menubutton = Button(root, text='MENU', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=menuPage).place(relx=0.95, rely=0.05, anchor=CENTER)

def homePage():
    initialiseWindow()
    root.title('Property managment system - Home Page')
    root.configure(bg=secondry.data)
    topBorder = Label(root, text='Home', height=2 ,bg=primary.data, fg = secondry.data, width=42, font=(font.data,40), justify='center').place(relx=0,rely=0)
    displayMenuButton()
    displayBackButton()
    global previousPage
    previousPage = 'Home'
    happyFace = Label(root, text=':)', font=(font.data,'40'),fg=primary.data,bg=secondry.data,justify='center').place(relx=0.5,rely=0.5,anchor=CENTER)
    root.mainloop()

def displayBackButton():
    if previousPage == None:
        pass
    elif previousPage == 'Login':
        backButton = Button(root, text='BACK', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=loginPage).place(relx=0.05, rely=0.05, anchor=CENTER)
    elif previousPage == 'Create Account':
        backButton = Button(root, text='BACK', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=createAccountPage).place(relx=0.05, rely=0.05, anchor=CENTER)
    elif previousPage == 'Terms and Conditions':
        backButton = Button(root, text='BACK', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=displayTCs).place(relx=0.05, rely=0.05, anchor=CENTER)
    elif previousPage == 'Forgotten Password Page 1':
        backButton = Button(root, text='BACK', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=forgottenPasswordPageOne).place(relx=0.05, rely=0.05, anchor=CENTER)
    elif previousPage == 'Home':
        backButton = Button(root, text='BACK', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=homePage).place(relx=0.05, rely=0.05, anchor=CENTER)
    elif previousPage == 'Menu':
        backButton = Button(root, text='BACK', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=menuPage).place(relx=0.05, rely=0.05, anchor=CENTER)
    elif previousPage == 'Properties':
        backButton = Button(root, text='BACK', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=propertiesPage).place(relx=0.05, rely=0.05, anchor=CENTER)
    elif previousPage == 'Add unit':
        backButton = Button(root, text='BACK', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=newUnitPage).place(relx=0.05, rely=0.05, anchor=CENTER)
    elif previousPage == 'Tenants':
        backButton = Button(root, text='BACK', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=tenantsPage).place(relx=0.05, rely=0.05, anchor=CENTER)
    elif previousPage == 'Add Tenant':
        backButton = Button(root, text='BACK', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=newTenantPage).place(relx=0.05, rely=0.05, anchor=CENTER)
    elif previousPage == 'Tax':
        backButton = Button(root, text='BACK', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=taxPage).place(relx=0.05, rely=0.05, anchor=CENTER)
    elif previousPage == 'Settings':
        backButton = Button(root, text='BACK', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=settingsPage).place(relx=0.05, rely=0.05, anchor=CENTER)
    elif previousPage == 'Contact':
        backButton = Button(root, text='BACK', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=contactPage).place(relx=0.05, rely=0.05, anchor=CENTER)
    elif previousPage == 'Change Password':
        backButton = Button(root, text='BACK', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=changePasswordPage).place(relx=0.05, rely=0.05, anchor=CENTER)
    elif previousPage == 'Delete Account':
        backButton = Button(root, text='BACK', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=deleteAccountPage).place(relx=0.05, rely=0.05, anchor=CENTER)
    elif previousPage == 'Change Username':
        backButton = Button(root, text='BACK', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=changeUsername).place(relx=0.05, rely=0.05, anchor=CENTER)
    elif previousPage == 'individualTenantPage':
        backButton = Button(root, text='BACK', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=lambda: tenantPage(current_tenant_ID)).place(relx=0.05, rely=0.05, anchor=CENTER)
    elif previousPage == 'ComplaintsMangment':
        backButton = Button(root, text='BACK', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=lambda: complaintsManagmentPage(current_tenant_ID)).place(relx=0.05, rely=0.05, anchor=CENTER)

def displayNextButton(nextPageCommand):
    if nextPageCommand == None:
        pass
    elif nextPageCommand == 'Login':
        continueButton = Button(root, text='CONTINUE', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=loginPage).place(relx=0.5, rely=0.9, anchor=CENTER)
    elif nextPageCommand == 'Create Account':
        continueButton = Button(root, text='CONTINUE', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=createAccountPage).place(relx=0.5, rely=0.9, anchor=CENTER)
    elif nextPageCommand == 'Terms and Conditions':
        continueButton = Button(root, text='CONTINUE', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=displayTCs).place(relx=0.5, rely=0.9, anchor=CENTER)
    elif nextPageCommand == 'Forgotten Password Page 1':
        continueButton = Button(root, text='CONTINUE', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=forgottenPasswordPageOne).place(relx=0.5, rely=0.9, anchor=CENTER)
    elif nextPageCommand == 'Home':
        continueButton = Button(root, text='CONTINUE', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=homePage).place(relx=0.5, rely=0.9, anchor=CENTER)
    elif nextPageCommand == 'Menu':
        continueButton = Button(root, text='CONTINUE', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=menuPage).place(relx=0.5, rely=0.9, anchor=CENTER)
    elif nextPageCommand == 'Properties':
        continueButton = Button(root, text='CONTINUE', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=propertiesPage).place(relx=0.5, rely=0.9, anchor=CENTER)
    elif nextPageCommand == 'Add unit':
        continueButton = Button(root, text='CONTINUE', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=newUnitPage).place(relx=0.5, rely=0.9, anchor=CENTER)
    elif nextPageCommand == 'Tenants':
        continueButton = Button(root, text='CONTINUE', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=tenantsPage).place(relx=0.5, rely=0.9, anchor=CENTER)
    elif nextPageCommand == 'Add Tenant':
        continueButton = Button(root, text='CONTINUE', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=newTenantPage).place(relx=0.5, rely=0.9, anchor=CENTER)
    elif nextPageCommand == 'Tax':
        continueButton = Button(root, text='CONTINUE', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=taxPage).place(relx=0.5, rely=0.9, anchor=CENTER)
    elif nextPageCommand == 'Settings':
        continueButton = Button(root, text='CONTINUE', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=settingsPage).place(relx=0.5, rely=0.9, anchor=CENTER)
    elif nextPageCommand == 'Contact':
        continueButton = Button(root, text='CONTINUE', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=contactPage).place(relx=0.5, rely=0.9, anchor=CENTER)
    elif nextPageCommand == 'Change Password':
        continueButton = Button(root, text='CONTINUE', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=changePasswordPage).place(relx=0.5, rely=0.9, anchor=CENTER)
    elif nextPageCommand == 'Delete Account':
        continueButton = Button(root, text='CONTINUE', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=deleteAccountPage).place(relx=0.5, rely=0.9, anchor=CENTER)
    elif nextPageCommand == 'Change Username':
        continueButton = Button(root, text='CONTINUE', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=changeUsername).place(relx=0.5, rely=0.9, anchor=CENTER)
    elif nextPageCommand == 'individualTenantPage':
        continueButton = Button(root, text='CONTINUE', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=lambda: tenantPage(current_tenant_ID)).place(relx=0.5, rely=0.9, anchor=CENTER)
    elif nextPageCommand == 'ComplaintsMangment':
        continueButton = Button(root, text='CONTINUE', font=(font.data,'15','underline','bold'),fg=tertiary.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=lambda: complaintsManagmentPage(current_tenant_ID)).place(relx=0.5, rely=0.9, anchor=CENTER)

def displayGovermentNationalInsurancePage():
    try:
        webbrowser.open_new('https://www.gov.uk/government/collections/how-to-manually-check-your-payroll-calculations ')
    except OSError:
        if connectionError.state() != 'Normal':
                displayConnectionError()

def getTaxRate(accountID):
    if type(other_Income_Estimate) == float or type(other_Income_Estimate) == int:
        if operation_Type.data == 'personal':
            if other_Income_Estimate < bIncCutOff.data:
                tax_Rate = 'b'
            elif other_Income_Estimate < hIncCutOff.data:
                tax_Rate = 'h'
            else:
                tax_Rate = 'a'
        elif operation_Type == 'buisness':
            tax_Rate = 'c'
    else:
        tax_Rate='b'
    return(tax_Rate)

#scrambling alg used for encrpytin data so that it cannot be easily read straight from the DB file
def scramble(data):
    # data = list(str(data))
    # for i in range (len(data)):
    #     ascii_Code = ord(data[i])+len(data)
    #     if ascii_Code == 92: #This takes out the \ character because this messes with the SQL as it is used in f stirngs
    #         ascii_Code = 0
    #     data[i] = chr(ascii_Code) #uses a variable cipher to make it more complex
    # cipherText = listToString(data[::-1])
    #return cipherText
    return data

#used to decrypt the data from the db
def deScramble(cipherText):
    # cipherText = list(str(cipherText))
    # cipherText = cipherText[::-1]
    # cipherText = list(cipherText)
    # for i in range(len(cipherText)):
    #     ascii_Code = ord(cipherText[i])
    #     if ascii_Code == 0: #subs back in the \ character so that data is not lost
    #         ascii_Code = 92
    #     cipherText[i] = chr(ascii_Code - len(cipherText))
    # data = listToString(cipherText)
    # return data
    return cipherText

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

def findOS():
    global path_seperator
    if platform.system() == 'Windows': #Windows (for me to develope the program)
        path_seperator = '\\'
    elif platform.system() == 'Darwin': #MAC OS (for my end user to run the program)
        path_seperator = '/'
    else:
        path_seperator = None
        invalidOSRunning()

#data validation tests
def menuOptionCheck(entry,globalMenuList):
    if castingTypeCheckFunc(entry.data,entry.prefferredType) != False:
        if castingTypeCheckFunc(entry.data,entry.prefferredType) in globalMenuList:
            return True
        else:
            return False 
    else: 
        return False

def castingTypeCheckFunc(dataInput,preferredType):
    if preferredType == str:
        if type(dataInput) == str:
            return dataInput
        else:
            return False
    if preferredType == float or preferredType == int:
        dataInput = dataInput.replace(',','')
    try:
        dataInput = preferredType(dataInput)
        return dataInput
    except:
        return False

def uniqueDataCheck(inputData,fieldName,table):
    if castingTypeCheckFunc(inputData.data,inputData.prefferredType) != False:
        returnedValue = []
        openDatabase()
        for line in cursor.execute('SELECT '+str(fieldName) + ' FROM ' + str(table) + ' WHERE ' + str(fieldName) + " = '" +str(scramble(castingTypeCheckFunc(inputData.data,inputData.prefferredType)))+str("'")):
            returnedValue.append(line[0])
        closeDatabase()
        if returnedValue == None or returnedValue == []:
            return True
        else:
            return False
    else:
        return False

def howManySymbolsInStr(inputData, symbolLookingFor):
    if type(inputData) == str and type(symbolLookingFor) == str:
        count = 0
        for i in range(len(inputData)):
            if inputData[i] == symbolLookingFor:
                count = count + 1
        return count
    else: 
        raise TypeError('All data inputted must be a string')

def pictureCheck(inputData,symbol,minimum, maximum):
    if castingTypeCheckFunc(inputData.data,inputData.prefferredType) != False:
        if type(inputData.data) == str and type(symbol) == str:
            if type(minimum) == int or minimum == None and type(maximum) == int or maximum == None:
                numberOfSymbols = howManySymbolsInStr(inputData.data, symbol)
                if maximum == None:
                    if numberOfSymbols >= minimum:
                        return True      
                    else: 
                        return False
                else:
                    if numberOfSymbols >= minimum and numberOfSymbols <= maximum:
                        return True      
                    else: 
                        return False
            else:
                raise TypeError('min and max (bound) parameters inputted must be ints or None')
        else:
            raise TypeError('Data and symbol parameters inputted must be a string')
    else:
        return False

def rangeCheck(inputData,lowerBound,upperBound):
    if castingTypeCheckFunc(inputData.data,inputData.prefferredType) != False:
        if inputData.prefferredType == str:
            dataToTest = len(castingTypeCheckFunc(inputData.data,inputData.prefferredType))
        else:
            dataToTest = castingTypeCheckFunc(inputData.data,inputData.prefferredType)
        #inclusive of bounds - this func can be used for length checking aswell by using the len method on data as an argument for the func
        if (type(lowerBound) == float or type(lowerBound) == int or lowerBound == None) and (type(upperBound) == float or type(upperBound) == int or upperBound == None):
            if lowerBound == None and upperBound != None:
                if upperBound >= dataToTest:
                    return True
                else:
                    return False
            elif lowerBound == 0 and upperBound == None and (inputData.data == 0.0 or inputData.data == 0 or inputData.data == '0' or inputData.data == '0.0'):
                return True
            elif upperBound == None and lowerBound != None:
                if dataToTest >= lowerBound:
                    return True
                else:
                    return False
            elif upperBound == None and lowerBound == None:
                raise TypeError('Both Bounds cannot be None')
            else:

                if dataToTest >= lowerBound and upperBound >= dataToTest:
                    return True
                else:
                    return False
        else:
            raise TypeError('Bounds where the incorrect data type') 
    else:
        if (str(inputData.data) == '0.0' or str(inputData.data) == '0') and lowerBound == 0:
            return True
        return False

def presenceCheck(inputData):
    if inputData.data == '0' or inputData.data == '0.0':
        return True
    if castingTypeCheckFunc(inputData.data,inputData.prefferredType) != False:
        if inputData.data != None and inputData.data != '':

            return True
        else:
            return False
    else:
        return False

def containsOnlyLetters(inputData):
    if castingTypeCheckFunc(inputData.data,inputData.prefferredType) != False:
        if type(inputData.data) == str:
            if inputData.data.isalpha():
                return True
            else:
                return False
        else:
            raise TypeError('All data inputted must be a string')
    else:
        return False

def containsLetters(inputData):
    if castingTypeCheckFunc(inputData.data,inputData.prefferredType) != False:
        if type(inputData.data) == str:
            for i in range(len(inputData.data)):
                if inputData.data[i].isalpha() == True:
                    return True
            return False
        else:
            raise TypeError('All data inputted muse be a string')    
    else:
        return False

def containsNumbers(inputData):
    if castingTypeCheckFunc(inputData.data,inputData.prefferredType) != False:
        if type(inputData.data) == str:
            for i in range(len(inputData.data)):
                if inputData.data[i].isnumeric() == True:
                    return True
            return False
        else:
            raise TypeError('All data inputted muse be a string')    
    else:
        return False

def hexCodeCheck(inputData):
    hexCodePossibleCharacters = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','a','b','c','d','e','f']
    if castingTypeCheckFunc(inputData.data, inputData.prefferredType) != False:
        if len(inputData.data) != 0:
            if inputData.data[0] =='#' and len(inputData.data) == 7:
                inputData.setData(inputData.data.title())
                invalidChacracters = 0
                for i in range(6):
                    if inputData.data[i+1] in hexCodePossibleCharacters:
                        pass
                    else:
                        invalidChacracters = invalidChacracters + 1
                if invalidChacracters == 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def matchesCheck(x,y):
    if x.data == y.data:
        return True
    else:
        return False
# end of data validation tests

def disaplayEM(errorType,x,y):
    warning = Label(root, text = errorMessgesDict[errorType],bg=primary.data,width=65, fg = bannedColours['errorRed'], font=(font.data,9),justify='center').place(relx=x,rely=y,anchor=CENTER)

def createAccountCoverUpErrorMessage():
    for entryboxData in dictOfDataValdationResults.keys():
        if dictOfDataValdationResults[entryboxData] != None:
            coverUp = Label(root,bg=primary.data,width=75,font=(font.data,7),justify='center').place(relx=accountPageEntryMessageBoxCords[entryboxData]['x'],rely=accountPageEntryMessageBoxCords[entryboxData]['y'],anchor=CENTER)

def displayConfirmation(nextPageCommand):
    if ((os.getcwd()).split(path_seperator))[len(os.getcwd().split(path_seperator))-1] != 'Assets':
        chdir(f'.{path_seperator}Assets')
    initialiseWindow()
    root.geometry('500x500')
    root.resizable(width=False, height=False)
    root.title('Property managment system - Confirmation Message')
    DataAddedTitle = Label(root, font=(font.data,'20','underline'), text='Submission Success', justify='center', width='71', bg=primary.data,fg=secondry.data).place(relx=0.5, rely=0.15, anchor=CENTER)
    DataAddedMessage = Label(root, font=(font.data,'12'), text="Your previous page's submission was successful", justify='center', width='71', bg=primary.data,fg=secondry.data).place(relx=0.5, rely=0.5, anchor=CENTER)
    displayNextButton(nextPageCommand)
    root.mainloop()

def login():
    coverUp1 = Label(root,bg=primary.data,width=150,font=(font.data,7),justify='center').place(relx=0.5,rely=0.45,anchor=CENTER)
    coverUp2 = Label(root,bg=primary.data,width=150,font=(font.data,7),justify='center').place(relx=0.5,rely=0.72,anchor=CENTER)
    password = uInputDataObj(passwordEntry.get(),str)
    recovery_Email = uInputDataObj(usernameEntry.get(),str)
    openDatabase()
    storedPasswordForAccountObject = cursor.execute("SELECT password FROM ACCOUNTS WHERE recovery_Email = '" + str(scramble(castingTypeCheckFunc(recovery_Email.data,recovery_Email.prefferredType)))+str("'"))
    storedPasswordForAccount = storedPasswordForAccountObject.fetchall()
    closeDatabase()
    if len(storedPasswordForAccount) == 0:
        warning = Label(root, text = 'Sorry an account with this username does not exsist',bg=primary.data,width=150, fg = bannedColours['errorRed'], font=(font.data,12),justify='center').place(relx=0.5,rely=0.45,anchor=CENTER)
        validEmail = False
    else:
        validEmail = True
        if deScramble(str(storedPasswordForAccount[0][0])) == password.data:
            openDatabase()
            account_ID_Dirty = cursor.execute("SELECT account_ID FROM ACCOUNTS WHERE recovery_Email = '" + str(scramble(castingTypeCheckFunc(recovery_Email.data,recovery_Email.prefferredType)))+str("'") )
            #global databaseCurrentAccount_ID
            global databaseCurrentAccount_ID
            databaseCurrentAccount_ID.setData(deScramble(account_ID_Dirty.fetchall()[0][0]))
            redoConfigureAccountSettingsVariables()
            convertAssetColor(primary,secondry)
            #print(databaseCurrentAccount_ID)
            #displayConfirmation('Home')
            homePage()
        else:
            warning = Label(root, text = 'Incorrect Password',bg=primary.data,width=150, fg = bannedColours['errorRed'], font=(font.data,12),justify='center').place(relx=0.5,rely=0.72,anchor=CENTER)
    root.mainloop()

#This menu page is for allowing access to a few of the most commonly used and most important pages in terms on navigation
def menuPage():
    initialiseWindow()
    root.title('Property managment system - Menu')
    root.configure(bg=secondry.data)
    topBorder = Label(root, text='Menu', height=2 ,bg=primary.data, fg = secondry.data, width=42, font=(font.data,40), justify='center').place(relx=0,rely=0)
    displayBackButton()
    global previousPage
    previousPage = 'Menu'
    homePageButton = Button(root, text='Home Page', font=(font.data,'17','underline'),fg=primary.data,bg=secondry.data,activeforeground=bannedColours['activeTextColor'],activebackground=secondry.data,border=0,command=homePage).place(relx=0.5, rely=0.25, anchor=CENTER)
    properitesPageButton = Button(root, text='Properties Page', font=(font.data,'17','underline'),fg=primary.data,bg=secondry.data,activeforeground=bannedColours['activeTextColor'],activebackground=secondry.data,border=0,command=propertiesPage).place(relx=0.5, rely=0.325, anchor=CENTER)
    newUnitPageButton = Button(root, text='Add New Unit Page', font=(font.data,'17','underline'),fg=primary.data,bg=secondry.data,activeforeground=bannedColours['activeTextColor'],activebackground=secondry.data,border=0,command=newUnitPage).place(relx=0.5, rely=0.4, anchor=CENTER)
    TenantPageButton = Button(root, text='Tenant Page', font=(font.data,'17','underline'),fg=primary.data,bg=secondry.data,activeforeground=bannedColours['activeTextColor'],activebackground=secondry.data,border=0,command=tenantsPage).place(relx=0.5, rely=0.475, anchor=CENTER)
    addNewTenantButton = Button(root, text='Add New Tenant Page', font=(font.data,'17','underline'),fg=primary.data,bg=secondry.data,activeforeground=bannedColours['activeTextColor'],activebackground=secondry.data,border=0,command=newTenantPage).place(relx=0.5, rely=0.55, anchor=CENTER)
    taxPageButton = Button(root, text='Tax Page', font=(font.data,'17','underline'),fg=primary.data,bg=secondry.data,activeforeground=bannedColours['activeTextColor'],activebackground=secondry.data,border=0,command=taxPage).place(relx=0.5, rely=0.625, anchor=CENTER)
    settingsPageButton = Button(root, text='Settings Page', font=(font.data,'17','underline'),fg=primary.data,bg=secondry.data,activeforeground=bannedColours['activeTextColor'],activebackground=secondry.data,border=0,command=settingsPage).place(relx=0.5, rely=0.7, anchor=CENTER)
    contactPageButton = Button(root, text='Contact Page', font=(font.data,'17','underline'),fg=primary.data,bg=secondry.data,activeforeground=bannedColours['activeTextColor'],activebackground=secondry.data,border=0,command=contactPage)
    contactPageButton.place(relx=0.5, rely=0.775, anchor=CENTER)
    contactPageButton["state"] = "disabled" #To disable contact button as Im no longer using this
    signOutButton = Button(root, text='Sign Out', font=(font.data,'17','underline'),fg=primary.data,bg=secondry.data,activeforeground=bannedColours['activeTextColor'],activebackground=secondry.data,border=0,command=loginPage).place(relx=0.5, rely=0.85, anchor=CENTER)
    root.mainloop()

#This page is for presenting data about the overall state of my end users portfolio aswell as a way to access data for each individual unit
def propertiesPage():
    initialiseWindow()
    root.title('Property managment system - Properties Page')
    root.configure(bg=secondry.data)
    topBorder = Label(root, text='Properties', height=2 ,bg=primary.data, fg = secondry.data, width=42, font=(font.data,40), justify='center').place(relx=0,rely=0)
    displayBackButton()
    global previousPage
    previousPage = 'Properties'
    displayMenuButton()
    root.mainloop()

#This page is for adding a new units to a user's portfolio. It is very similar in desing and functionalty to the create account page and add new tenant page
def newUnitPage():
    initialiseWindow()
    root.title('Property managment system - Add New Unit Page')
    topBorder = Label(root, text='Add Unit', height=2 ,bg=primary.data, fg = secondry.data, width=42, font=(font.data,40), justify='center').place(relx=0,rely=0)
    displayBackButton()
    global previousPage
    previousPage = 'Add unit'
    displayMenuButton()

    shortNormal = PhotoImage(file = "Short-Normal.PNG")
    shortFat = PhotoImage(file = "Short-Fat.PNG")

    unitIDEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.175,rely=0.25,anchor=CENTER)
    global unitIDEntryBox
    unitIDEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    unitIDEntryBox.place(relx=0.175,rely=0.25,anchor=CENTER)
    unitIDEntryLabel = Label(root, text='Unit ID',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.175,rely=0.17,anchor=CENTER)
    unittIDEntryBoxSubText = Label(root, text='This input is unchangable once submitted', bg=primary.data, fg=secondry.data, width=50, font=(font.data,9), justify='center', relief='flat').place(relx=0.175, rely=0.3175,anchor=CENTER)

    dateOfPurchaseEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.175,rely=0.43,anchor=CENTER)
    global monthDateOfPurchaseEntryBoxTenant
    slashLabel1 = Label(root,bg=primary.data, fg=secondry.data, font = ('Bahnschrift SemiLight',40),text='/').place(relx=0.165,rely=0.385)
    monthDateOfPurchaseEntryBoxTenant = Entry(root, bg=primary.data,fg=secondry.data, width=10,font=(font.data,18),justify='center',relief='flat')
    monthDateOfPurchaseEntryBoxTenant.place(relx=0.110,rely=0.43,anchor=CENTER)
    global yearDateOfPurchaseEntryBoxTenant
    yearDateOfPurchaseEntryBoxTenant = Entry(root, bg=primary.data,fg=secondry.data, width=10,font=(font.data,18),justify='center',relief='flat')
    yearDateOfPurchaseEntryBoxTenant.place(relx=0.24,rely=0.43,anchor=CENTER)
    dateOfPurchaseEntryBoxTenantLabel = Label(root, text='Date of Purchase',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.175,rely=0.35,anchor=CENTER)
    dateOfPurchaseEntryBoxTenantSubText = Label(root, text='In the format MM/YYYY', bg=primary.data, fg=secondry.data, width=50, font=(font.data,9), justify='center', relief='flat').place(relx=0.175, rely=0.4975,anchor=CENTER)

    downPaymentEntryBoxBackground = Label(image = shortNormal, border = 0).place(relx=0.175,rely=0.61,anchor=CENTER)
    global downPaymentEntryBox
    downPaymentEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    downPaymentEntryBox.place(relx=0.175,rely=0.61,anchor=CENTER)
    downPaymentBoxTenantLabel = Label(root, text='Down Payment',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.175,rely=0.53,anchor=CENTER)

    addressEntryBoxbackground = Label(image = shortFat, border = 0).place(relx=0.175,rely=0.84,anchor=CENTER)
    global addressEntryBoxTenant
    addressEntryBoxTenant = Text(root, bg=primary.data,fg=secondry.data, width=22,height = 3,font=(font.data,18),relief='flat')
    addressEntryBoxTenant.place(relx=0.175,rely=0.84,anchor=CENTER)
    addressEntryBoxTenantLabel = Label(root, text='Address',bg=primary.data,fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.175,rely=0.705,anchor=CENTER)

    occupingTenantEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.5,rely=0.25,anchor=CENTER)
    #global occupyingTenantOptions
    openDatabase()
    occpyingTenantsOptionsScrambled = cursor.execute("SELECT tenant_ID FROM tenants WHERE account_ID = '"+scramble(databaseCurrentAccount_ID.data)+"'")
    occpyingTenantsOptionsScrambled = occpyingTenantsOptionsScrambled.fetchall()
    closeDatabase()
    #TODO: need to only show tenants not already located
    global occupyingTenantOptions
    occupyingTenantOptions = []
    for i in range(len(occpyingTenantsOptionsScrambled)):
        occupyingTenant = deScramble(occpyingTenantsOptionsScrambled[i][0])
        occupyingTenantOptions.append(occupyingTenant)
    occupyingTenantOptions.append('None')
    global occupyingTenantMenu
    occupyingTenantMenu = ttk.Combobox(root, value=occupyingTenantOptions, justify=tkinter.CENTER, font=(font.data,18))
    occupyingTenantMenu.current(0)
    occupyingTenantMenu.place(relx=0.5,rely=0.25,anchor=CENTER)
    root.option_add('*TCombobox*Listbox.font', (font.data,14)) 
    occupingTenantEntryLabel = Label(root, text='Occupying Tenant',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.5,rely=0.17,anchor=CENTER)

    mortgageIntrestRateEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.5,rely=0.43,anchor=CENTER)
    global mortgageIntrestRateEntryBoxTenant
    mortgageIntrestRateEntryBoxTenant = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    mortgageIntrestRateEntryBoxTenant.place(relx=0.5,rely=0.43,anchor=CENTER)
    mortgageIntrestRateEntryBoxTenantLabel = Label(root, text='Mortage Intrest Rate (%)',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.5,rely=0.35,anchor=CENTER)
    imortgageIntrestRateEntryBoxTenantLabelSubText = Label(root, text='Enter the Annual Intrest Rate of The Mortgage', bg=primary.data, fg=secondry.data, width=50, font=(font.data,9), justify='center', relief='flat').place(relx=0.5, rely=0.4975,anchor=CENTER)

    mortgageInstallmentsEntryBoxBachground = Label(image = shortNormal, border = 0).place(relx=0.5,rely=0.61,anchor=CENTER)
    global mortgageInstallmentsEntryBox
    mortgageInstallmentsEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    mortgageInstallmentsEntryBox.place(relx=0.5,rely=0.61,anchor=CENTER)
    mortgageInstallmentsEntryBoxLabel = Label(root, text="Mortage Installments size (£)",bg=primary.data, fg=secondry.data, width=24, font=(font.data,18), justify='center',relief='flat').place(relx=0.5,rely=0.53,anchor=CENTER)

    rentEntryBoxBachground2 = Label(image = shortNormal, border = 0).place(relx=0.5,rely=0.79,anchor=CENTER)
    global rentEntryBox2
    rentEntryBox2 = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    rentEntryBox2.place(relx=0.5,rely=0.79,anchor=CENTER)
    rentEntryBoxLabel2 = Label(root, text="Rent (£)",bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.5,rely=0.71,anchor=CENTER)
    rentEntryBoxLabel2SubText = Label(root, text='Enter an approx value if the actual value is not yet known', bg=primary.data, fg=secondry.data, width=50, font=(font.data,9), justify='center', relief='flat').place(relx=0.5, rely=0.8575,anchor=CENTER)


    postCodeEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.825,rely=0.25,anchor=CENTER)
    global postCodeEntryBox
    postCodeEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    postCodeEntryBox.place(relx=0.825,rely=0.25,anchor=CENTER)
    postCodeEntryLabel = Label(root, text='Post Code',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.825,rely=0.17,anchor=CENTER)

    intialLoanIDEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.825,rely=0.43,anchor=CENTER)
    global intialLoanIDEntryBoxTenant
    intialLoanIDEntryBoxTenant = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    intialLoanIDEntryBoxTenant.place(relx=0.825,rely=0.43,anchor=CENTER)
    intialLoanIDEntryBoxTenantLabel = Label(root, text='Initail Loan ID',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.825,rely=0.35,anchor=CENTER)
    intialLoanIDEntryBoxTenantLabelSubText = Label(root, text='This input is unchangable once submitted', bg=primary.data, fg=secondry.data, width=50, font=(font.data,9), justify='center', relief='flat').place(relx=0.825, rely=0.4975,anchor=CENTER)

    mortageSizeEntryBoxBachground = Label(image = shortNormal, border = 0).place(relx=0.825,rely=0.61,anchor=CENTER)
    global mortageSizeEntryBox
    mortageSizeEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    mortageSizeEntryBox.place(relx=0.825,rely=0.61,anchor=CENTER)
    mortageSizeEntryBoxLabel = Label(root, text="Mortgage Size (£)",bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.825,rely=0.53,anchor=CENTER)

    generalNotesEntryBoxBachground = Label(image = shortFat, border = 0).place(relx=0.825,rely=0.84,anchor=CENTER)
    global generalNotesEntryBox
    generalNotesEntryBox = Text(root, bg=primary.data,fg=secondry.data, width=22,height = 3,font=(font.data,18),relief='flat')
    generalNotesEntryBox.place(relx=0.825,rely=0.84,anchor=CENTER)
    generalNotesEntryBoxLabel = Label(root, text="General Notes",bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.825,rely=0.705,anchor=CENTER)

    submitUnitDetailsB = Button(root, text='S U B M I T', font=(font.data,'20','underline','bold'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=addUnit).place(relx=0.5, rely=0.93, anchor=CENTER)

    global newUnitPageCords
    newUnitPageCords = {'unit_ID':{'x':0.175,'y':0.3175},'tenant_ID':{'x':0.5,'y':0.3175},'postcode':{'x':0.825,'y':0.3175},'buy_Month':{'x':0.175,'y':0.4975},'buy_Year':{'x':0.175,'y':0.4975},'dayOfPurchase':{'x':0.175,'y':0.4975},'intrest_Rate':{'x':0.5,'y':0.4975},'loan_ID':{'x':0.825,'y':0.4975},'property_Equity':{'x':0.175,'y':0.6775},'instalments':{'x':0.5,'y':0.6775},'capital_Owed':{'x':0.825,'y':0.6775},'address':{'x':0.175,'y':0.96},'rent':{'x':0.5,'y':0.8575},'general_Notes':{'x':0.825,'y':0.96}}
    root.mainloop()

def addUnit():
    unit_ID = uInputDataObj(unitIDEntryBox.get(),str)
    buy_Month = uInputDataObj(monthDateOfPurchaseEntryBoxTenant.get(),int)
    buy_Year = uInputDataObj(yearDateOfPurchaseEntryBoxTenant.get(),int)
    property_Equity = uInputDataObj(downPaymentEntryBox.get(),float)
    address = uInputDataObj(addressEntryBoxTenant.get('1.0','end-1c'),str)
    tenant_ID = uInputDataObj(occupyingTenantMenu.get(),str)
    intrest_Rate = uInputDataObj(mortgageIntrestRateEntryBoxTenant.get(),float)
    instalments = uInputDataObj(mortgageInstallmentsEntryBox.get(),float)
    postcode = uInputDataObj(postCodeEntryBox.get(),str)
    loan_ID =  uInputDataObj(intialLoanIDEntryBoxTenant.get(),str)
    capital_Owed = uInputDataObj(mortageSizeEntryBox.get(),float)
    general_Notes = uInputDataObj(generalNotesEntryBox.get('1.0','end-1c'),str)
    rent = uInputDataObj(rentEntryBox2.get(),str)

    most_Recent_Valuation = castingTypeCheckFunc(property_Equity.data,property_Equity.prefferredType)+castingTypeCheckFunc(capital_Owed.data,capital_Owed.prefferredType)

    newUnitArray = [unit_ID.data,databaseCurrentAccount_ID.data,tenant_ID.data,most_Recent_Valuation,most_Recent_Valuation,address.data,postcode.data,buy_Month.data,buy_Year.data,property_Equity.data,rent.data,general_Notes.data]
    newLoanArary = [loan_ID.data,unit_ID.data,intrest_Rate.data,instalments.data,capital_Owed.data]
    unitFields = ['unit_ID','account_ID','tenant_ID','property_Equity','most_Recent_Valuation','buy_Price','address','postcode','buy_Month','buy_Year','property_Equity','rent','general_Notes']
    loanFields = ['loan_ID','unit_ID','interest_ID','instalments','capital_Owed']
    total_Fields = unitFields + loanFields

    global dictOfDataValdationResults
    dictOfDataValdationResults = dict.fromkeys(total_Fields)
    dictOfDataValdationResults['unit_ID'] = {'presenceCheck':presenceCheck(unit_ID),'noSpaces':pictureCheck(unit_ID,'',0,0),'uniqueDataCheck':uniqueDataCheck(unit_ID,'unit_ID','units')}
    dictOfDataValdationResults['tenant_ID'] = {'menuOptionCheck':menuOptionCheck(tenant_ID,occupyingTenantOptions)}
    dictOfDataValdationResults['postcode'] = {'presenceCheck':presenceCheck(postcode),'lengthCheck':rangeCheck(postcode,6,11),'mustContainsLetters':containsLetters(postcode),'mustContainNumbers':containsNumbers(postcode)}
    dictOfDataValdationResults['buy_Month'] = {'presenceCheck':presenceCheck(buy_Month),'monthBetween1/12':rangeCheck(buy_Month,1,12)}
    dictOfDataValdationResults['buy_Year'] = {'presenceCheck':presenceCheck(buy_Year),'yearBetween1900/2100':rangeCheck(buy_Year,1900,2100)}
    dictOfDataValdationResults['intrest_Rate'] = {'presenceCheck':presenceCheck(intrest_Rate),'between0/100':rangeCheck(intrest_Rate,0,100)}
    dictOfDataValdationResults['loan_ID'] = {'presenceCheck':presenceCheck(loan_ID),'noSpaces':pictureCheck(unit_ID,'',0,0),'uniqueDataCheck':uniqueDataCheck(loan_ID,'loan_ID','loan')}
    dictOfDataValdationResults['property_Equity'] = {'presenceCheck':presenceCheck(property_Equity),'positiveCheck':rangeCheck(property_Equity,0,None)}
    dictOfDataValdationResults['instalments'] = {'presenceCheck':presenceCheck(instalments),'positiveCheck':rangeCheck(property_Equity,0,None)}
    dictOfDataValdationResults['capital_Owed'] = {'presenceCheck':presenceCheck(capital_Owed),'positiveCheck':rangeCheck(capital_Owed,0,None)}
    dictOfDataValdationResults['address'] = {'presenceCheck':presenceCheck(address),'mustContainsLetters':containsLetters(address)}
    dictOfDataValdationResults['rent'] = {'presenceCheck':presenceCheck(rent),'positiveCheck':rangeCheck(rent,0,None)}
    dictOfDataValdationResults['general_Notes'] = {'presenceCheck':presenceCheck(general_Notes),'mustContainsLetters':containsLetters(general_Notes)}
    newUntCoverUp()
    
    for entryboxData in dictOfDataValdationResults.keys():
        countOfFailedTests = 0
        if dictOfDataValdationResults[entryboxData] != None:
            for test in dictOfDataValdationResults[entryboxData].keys():
                while dictOfDataValdationResults[entryboxData][test] == False and countOfFailedTests == 0:
                    disaplayEM(test,newUnitPageCords[entryboxData]['x'],newUnitPageCords[entryboxData]['y'])
                    countOfFailedTests = countOfFailedTests + 1

    countOfFailedTests = 0
    for entryboxData in dictOfDataValdationResults.keys():
        if dictOfDataValdationResults[entryboxData] != None:
            for test in dictOfDataValdationResults[entryboxData].values():
                if test == False:
                    countOfFailedTests = countOfFailedTests +1

    if countOfFailedTests == 0:
        for i in range(len(newUnitArray)):
            newUnitArray[i] = scramble(newUnitArray[i])
        for i in range(len(newLoanArary)):
            newLoanArary[i] = scramble(newLoanArary[i])

        openDatabase()
        global newLoanInsertionCommand
        newLoanInsertionCommand = """INSERT INTO loan(loan_ID,unit_ID,interest_Rate,instalments,capital_Owed)
        Values(?,?,?,?,?)"""
        cursor.execute(newLoanInsertionCommand,newLoanArary)
        global newUnitInsetionCommand
        newUnitInsetionCommand = """INSERT INTO units(unit_ID,account_ID,tenant_ID,most_Recent_Valuation,buy_Price,address,postcode,buy_Month,buy_Year,property_Equity,rent,general_Notes)
        Values(?,?,?,?,?,?,?,?,?,?,?,?)"""
        cursor.execute(newUnitInsetionCommand,newUnitArray)
        closeDatabase()
        
        displayConfirmation('Properties')

def newUntCoverUp():
    for entryboxData in dictOfDataValdationResults.keys():
        if dictOfDataValdationResults[entryboxData] != None:
            coverUp = Label(root,bg=primary.data,width=65,font=(font.data,7),justify='center').place(relx=newUnitPageCords[entryboxData]['x'],rely=newUnitPageCords[entryboxData]['y'],anchor=CENTER)

#This page is for accessing but not editing data relevant to all tenants e.g. averages aswell as a means of accessing each individual tenant's page
def tenantsPage():
    initialiseWindow()
    root.title('Property managment system - Tenants Page')
    root.configure(bg=secondry.data)
    addPageSeperator()
    topBorder = Label(root, text='Tenants', height=2 ,bg=primary.data, fg = secondry.data, width=42, font=(font.data,40), justify='center').place(relx=0,rely=0)
    displayBackButton()
    global previousPage 
    previousPage = 'Tenants'
    global currentTentantNumber
    currentTentantNumber = 0
    global startValueForAccountListing
    startValueForAccountListing = createTableForTenant(0)
    displayMenuButton()
   
    root.mainloop()

def createTenantXaxisLines(y):
    canvasForTable.create_line(160,y,160,y+76,fill=primary.data)
    canvasForTable.create_line(285,y,285,y+76,fill=primary.data)
    canvasForTable.create_line(505,y,505,y+76,fill=primary.data)  
    canvasForTable.create_line(655,y,655,y+76,fill=primary.data)

def createTenantYaxisLine(y):
    canvasForTable.create_line(0,y,850,y,fill=primary.data)

def addTenantLineOfData(tenant_ID,score,tenant_Email,nlateRent,nOfCompaints,i):
    createTenantXaxisLines(76+76*((i%5)))
    tenant_ID_ColumHeader = Button(canvasForTable, text=tenant_ID, height=2 ,bg=secondry.data, fg = primary.data, font=(font.data,14,'underline'), justify='left',activebackground=secondry.data,border=0,activeforeground=bannedColours['activeTextColor'],command=lambda: tenantPage(tenant_ID))
    tenant_ID_ColumHeader.place(relx = 0.01, rely=0.23+0.15*((i)%5),anchor='w')
    score_ColumHeader = Label(canvasForTable, text=score, height=2 ,bg=secondry.data, fg = primary.data, font=(font.data,14), justify='left').place(relx = 0.20, rely=0.23+0.15*((i)%5),anchor='w')
    email_ColumHeader = Label(canvasForTable, text=tenant_Email, height=2 ,bg=secondry.data, fg = primary.data, font=(font.data,9), justify='left').place(relx = 0.35, rely=0.23+0.15*((i)%5),anchor='w')
    late_Rent_ColumHeader = Label(canvasForTable, text=nlateRent, height=2 ,bg=secondry.data, fg = primary.data, font=(font.data,14), justify='left').place(relx = 0.61, rely=0.23+0.15*((i)%5),anchor='w')
    unresolved_Complaints_ColumHeader = Label(canvasForTable, text=nOfCompaints, height=2 ,bg=secondry.data, fg = primary.data, font=(font.data,14), justify='left').place(relx = 0.79, rely=0.23+0.15*((i)%5),anchor='w')
    createTenantYaxisLine(152+76*((i%5)))

def createTableForTenant(startValueForAccountListing):
    frameToGiveOtheCanvasABorder = Frame(root,width=840,height=500,bg=secondry.data,relief='solid',highlightthickness=2,highlightbackground=primary.data)
    frameToGiveOtheCanvasABorder.place(relx=0.315,rely=0.18)
    frameToGiveOtheCanvasABorder.grid_propagate(False) #Stops frame from changing size to fit the inside of it
    global canvasForTable
    canvasForTable = Canvas(frameToGiveOtheCanvasABorder,width=840,height=500,bg=secondry.data,highlightthickness=0)
    canvasForTable.pack()
    canvasForTable.grid_propagate(False) #Stops frame from changing size to fit the inside of it
    tenant_ID_ColumHeader = Label(canvasForTable, text='Tenant ID', height=1 ,bg=secondry.data, fg = primary.data, font=(font.data,14,'bold'), justify='center').place(relx = 0.04, rely=0.05)
    score_ColumHeader = Label(canvasForTable, text='Score', height=1 ,bg=secondry.data, fg = primary.data, font=(font.data,14,'bold'), justify='center').place(relx = 0.23, rely=0.05)
    email_ColumHeader = Label(canvasForTable, text='Email', height=1 ,bg=secondry.data, fg = primary.data, font=(font.data,14,'bold'), justify='center').place(relx = 0.43, rely=0.05)
    late_Rent_ColumHeader = Label(canvasForTable, text='Late Rents', height=1 ,bg=secondry.data, fg = primary.data, font=(font.data,14,'bold'), justify='center').place(relx = 0.63, rely=0.05)
    unresolved_Complaints_ColumHeader = Label(canvasForTable, text='Unresolved\nComplaints', height=2 ,bg=secondry.data, fg = primary.data, font=(font.data,14,'bold'), justify='center').place(relx = 0.82, rely=0.028,)
    canvasForTable.create_line(160,0,160,76,fill=primary.data)
    canvasForTable.create_line(285,0,285,76,fill=primary.data)
    canvasForTable.create_line(505,0,505,76,fill=primary.data)  
    canvasForTable.create_line(655,0,655,76,fill=primary.data)
    canvasForTable.create_line(0,76,850,76,fill=primary.data)

    # INSERT INTO complaints (complaint_ID, tenant_ID, month, year, complaint_Nature, resoltion)
    # VALUES ('newComplaintID','TA1','12','2019','testing','This is solved') #SQL to add a new complaint

    openDatabase()
    tenantBriefInfoD = cursor.execute("SELECT tenant_ID, score, tenant_Email FROM tenants WHERE account_ID = '" + str(scramble(databaseCurrentAccount_ID.data)) + str("'")) 
    tenantBriefInfo = tenantBriefInfoD.fetchall()
    closeDatabase()
    if len(tenantBriefInfo) != 0: #If there is a tenants in the database
        #TODO: need to order tenant's by descrambled tenant_ID
        i = startValueForAccountListing
        count = 0
        while i < len(tenantBriefInfo) and count < 5:
            tenant_ID = deScramble(tenantBriefInfo[i][0])
            score = deScramble(tenantBriefInfo[i][1])
            tenant_Email = deScramble(tenantBriefInfo[i][2])
            openDatabase()
            complaintsIDsD = cursor.execute("SELECT complaint_ID FROM complaints WHERE tenant_ID = '" + str(scramble(tenant_ID))+ "'")
            complaintsIDs = complaintsIDsD.fetchall()
            if len(complaintsIDs) != 0:
                nOfCompaints = 0
                for x in range(len(complaintsIDs)):
                    complaintResolution = deScramble(cursor.execute("SELECT resoltion FROM complaints WHERE complaint_ID = '" + str(complaintsIDs[x][0]) + "'").fetchall()[0][0])
                    if complaintResolution == None:
                        nOfCompaints = nOfCompaints + 1        
            else:
                nOfCompaints = 0
            nlateRent = 0
            lateRent = cursor.execute("SELECT rent_Late FROM units_Monthly WHERE tenant_ID = '" + str(scramble(tenant_ID)) + "'").fetchall()
            if len(lateRent) != 0:
                for x in range(len(lateRent)):
                    if deScramble(lateRent[x][0]) == True:
                        nlateRent = nlateRent + 1
            addTenantLineOfData(tenant_ID,score,tenant_Email,nlateRent,nOfCompaints,i)
            i = i + 1
            count = count + 1
            global currentTentantNumber
            currentTentantNumber = currentTentantNumber + 1
        if currentTentantNumber != len(tenantBriefInfo):
            downButton = Button(canvasForTable, text='Down',height=1,bg=secondry.data, fg = primary.data, font=(font.data,16), justify='center',border=0,activeforeground=bannedColours['activeTextColor'],activebackground=secondry.data,command= lambda:changeTableHieghtButtonCommand(currentTentantNumber)).place(relx=0.4,rely=0.96,anchor='center')
        else:
            downButtonCover = Label(canvasForTable,height=1,bg=secondry.data,font=(font.data,16), justify='center',border=0).place(relx=0.4,rely=0.96,anchor='center')
        if currentTentantNumber > 5:
            upButton = Button(canvasForTable, text='Up',height=1,bg=secondry.data, fg = primary.data, font=(font.data,16), justify='center',border=0,activeforeground=bannedColours['activeTextColor'],activebackground=secondry.data,command= lambda:changeTableHieghtButtonCommand(currentTentantNumber-count-5)).place(relx=0.6,rely=0.96,anchor='center')
        else:
            downButtonCover = Label(canvasForTable,height=1,bg=secondry.data,font=(font.data,16), justify='center',border=0).place(relx=0.6,rely=0.96,anchor='center')
    else:
        noTenantLabel = Label(canvasForTable, text='You have no exsisting tenants', height=3 ,bg=secondry.data, fg = primary.data, font=(font.data,14), justify='center').place(relx=0.5,rely=0.5,anchor='center')
    return startValueForAccountListing

def changeTableHieghtButtonCommand(inputNumber):
    global currentTentantNumber
    currentTentantNumber = inputNumber
    createTableForTenant(inputNumber)

def newTenantPage():
    initialiseWindow()
    root.title('Property managment system - Add New Tenant Page')
    topBorder = Label(root, text='Add Tenant', height=2 ,bg=primary.data, fg = secondry.data, width=42, font=(font.data,40), justify='center').place(relx=0,rely=0)
    topMessage = Label(root, text='To add a tenant to a unit add go the edit unit page and select the tenant from the tenant menu',bg=primary.data, fg = secondry.data, font=(font.data,15), justify='center').place(relx=0.5,rely=0.02,anchor='center')
    displayBackButton()
    global previousPage
    previousPage = 'Add Tenant'
    displayMenuButton()
    
    shortNormal = PhotoImage(file = "Short-Normal.PNG")
    shortFat = PhotoImage(file = "Short-Fat.PNG")
    tenantIDEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.175,rely=0.25,anchor=CENTER)
    global tenantIDEntryBox
    tenantIDEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    tenantIDEntryBox.place(relx=0.175,rely=0.25,anchor=CENTER)
    tenantIDEntryLabel = Label(root, text='Tenant ID',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.175,rely=0.17,anchor=CENTER)
    tenantIDEntryBoxSubText = Label(root, text='This input is unchangable once submitted', bg=primary.data, fg=secondry.data, width=50, font=(font.data,9), justify='center', relief='flat').place(relx=0.175, rely=0.3175,anchor=CENTER)

    tileEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.175,rely=0.43,anchor=CENTER)
    global titleEntryBoxTenant
    titleEntryBoxTenant = Entry(root, bg=primary.data,fg=secondry.data, width=23,font=(font.data,18),justify='center',relief='flat')
    titleEntryBoxTenant.place(relx=0.175,rely=0.43,anchor=CENTER)
    titleEntryBoxTenantLabel = Label(root, text='Title',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.175,rely=0.35,anchor=CENTER)

    dateOfEntryBoxBackground = Label(image = shortNormal, border = 0).place(relx=0.175,rely=0.61,anchor=CENTER)
    slashLabel1 = Label(root,bg=primary.data, fg=secondry.data, font = ('Bahnschrift SemiLight',40),text='/').place(relx=0.125,rely=0.565)
    slashLabel2 = Label(root,bg=primary.data, fg=secondry.data, font = ('Bahnschrift SemiLight',40),text='/').place(relx=0.205,rely=0.565)
    global dayEntryBox
    dayEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=6, font=(font.data,18),justify='center',relief='flat')
    dayEntryBox.place(relx=0.093,rely=0.61,anchor=CENTER)
    global monthEntryBox
    monthEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=5, font=(font.data,18),justify='center',relief='flat')
    monthEntryBox.place(relx=0.177,rely=0.61, anchor=CENTER)
    global yearEntryBox
    yearEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=6, font=(font.data,18),justify='center',relief='flat')
    yearEntryBox.place(relx=0.26,rely=0.61, anchor=CENTER)
    dateEntryBoxTenantLabel = Label(root, text='Date of birth',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.175,rely=0.53,anchor=CENTER)
    dateEntryBoxSubText = Label(root, text='In the form DD/MM/YYYY', bg=primary.data, fg=secondry.data, width=50, font=(font.data,9), justify='center', relief='flat').place(relx=0.175, rely=0.6775,anchor=CENTER)

    geneneralNotesEntryBoxbackground = Label(image = shortFat, border = 0).place(relx=0.175,rely=0.84,anchor=CENTER)
    global geneneralNotesEntryBoxTenant
    geneneralNotesEntryBoxTenant = Text(root, bg=primary.data,fg=secondry.data, width=22,height = 3,font=(font.data,18),relief='flat')
    geneneralNotesEntryBoxTenant.place(relx=0.175,rely=0.84,anchor=CENTER)
    geneneralNotesEntryBoxTenantLabel = Label(root, text='General notes',bg=primary.data,fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.175,rely=0.705,anchor=CENTER)

    surnameEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.5,rely=0.25,anchor=CENTER)
    global surnameEntryBoxTenant
    surnameEntryBoxTenant = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    surnameEntryBoxTenant.place(relx=0.5,rely=0.25,anchor=CENTER)
    surnameEntryLabel = Label(root, text='Surname',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.5,rely=0.17,anchor=CENTER)

    nOtherOccupantsEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.5,rely=0.43,anchor=CENTER)
    global nOtherOccupantsEntryBoxTenant
    nOtherOccupantsEntryBoxTenant = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    nOtherOccupantsEntryBoxTenant.place(relx=0.5,rely=0.43,anchor=CENTER)
    nOtherOccupantsEntryBoxTenantLabel = Label(root, text='Total Occupants',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.5,rely=0.35,anchor=CENTER)

    tenantsDepositEntryBoxBachground = Label(image = shortNormal, border = 0).place(relx=0.5,rely=0.61,anchor=CENTER)
    global tenantsDepositEntryBox
    tenantsDepositEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    tenantsDepositEntryBox.place(relx=0.5,rely=0.61,anchor=CENTER)
    tenantsDepositEntryBoxLabel = Label(root, text="Tenant's deposit (£)",bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.5,rely=0.53,anchor=CENTER)

    firstnameEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.825,rely=0.25,anchor=CENTER)
    global firstnameEntryBox
    firstnameEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    firstnameEntryBox.place(relx=0.825,rely=0.25,anchor=CENTER)
    firstnameEntryLabel = Label(root, text='Forename',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.825,rely=0.17,anchor=CENTER)

    startOfLeaseDateEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.825,rely=0.43,anchor=CENTER)
    slashLabel2 = Label(root,bg=primary.data, fg=secondry.data, font = ('Bahnschrift SemiLight',40),text='/').place(relx=0.815,rely=0.385)
    global startOfLeaseDateMonthEntryBoxTenant
    startOfLeaseDateMonthEntryBoxTenant = Entry(root, bg=primary.data,fg=secondry.data, width=10, font=(font.data,18),justify='center',relief='flat')
    startOfLeaseDateMonthEntryBoxTenant.place(relx=0.76,rely=0.43,anchor=CENTER)
    global startOfLeaseDateYearEntryBoxTenant
    startOfLeaseDateYearEntryBoxTenant = Entry(root, bg=primary.data,fg=secondry.data, width=10, font=(font.data,18),justify='center',relief='flat')
    startOfLeaseDateYearEntryBoxTenant.place(relx=0.89,rely=0.43,anchor=CENTER)
    startOfLeaseDateEntryBoxTenantLabel = Label(root, text='Start of lease date',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.825,rely=0.35,anchor=CENTER)
    startOfLeaseDateEntryBoxSubText = Label(root, text='In the form MM/YYYY', bg=primary.data, fg=secondry.data, width=50, font=(font.data,9), justify='center', relief='flat').place(relx=0.825, rely=0.4975,anchor=CENTER)

    scoreEntryBoxBachground = Label(image = shortNormal, border = 0).place(relx=0.825,rely=0.61,anchor=CENTER)
    global scoreEntryBox
    scoreEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    scoreEntryBox.insert(END,'100')
    scoreEntryBox.place(relx=0.825,rely=0.61,anchor=CENTER)
    scoreEntryBoxLabel = Label(root, text="Score",bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.825,rely=0.53,anchor=CENTER)
    scoreEntryBoxSubText = Label(root, text='Keep 100 unless you have previous experience with this tenant', bg=primary.data, fg=secondry.data, width=50, font=(font.data,9), justify='center', relief='flat').place(relx=0.825, rely=0.6756,anchor=CENTER)

    emailEntryBoxBachground = Label(image = shortNormal, border = 0).place(relx=0.825,rely=0.79,anchor=CENTER)
    global emailEntryBox
    emailEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    emailEntryBox.place(relx=0.825,rely=0.79,anchor=CENTER)
    emailEntryBoxLabel = Label(root, text="Tenant email",bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.825,rely=0.71,anchor=CENTER)

    global newTenantEntryBoxCords
    newTenantEntryBoxCords = {'tenant_Email':{'x':0.825,'y':0.8575},'tenant_ID':{'x':0.175,'y':0.3175},'title':{'x':0.175,'y':0.4975},'day':{'x':0.175,'y':0.6775},'month':{'x':0.175,'y':0.6775},'year':{'x':0.175,'y':0.6775},'gerneral_Notes':{'x':0.175,'y':0.96},'last_Name':{'x':0.5,'y':0.3175},'total_Residents':{'x':0.5,'y':0.4975},'deposit':{'x':0.5,'y':0.6775},'first_Name':{'x':0.825,'y':0.3175},'startMonth':{'x':0.825,'y':0.4975},'startYear':{'x':0.825,'y':0.4975},'score':{'x':0.825,'y':0.6775}}

    submitLoginDetailsB = Button(root, text='S U B M I T', font=(font.data,'20','underline','bold'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=addTenant).place(relx=0.5, rely=0.93, anchor=CENTER)

    root.mainloop()

def taxPage():
    initialiseWindow()
    root.title('Property managment system - Tax Page')
    topBorder = Label(root, text='Tax', height=2 ,bg=primary.data, fg = secondry.data, width=42, font=(font.data,40), justify='center').place(relx=0,y=-20)
    displayBackButton()
    global previousPage
    previousPage = 'Tax'
    displayMenuButton()
    shortNormal = PhotoImage(file = "Short-Normal.PNG")

    personalIncomeBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.175,rely=0.20,anchor=CENTER)
    global personalIncomeEntryBox
    personalIncomeEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    openDatabase()
    primaryColourD = cursor.execute("SELECT personal_Income_Allowence FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.getData())+"'")
    data_To_Descrmable = primaryColourD.fetchall()[0][0]
    primaryColourD = deScramble(data_To_Descrmable)
    personalIncomeEntryBox.insert(END,primaryColourD)
    closeDatabase()
    personalIncomeEntryBox.place(relx=0.175,rely=0.20,anchor=CENTER)
    primaryHexEntryLabel = Label(root, text='Income personal allowance (£)',bg=primary.data, fg=secondry.data, width=33, font=(font.data,18), justify='center',relief='flat').place(relx=0.175,rely=0.12,anchor=CENTER)

    basicIncomeTaxRateBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.175,rely=0.375,anchor=CENTER)
    global basicIncomeTaxRateEntryBox
    basicIncomeTaxRateEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    openDatabase()
    primaryColourD = cursor.execute("SELECT basic_Income_Rate FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.getData())+"'")
    data_To_Descrmable = primaryColourD.fetchall()[0][0]
    primaryColourD = deScramble(data_To_Descrmable)
    basicIncomeTaxRateEntryBox.insert(END,primaryColourD)
    closeDatabase()
    basicIncomeTaxRateEntryBox.place(relx=0.175,rely=0.375,anchor=CENTER)
    primaryHexEntryLabel = Label(root, text='Basic income tax rate (%)',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.175,rely=0.295,anchor=CENTER)

    highIncomeTaxRateBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.175,rely=0.55,anchor=CENTER)
    global highIncomeTaxRateEntryBox
    highIncomeTaxRateEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    openDatabase()
    primaryColourD = cursor.execute("SELECT high_Income_Rate FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.getData())+"'")
    data_To_Descrmable = primaryColourD.fetchall()[0][0]
    primaryColourD = deScramble(data_To_Descrmable)
    highIncomeTaxRateEntryBox.insert(END,primaryColourD)
    closeDatabase()
    highIncomeTaxRateEntryBox.place(relx=0.175,rely=0.55,anchor=CENTER)
    primaryHexEntryLabel = Label(root, text='High income tax rate (%)',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.175,rely=0.47,anchor=CENTER)

    additionalIncomeTaxRateBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.175,rely=0.725,anchor=CENTER)
    global additionalIncomeTaxRateEntryBox
    additionalIncomeTaxRateEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    openDatabase()
    primaryColourD = cursor.execute("SELECT additional_Income_Rate FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.getData())+"'")
    data_To_Descrmable = primaryColourD.fetchall()[0][0]
    primaryColourD = deScramble(data_To_Descrmable)
    additionalIncomeTaxRateEntryBox.insert(END,primaryColourD)
    closeDatabase()
    additionalIncomeTaxRateEntryBox.place(relx=0.175,rely=0.725,anchor=CENTER)
    primaryHexEntryLabel = Label(root, text='Additional income tax rate (%)',bg=primary.data, fg=secondry.data, width=33, font=(font.data,18), justify='center',relief='flat').place(relx=0.175,rely=0.645,anchor=CENTER)

    natInsuranceBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.175,rely=0.9,anchor=CENTER)
    global natInsuranceEntryBox
    natInsuranceEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    openDatabase()
    primaryColourD = cursor.execute("SELECT national_Insurance_Due FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.getData())+"'")
    data_To_Descrmable = primaryColourD.fetchall()[0][0]
    primaryColourD = deScramble(data_To_Descrmable)
    natInsuranceEntryBox.insert(END,primaryColourD)
    closeDatabase()
    natInsuranceEntryBox.place(relx=0.175,rely=0.9,anchor=CENTER)
    primaryHexEntryLabel = Label(root, text='National insurance due (£)',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.175,rely=0.82,anchor=CENTER)

    basicRateCapGainsAllowenceBackGround = Label(image = shortNormal, border = 0).place(relx=0.5,rely=0.20,anchor=CENTER)
    global basicRateCapGainsAllowenceEntryBox
    basicRateCapGainsAllowenceEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    openDatabase()
    primaryColourD = cursor.execute("SELECT basic_Capital_Gains_Allowence FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.getData())+"'")   
    data_To_Descrmable = primaryColourD.fetchall()[0][0]
    primaryColourD = deScramble(data_To_Descrmable)
    basicRateCapGainsAllowenceEntryBox.insert(END,primaryColourD)
    closeDatabase()
    basicRateCapGainsAllowenceEntryBox.place(relx=0.5,rely=0.20,anchor=CENTER)
    primaryHexEntryLabel = Label(root, text='Basic rate capital gains allowance (£)',bg=primary.data, fg=secondry.data, width=30, font=(font.data,15), justify='center',relief='flat').place(relx=0.5,rely=0.12,anchor=CENTER)

    basicIncomeCutOffBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.5,rely=0.375,anchor=CENTER)
    global basicIncomeCutOffEntryBox
    basicIncomeCutOffEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    openDatabase()
    primaryColourD = cursor.execute("SELECT basic_Income_Cut_Off FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.getData())+"'")
    data_To_Descrmable = primaryColourD.fetchall()[0][0]
    primaryColourD = deScramble(data_To_Descrmable)
    basicIncomeCutOffEntryBox.insert(END,primaryColourD)
    closeDatabase()
    basicIncomeCutOffEntryBox.place(relx=0.5,rely=0.375,anchor=CENTER)
    primaryHexEntryLabel = Label(root, text='Basic income cut off (£)',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.5,rely=0.295,anchor=CENTER)

    highIncomeCutOffBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.5,rely=0.55,anchor=CENTER)
    global highIncomeCutOffEntryBox
    highIncomeCutOffEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    openDatabase()
    primaryColourD = cursor.execute("SELECT high_Income_Cut_Off FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.getData())+"'")
    data_To_Descrmable = primaryColourD.fetchall()[0][0]
    primaryColourD = deScramble(data_To_Descrmable)
    highIncomeCutOffEntryBox.insert(END,primaryColourD)
    closeDatabase()
    highIncomeCutOffEntryBox.place(relx=0.5,rely=0.55,anchor=CENTER)
    primaryHexEntryLabel = Label(root, text='High income cut off (£)',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.5,rely=0.47,anchor=CENTER)

    corperationTaxRateBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.5,rely=0.725,anchor=CENTER)
    global corperationTaxRateEntryBox
    corperationTaxRateEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    openDatabase()
    primaryColourD = cursor.execute("SELECT corporation_Rate FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.getData())+"'")
    data_To_Descrmable = primaryColourD.fetchall()[0][0]
    primaryColourD = deScramble(data_To_Descrmable)
    corperationTaxRateEntryBox.insert(END,primaryColourD)
    closeDatabase()
    corperationTaxRateEntryBox.place(relx=0.5,rely=0.725,anchor=CENTER)
    primaryHexEntryLabel = Label(root, text='Corporation tax rate (%)',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.5,rely=0.645,anchor=CENTER)

    corporationCapitalGainsBackGround = Label(image = shortNormal, border = 0).place(relx=0.825,rely=0.20,anchor=CENTER)
    global corporationCapitalGainsEntryBox
    corporationCapitalGainsEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    openDatabase()
    primaryColourD = cursor.execute("SELECT corporation_Capital_Gains_Rate FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.getData())+"'")   
    data_To_Descrmable = primaryColourD.fetchall()[0][0]
    primaryColourD = deScramble(data_To_Descrmable)
    corporationCapitalGainsEntryBox.insert(END,primaryColourD)
    closeDatabase()
    corporationCapitalGainsEntryBox.place(relx=0.825,rely=0.20,anchor=CENTER)
    primaryHexEntryLabel = Label(root, text='Corporation capital gains tax rate (%)',bg=primary.data, fg=secondry.data, width=30, font=(font.data,15), justify='center',relief='flat').place(relx=0.825,rely=0.12,anchor=CENTER)

    basicIncomeCapaitalTaxRateBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.825,rely=0.375,anchor=CENTER)
    global basicIncomeCapaitalTaxRateEntryBox
    basicIncomeCapaitalTaxRateEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    openDatabase()
    primaryColourD = cursor.execute("SELECT basic_Capital_Gains_Rate FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.getData())+"'")
    data_To_Descrmable = primaryColourD.fetchall()[0][0]
    primaryColourD = deScramble(data_To_Descrmable)
    basicIncomeCapaitalTaxRateEntryBox.insert(END,primaryColourD)
    closeDatabase()
    basicIncomeCapaitalTaxRateEntryBox.place(relx=0.825,rely=0.375,anchor=CENTER)
    primaryHexEntryLabel = Label(root, text='Basic income capital gains rate (%)',bg=primary.data, fg=secondry.data, width=33, font=(font.data,15), justify='center',relief='flat').place(relx=0.825,rely=0.295,anchor=CENTER)

    highIncomeCapaitalTaxRateBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.825,rely=0.55,anchor=CENTER)
    global highIncomeCapaitalTaxRateEntryBox
    highIncomeCapaitalTaxRateEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    openDatabase()
    primaryColourD = cursor.execute("SELECT high_Capital_Gains_Rate FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.getData())+"'")
    data_To_Descrmable = primaryColourD.fetchall()[0][0]
    primaryColourD = deScramble(data_To_Descrmable)
    highIncomeCapaitalTaxRateEntryBox.insert(END,primaryColourD)
    closeDatabase()
    highIncomeCapaitalTaxRateEntryBox.place(relx=0.825,rely=0.55,anchor=CENTER)
    primaryHexEntryLabel = Label(root, text='High income capital gains rate (%)',bg=primary.data, fg=secondry.data, width=33, font=(font.data,15), justify='center',relief='flat').place(relx=0.825,rely=0.47,anchor=CENTER)

    additionalIncomeCapaitalTaxRateBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.825,rely=0.725,anchor=CENTER)
    global additionalIncomeCapaitalTaxRateEntryBix
    additionalIncomeCapaitalTaxRateEntryBix = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    openDatabase()
    primaryColourD = cursor.execute("SELECT additional_Capital_Gains_Rate FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.getData())+"'")
    data_To_Descrmable = primaryColourD.fetchall()[0][0]
    primaryColourD = deScramble(data_To_Descrmable)
    additionalIncomeCapaitalTaxRateEntryBix.insert(END,primaryColourD)
    closeDatabase()
    additionalIncomeCapaitalTaxRateEntryBix.place(relx=0.825,rely=0.725,anchor=CENTER)
    primaryHexEntryLabel = Label(root, text='Additional income capital gains rate (%)',bg=primary.data, fg=secondry.data, width=33, font=(font.data,15), justify='center',relief='flat').place(relx=0.825,rely=0.645,anchor=CENTER)

    otherIncomeBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.825,rely=0.9,anchor=CENTER)
    global otherIncomeEntryBox
    otherIncomeEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    openDatabase()
    primaryColourD = cursor.execute("SELECT other_Income_Estimate FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.getData())+"'")
    data_To_Descrmable = primaryColourD.fetchall()[0][0]
    primaryColourD = deScramble(data_To_Descrmable)
    otherIncomeEntryBox.insert(END,primaryColourD)
    closeDatabase()
    otherIncomeEntryBox.place(relx=0.825,rely=0.9,anchor=CENTER)
    primaryHexEntryLabel = Label(root, text='Other income estimate (£)',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.825,rely=0.82,anchor=CENTER)

    submitUnitDetailsB = Button(root, text='S U B M I T', font=(font.data,'20','underline','bold'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=updateTax).place(relx=0.5, rely=0.9, anchor=CENTER)

    global updateTaxCords
    updateTaxCords = {'personal_Income_Allowence':{'x':0.175,'y':0.2675},'other_Income_Estimate':{'x':0.825,'y':0.9675}, 'basic_Income_Rate':{'x':0.175,'y':0.4425}, 'high_Income_Rate':{'x':0.175,'y':0.6175}, 'additional_Income_Rate':{'x':0.175,'y':0.7925}, 'basic_Income_Cut_Off':{'x':0.5,'y':0.2675}, 'high_Income_Cut_Off':{'x':0.5,'y':0.4425}, 'corporation_Rate':{'x':0.5,'y':0.6175}, 'basic_Capital_Gains_Rate':{'x':0.5,'y':0.7925}, 'basic_Capital_Gains_Allowence':{'x':0.825,'y':0.2675}, 'high_Capital_Gains_Rate':{'x':0.825,'y':0.4425}, 'additional_Capital_Gains_Rate':{'x':0.825,'y':0.6175}, 'corporation_Capital_Gains_Rate':{'x':0.825,'y':0.7925}, 'national_Insurance_Due':{'x':0.175,'y':0.9675}}
    root.mainloop()

def updateTax():
    personal_Income_Allowence = uInputDataObj(personalIncomeEntryBox.get(),float)
    basic_Income_Rate = uInputDataObj(basicIncomeTaxRateEntryBox.get(),float)
    high_Income_Rate = uInputDataObj(highIncomeTaxRateEntryBox.get(),float)
    additional_Income_Rate = uInputDataObj(additionalIncomeTaxRateEntryBox.get(),float)
    national_Insurance_Due = uInputDataObj(natInsuranceEntryBox.get(),float)
    basic_Capital_Gains_Allowence = uInputDataObj(basicRateCapGainsAllowenceEntryBox.get(),float)
    basic_Income_Cut_Off = uInputDataObj(basicIncomeCutOffEntryBox.get(),float)
    high_Income_Cut_Off = uInputDataObj(highIncomeCutOffEntryBox.get(),float)
    corporation_Rate = uInputDataObj(corperationTaxRateEntryBox.get(),float)
    corporation_Capital_Gains_Rate = uInputDataObj(corporationCapitalGainsEntryBox.get(),float)
    basic_Capital_Gains_Rate = uInputDataObj(basicIncomeCapaitalTaxRateEntryBox.get(),float)
    high_Capital_Gains_Rate = uInputDataObj(highIncomeCapaitalTaxRateEntryBox.get(),float)
    additional_Capital_Gains_Rate = uInputDataObj(additionalIncomeCapaitalTaxRateEntryBix.get(),float)
    other_Income_Estimate = uInputDataObj(otherIncomeEntryBox.get(),float)
    redoConfigureAccountSettingsVariables()

    createAccountArray = [databaseCurrentAccount_ID.data,password.data,recovery_Email.data,first_Name.data,last_Name.data, operation_Type.data, title.data, getTaxRate(databaseCurrentAccount_ID.data),personal_Income_Allowence.data,other_Income_Estimate.data,basic_Income_Rate.data, high_Income_Rate.data, additional_Income_Rate.data, basic_Income_Cut_Off.data, high_Income_Cut_Off.data, corporation_Rate.data, basic_Capital_Gains_Rate.data, basic_Capital_Gains_Allowence.data, high_Capital_Gains_Rate.data, additional_Capital_Gains_Rate.data, corporation_Capital_Gains_Rate.data,national_Insurance_Due.data, primary.data, secondry.data, tertiary.data, font.data]
    accountFields = ['account_ID', 'password', 'recovery_Email', 'first_Name', 'last_Name', 'operation_Type', 'title', 'tax_Rate','personal_Income_Allowence','other_Income_Estimate', 'basic_Income_Rate', 'high_Income_Rate', 'additional_Income_Rate', 'basic_Income_Cut_Off', 'high_Income_Cut_Off', 'corporation_Rate', 'basic_Capital_Gains_Rate', 'basic_Capital_Gains_Allowence', 'high_Capital_Gains_Rate', 'additional_Capital_Gains_Rate', 'corporation_Capital_Gains_Rate', 'national_Insurance_Due', 'primary_Colour', 'secondry_Colour', 'tertiary_Colour','font'] 

    global dictOfDataValdationResults
    dictOfDataValdationResults = dict.fromkeys(accountFields)
    dictOfDataValdationResults['personal_Income_Allowence'] = {'presenceCheck':presenceCheck(personal_Income_Allowence),'positiveCheck':rangeCheck(personal_Income_Allowence,0,None)}
    dictOfDataValdationResults['basic_Income_Rate'] = {'presenceCheck':presenceCheck(basic_Income_Rate),'between0/100':rangeCheck(basic_Income_Rate,0,100)}
    dictOfDataValdationResults['high_Income_Rate'] = {'presenceCheck':presenceCheck(high_Income_Rate),'between0/100':rangeCheck(high_Income_Rate,0,100)}
    dictOfDataValdationResults['additional_Income_Rate'] = {'presenceCheck':presenceCheck(additional_Income_Rate),'between0/100':rangeCheck(additional_Income_Rate,0,100)}
    dictOfDataValdationResults['national_Insurance_Due'] = {'presenceCheck':presenceCheck(national_Insurance_Due),'positiveCheck':rangeCheck(national_Insurance_Due,0,None)}
    dictOfDataValdationResults['basic_Capital_Gains_Allowence'] = {'presenceCheck':presenceCheck(basic_Capital_Gains_Allowence),'positiveCheck':rangeCheck(basic_Capital_Gains_Allowence,0,None)}
    dictOfDataValdationResults['basic_Income_Cut_Off'] = {'presenceCheck':presenceCheck(basic_Income_Cut_Off),'positiveCheck':rangeCheck(basic_Income_Cut_Off,0,None)}
    dictOfDataValdationResults['high_Income_Cut_Off'] =  {'presenceCheck':presenceCheck(high_Income_Cut_Off),'positiveCheck':rangeCheck(high_Income_Cut_Off,0,None)}
    dictOfDataValdationResults['corporation_Rate'] = {'presenceCheck':presenceCheck(corporation_Rate),'between0/100':rangeCheck(corporation_Rate,0,100)}
    dictOfDataValdationResults['corporation_Capital_Gains_Rate'] = {'presenceCheck':presenceCheck(corporation_Capital_Gains_Rate),'between0/100':rangeCheck(corporation_Capital_Gains_Rate,0,100)}
    dictOfDataValdationResults['basic_Capital_Gains_Rate'] = {'presenceCheck':presenceCheck(basic_Capital_Gains_Rate),'between0/100':rangeCheck(basic_Capital_Gains_Rate,0,100)}
    dictOfDataValdationResults['high_Capital_Gains_Rate'] = {'presenceCheck':presenceCheck(high_Capital_Gains_Rate),'between0/100':rangeCheck(high_Capital_Gains_Rate,0,100)}
    dictOfDataValdationResults['additional_Capital_Gains_Rate'] = {'presenceCheck':presenceCheck(additional_Capital_Gains_Rate),'between0/100':rangeCheck(additional_Capital_Gains_Rate,0,100)}
    dictOfDataValdationResults['other_Income_Estimate'] =  {'presenceCheck':presenceCheck(other_Income_Estimate),'positiveCheck':rangeCheck(other_Income_Estimate,0,None)}
    taxPageCoverUpErrorMessage()

    for entryboxData in dictOfDataValdationResults.keys():
        countOfFailedTests = 0
        if dictOfDataValdationResults[entryboxData] != None:
            for test in dictOfDataValdationResults[entryboxData].keys():
                while dictOfDataValdationResults[entryboxData][test] == False and countOfFailedTests == 0:
                    disaplayEM(test,updateTaxCords[entryboxData]['x'],updateTaxCords[entryboxData]['y'])
                    countOfFailedTests = countOfFailedTests + 1

    countOfFailedTests = 0
    for entryboxData in dictOfDataValdationResults.keys():
        if dictOfDataValdationResults[entryboxData] != None:
            for test in dictOfDataValdationResults[entryboxData].values():
                if test == False:
                    countOfFailedTests = countOfFailedTests +1


    if countOfFailedTests == 0:
        openDatabase()
        accocountUpdateCommand = ("UPDATE accounts SET personal_Income_Allowence = '" + str(scramble(personal_Income_Allowence.data)) + "', basic_Income_Rate = '" + str(scramble(basic_Income_Rate.data)) + "', high_Income_Rate = '" + str(scramble(high_Income_Rate.data)) + "', additional_Income_Rate = '" + str(scramble(additional_Income_Rate.data)) + "', national_Insurance_Due = '" + str(scramble(national_Insurance_Due.data)) + "', basic_Capital_Gains_Allowence = '" + str(scramble(basic_Capital_Gains_Allowence.data)) + "', basic_Income_Cut_Off = '" + str(scramble(basic_Income_Cut_Off.data)) + "', high_Income_Cut_Off = '" + str(scramble(high_Income_Cut_Off.data)) + "', corporation_Rate = '" + str(scramble(corporation_Rate.data)) + "', corporation_Capital_Gains_Rate = '" + str(scramble(corporation_Capital_Gains_Rate.data)) + "', basic_Capital_Gains_Rate = '" + str(scramble(basic_Capital_Gains_Rate.data)) + "', high_Capital_Gains_Rate = '" + str(scramble(high_Capital_Gains_Rate.data)) + "', additional_Capital_Gains_Rate = '" + str(scramble(additional_Capital_Gains_Rate.data)) + "', other_Income_Estimate = '" + str(scramble(other_Income_Estimate.data)) + "' WHERE account_ID = '" + str(scramble(databaseCurrentAccount_ID.data)) +"'")
        cursor.execute(accocountUpdateCommand)
        closeDatabase()

        displayConfirmation('Tax')

def taxPageCoverUpErrorMessage():
    for entryboxData in dictOfDataValdationResults.keys():
        if dictOfDataValdationResults[entryboxData] != None:
            coverUp = Label(root,bg=primary.data,width=75,font=(font.data,7),justify='center').place(relx=updateTaxCords[entryboxData]['x'],rely=updateTaxCords[entryboxData]['y'],anchor=CENTER)

def settingsPage():
    initialiseWindow()
    root.title('Property managment system - Settings Page')
    topBorder = Label(root, text='Settings', height=2 ,bg=primary.data, fg = secondry.data, width=42, font=(font.data,40), justify='center').place(relx=0,rely=0)
    displayBackButton()
    global previousPage
    previousPage = 'Settings'
    displayMenuButton()
    shortNormal = PhotoImage(file = "Short-Normal.PNG")
    longNormal = PhotoImage(file = "Long-Normal.PNG")

    primaryHexEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.175,rely=0.25,anchor=CENTER)
    global primaryHexEntryBox
    primaryHexEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    openDatabase()
    primaryColourD = cursor.execute("SELECT primary_Colour FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.getData())+"'")
    data_To_Descrmable = primaryColourD.fetchall()[0][0]
    primaryColourD = deScramble(data_To_Descrmable).upper()
    primaryHexEntryBox.insert(END,primaryColourD)
    closeDatabase()
    primaryHexEntryBox.place(relx=0.175,rely=0.25,anchor=CENTER)
    primaryHexEntryLabel = Label(root, text='Primary Colour Hex Code',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.175,rely=0.17,anchor=CENTER)


    secondryHexEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.175,rely=0.43,anchor=CENTER)
    global secondryHexEntryBox
    secondryHexEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    openDatabase()
    primaryColourD = cursor.execute("SELECT secondry_Colour FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.getData())+"'")
    data_To_Descrmable = primaryColourD.fetchall()[0][0]
    secondryHexData = deScramble(data_To_Descrmable).upper()
    secondryHexEntryBox.insert(END,secondryHexData)
    closeDatabase()
    secondryHexEntryBox.place(relx=0.175,rely=0.43,anchor=CENTER)
    secondryHexEntryBoxLabel = Label(root, text='Secondry Colour Hex Code',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.175,rely=0.35,anchor=CENTER)

    tertiaryHexEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.175,rely=0.61,anchor=CENTER)
    global tertiaryHexEntryBox
    tertiaryHexEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    openDatabase()
    tertiaryColourD = cursor.execute("SELECT tertiary_colour FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.data)+"'")
    tertiaryColourD = deScramble(tertiaryColourD.fetchall()[0][0]).upper()
    tertiaryHexEntryBox.insert(END,tertiaryColourD)
    closeDatabase()
    tertiaryHexEntryBox.place(relx=0.175,rely=0.61,anchor=CENTER)
    tertiaryyHexEntryLabel = Label(root, text='Tertiary Colour Hex Code',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.175,rely=0.53,anchor=CENTER)

    textFontBoxBackground = Label(image = longNormal, border = 0).place(relx=0.6625,rely=0.25,anchor=CENTER)
    openDatabase()
    fontD = cursor.execute("SELECT font FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.data)+"'")
    fontD = deScramble(fontD.fetchall()[0][0]).title()
    global fontMenu
    fontMenu = ttk.Combobox(root, value=listOfAcceptedFonts, justify=tkinter.CENTER, width = 50,font=(font.data,18))
    fontMenu.current(listOfAcceptedFonts.index(fontD))
    root.option_add('*TCombobox*Listbox.font', (font.data,14)) 
    fontMenu.place(relx=0.6635,rely=0.25,anchor=CENTER)
    closeDatabase()
    fontEntryLabel = Label(root, text='Text Font',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.6625,rely=0.17,anchor=CENTER)

    titleEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.5,rely=0.43,anchor=CENTER)
    global titleEntryBox
    titleEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    openDatabase()
    titleD = cursor.execute("SELECT title FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.data)+"'")
    titleD = deScramble(titleD.fetchall()[0][0])
    titleEntryBox.insert(END,titleD)
    closeDatabase()
    titleEntryBox.place(relx=0.5,rely=0.43,anchor=CENTER)
    titleEntryLabel = Label(root, text='Title',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.5,rely=0.35,anchor=CENTER)

    firstNameEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.5,rely=0.61,anchor=CENTER)
    global firstNameEntryBox
    firstNameEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    openDatabase()
    firstD = cursor.execute("SELECT first_Name FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.data)+"'")
    firstD = deScramble(firstD.fetchall()[0][0])
    firstNameEntryBox.insert(END,firstD)
    closeDatabase()
    firstNameEntryBox.place(relx=0.5,rely=0.61,anchor=CENTER)
    firstNameEntryLabel = Label(root, text='First Name',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.5,rely=0.53,anchor=CENTER)

    operationTypeEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.83,rely=0.43,anchor=CENTER)
    openDatabase()
    operationTypeD = cursor.execute("SELECT operation_Type FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.data)+"'")
    operationTypeD = deScramble(operationTypeD.fetchall()[0][0])
    global operation_TypeOptions
    operation_TypeOptions = ['Business','Personal']
    global operationTypeMenu
    operationTypeMenu = ttk.Combobox(root, value=operation_TypeOptions, justify=tkinter.CENTER, font=(font.data,18))
    operationTypeMenu.current(operation_TypeOptions.index(operationTypeD))
    root.option_add('*TCombobox*Listbox.font', (font.data,14)) 
    operationTypeMenu.place(relx=0.83,rely=0.43,anchor=CENTER)
    closeDatabase()
    operationTypeEntryLabel = Label(root, text='Operation Type',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.83,rely=0.35,anchor=CENTER)
    
    surnameEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.83,rely=0.61,anchor=CENTER)
    global surnameEntryBox
    surnameEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    openDatabase()
    lastD = cursor.execute("SELECT last_Name FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.data)+"'")
    lastD = deScramble(lastD.fetchall()[0][0])
    surnameEntryBox.insert(END,lastD)
    closeDatabase()
    surnameEntryBox.place(relx=0.83,rely=0.61,anchor=CENTER)
    surnameEntryLabel = Label(root, text='Surname',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.83,rely=0.53,anchor=CENTER)

    global settingsCords
    settingsCords = {'primary_Colour':{'x':0.175,'y':0.3175},'secondry_Colour':{'x':0.175,'y':0.4975},'tertiary_Colour':{'x':0.175,'y':0.6775},'font':{'x':0.6635,'y':0.3175},'title':{'x':0.5,'y':0.4975},'operation_Type':{'x':0.83,'y':0.4975},'first_Name':{'x':0.5,'y':0.6775},'last_Name':{'x':0.83,'y':0.6775}}
    submitUnitDetailsB = Button(root, text='S U B M I T', font=(font.data,'20','underline','bold'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=updateSetings).place(relx=0.5, rely=0.93, anchor=CENTER)
    timeLabel = Label(root,text="This submit may take some time please be patient",bg=primary.data,fg=secondry.data, width=75, font=(font.data,12), justify='center',relief='flat').place(relx=0.5, rely=0.97 ,anchor=CENTER)
    
    changePasswordPageButton = Button(root, text='Want to change your password?', font=(font.data,'12','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=changePasswordPage).place(relx=0.825, rely=0.8, anchor=CENTER)
    deleteAccountPageButton = Button(root, text='Want to delete your account?', font=(font.data,'12','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=deleteAccountPage).place(relx=0.825, rely=0.85, anchor=CENTER)
    changeUsernamePageButton = Button(root, text='Want to change your username?', font=(font.data,'12','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=changeUsernamePage).place(relx=0.825, rely=0.9, anchor=CENTER)

    hexCodeB = Button(root, text='Unsure about hex codes?', font=(font.data,'12','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=hexCodeInfoPage).place(relx=0.175, rely=0.85, anchor=CENTER)

    root.mainloop()

def updateSetings():
    primary_Colour = uInputDataObj(primaryHexEntryBox.get(),str)
    secondry_Colour = uInputDataObj(secondryHexEntryBox.get(),str)
    tertiary_Colour = uInputDataObj(tertiaryHexEntryBox.get(),str)
    font = uInputDataObj(fontMenu.get(),str)
    title = uInputDataObj(titleEntryBox.get(),str)
    operation_Type = uInputDataObj(operationTypeMenu.get(),str)
    first_Name = uInputDataObj(firstNameEntryBox.get(),str) 
    last_Name = uInputDataObj(surnameEntryBox.get(),str)
    
    accountFields = ['account_ID', 'password', 'recovery_Email', 'first_Name', 'last_Name', 'operation_Type', 'title', 'tax_Rate', 'other_Income_Estimate', 'basic_Income_Rate', 'high_Income_Rate', 'additional_Income_Rate', 'basic_Income_Cut_Off', 'high_Income_Cut_Off', 'corporation_Rate', 'basic_Capital_Gains_Rate', 'basic_Capital_Gains_Allowence', 'high_Capital_Gains_Rate', 'additional_Capital_Gains_Rate', 'corporation_Capital_Gains_Rate', 'national_Insurance_Due', 'primary_Colour', 'secondry_Colour', 'tertiary_Colour','font']

    openDatabase()
    listOfUnchangable = cursor.execute(" SELECT account_ID, password, recovery_Email, tax_Rate, other_Income_Estimate, basic_Income_Rate, high_Income_Rate, additional_Income_Rate, basic_Income_Cut_Off, high_Income_Cut_Off, corporation_Rate, basic_Capital_Gains_Rate, basic_Capital_Gains_Allowence, high_Capital_Gains_Rate, additional_Capital_Gains_Rate, corporation_Capital_Gains_Rate, national_Insurance_Due FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.data)+"'")
    listOfUnchangable = listOfUnchangable.fetchall()[0]
    dictOfUnchangable = {'account_ID':listOfUnchangable[0],'password':listOfUnchangable[1],'recovery_Email':listOfUnchangable[2],'tax_Rate':listOfUnchangable[3],'other_Income_Estimate':listOfUnchangable[4],'basic_Income_Rate':listOfUnchangable[5],'high_Income_Rate':listOfUnchangable[6],'additional_Income_Rate':listOfUnchangable[7],'basic_Income_Cut_Off':listOfUnchangable[8],'high_Income_Cut_Off':listOfUnchangable[9],'corporation_Rate':listOfUnchangable[10],'basic_Capital_Gains_Rate':listOfUnchangable[11],'basic_Capital_Gains_Allowence':listOfUnchangable[12],'high_Capital_Gains_Rate':listOfUnchangable[13],'additional_Capital_Gains_Rate':listOfUnchangable[14],'corporation_Capital_Gains_Rate':listOfUnchangable[15],'national_Insurance_Due':listOfUnchangable[16]}
    closeDatabase()

    newListOfAccount = [dictOfUnchangable['account_ID'],dictOfUnchangable['password'],dictOfUnchangable['recovery_Email'],first_Name.data,last_Name.data,operation_Type.data,title.data,dictOfUnchangable['tax_Rate'],dictOfUnchangable['other_Income_Estimate'],dictOfUnchangable['basic_Income_Rate'],dictOfUnchangable['high_Income_Rate'],dictOfUnchangable['additional_Income_Rate'],dictOfUnchangable['basic_Income_Cut_Off'],dictOfUnchangable['high_Income_Cut_Off'],dictOfUnchangable['corporation_Rate'],dictOfUnchangable['basic_Capital_Gains_Rate'],dictOfUnchangable['basic_Capital_Gains_Allowence'],dictOfUnchangable['high_Capital_Gains_Rate'],dictOfUnchangable['additional_Capital_Gains_Rate'],dictOfUnchangable['corporation_Capital_Gains_Rate'],dictOfUnchangable['national_Insurance_Due']]

    global dictOfDataValdationResults
    dictOfDataValdationResults = dict.fromkeys(accountFields)
    dictOfDataValdationResults['primary_Colour'] = {'presenceCheck':presenceCheck(primary_Colour),'hexCodeCheck':hexCodeCheck(primary_Colour)}
    dictOfDataValdationResults['secondry_Colour'] = {'presenceCheck':presenceCheck(secondry_Colour),'hexCodeCheck':hexCodeCheck(secondry_Colour)}
    dictOfDataValdationResults['tertiary_Colour'] = {'presenceCheck':presenceCheck(tertiary_Colour),'hexCodeCheck':hexCodeCheck(tertiary_Colour)}
    dictOfDataValdationResults['font'] = {'menuOptionCheck':menuOptionCheck(font,listOfAcceptedFonts)}
    dictOfDataValdationResults['operation_Type'] = {'menuOptionCheck':menuOptionCheck(operation_Type,operation_TypeOptions)}
    dictOfDataValdationResults['title'] = {'presenceCheck':presenceCheck(title),'containsOnlyLetters':containsOnlyLetters(title),'noSpaces':pictureCheck(title,'',0,0)}
    dictOfDataValdationResults['first_Name'] ={'presenceCheck':presenceCheck(first_Name),'containsOnlyLetters':containsOnlyLetters(first_Name),'noSpaces':pictureCheck(first_Name,'',0,0)}
    dictOfDataValdationResults['last_Name'] = {'presenceCheck':presenceCheck(last_Name),'containsOnlyLetters':containsOnlyLetters(last_Name),'noSpaces':pictureCheck(last_Name,'',0,0)}
    settingsPageCoverUp()

    for entryboxData in dictOfDataValdationResults.keys():
        countOfFailedTests = 0
        if dictOfDataValdationResults[entryboxData] != None:
            for test in dictOfDataValdationResults[entryboxData].keys():
                while dictOfDataValdationResults[entryboxData][test] == False and countOfFailedTests == 0:
                    disaplayEM(test,settingsCords[entryboxData]['x'],settingsCords[entryboxData]['y'])
                    countOfFailedTests = countOfFailedTests + 1

    countOfFailedTests = 0
    for entryboxData in dictOfDataValdationResults.keys():
        if dictOfDataValdationResults[entryboxData] != None:
            for test in dictOfDataValdationResults[entryboxData].values():
                if test == False:
                    countOfFailedTests = countOfFailedTests +1

    if countOfFailedTests == 0:

        openDatabase()
        accocountUpdateCommand = ("UPDATE accounts SET primary_Colour = '" + str(scramble(primary_Colour.data)) + "', secondry_Colour = '" + str(scramble(secondry_Colour.data)) + "', tertiary_Colour = '" + str(scramble(tertiary_Colour.data)) + "', font = '" + str(scramble(font.data)) + "', operation_Type = '" + str(scramble(operation_Type.data)) + "', title = '" + str(scramble(title.data)) + "', first_Name = '" + str(scramble(first_Name.data)) + "', last_Name = '" + str(scramble(last_Name.data)) + "' WHERE account_ID = '" + str(scramble(databaseCurrentAccount_ID.data)) +"'")
        cursor.execute(accocountUpdateCommand)
        closeDatabase()

        redoConfigureAccountSettingsVariables()
        convertAssetColor(primary,secondry)
        displayConfirmation('Settings')

def settingsPageCoverUp():
    for entryboxData in dictOfDataValdationResults.keys():
        if dictOfDataValdationResults[entryboxData] != None:
            coverUp = Label(root,bg=primary.data,width=75,font=(font.data,7),justify='center').place(relx=settingsCords[entryboxData]['x'],rely=settingsCords[entryboxData]['y'],anchor=CENTER)

def hexCodeInfoPage():
    try:
        webbrowser.open_new('https://htmlcolorcodes.com/color-picker/')
        webbrowser.open_new('https://www.pluralsight.com/blog/tutorials/understanding-hexadecimal-colors-simple')
    except OSError:
        if connectionError.state() != 'Normal':
                displayConnectionError()

def contactPage():
    initialiseWindow()
    root.title('Property managment system - Contact Page')
    topBorder = Label(root, text='Contact', height=2 ,bg=primary.data, fg = secondry.data, width=42, font=(font.data,40), justify='center').place(relx=0,rely=0)
    displayBackButton()
    global previousPage
    previousPage = 'Contact'
    displayMenuButton()
    root.mainloop()

def addTenant():
    tenant_ID = uInputDataObj(tenantIDEntryBox.get(),str)
    account_ID = uInputDataObj(databaseCurrentAccount_ID.data,str)
    tenant_Email = uInputDataObj(emailEntryBox.get(),str)
    first_Name = uInputDataObj(firstnameEntryBox.get(),str)
    last_Name = uInputDataObj(surnameEntryBoxTenant.get(),str)
    title = uInputDataObj(titleEntryBoxTenant.get(),str)
    day = uInputDataObj(dayEntryBox.get(),int)
    month = uInputDataObj(monthEntryBox.get(),int)
    year = uInputDataObj(yearEntryBox.get(),int)
    score = uInputDataObj(scoreEntryBox.get(),float)
    total_Residents = uInputDataObj(nOtherOccupantsEntryBoxTenant.get(),str)
    startMonth = uInputDataObj(startOfLeaseDateMonthEntryBoxTenant.get(),int)
    startYear = uInputDataObj(startOfLeaseDateYearEntryBoxTenant.get(),int)
    deposit = uInputDataObj(tenantsDepositEntryBox.get(),float)
    gerneral_Notes = uInputDataObj(geneneralNotesEntryBoxTenant.get('1.0','end-1c'),str)

    dateOfBirth = uInputDataObj(day.data+'/'+month.data+'/'+year.data,str)
    startDate = uInputDataObj(startMonth.data+'/'+startYear.data,str)

    newTenantArray = [tenant_ID.data,account_ID.data,tenant_Email.data,first_Name.data,last_Name.data,title.data,dateOfBirth.data,score.data,total_Residents.data,startDate.data,deposit.data,gerneral_Notes.data]
    tenantsFields = ['tenant_ID','account_ID','tenant_Email','first_Name','last_Name','title','date_Of_Birth','score','total_Residents','start_Date','deposit','gerneral_Notes']
    
    global dictOfDataValdationResults
    dictOfDataValdationResults = dict.fromkeys(tenantsFields)
    dictOfDataValdationResults['tenant_ID'] = {'presenceCheck':presenceCheck(tenant_ID),'noSpaces':pictureCheck(tenant_ID,'',0,0),'uniqueDataCheck':uniqueDataCheck(tenant_ID,'tenant_ID','tenants')}
    dictOfDataValdationResults['tenant_Email'] = {'lengthCheck':rangeCheck(tenant_Email,3,None),'@check':pictureCheck(tenant_Email,'@',1,1),'noSpaces':pictureCheck(tenant_Email,'',0,0),'uniqueDataCheck':uniqueDataCheck(tenant_Email,'tenant_Email','tenants')}
    dictOfDataValdationResults['title'] = {'presenceCheck':presenceCheck(title),'containsOnlyLetters':containsOnlyLetters(title)}
    dictOfDataValdationResults['first_Name'] = {'presenceCheck':presenceCheck(first_Name),'containsOnlyLetters':containsOnlyLetters(first_Name)}
    dictOfDataValdationResults['last_Name'] = {'presenceCheck':presenceCheck(last_Name),'containsOnlyLetters':containsOnlyLetters(last_Name)}
    dictOfDataValdationResults['day'] = {'presenceCheck':presenceCheck(day),'dayBetween0/31':rangeCheck(day,0,31)}
    dictOfDataValdationResults['month'] = {'presenceCheck':presenceCheck(month),'monthBetween1/12':rangeCheck(month,1,12)}
    dictOfDataValdationResults['year'] = {'presenceCheck':presenceCheck(year),'yearBetween1900/2100':rangeCheck(year,1900,2100)}
    dictOfDataValdationResults['score'] = {'presenceCheck':presenceCheck(score),'between0/100':rangeCheck(score,0,100)}
    dictOfDataValdationResults['total_Residents'] = {'presenceCheck':presenceCheck(total_Residents),'positiveCheck':rangeCheck(total_Residents,0,None)}
    dictOfDataValdationResults['startMonth'] = {'presenceCheck':presenceCheck(startMonth),'monthBetween1/12':rangeCheck(startMonth,1,12)}
    dictOfDataValdationResults['startYear'] = {'presenceCheck':presenceCheck(startYear),'yearBetween1900/2100':rangeCheck(startYear,1900,2100)}
    dictOfDataValdationResults['deposit'] = {'presenceCheck':presenceCheck(deposit),'postiveCheck':rangeCheck(deposit,0,None)}
    dictOfDataValdationResults['gerneral_Notes'] = {'lengthCheck':rangeCheck(gerneral_Notes,0,1024)}
    newTenantCoverUp()

    for entryboxData in dictOfDataValdationResults.keys():
        countOfFailedTests = 0
        if dictOfDataValdationResults[entryboxData] != None:
            for test in dictOfDataValdationResults[entryboxData].keys():
                while dictOfDataValdationResults[entryboxData][test] == False and countOfFailedTests == 0:
                    disaplayEM(test,newTenantEntryBoxCords[entryboxData]['x'],newTenantEntryBoxCords[entryboxData]['y'])
                    countOfFailedTests = countOfFailedTests + 1

    countOfFailedTests = 0
    for entryboxData in dictOfDataValdationResults.keys():
        if dictOfDataValdationResults[entryboxData] != None:
            for test in dictOfDataValdationResults[entryboxData].values():
                if test == False:
                    countOfFailedTests = countOfFailedTests +1

    if countOfFailedTests == 0:
        for i in range(len(newTenantArray)):
            newTenantArray[i] = scramble(newTenantArray[i])

        openDatabase()
        global newTenantInsertionCommand
        newTenantInsertionCommand = """INSERT INTO tenants(tenant_ID,account_ID,tenant_Email,first_Name,last_Name,title,date_Of_Birth,score,total_Residents,start_Date,deposit,gerneral_Notes)
        Values(?,?,?,?,?,?,?,?,?,?,?,?)"""
        cursor.execute(newTenantInsertionCommand,newTenantArray)
        closeDatabase()

        displayConfirmation('Tenants')

def newTenantCoverUp():
    for entryboxData in dictOfDataValdationResults.keys():
        if dictOfDataValdationResults[entryboxData] != None:
            coverUp = Label(root,bg=primary.data,width=75,font=(font.data,7),justify='center').place(relx=newTenantEntryBoxCords[entryboxData]['x'],rely=newTenantEntryBoxCords[entryboxData]['y'],anchor=CENTER)

def redoConfigureAccountSettingsVariables():
    openDatabase()
    allAcoountData = cursor.execute("SELECT * FROM accounts WHERE account_ID = '" + str(scramble(databaseCurrentAccount_ID.data)) + "'")
    allAcoountData = allAcoountData.fetchall()[0]
    accountArray = [databaseCurrentAccount_ID,password,recovery_Email,first_Name,last_Name, operation_Type, title, tax_Rate, incPA,other_Income_Estimate,bIncTR, hIncTR, aIncTR, bIncCutOff, hIncCutOff, corpTR, bCapGainsTR, bCapGainsAllowence, hCapGainsTR, aCapGainsTR, corpCapGainsTR,national_Insurance_Due, primary, secondry, tertiary, font]
    for i in range(len(accountArray)):
        accountArray[i] = accountArray[i].setData(allAcoountData[i]) 
    closeDatabase()

def changePasswordPage():
    initialiseWindow()
    root.title('Property managment system - Change Password')
    topBorder = Label(root, text='Change Password', height=2 ,bg=primary.data, fg = secondry.data, width=42, font=(font.data,40), justify='center').place(relx=0,rely=0)
    displayBackButton()
    global previousPage
    previousPage = 'Change Password'
    displayMenuButton()

    longNormalTwo = PhotoImage(file = "Long-Normal 2.PNG")
    
    orignalPasswordBackGround = Label(image = longNormalTwo, border = 0).place(relx=0.5,rely=0.33,anchor=CENTER)
    global orignalPasswordEntryBox
    orignalPasswordEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    orignalPasswordEntryBox.place(relx=0.5,rely=0.33,anchor=CENTER)
    orignalPasswordEntryBoxLabel = Label(root, text='Current Password',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.5,rely=0.24,anchor=CENTER)

    newPasswordBackGround = Label(image = longNormalTwo, border = 0).place(relx=0.5,rely=0.55,anchor=CENTER)
    global newPasswordEntryBox
    newPasswordEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    newPasswordEntryBox.place(relx=0.5,rely=0.55,anchor=CENTER)
    newPasswordEntryBoxLabel = Label(root, text='New Password',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.5,rely=0.46,anchor=CENTER)

    newPasswordCBackGround = Label(image = longNormalTwo, border = 0).place(relx=0.5,rely=0.77,anchor=CENTER)
    global newPasswordConfirmEntryBox
    newPasswordConfirmEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    newPasswordConfirmEntryBox.place(relx=0.5,rely=0.77,anchor=CENTER)
    newPasswordConfirmEntryBoxLabel = Label(root, text='Confirm New Password',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.5,rely=0.68,anchor=CENTER)

    submitUnitDetailsB = Button(root, text='S U B M I T', font=(font.data,'20','underline','bold'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=changePassword).place(relx=0.5, rely=0.93, anchor=CENTER)
    hidePasswordChangePOG = Button(root, text='Hide', font=(font.data,'15','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command= lambda: hideEntryBox(orignalPasswordEntryBox,0.14,0.33)).place(relx=0.14, rely=0.33, anchor=CENTER)
    hidePasswordChangePN = Button(root, text='Hide', font=(font.data,'15','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command= lambda: hideEntryBox(newPasswordEntryBox,0.14,0.55)).place(relx=0.14, rely=0.55, anchor=CENTER)
    hidePasswordChangePCN = Button(root, text='Hide', font=(font.data,'15','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command= lambda: hideEntryBox(newPasswordConfirmEntryBox,0.14,0.77)).place(relx=0.14, rely=0.77, anchor=CENTER)

    global changePasswordCord
    changePasswordCord = {'orignalPassword':{'x':0.5,'y':0.4075},'newPassword':{'x':0.5,'y':0.6275},'confirmNewPassword':{'x':0.5,'y':0.8475}}

    root.mainloop()

def changePassword():
    listOfPassword = ['orignalPassword','newPassword','confirmNewPassword']

    orignalPassword = uInputDataObj(orignalPasswordEntryBox.get(),str)
    newPassword = uInputDataObj(newPasswordEntryBox.get(),str)
    confirmNewPassword = uInputDataObj(newPasswordConfirmEntryBox.get(),str)

    openDatabase()
    passwordD = cursor.execute("SELECT password FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.getData())+"'")
    password = deScramble(passwordD.fetchall()[0][0])
    closeDatabase()

    global dictOfDataValdationResults
    dictOfDataValdationResults = dict.fromkeys(listOfPassword)
    if orignalPassword.data == password:
        dictOfDataValdationResults['orignalPassword'] = {'checkPassword':True}
    else:
        dictOfDataValdationResults['orignalPassword'] = {'checkPassword':False}
    dictOfDataValdationResults['newPassword'] = {'presenceCheck':presenceCheck(newPassword),'lengthOverSevenCheck':rangeCheck(newPassword,7,None)}
    dictOfDataValdationResults['confirmNewPassword'] = {'presenceCheck':presenceCheck(confirmNewPassword),'matchesNewPassword':matchesCheck(confirmNewPassword,newPassword)}
    coverUpChangePassword()
    
    for entryboxData in dictOfDataValdationResults.keys():
        countOfFailedTests = 0
        if dictOfDataValdationResults[entryboxData] != None:
            for test in dictOfDataValdationResults[entryboxData].keys():
                while dictOfDataValdationResults[entryboxData][test] == False and countOfFailedTests == 0:
                    disaplayEM(test,changePasswordCord[entryboxData]['x'],changePasswordCord[entryboxData]['y'])
                    countOfFailedTests = countOfFailedTests + 1

    countOfFailedTests = 0
    for entryboxData in dictOfDataValdationResults.keys():
        if dictOfDataValdationResults[entryboxData] != None:
            for test in dictOfDataValdationResults[entryboxData].values():
                if test == False:
                    countOfFailedTests = countOfFailedTests +1

    if countOfFailedTests == 0:
        password = scramble(newPassword.data)

        openDatabase()
        accocountUpdateCommand = ("UPDATE accounts SET password = '" + str(password) + "' WHERE account_ID = '" + str(scramble(databaseCurrentAccount_ID.data)) +"'")
        cursor.execute(accocountUpdateCommand)
        closeDatabase()

        displayConfirmation('Settings')

def coverUpChangePassword():
    for entryboxData in dictOfDataValdationResults.keys():
        if dictOfDataValdationResults[entryboxData] != None:
            coverUp = Label(root,bg=primary.data,width=100,font=(font.data,7),justify='center').place(relx=changePasswordCord[entryboxData]['x'],rely=changePasswordCord[entryboxData]['y'],anchor=CENTER)

def deleteAccountPage():
    initialiseWindow()
    root.title('Property managment system - Delete Account')
    topBorder = Label(root, text='Delete Account', height=2 ,bg=primary.data, fg = secondry.data, width=42, font=(font.data,40), justify='center').place(relx=0,rely=0)
    displayBackButton()
    global previousPage
    previousPage = 'Delete Account'
    displayMenuButton()

    longNormalTwo = PhotoImage(file = "Long-Normal 2.PNG")
    cautionLabel = Label(root, text='Caution',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18,'bold'), justify='center',relief='flat').place(relx=0.5,rely=0.28,anchor=CENTER)
    cautionSubLabel = Label(root, text='Once an account is deleted all data linked to that account is lost. There is no way to retrieve an\naccount once it is deleted! Once an account is deleted it is gone for ever.',bg=primary.data, fg=secondry.data, width=100, font=(font.data,14), justify='center',relief='flat').place(relx=0.5,rely=0.33,anchor=CENTER)

    passwordForConfirmationBackGround = Label(image = longNormalTwo, border = 0).place(relx=0.5,rely=0.55,anchor=CENTER)
    global passwordForConfirmationEntryBox
    passwordForConfirmationEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    passwordForConfirmationEntryBox.place(relx=0.5,rely=0.55,anchor=CENTER)
    passwordForConfirmationEntryBoxLabel = Label(root, text='Enter password as confirmation',bg=primary.data, fg=secondry.data, width=33, font=(font.data,18), justify='center',relief='flat').place(relx=0.5,rely=0.46,anchor=CENTER)
    hidePasswordChangePN = Button(root, text='Hide', font=(font.data,'15','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command= lambda: hideEntryBox(passwordForConfirmationEntryBox,0.14,0.55)).place(relx=0.14, rely=0.55, anchor=CENTER)

    deleteAccountButton = Button(root, text='Delete Account', font=(font.data,'18','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=deleteAccount).place(relx=0.5, rely=0.8, anchor=CENTER)
    canceldeleteAccountButton = Button(root, text='Cancel Deletion', font=(font.data,'18','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=settingsPage).place(relx=0.5, rely=0.9, anchor=CENTER)

    root.mainloop()

def deleteAccount():
    passwordForConfirmation = uInputDataObj(passwordForConfirmationEntryBox.get(),str)
    
    openDatabase()
    passwordD = cursor.execute("SELECT password FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.getData())+"'")
    password = deScramble(passwordD.fetchall()[0][0])
    closeDatabase()

    if passwordForConfirmation.data == password:
        coverUpLabel = Label(root,bg=primary.data, width=60, justify='center',relief='flat').place(relx=0.5,rely=0.63,anchor=CENTER)
        openDatabase()
        cursor.execute("DELETE FROM accounts WHERE account_ID = '" + str(scramble(databaseCurrentAccount_ID.getData()) + "'"))
        unitIDs = cursor.execute("SELECT unit_ID FROM units WHERE account_ID = '" + str(scramble(databaseCurrentAccount_ID.getData()) + "'")).fetchall()[0]
        for i in range (len(unitIDs)):
            cursor.execute("DELETE FROM units_Monthly WHERE unit_ID = '" + str((unitIDs[i]) + "'")) #I used a sneaky trick where I do not descramble the unit as I would just rescramble them again for there purpose.
            cursor.execute("DELETE FROM refinance WHERE unit_ID = '" + str((unitIDs[i]) + "'"))
            cursor.execute("DELETE FROM loan WHERE unit_ID = '" + str((unitIDs[i]) + "'"))
        cursor.execute("DELETE FROM sold_Units WHERE account_ID = '" + str(scramble(databaseCurrentAccount_ID.getData()) + "'"))
        tenant_IDs = cursor.execute("SELECT tenant_ID FROM tenants WHERE account_ID = '" + str(scramble(databaseCurrentAccount_ID.getData()) + "'")).fetchall()[0]
        for i in range(len(tenant_IDs)):
            cursor.execute("DELETE FROM complaints WHERE tenant_ID = '" + str(tenant_IDs[i] + "'"))
        cursor.execute("DELETE FROM units WHERE account_ID = '" + str(scramble(databaseCurrentAccount_ID.getData()) + "'"))
        cursor.execute("DELETE FROM tenants WHERE account_ID = '" + str(scramble(databaseCurrentAccount_ID.getData()) + "'"))
        closeDatabase()
        displayConfirmation('Login')
    else:
        warning = Label(root, text = 'Password incorrect',bg=primary.data,width=65, fg = bannedColours['errorRed'], font=(font.data,9),justify='center').place(relx=0.5,rely=0.63,anchor=CENTER)

def changeUsernamePage():
    initialiseWindow()
    root.title('Property managment system - Change Username')
    topBorder = Label(root, text='Change Username', height=2 ,bg=primary.data, fg = secondry.data, width=42, font=(font.data,40), justify='center').place(relx=0,rely=0)
    displayBackButton()
    global previousPage
    previousPage = 'Change Username'
    displayMenuButton()

    longNormalTwo = PhotoImage(file = "Long-Normal 2.PNG")
    
    passwordBackGround = Label(image = longNormalTwo, border = 0).place(relx=0.5,rely=0.33,anchor=CENTER)
    global passwordEntryBox
    passwordEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    passwordEntryBox.place(relx=0.5,rely=0.33,anchor=CENTER)
    passwordEntryBoxLabel = Label(root, text='Password',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.5,rely=0.24,anchor=CENTER)

    newUsernameBackGround = Label(image = longNormalTwo, border = 0).place(relx=0.5,rely=0.55,anchor=CENTER)
    global newUsernameEntryBox
    newUsernameEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    newUsernameEntryBox.place(relx=0.5,rely=0.55,anchor=CENTER)
    newUsernameEntryBoxLabel = Label(root, text='New Username',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.5,rely=0.46,anchor=CENTER)

    newUsernameCBackGround = Label(image = longNormalTwo, border = 0).place(relx=0.5,rely=0.77,anchor=CENTER)
    global newUsernameConfirmEntryBox
    newUsernameConfirmEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    newUsernameConfirmEntryBox.place(relx=0.5,rely=0.77,anchor=CENTER)
    newUsernameConfirmEntryBoxLabel = Label(root, text='Confirm New Username',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.5,rely=0.68,anchor=CENTER)

    submitUnitDetailsB = Button(root, text='S U B M I T', font=(font.data,'20','underline','bold'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=changeUsername).place(relx=0.5, rely=0.93, anchor=CENTER)
    hidePasswordChangePOG = Button(root, text='Hide', font=(font.data,'15','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command= lambda: hideEntryBox(passwordEntryBox,0.14,0.33)).place(relx=0.14, rely=0.33, anchor=CENTER)

    global changeUsernameCord
    changeUsernameCord = {'password':{'x':0.5,'y':0.4075},'newUsername':{'x':0.5,'y':0.6275},'newUsernameConfirm':{'x':0.5,'y':0.8475}}

    root.mainloop()

def changeUsername():
    listOfPassword = ['password','newUsername','newUsernameConfirm']

    passwordFromEntry = uInputDataObj(passwordEntryBox.get(),str)
    newUsername = uInputDataObj(newUsernameEntryBox.get(),str)
    newUsernameConfirm = uInputDataObj(newUsernameConfirmEntryBox.get(),str)

    openDatabase()
    passwordD = cursor.execute("SELECT password FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.getData())+"'")
    password = deScramble(passwordD.fetchall()[0][0])
    closeDatabase()

    global dictOfDataValdationResults
    dictOfDataValdationResults = dict.fromkeys(listOfPassword)
    if passwordFromEntry.data == password:
        dictOfDataValdationResults['password'] = {'checkPassword':True}
    else:
        dictOfDataValdationResults['password'] = {'checkPassword':False}
    dictOfDataValdationResults['newUsername'] = {'presenceCheck':presenceCheck(newUsername),'lengthCheck':rangeCheck(newUsername,3,None),'@check':pictureCheck(newUsername,'@',1,1),'noSpaces':pictureCheck(newUsername,'',0,0),'uniqueDataCheck':uniqueDataCheck(newUsername,'recovery_Email','accounts')}
    dictOfDataValdationResults['newUsernameConfirm'] = {'presenceCheck':presenceCheck(newUsernameConfirm),'matchesNewPassword':matchesCheck(newUsernameConfirm,newUsername)}
    coverUpChangeUsername()
    
    for entryboxData in dictOfDataValdationResults.keys():
        countOfFailedTests = 0
        if dictOfDataValdationResults[entryboxData] != None:
            for test in dictOfDataValdationResults[entryboxData].keys():
                while dictOfDataValdationResults[entryboxData][test] == False and countOfFailedTests == 0:
                    disaplayEM(test,changeUsernameCord[entryboxData]['x'],changeUsernameCord[entryboxData]['y'])
                    countOfFailedTests = countOfFailedTests + 1

    countOfFailedTests = 0
    for entryboxData in dictOfDataValdationResults.keys():
        if dictOfDataValdationResults[entryboxData] != None:
            for test in dictOfDataValdationResults[entryboxData].values():
                if test == False:
                    countOfFailedTests = countOfFailedTests +1

    if countOfFailedTests == 0:
        recovery_Email = scramble(newUsername.data)

        openDatabase()
        accocountUpdateCommand = ("UPDATE accounts SET recovery_Email = '" + str(recovery_Email) + "' WHERE account_ID = '" + str(scramble(databaseCurrentAccount_ID.data)) +"'")
        cursor.execute(accocountUpdateCommand)
        closeDatabase()

        displayConfirmation('Settings')

def coverUpChangeUsername():
    for entryboxData in dictOfDataValdationResults.keys():
        if dictOfDataValdationResults[entryboxData] != None:
            coverUp = Label(root,bg=primary.data,width=100,font=(font.data,7),justify='center').place(relx=changeUsernameCord[entryboxData]['x'],rely=changeUsernameCord[entryboxData]['y'],anchor=CENTER)

def hideEntryBox(globalEntryBox,xcord,ycord): #x and y cord of the hide/show button
    globalEntryBox.config(show='\u2022')
    showPasswordB = Button(root, text='Show', font=(font.data,'15','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=lambda: showEntryBox(globalEntryBox,xcord,ycord)).place(relx=xcord, rely=ycord, anchor=CENTER)

def showEntryBox(globalEntryBox,xcord,ycord): #x and y cord of the hide/show button
    globalEntryBox.config(show='')
    hidePasswordB = Button(root, text='Hide', font=(font.data,'15','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=lambda: hideEntryBox(globalEntryBox,xcord,ycord)).place(relx=xcord, rely=ycord, anchor=CENTER)

def addPageSeperator():
    xCord = 0.3
    frontOfThinLine = Label(root,bg=primary.data,width=1,height=100).place(relx=xCord,rely=0)
    backgroundOfThinLine = Label(root,bg=secondry.data,width=1,height=100).place(relx=xCord+0.002,rely=0)

def tenantPage(tenant_ID):
    global current_tenant_ID
    current_tenant_ID = tenant_ID
    initialiseWindow()
    root.title('Property managment system - Tenant Page ' + str(tenant_ID))
    root.configure(bg=secondry.data)
    addPageSeperator()
    topBorder = Label(root, text='Tenant ' + str(tenant_ID), height=2 ,bg=primary.data, fg = secondry.data, width=42, font=(font.data,40), justify='center').place(relx=0,rely=0)
    displayMenuButton()
    displayBackButton()
    global previousPage
    previousPage = 'individualTenantPage'
    global currentTentantMonthlyNumber
    currentTentantMonthlyNumber = 0
    global startValueForMonth
    startValueForMonth = createTableForIndividualTenant(0)
    complaintsManagmentButton = Button(root, text='Complaints Managment', font=(font.data,'14','underline'),bg=secondry.data,fg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=secondry.data,border=0,command= lambda: complaintsManagmentPage(current_tenant_ID)).place(relx=0.4, rely=0.85, anchor=CENTER)
    root.mainloop()

def createTableForIndividualTenant(startValueForAccountListing):
    frameToGiveOtheCanvasABorder = Frame(root,width=440,height=500,bg=secondry.data,relief='solid',highlightthickness=2,highlightbackground=primary.data)
    frameToGiveOtheCanvasABorder.place(relx=0.65,rely=0.5,anchor='center')
    frameToGiveOtheCanvasABorder.grid_propagate(False) #Stops frame from changing size to fit the inside of it
    global canvasForTable
    canvasForTable = Canvas(frameToGiveOtheCanvasABorder,width=440,height=500,bg=secondry.data,highlightthickness=0)
    canvasForTable.pack()
    canvasForTable.grid_propagate(False) #Stops frame from changing size to fit the inside of it
    tenant_ID_ColumHeader = Label(canvasForTable, text='Date', height=1 ,bg=secondry.data, fg = primary.data, font=(font.data,14,'bold'), justify='center').place(relx = 0.04, rely=0.05)
    score_ColumHeader = Label(canvasForTable, text='Rent Paid', height=1 ,bg=secondry.data, fg = primary.data, font=(font.data,14,'bold'), justify='center').place(relx = 0.33, rely=0.05)
    email_ColumHeader = Label(canvasForTable, text='Complaints', height=1 ,bg=secondry.data, fg = primary.data, font=(font.data,14,'bold'), justify='center').place(relx = 0.69, rely=0.05)
    canvasForTable.create_line(110,0,110,76,fill=primary.data)
    canvasForTable.create_line(285,0,285,76,fill=primary.data)
    canvasForTable.create_line(0,76,850,76,fill=primary.data)

    # INSERT INTO units_Monthly (year, month, unit_ID, tenant_ID, rent_Paid, rent_Late, income, non_Taxable_Expenses, taxable_Expenses, suspected_Property_Value, equity_In_Property,money_Taken_From_Deposit)
    # VALUES ('2020','12','LT2','MC9',True,True,3500,3000,0,135000,35000,0) #SQL to add a new monthly

    openDatabase()
    tenantBriefInfoD = cursor.execute("SELECT year, month, rent_Paid, rent_Late FROM units_Monthly WHERE tenant_ID = '" + str(scramble(current_tenant_ID)) + str("'")) 
    tenantBriefInfoMonthly = tenantBriefInfoD.fetchall()
    closeDatabase()
    if len(tenantBriefInfoMonthly) != 0: #If there is a tenant's month in the database
        i = startValueForAccountListing
        count = 0
        while i < len(tenantBriefInfoMonthly) and count < 5:
            year = deScramble(tenantBriefInfoMonthly[i][0])
            month = deScramble(tenantBriefInfoMonthly[i][1])
            rentPaid = deScramble(tenantBriefInfoMonthly[i][2])
            rentLate = deScramble(tenantBriefInfoMonthly[i][3])
            date = str(month) + '/' + str(year)
            openDatabase()
            complaintsIDsD = cursor.execute("SELECT complaint_ID FROM complaints WHERE year = '" + str(scramble(year)) + "' AND month = '" + str(scramble(month)) + "'")
            complaintsIDs = complaintsIDsD.fetchall()
            nOfCompaints = 0
            if len(complaintsIDs) != 0:
                for x in range(len(complaintsIDs)):
                    nOfCompaints = nOfCompaints + 1    
            if rentPaid == True:
                if rentLate == True:
                    rentPaidAnswer = 'Paid Late'
                else:
                    rentPaidAnswer = 'Paid on time'
            else:
                rentPaidAnswer = 'Not Paid'
            addTenantMonthlyLineOfData(date,rentPaidAnswer,nOfCompaints,i)
            i = i + 1
            count = count + 1
            global currentTentantMonthlyNumber
            currentTentantMonthlyNumber = currentTentantMonthlyNumber + 1
        if currentTentantMonthlyNumber != len(tenantBriefInfoMonthly):
            downButton = Button(canvasForTable, text='Down',height=1,bg=secondry.data, fg = primary.data, font=(font.data,16), justify='center',border=0,activeforeground=bannedColours['activeTextColor'],activebackground=secondry.data,command= lambda:changeTenantMonthlyTableHeight(currentTentantMonthlyNumber)).place(relx=0.4,rely=0.96,anchor='center')
        else:
            downButtonCover = Label(canvasForTable,height=1,bg=secondry.data,font=(font.data,16), justify='center',border=0).place(relx=0.4,rely=0.96,anchor='center')
        if currentTentantMonthlyNumber > 5:
            upButton = Button(canvasForTable, text='Up',height=1,bg=secondry.data, fg = primary.data, font=(font.data,16), justify='center',border=0,activeforeground=bannedColours['activeTextColor'],activebackground=secondry.data,command= lambda:changeTenantMonthlyTableHeight(currentTentantMonthlyNumber-count-5)).place(relx=0.6,rely=0.96,anchor='center')
        else:
            downButtonCover = Label(canvasForTable,height=1,bg=secondry.data,font=(font.data,16), justify='center',border=0).place(relx=0.6,rely=0.96,anchor='center')
    else:
        noTenantLabel = Label(canvasForTable, text='This tenant has no recorded monthly entrees', height=3 ,bg=secondry.data, fg = primary.data, font=(font.data,14), justify='center').place(relx=0.5,rely=0.5,anchor='center')
    return startValueForAccountListing

def addTenantMonthlyLineOfData(Date,RentPaid,nOfCompaints,i):
    rentPaidColourDict = {'Paid Late':bannedColours['warningYellow'],'Paid on time':bannedColours['emaraldGreen'],'Not Paid':bannedColours['errorRed']}
    createTenantMonthlyXaxisLines(76+76*((i%5)))
    score_ColumHeader = Label(canvasForTable, text=Date, height=2 ,bg=secondry.data, fg = primary.data, font=(font.data,14), justify='left').place(relx = 0.01, rely=0.23+0.15*((i)%5),anchor='w')
    email_ColumHeader = Label(canvasForTable, text=RentPaid, height=2 ,bg=secondry.data, fg = rentPaidColourDict[RentPaid], font=(font.data,14), justify='left').place(relx = 0.27, rely=0.23+0.15*((i)%5),anchor='w')
    late_Rent_ColumHeader = Label(canvasForTable, text=nOfCompaints, height=2 ,bg=secondry.data, fg = primary.data, font=(font.data,14), justify='left').place(relx = 0.66, rely=0.23+0.15*((i)%5),anchor='w')
    createTenantMonthlyYaxisLines(152+76*((i%5)))

def createTenantMonthlyXaxisLines(y):
    canvasForTable.create_line(110,y,110,y+76,fill=primary.data)
    canvasForTable.create_line(285,y,285,y+76,fill=primary.data)

def createTenantMonthlyYaxisLines(y):
    canvasForTable.create_line(0,y,850,y,fill=primary.data)

def changeTenantMonthlyTableHeight(inputNumber):
    global currentTentantNumber
    currentTentantNumber = inputNumber
    createTableForIndividualTenant(inputNumber)

def complaintsManagmentPage(tenantID):
    global current_tenant_ID
    current_tenant_ID = tenantID
    initialiseWindow()
    root.title('Property managment system - Complaints Management')
    topBorder = Label(root, text='Complaints Management', height=2 ,bg=primary.data, fg = secondry.data, width=42, font=(font.data,40), justify='center').place(relx=0,rely=0)
    displayBackButton()
    global previousPage
    previousPage = 'ComplaintsMangment'
    displayMenuButton()
    longNormal = PhotoImage(file = "Long-Normal.PNG")
    shortNormal = PhotoImage(file = "Short-Normal.PNG")

    personalIncomeBoxbackground = Label(image = longNormal, border = 0).place(relx=0.35,rely=0.25,anchor=CENTER)
    openDatabase()
    primaryColourD = cursor.execute("SELECT complaint_ID FROM complaints WHERE tenant_ID = '" +scramble(tenantID)+"'")
    data_To_Descrmable = primaryColourD.fetchall()
    global compaintsIDMenuOptions
    compaintsIDMenuOptions = []
    for i in range(len(data_To_Descrmable)):
        compaintsIDMenuOptions.append(data_To_Descrmable[i][0])
    compaintsIDMenuOptions.append('None')
    closeDatabase()
    global complaintIDMenu
    complaintIDMenu = ttk.Combobox(root, value=compaintsIDMenuOptions, justify=tkinter.CENTER, width = 50,font=(font.data,18))
    complaintIDMenu.place(relx=0.35,rely=0.25,anchor=CENTER)
    primaryHexEntryLabel = Label(root, text='Complaint ID',bg=primary.data, fg=secondry.data, width=33, font=(font.data,18), justify='center',relief='flat').place(relx=0.35,rely=0.17,anchor=CENTER)
    complaintIDMenu.current(compaintsIDMenuOptions.index('None'))
    root.option_add('*TCombobox*Listbox.font', (font.data,14)) 

    tenantIDBoxBackground = Label(image = shortNormal, border = 0).place(relx=0.82,rely=0.25,anchor=CENTER)
    openDatabase()
    primaryColourD = cursor.execute("SELECT tenant_ID FROM tenants WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.data)+"'")
    data_To_Descrmable = deScramble(primaryColourD.fetchall())
    global listOfTenantIDs
    listOfTenantIDs = []
    for i in range(len(data_To_Descrmable)):
        listOfTenantIDs.append(data_To_Descrmable[i][0])
    closeDatabase()
    global tenantIDMenu
    tenantIDMenu = ttk.Combobox(root, value=listOfTenantIDs, justify=tkinter.CENTER, width = 20,font=(font.data,18))
    tenantIDMenu.place(relx=0.82,rely=0.25,anchor=CENTER)
    primaryHexEntryLabel = Label(root, text='Complaint ID',bg=primary.data, fg=secondry.data, width=33, font=(font.data,18), justify='center',relief='flat').place(relx=0.82,rely=0.17,anchor=CENTER)
    tenantIDMenu.current(listOfTenantIDs.index(tenantID))

    DateBoxBackground = Label(image = shortNormal, border = 0).place(relx=0.185,rely=0.45,anchor=CENTER)
    activeComplaintID = complaintIDMenu.get()
    if activeComplaintID == 'None':
        month = 'Na'
        year = 'Na'
    else:
        openDatabase()
        primaryColourD = cursor.execute("SELECT month, year FROM complaints WHERE complaint_ID = '" +scramble(activeComplaintID)+"'")
        data_To_Descrmable = primaryColourD.fetchall()
        month = deScramble(data_To_Descrmable[0][0])
        year =  deScramble(data_To_Descrmable[0][1])
    primaryHexEntryLabel = Label(root, text='Date Complaint Made',bg=primary.data, fg=secondry.data, width=33, font=(font.data,18), justify='center',relief='flat').place(relx=0.185,rely=0.37,anchor=CENTER)
    slashLabel1 = Label(root,bg=primary.data, fg=secondry.data, font = ('Bahnschrift SemiLight',40),text='/').place(relx=0.18,rely=0.405)
    global monthEntryBox
    monthEntryBox = Entry(root, bg= primary.data,fg=secondry.data, width=10, font=(font.data,18),justify='center',relief='flat')
    monthEntryBox.insert(END,month)
    monthEntryBox.place(relx=0.12,rely=0.45,anchor=CENTER)
    global yearEntryBox
    yearEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=10, font=(font.data,18),justify='center',relief='flat')
    yearEntryBox.insert(END,year)
    yearEntryBox.place(relx=0.255,rely=0.45,anchor=CENTER)
    dateSubMessage = Label(root, text='In the form MM/YYYY',bg=primary.data, fg=secondry.data, font=(font.data,12), justify='center',relief='flat').place(relx=0.185,rely=0.52,anchor=CENTER)


    DateBoxBackground = Label(image = longNormal, border = 0).place(relx=0.65,rely=0.45,anchor=CENTER)
    activeComplaintID = complaintIDMenu.get()
    if activeComplaintID == 'None':
        complaintMessage = 'Not Applicable'
    else:
        openDatabase()
        primaryColourD = cursor.execute("SELECT complaint_Nature FROM complaints WHERE complaint_ID = '" +scramble(activeComplaintID)+"'")
        data_To_Descrmable = primaryColourD.fetchall()
        complaintMessage = deScramble(data_To_Descrmable[0][0])
    primaryHexEntryLabel = Label(root, text='Complaint Nature',bg=primary.data, fg=secondry.data, width=33, font=(font.data,18), justify='center',relief='flat').place(relx=0.65,rely=0.37,anchor=CENTER)
    global complaintMessageEntryBox
    complaintMessageEntryBox = Text(root, bg= primary.data,fg=secondry.data,height=3, width=90, font=(font.data,10),relief='flat')
    complaintMessageEntryBox.insert(END,complaintMessage)
    complaintMessageEntryBox.place(relx=0.65,rely=0.45,anchor=CENTER)

    resolutionBoxBackground = Label(image = longNormal, border = 0).place(relx=0.65,rely=0.65,anchor=CENTER)
    activeComplaintID = complaintIDMenu.get()
    if activeComplaintID == 'None':
        resolutionMessage = 'Not Applicable'
    else:
        openDatabase()
        primaryColourD = cursor.execute("SELECT resoltion FROM complaints WHERE complaint_ID = '" +scramble(activeComplaintID)+"'")
        data_To_Descrmable = primaryColourD.fetchall()
        resolutionMessage = deScramble(data_To_Descrmable[0][0])
    primaryHexEntryLabel = Label(root, text='Resolution',bg=primary.data, fg=secondry.data, width=33, font=(font.data,18), justify='center',relief='flat').place(relx=0.65,rely=0.57,anchor=CENTER)
    global resolutionEntryBox
    resolutionEntryBox = Text(root, bg= primary.data,fg=secondry.data,height=3, width=90, font=(font.data,10),relief='flat')
    resolutionEntryBox.insert(END,resolutionMessage)
    resolutionEntryBox.place(relx=0.65,rely=0.65,anchor=CENTER)
    resoluionSubMessage = Label(root, text='This box being empty implies that the complaint has not been resolved',bg=primary.data, fg=secondry.data, font=(font.data,12), justify='center',relief='flat').place(relx=0.65,rely=0.72,anchor=CENTER)

    submitButton = Button(root, text='S U B M I T', font=(font.data,'20','underline','bold'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=updateComplaints).place(relx=0.5, rely=0.90, anchor=CENTER)
    refreshButton = Button(root, text='Refresh Values', font=(font.data,'20','underline','bold'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=refreshValues).place(relx=0.185, rely=0.65, anchor=CENTER)
    deleteComplaintButton = Button(root, text='Delete Complaint', font=(font.data,'12','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=deleteComplaint).place(relx=0.185, rely=0.9, anchor=CENTER)
    addComplaintButton = Button(root, text='Add New Complaint', font=(font.data,'12','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=deleteComplaint).place(relx=1-0.185, rely=0.9, anchor=CENTER)

    global complaintsCords
    complaintsCords = {'complaint_ID':{'x':0.35,'y':0.32},'tenant_ID':{'x':0.82,'y':0.32},'month':{'x':0.185,'y':0.52},'year':{'x':0.185,'y':0.52},'complaint_Nature':{'x':0.65,'y':0.52},'resoltion':{'x':0.65,'y':0.72}}

    root.mainloop()

def updateComplaints():
    tenant_ID = tenantIDMenu.get()
    complaint_ID = complaintIDMenu.get()
    openDatabase()
    listOfPossibleComplaintIDsD = cursor.execute("SELECT complaint_ID FROM complaints WHERE tenant_ID = '" +scramble(tenant_ID)+"'")
    listOfPossibleComplaintIDsD = listOfPossibleComplaintIDsD.fetchall()
    complaintIDValid = False
    for i in range(len(listOfPossibleComplaintIDsD)):
        if listOfPossibleComplaintIDsD[i][0] == complaint_ID:
            complaintIDValid = True
    if complaintIDValid == False:
        warningTwo = Label(root,bg=primary.data,fg=bannedColours['errorRed'],text='This complaint doesnt belong to the tenant',font=(font.data,10),justify='center').place(relx=0.35,rely=0.32,anchor=CENTER)
    else:
        coverup = Label(root,bg=primary.data,width=75,font=(font.data,10),justify='center').place(relx=0.35,rely=0.32,anchor=CENTER)
        complaint_ID = uInputDataObj(complaintIDMenu.get(),str)
        tenant_ID = uInputDataObj(complaintIDMenu.get(),str)
        month = uInputDataObj(monthEntryBox.get(),int)
        year = uInputDataObj(yearEntryBox.get(),int)
        complaint_Nature = uInputDataObj(complaintMessageEntryBox.get('1.0','end-1c'),str)
        resoltion = uInputDataObj(resolutionEntryBox.get('1.0','end-1c'),str)
        compaintsFields = ['complaint_ID','tenant_ID','month','year','complaint_Nature','resoltion']
        newComplaintsField = [complaint_ID,tenant_ID,month,year,complaint_Nature,resoltion]
        global dictOfDataValdationResults
        dictOfDataValdationResults = dict.fromkeys(compaintsFields)
        #dictOfDataValdationResults['complaint_ID'] = {'presenceCheck':presenceCheck(complaint_ID)}
        #dictOfDataValdationResults['tenant_ID'] = {'presenceCheck':presenceCheck(tenant_ID)}
        dictOfDataValdationResults['month'] = {'presenceCheck':presenceCheck(month),'monthBetween1/12':rangeCheck(month,1,12)}
        dictOfDataValdationResults['year'] = {'presenceCheck':presenceCheck(year),'yearBetween1900/2100':rangeCheck(year,1900,2100)}
        dictOfDataValdationResults['complaint_Nature'] = {'presenceCheck':presenceCheck(complaint_Nature),'mustContainsLetters':containsLetters(complaint_Nature)}

        for entryboxData in dictOfDataValdationResults.keys():
            if dictOfDataValdationResults[entryboxData] != None:
                coverUp = Label(root,bg=primary.data,width=75,font=(font.data,7),justify='center').place(relx=complaintsCords[entryboxData]['x'],rely=complaintsCords[entryboxData]['y'],anchor=CENTER)

        for entryboxData in dictOfDataValdationResults.keys():
            countOfFailedTests = 0
            if dictOfDataValdationResults[entryboxData] != None:
                for test in dictOfDataValdationResults[entryboxData].keys():
                    while dictOfDataValdationResults[entryboxData][test] == False and countOfFailedTests == 0:
                        disaplayEM(test,complaintsCords[entryboxData]['x'],complaintsCords[entryboxData]['y'])
                        countOfFailedTests = countOfFailedTests + 1

        countOfFailedTests = 0
        for entryboxData in dictOfDataValdationResults.keys():
            if dictOfDataValdationResults[entryboxData] != None:
                for test in dictOfDataValdationResults[entryboxData].values():
                    if test == False:
                        countOfFailedTests = countOfFailedTests +1

        if countOfFailedTests == 0:
            for i in range(len(newComplaintsField)):
                newComplaintsField[i] = scramble(newComplaintsField[i].data)
            print("UPDATE complaints SET month = '" + newComplaintsField[2] + "', year = '" + newComplaintsField[3] + "', complaint_Nature = '" + newComplaintsField[4] + "', resoltion = '" + newComplaintsField[5] + "' WHERE complaint_ID = '" + scramble(complaint_ID.data) + "'")
            openDatabase()
            cursor.execute("UPDATE complaints SET month = '" + newComplaintsField[2] + "', year = '" + newComplaintsField[3] + "', complaint_Nature = '" + newComplaintsField[4] + "', resoltion = '" + newComplaintsField[5] + "' WHERE complaint_ID = '" + scramble(complaint_ID.data) + "'")
            closeDatabase()
            
            displayConfirmation('ComplaintsMangment')
    closeDatabase()

def refreshValues():
    global current_tenant_ID
    tenant_ID = tenantIDMenu.get()
    complaint_ID = complaintIDMenu.get()
    openDatabase()
    listOfPossibleComplaintIDsD = cursor.execute("SELECT complaint_ID FROM complaints WHERE tenant_ID = '" +scramble(tenant_ID)+"'")
    listOfPossibleComplaintIDsD = listOfPossibleComplaintIDsD.fetchall()
    closeDatabase()
    if len(listOfPossibleComplaintIDsD) != 0:
        coverup = Label(root,bg=primary.data,width=75,font=(font.data,10),justify='center').place(relx=0.35,rely=0.32,anchor=CENTER)
        complaintIDValid = False
        for i in range(len(listOfPossibleComplaintIDsD)):
            if listOfPossibleComplaintIDsD[i][0] == complaint_ID:
                complaintIDValid = True
        if complaintIDValid == True:
            coverupTwo = Label(root,bg=primary.data,fg=bannedColours['warningYellow'],width=100,font=(font.data,10),justify='center').place(relx=0.35,rely=0.32,anchor=CENTER)
            openDatabase()
            complaintInfo = cursor.execute("SELECT month, year, complaint_Nature, resoltion FROM complaints WHERE complaint_ID = '" + scramble(complaint_ID) + "'")
            complaintInfo = complaintInfo.fetchall()
            print(complaintInfo)
            closeDatabase()
            monthEntryBox.delete(0,'end') #entry boxes use (0,'end') as the arguemnt to clear themselves
            monthEntryBox.insert(END, deScramble(complaintInfo[0][0]))
            yearEntryBox.delete(0,'end')
            yearEntryBox.insert(END, deScramble(complaintInfo[0][1]))
            complaintMessageEntryBox.delete(1.0,'end') #text boxes use (1.0,'end') as the arguemnt to clear themselves
            complaintMessageEntryBox.insert(END, deScramble(complaintInfo[0][2]))
            resolutionEntryBox.delete(1.0,'end')
            resolutionEntryBox.insert(END, deScramble(complaintInfo[0][3]))
        else:
            warningTwo = Label(root,bg=primary.data,fg=bannedColours['warningYellow'],text='This complaint doesnt belong to the tenant',font=(font.data,10),justify='center').place(relx=0.35,rely=0.32,anchor=CENTER)
    else:
        warning = Label(root,bg=primary.data,fg=bannedColours['warningYellow'],text='This tenant has no complaints',font=(font.data,10),justify='center').place(relx=0.82,rely=0.32,anchor=CENTER)

def deleteComplaint():
    compalaint_ID = complaintIDMenu.get()
    openDatabase()
    cursor.execute("DELETE FROM complaints WHERE complaint_ID = '" + scramble(compalaint_ID) + "'")
    closeDatabase()

def addComplaintPage():
    pass


initialise()
print('Program Finished')