from rolepermissions.roles import AbstractUserRole

class Admin(AbstractUserRole):
    available_permissions = {
        'admin': True,
    }

class HrAdmin(AbstractUserRole):
    available_permissions = {
        'hr_user': True,
    }


class User(AbstractUserRole):
    available_permissions = {
        'user': True,
    }    