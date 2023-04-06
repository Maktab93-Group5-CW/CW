from sys import argv


class User:


    list_of_users = []


def init(self, name, l_name, username, password, is_su=False):


self.name = name

self.l_name = l_name

self.username = username

self.password = password

self.is_su = is_su

self.__class__.list_of_users.append(self)


@classmethod
def show_list(cls):


return "\n".join(list(map(str, cls.list_of_users)))


def str(self):


return f"username: {self.username} role: {self.is_su}"


if argv[1] == "createuser":

name = argv[2]

l_name = argv[3]

with open("createuser.txt", "a+") as f:
