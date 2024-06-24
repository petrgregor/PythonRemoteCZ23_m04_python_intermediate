"""
Implement an object-oriented mechanism for handling user access.
Create a User class that will keep the current accesses and history of changes.
Take care of proper encapsulation of data and provide methods:

- grant_permission
- revoke_permission
- get_first_permissions_change
- get_permissions_change_history

In addition, allow to assign access lists to a user. Use enum to define access.
"""
import datetime
from enum import Enum, auto


class Permission(Enum):
    READ = auto()
    WRITE = auto()


class Sex(Enum):
    MAN = auto()
    WOMAN = auto()
    NONBINARY = auto()


class User:
    def __init__(self, name, sex=Sex.MAN):
        self.name = name
        self.sex = sex
        self.__permissions = set()
        self.__permissions_history = []

    @property
    def permissions(self):
        return self.__permissions

    @permissions.setter
    def permissions(self, permissions):
        for permission in permissions:
            self.grant_permission(permission)

    def __str__(self):
        return f"{self.name}"

    def grant_permission(self, permission):
        self.__permissions.add(permission)
        self.__permissions_history.append(f"{datetime.datetime.now()}: Grant permission '{permission}'")

    def revoke_permission(self, permission):
        self.__permissions.remove(permission)
        self.__permissions_history.append(f"{datetime.datetime.now()}: Revoke permission '{permission}'")

    def get_first_permissions_change(self):
        if len(self.__permissions_history):
            return self.__permissions_history[0]
        return None

    def get_permissions_change_history(self):
        return self.__permissions_history

    def print_permissions_info(self):
        print(f"{self} has permissions:")
        if self.permissions:
            for permission in self.permissions:
                print(f"\t{permission}")
        else:
            print("\tNone")
        print(f"{self} has permissions change history:")
        for permission in self.__permissions_history:
            print(f"\t{permission}")
        print(f"{self} has first permissions change:\n\t{self.get_first_permissions_change()}")


if __name__ == "__main__":
    user1 = User("Petr")

    user1.print_permissions_info()

    print('-' * 80)
    user1.grant_permission(Permission.READ)
    user1.print_permissions_info()

    print('-' * 80)
    user1.grant_permission(Permission.READ)
    user1.print_permissions_info()

    print('-' * 80)
    user1.grant_permission(Permission.WRITE)
    user1.print_permissions_info()

    print('-' * 80)
    user1.revoke_permission(Permission.READ)
    user1.print_permissions_info()

    print('-' * 80)
    user1.revoke_permission(Permission.WRITE)
    user1.print_permissions_info()

    print('-'*80)
    user1.permissions = {Permission.READ, Permission.WRITE}
    user1.print_permissions_info()
