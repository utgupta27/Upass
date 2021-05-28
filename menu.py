import os
from database import UserBase
from encrypt import Encrypt
class menu():
    def __init__(self):
        self.obj=UserBase()

    def _getDetails(self):
        self.userName = input("Enter your UserName: ")
        self.userPassword = input("Enter your Password: ")

    def _getData(self):
        self.siteName = input("Enter the Name of Website: ")
        self.siteUserName = input("Enter Website Username : ")
        self.sitePassword = input("Enter Website Password: ")

    def _mainMenu(self):
        while True:
            os.system('clear')    
            print("""
        *********MAIN MENU**********
            1. Login (Existing User)
            2. Create New Account
            3. Exit""")
            choice = input("Enter Your choice : ")
            if choice == "1":
                self._loginMenu()
            elif choice == "2":
                self._createMenu()
            elif choice =="3":
                break

    def showAllPassMenu(self):
        while True:
            os.system('clear')
            self.obj.showAllPassword(self.userName,self.userPassword)
            print("""
            2. Go back to previous menu""")
            ch = int(input("Enter Your Choice: "))
            if ch == 2:
                break

    def addMenu(self):
        self._getData()
        UserBase().addEntry(self.userName,self.userPassword,self.siteName,self.siteUserName,self.sitePassword)
        print("""
        ## Password Added Successfully ##
        press enter to continue...""")
        input("")


    def _loginSubMenu(self):
        while True:
            os.system('clear')
            print("\t**********"+self.userName+"*********")
            print("""
            1. Show All Passwords
            2. Add New Password
            3. Remove Password From List
            4. Change Master Password
            5. Delete Account
            6. Logout\n""")
            choice= int(input("Enter Your Choice : "))
            if choice == 1:
                self.showAllPassMenu()
            elif choice == 2:
                self.addMenu()
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                self._deleteMenu()
            elif choice == 6:
                print("## Logging Out ##")
                print("Press Enter to Continue...")
                input("")
                break

    def _loginMenu(self):
        self._getDetails()
        if self.obj.verify(self.userName,self.userPassword) == True:
            self._loginSubMenu()
        else :
            print("\n## Incorrect Credentials ##")
            print("Press Enter to go back to Main Menu...")
            input(" ")

    def _createMenu(self):
        while True:
            os.system('clear')
            print("""
        *********NEW USER**********
            1.Enter New Credentials
            2.Back to Main Menu""")
            choice =  int(input("Enter Your Choice :"))
            if choice == 1:
                self._getDetails()
                self.obj.createUserAccount(self.userName,self.userPassword)
            elif choice==2:
                break        

    def _deleteMenu(self):
        while True:
            os.system('clear')
            print("""
        *********DELETE USER ACCOUNT**********
            1.Enter Credentials
            2.Back to Main Menu""")
            choice =  int(input("Enter Your Choice :"))
            if choice == 1:
                self._getDetails()
                if self.obj.verify(self.userName, self.userPassword) == True:
                    self.obj.deleteUserAccount(self.userName)
                    print("Account Deleted Successfully.\nPress Enter to Exit")
                    input('')
                    exit()
                else:
                    print("\n## Incorrect Credentials ##")
                    print("Press Enter to Resubmit Credentials")
                # self.obj.createUserAccount(self.userName,self.userPassword)
            elif choice==2:
                break

if __name__ == "__main__":
    menuobj = menu()
    menuobj._mainMenu()