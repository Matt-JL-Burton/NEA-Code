
#data validation tests
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

def howManySymbolsInStr(data, symbolLookingFor):
    if type(data) == string and type(symbolLookingFor) == string:
        count = 0
        for i in range(len(data)):
            if data[i] == symbolLookingFor:
                count = count + 1
        return count
    else: 
        raise TypeError('All data inputted must be a string')

def pictureCheck(data,symbol,minimum, maximum):
    if type(data) == str and type(symbol) == str:
        if type(minimum) == int or minimum == None and type(maximum) == int or maximum == None:
            numberOfSymbols = howManySymbolsInStr(data, symbol)
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

def rangeCheck(data,lowerBound,upperBound):
    #inclusive of bounds - this func can be used for length checking aswell by using the len method on data as an argument for the func
    if (type(lowerBound) == float or type(lowerBound) == int or lowerBound == None) and (type(upperBound) == float or type(upperBound) == int or upperBound == None):
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

def noNumbers(data):
    if type(data) == str:
        if data.isalpha():
            return True
        else:
            return False
    else:
        raise TypeError('All data inputted must be a string')
         
def startsWith(data, symbol):
    if type(data) != str:
        if data[0] == symbol:
            return True
        else:
            return False
    else:
        raise TypeError('All data inputted must be a string')

