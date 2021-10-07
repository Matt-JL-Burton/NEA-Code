#importing modules
from email import message
from http.client import GATEWAY_TIMEOUT
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
import pathlib
import platform
import tkinter.font as tkfont
import urllib.request
from matplotlib.pyplot import autoscale, flag, get, pink, prism, text
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
            displayTCs()
            #settingsPage()

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
    global errorMessgesDict, databaseCurrentAccount_ID, listOfSecondryColourOptions, listOfAcceptedFonts
    primary = uInputDataObj('#373f51',str)
    secondry = uInputDataObj('white',str)
    tertiary = uInputDataObj('#a9a9a9',str)
    listOfSecondryColourOptions = ['white','light grey','grey','dark grey','black']
    bannedColours = {'errorRed':'#FF0000','warningYellow':'#','activeTextColor':'dark grey'}
    errorMessgesDict = {'presenceCheck':'Please give an input of correct data type','uniqueDataCheck':'Sorry a this data is not unique in the database - it must be unique','lengthCheck':'Sorry the length of this input is not appropriate','pictureCheck':'Sorry the format of this input is invalid','lengthOverSevenCheck':'This input must be more than 7 charcters long','@check':'This input must contain 1 "@" symbol','containsOnlyLetters':'This input should only contain letters','typeCheck':'Sorry the data type of this data is wrong','positiveCheck':'This input must be a positive number','menuOptionCheck':'Please pick and option that is in the menu','noSpaces':'Sorry this input cannot have any spaces in it','dayBetween0/31':'Please enter a day between 0 and 31','monthBetween1/12':'Please enter an integar between 1 and 12','yearBetween1900/2100':'Please enter a year in 1900 and 2100','between0/100':'Please enter number between 0 and 100','mustContainsLetters':'The input must contain atleast one letter','mustContainNumbers':'The input must contain atleast one number','hexCodeCheck':'Please enter a valid hex code','fontCheck':'Sorry this font is not supported please try again'}
    font = uInputDataObj('Bahnschrift SemiLight',str)
    listOfIdealTables = ['accounts', 'complaints', 'loan', 'refinance', 'sold_Units', "tenants", "units_Monthly", 'units']
    databaseName = 'Property Managment System Database.db'
    listOfIdealAssets = ['Long-Fat.PNG','Long-Normal.PNG','Long-Skinny.PNG','Short-Fat.PNG','Short-Normal.PNG','House.ico','Long-Normal 2.PNG']
    connectionError = Tk()
    connectionError.destroy()
    previousPage = None
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
    databaseCurrentAccount_ID = uInputDataObj(deScramble('XTN:[?]NVS'),str) #instansaite the current account object - also allows me the developer to access pages using test accoutns without signing in
    listOfAcceptedFonts = ['Bahnschrift Semilight','Georgia','Courier New','Microsoft Sans Serif','Franklin Gothic Medium','Times New Roman','Calibri','Comic Sans MS']
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
            chdir('..')
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
    hidePasswordLoginPageB = Button(root, text='Hide', font=(font.data,'15','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=hidePasswordLoginPage).place(relx=0.15, rely=0.64, anchor=CENTER)
    createAccountPageB = Button(root, text='Create Account', font=(font.data,'15','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=createAccountPage).place(relx=0.2, rely=0.9, anchor=CENTER)
    ForgottenPageB = Button(root, text='Forgotten Password?', font=(font.data,'15','underline'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=forgottenPasswordPageOne).place(relx=0.8, rely=0.9, anchor=CENTER)
    submitLoginDetailsB = Button(root, text='L O G I N', font=(font.data,'20','underline','bold'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=login).place(relx=0.5, rely=0.9, anchor=CENTER)
    root.mainloop()

def convertAssetColor(primaryHex,secondryHex):
    if ((os.getcwd()).split(path_seperator))[len(os.getcwd().split(path_seperator))-1] != 'Assets':
        chdir(f'.{path_seperator}Assets')
    listOfAssets = os.listdir(os.getcwd())
    testAsset = listOfAssets[1]
    img = Image.open(testAsset)
    newPrimary = list(ImageColor.getcolor(primaryHex.data, "RGBA"))
    newSecondry = list(ImageColor.getcolor(secondryHex.data, "RGBA"))
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

def hidePasswordLoginPage():
    #TODO: hide the password 
    #TODO: replace the hide button with a show button and then code show button
    pass

def showPasswordLoginPage():
    #TODO: same as above function
    pass

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

    createAccountArray = [account_ID.data,password.data,recovery_Email.data,first_Name.data,last_Name.data, operation_Type.data, title.data, getTaxRate(account_ID.data),other_Income_Estimate.data,bIncTR.data, hIncTR.data, aIncTR.data, bIncCutOff.data, hIncCutOff.data, corpTR.data, bCapGainsTR.data, bCapGainsAllowence.data, hCapGainsTR.data, aCapGainsTR.data, corpCapGainsTR.data,national_Insurance_Due.data, primary.data, secondry.data, tertiary.data, font.data]
    accountFields = ['account_ID', 'password', 'recovery_Email', 'first_Name', 'last_Name', 'operation_Type', 'title', 'tax_Rate', 'other_Income_Estimate', 'basic_Income_Rate', 'high_Income_Rate', 'additional_Income_Rate', 'basic_Income_Cut_Off', 'high_Income_Cut_Off', 'corporation_Rate', 'basic_Capital_Gains_Rate', 'basic_Capital_Gains_Allowence', 'high_Capital_Gains_Rate', 'additional_Capital_Gains_Rate', 'corporation_Capital_Gains_Rate', 'national_Insurance_Due', 'primary_Colour', 'secondry_Colour', 'tertiary_Colour','font']
        

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
        accountsInsertionCommand = """INSERT INTO accounts(account_ID, password, recovery_Email, first_Name, last_Name, operation_Type, title, tax_Rate, other_Income_Estimate, basic_Income_Rate, high_Income_Rate, additional_Income_Rate, basic_Income_Cut_Off, high_Income_Cut_Off, corporation_Rate, basic_Capital_Gains_Rate, basic_Capital_Gains_Allowence, high_Capital_Gains_Rate, additional_Capital_Gains_Rate, corporation_Capital_Gains_Rate, national_Insurance_Due, primary_Colour, secondry_Colour, tertiary_Colour, font)
        Values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
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
    if castingTypeCheckFunc(inputData.data,inputData.prefferredType) != False or inputData.data == '0':
        if inputData.prefferredType == str:
            dataToTest = len(castingTypeCheckFunc(inputData.data,inputData.prefferredType))
        else:
            dataToTest = castingTypeCheckFunc(inputData.data,inputData.prefferredType)
        #inclusive of bounds - this func can be used for length checking aswell by using the len method on data as an argument for the func
        if (type(lowerBound) == float or type(lowerBound) == int or lowerBound == None) and (type(upperBound) == float or type(upperBound) == int or upperBound == None):
            if lowerBound == None and upperBound != None:
                if dataToTest <= upperBound:
                    return True
                else:
                    return False
            elif upperBound == None and lowerBound != None:
                if dataToTest >= lowerBound:
                    return True
                else:
                    return False
            elif upperBound == None and lowerBound == None:
                raise TypeError('Both Bounds cannot be None')
            else:

                if dataToTest >= lowerBound and dataToTest <= upperBound:
                    return True
                else:
                    return False
        else:
            raise TypeError('Bounds where the incorrect data type') 
    else:
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
    hexCodePossibleCharacters = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    if castingTypeCheckFunc(inputData.data, inputData.prefferredType) != False:
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
# end of data validation tests

def disaplayEM(errorType,x,y):
    warning = Label(root, text = errorMessgesDict[errorType],bg=primary.data,width=65, fg = bannedColours['errorRed'], font=(font.data,9),justify='center').place(relx=x,rely=y,anchor=CENTER)

def createAccountCoverUpErrorMessage():
    for entryboxData in dictOfDataValdationResults.keys():
        if dictOfDataValdationResults[entryboxData] != None:
            coverUp = Label(root,bg=primary.data,width=75,font=(font.data,7),justify='center').place(relx=accountPageEntryMessageBoxCords[entryboxData]['x'],rely=accountPageEntryMessageBoxCords[entryboxData]['y'],anchor=CENTER)

def displayConfirmation(nextPageCommand):
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
    contactPageButton = Button(root, text='Contact Page', font=(font.data,'17','underline'),fg=primary.data,bg=secondry.data,activeforeground=bannedColours['activeTextColor'],activebackground=secondry.data,border=0,command=contactPage).place(relx=0.5, rely=0.775, anchor=CENTER)
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

    newUnitArray = [unit_ID.data,databaseCurrentAccount_ID.data,tenant_ID.data,property_Equity.data+capital_Owed.data,property_Equity.data+capital_Owed.data,address.data,postcode.data,buy_Month.data,buy_Year.data,property_Equity.data,rent.data,general_Notes.data]
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
    topBorder = Label(root, text='Tenants', height=2 ,bg=primary.data, fg = secondry.data, width=42, font=(font.data,40), justify='center').place(relx=0,rely=0)
    displayBackButton()
    global previousPage
    previousPage = 'Tenants'
    displayMenuButton()
    root.mainloop()

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
    topBorder = Label(root, text='Tax', height=2 ,bg=primary.data, fg = secondry.data, width=42, font=(font.data,40), justify='center').place(relx=0,rely=0)
    displayBackButton()
    global previousPage
    previousPage = 'Tax'
    displayMenuButton()
    root.mainloop()

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
    primaryColourD = deScramble(data_To_Descrmable)
    primaryHexEntryBox.insert(END,primaryColourD)
    closeDatabase()
    primaryHexEntryBox.place(relx=0.175,rely=0.25,anchor=CENTER)
    primaryHexEntryLabel = Label(root, text='Primary Colour Hex Code',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.175,rely=0.17,anchor=CENTER)

    secondryHexEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.175,rely=0.43,anchor=CENTER)
    openDatabase()
    global secondryColourOptions
    secondryColourOptions = listOfSecondryColourOptions
    openDatabase()
    currentSecondryD = cursor.execute("SELECT secondry_Colour FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.getData())+"'")
    currentSecondryD = deScramble(currentSecondryD.fetchall()[0][0])
    global secondryColourMenu
    secondryColourMenu = ttk.Combobox(root, value=secondryColourOptions, justify=tkinter.CENTER, font=(font.data,18))
    secondryColourMenu.current(secondryColourOptions.index(currentSecondryD))
    root.option_add('*TCombobox*Listbox.font', (font.data,14)) 
    secondryColourMenu.place(relx=0.175,rely=0.43,anchor=CENTER)
    closeDatabase()
    secondryHexEntryLabel = Label(root, text='Secondry Colour Hex Code',bg=primary.data, fg=secondry.data, width=23, font=(font.data,18), justify='center',relief='flat').place(relx=0.175,rely=0.35,anchor=CENTER)

    tertiaryHexEntryBoxbackground = Label(image = shortNormal, border = 0).place(relx=0.175,rely=0.61,anchor=CENTER)
    global tertiaryHexEntryBox
    tertiaryHexEntryBox = Entry(root, bg=primary.data,fg=secondry.data, width=23, font=(font.data,18),justify='center',relief='flat')
    openDatabase()
    tertiaryColourD = cursor.execute("SELECT tertiary_colour FROM accounts WHERE account_ID = '" +scramble(databaseCurrentAccount_ID.data)+"'")
    tertiaryColourD = deScramble(tertiaryColourD.fetchall()[0][0])
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
    settingsCords = {'primary_Colour':{'x':0.175,'y':0.3175},'secondry_Colour':{'x':0.175,'y':4975},'tertiary_Colour':{'x':0.175,'y':0.6775},'font':{'x':0.6635,'y':0.3175},'title':{'x':0.5,'y':0.4975},'operation_Type':{'x':0.83,'y':0.4975},'first_Name':{'x':0.5,'y':0.6775},'last_Name':{'x':0.83,'y':0.6775}}
    submitUnitDetailsB = Button(root, text='S U B M I T', font=(font.data,'20','underline','bold'),fg=secondry.data,bg=primary.data,activeforeground=bannedColours['activeTextColor'],activebackground=primary.data,border=0,command=updateSetings).place(relx=0.5, rely=0.93, anchor=CENTER)

    root.mainloop()

def updateSetings():
    primary_Colour = uInputDataObj(primaryHexEntryBox.get(),str)
    secondry_Colour = uInputDataObj(secondryColourMenu.get(),str)
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
    dictOfDataValdationResults['secondry_Colour'] = {'menuOptionCheck':menuOptionCheck(secondry_Colour,secondryColourOptions)}
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
        for i in range(len(newListOfAccount)):
            newListOfAccount[i] = scramble(newListOfAccount[i])

        openDatabase()
        accocountUpdateCommand = ("UPDATE accounts SET primary_Colour = '" + str(primary_Colour.data) + "', secondry_Colour = '" + str(secondry_Colour.data) + "', tertiary_Colour = '" + str(tertiary_Colour.data) + "', font = '" + str(font.data) + "', operation_Type = '" + str(operation_Type.data) + "', title = '" + str(title.data) + "', first_Name = '" + str(first_Name.data) + "', last_Name = '" + str(last_Name.data) + "' WHERE account_ID = '" + str(scramble(databaseCurrentAccount_ID.data)) +"'")
        cursor.execute(accocountUpdateCommand)
        closeDatabase()

    redoConfigureAccountSettingsVariables()
    displayConfirmation('Settings')

def settingsPageCoverUp():
    for entryboxData in dictOfDataValdationResults.keys():
        if dictOfDataValdationResults[entryboxData] != None:
            coverUp = Label(root,bg=primary.data,width=75,font=(font.data,7),justify='center').place(relx=settingsCords[entryboxData]['x'],rely=settingsCords[entryboxData]['y'],anchor=CENTER)

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
    allAcoountData = allAcoountData.fetchall[0]
    print(allAcoountData)
    closeDatabase()

initialise()