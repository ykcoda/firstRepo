class Student:

    __pFirstName = ""
    __pLastName = ""

    def __getFirstName(self):
        return self.__pFirstName

    def __setFirstName(self, value):
        self.__pFirstName = value

    def __getLastName(self):
        return self.__pLastName

    def __setLastName(self, value):
        self.__pLastName = value

    FirstName = property(__getFirstName, __setFirstName)
    LastName = property(__getLastName, __setLastName)

    def getFullName(self):
        fullName = self.__pFirstName + " " + self.__pLastName
        return fullName
