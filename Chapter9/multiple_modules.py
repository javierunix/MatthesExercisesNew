from admin import Admin, Privileges


admin = Admin('manolo', 'caracol', 55, 'lobato', 'driver')
print(admin.describe_user())

privileges = Privileges()
privileges.show_privileges()
