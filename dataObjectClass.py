class uInputDataObj():
    def __init__(self, data, prefferredType):
        self.data = data
        self.prefferredType = prefferredType
    
    def setData(self,newData):
        self.data = newData

    def getData(self):
        return self.data