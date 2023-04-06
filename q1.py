from sys import argv
from enum import  Enum
from datetime import datetime


class Role(Enum):
  OrdinaryUser = 1
  AdminUser = 2
  
class User:
    _Users =[]
    def __init__(self,name,lname,username,password,role=Role.OrdinaryUser):
        self.name = name
        self.lname = lname
        self.username = username
        self.password = password
        self.role=role   
        self.__class__._Users.append(self)  
    
    @classmethod
    def getUsersList(cls):
        return "\n".join(list(map(str,cls._Users)))
    def __str__(self) -> str:
        return f"Username = {self.username}/role = {self.role.value}"    
    
def main():
    # User("moha")
    command = argv[1]
    if command == "createuser":
        User(argv[2],argv[3],argv[4],argv[5])
        print("User added successfully")
    elif command == "CreateSuperuser":
        User(argv[2],argv[3],argv[4],argv[5],Role.AdminUser)
        print("User added successfully")
    elif command == "showList":
        print(User.getUsersList())
    elif command == "Backup":
        with open("users.txt","a+") as f:
           f.write(datetime.now())
           f.write("---------------------------------")
           f.write(User.getUsersList())
           
    elif command == "Restore":
          with open(argv[2],"r") as f:      
             print(f.read())
        
if __name__=="__main__":
    main()