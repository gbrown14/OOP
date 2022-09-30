class PayrollDeduction: 

    def __init__(self, description, date, charge, empID):
        self._description = description
        self._date = date
        self._charge = charge
        self._empID = empID

        #returns

    def getDescription(self):
        return self._description
    
    def getDate(self):
        return self._date

    def getCharge(self):
        return self._charge

    def getEmpID(self):
        return self._empID