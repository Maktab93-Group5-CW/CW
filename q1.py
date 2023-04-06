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
        return f"Username = {self.username}/role = {self.role.name}"   
    
    def save(self):
        filename = "user.txt" if self.role==Role.OrdinaryUser else "superuser.txt"
        with open(filename,"a") as f:
            f.write(str(self)+"\n")
             
    
def main():
    # User("moha")
    command = argv[1]
    if command == "createuser":
        user = User(argv[2],argv[3],argv[4],argv[5])
        user.save()
        print("User added successfully")
        
        
        
    elif command == "Createsuperuser":
        user = User(argv[2],argv[3],argv[4],argv[5],Role.AdminUser)
        user.save()
        print("User added successfully")
    elif command == "showList":
        print(User.getUsersList())
    elif command == "Backup":
        with open("user.txt","r") as f:
            content1 = f.read()
        with open("superuser.txt","r") as f:
            content2 = f.read()
        with open("user-backup.txt","w") as f:
           f.write(str(datetime.now()))
           f.write("\n---------------------------------\n")
           f.write(content1)
        with open("superuser-backup.txt","w") as f:
           f.write(str(datetime.now()))
           f.write("\n---------------------------------\n")
           f.write(content2)
           
    elif command == "Restore":
          with open(argv[2],"r") as f:      
             print(f.read())
        
if __name__=="__main__":
    main()