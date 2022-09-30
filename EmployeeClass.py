
class employee:
    def __init__(self, name, ID, department, job_title, salary): 
        self._name = name
        self._ID = ID
        self._department = department
        self._job_title = job_title
        self._salary = salary

            #return

    def getName(self):
        return self._name
    def getID(self):
        return self._ID
    def getDepartment(self):
        return self._department
    def getJobTitle(self):
        return self._job_title
    def getSalary(self):
        return self._salary