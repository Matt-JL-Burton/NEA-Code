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
            #displayTCs()
            newTenantPage()

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
    global errorMessgesDict, databaseCurrentAccount_ID
    primary = uInputDataObj('#373f51',str)
    secondry = uInputDataObj('#ffffff',str)
    tertiary = uInputDataObj('#a9a9a9',str)
    bannedColours = {'errorRed':'#FF0000','warningYellow':'#','activeTextColor':'dark grey'}
    errorMessgesDict = {'presenceCheck':'Please give an input','uniqueDataCheck':'Sorry a this data is not unique in the database - it must be unique','lengthCheck':'Sorry the length of this input is not appropriate','pictureCheck':'Sorry the format of this input is invalid','lengthOverSevenCheck':'This input must be more than 7 charcters long','@check':'This input must contain 1 "@" symbol','containsOnlyLetters':'This input should only contain letters','typeCheck':'Sorry the data type of this data is wrong','positiveCheck':'This input must be a positive number','menuOptionCheck':'Please pick and option that is in the menu','noSpaces':'Sorry this input cannot have any spaces in it','dayBetween0/31':'Please enter a day between 0 and 31','monthBetween1/12':'Please enter an integar between 1 and 12','yearBetween1000/9999':'Please enter a year in 1000 and 9999','between0/100':'Please enter number between 0 and 100'}
    font = uInputDataObj('Bahnschrift SemiLight',str)
    listOfIdealTables = ['accounts', 'complaints', 'loan', 'refinance', 'sold_Units', "tenants", "units_Monthly", 'units']
    databaseName = 'Property Managment System Database.db'
    listOfIdealAssets = ['Long-Fat.PNG','Long-Normal.PNG','Long-Skinny.PNG','Short-Fat.PNG','Short-Normal.PNG','House.ico']
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
    normalSet = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','`','¬','!','"','£','$','%','^','&','*','(',')','_','-','=','+',';',':','@',"'",' ','#',',','.','?','/']
    mappingSet = ['m', '3', '4', 'A', 'e', 'b', 'o', 'B', 'u', 'w', 'C', 'a', '2', 'i', 'D', 'E', 'F', '9', "G", 'g', 'H', 'I', '7', 'J', 'h', 'K', '6', 'L', 'M', 'x', 's', 'N', 'O', 'p', 'P', '5', 'r','Q', '0', 'c', 'R', 't', 'd', 'q', 'f', 'S', 'z', 'k', 'T', 'y', 'j', 'U', 'V', 'n', 'W', '8', 'l', 'X', 'Y', 'Z', '1', 'v']
    databaseCurrentAccount_ID = None

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
    longNormal = PhotoImage(file = "Long-Normal.PNG")
    longNormalLabelU = Label(image = longNormal, border = 0).place(relx=0.5,rely=0.37,anchor=CENTER)
    global usernameEntry
    usernameEntry = Entry(root, bg=primary.data, fg=secondry.data, width=42, font=(font.data,24),justify='center',relief='flat')
    usernameEntry.place(relx=0.5,rely=0.37,anchor=CENTER)
    #password input
    passwordHeaderL = Label(root,text='Password',font=((font.data,'15')),fg=secondry.data,bg=primary.data).place(relx=0.5,rely=0.55, anchor=CENTER)
    longNormalLabelP = Label(image = longNormal, border = 0).place(relx=0.5,rely=0.64,anchor=CENTER)
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
    passwordSubLabel = Label(root, text='As with all user data input, the password is none case sensative',bg=primary.data, fg=secondry.data, width=60, font=(font.data,7), justify='center',relief='flat').place(relx=0.75,rely=0.315,anchor=CENTER)

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

def createAccount():
    recovery_Email = uInputDataObj(emailEntryBox.get(),str)
    first_Name = uInputDataObj(firstNameEntryBox.get(),str)
    operation_Type = uInputDataObj(operationTypeMenu.get(),str)
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
    dictOfDataValdationResults['title'] = {'containsOnlyLetters':containsOnlyLetters(title),'presenceCheck':presenceCheck(title)}
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
    # openDatabase()
    # otherIncome = cursor.execute('SELECT other_Income_Estimate FROM accounts WHERE account_ID ='+str(accountID))
    # closeDatabase()
    # #TODO: need to find other income streams
    tax_Rate = 'b'
    return(tax_Rate)

def scramble(data):
    data = str(data)
    data = data.lower()
    data = list(data)
    for i in range(len(data)):
        data[i] = mappingSet[normalSet.index(data[i])]
    data = listToString(data)
    data = data[::-1]
    return(data)

def deScramble(data):
    data = str(data)
    data = list(data)
    data = data[::-1]
    for i in range(len(data)):
        data[i] = normalSet[mappingSet.index(data[i])]
    data = listToString(data)
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
    if inputData.data == '0':
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

def disaplayEM(errorType,x,y):
    warning = Label(root, text = errorMessgesDict[errorType],bg=primary.data,width=75, fg = bannedColours['errorRed'], font=(font.data,9),justify='center').place(relx=x,rely=y,anchor=CENTER)

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
        if deScramble(str(storedPasswordForAccount[0][0])) == password.data.lower():
            openDatabase()
            account_ID_Dirty = cursor.execute("SELECT account_ID FROM ACCOUNTS WHERE recovery_Email = '" + str(scramble(castingTypeCheckFunc(recovery_Email.data,recovery_Email.prefferredType)))+str("'") )
            #global databaseCurrentAccount_ID
            databaseCurrentAccount_ID = account_ID_Dirty.fetchall()[0][0]
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
    root.mainloop()

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
    newTenantEntryBoxCords = {'tenant_Email':{'x':0.825,'y':0.8575},'tenant_ID':{'x':0.175,'y':0.3175},'title':{'x':0.175,'y':4975},'day':{'x':0.175,'y':0.6775},'month':{'x':0.175,'y':0.6775},'year':{'x':0.175,'y':0.6775},'gerneral_Notes':{'x':0.175,'y':0.9},'last_Name':{'x':0.5,'y':0.3175},'total_Residents':{'x':0.5,'y':0.4975},'deposit':{'x':0.5,'y':0.6775},'first_Name':{'x':0.825,'y':8575}}

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
    root.mainloop()

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
    global databaseCurrentAccount_ID
    if (databaseCurrentAccount_ID) == None:
        databaseCurrentAccount_ID = 'MLxCFaKADb'
    account_ID = uInputDataObj(databaseCurrentAccount_ID,str)
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

    tenantsFields = ['tenant_ID','account_ID','tenant_Email','first_Name','title','date_Of_Birth','score','total_Residents','start_Date','deposit','gerneral_Notes']
    global dictOfDataValdationResults
    dictOfDataValdationResults = dict.fromkeys(tenantsFields)
    dictOfDataValdationResults['tenant_Email'] = {'lengthCheck':rangeCheck(tenant_Email,3,None),'@check':pictureCheck(tenant_Email,'@',1,1),'noSpaces':pictureCheck(tenant_Email,'',0,0),'uniqueDataCheck':uniqueDataCheck(tenant_Email,'tenant_Email','tenants')}
    dictOfDataValdationResults['first_Name'] = {'presenceCheck':presenceCheck(first_Name),'containsOnlyLetters':containsOnlyLetters(first_Name)}
    dictOfDataValdationResults['last_Name'] = {'presenceCheck':presenceCheck(last_Name),'containsOnlyLetters':containsOnlyLetters(last_Name)}
    dictOfDataValdationResults['day'] = {'presenceCheck':presenceCheck(day),'dayBetween0/31':rangeCheck(day,0,31)}
    dictOfDataValdationResults['month'] = {'presenceCheck':presenceCheck(month),'monthBetween1/12':rangeCheck(month,1,12)}
    dictOfDataValdationResults['year'] = {'presenceCheck':presenceCheck(year),'yearBetween1000/9999':rangeCheck(year,1000,9999)}
    dictOfDataValdationResults['score'] = {'presenceCheck':presenceCheck(score),'between0/100':rangeCheck(score,0,100)}
    dictOfDataValdationResults['total_Residents'] = {'presenceCheck':presenceCheck(total_Residents),'positiveCheck':rangeCheck(total_Residents,0,None)}
    dictOfDataValdationResults['startMonth'] = {'presenceCheck':presenceCheck(startMonth),'monthBetween1/12':rangeCheck(startMonth,1,12)}
    dictOfDataValdationResults['startYear'] = {'presenceCheck':presenceCheck(startYear),'yearBetween1000/9999':rangeCheck(startYear,1000,9999)}
    dictOfDataValdationResults['deposit'] = {'presenceCheck':presenceCheck(deposit),'postiveCheck':rangeCheck(deposit,0,None)}
    dictOfDataValdationResults['gerneral_Notes'] = {'presenceCheck':presenceCheck(gerneral_Notes),'lengthCheck':rangeCheck(gerneral_Notes,0,1024)}
    print(dictOfDataValdationResults)

initialise()