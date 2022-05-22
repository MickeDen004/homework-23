# getattr() function
class Employee:
    emp_comp='Amazon'
    emp_age=30
    default_age=50

    def defaultMethod(self):
        print("This is a default method")


e = Employee
print(getattr(e, 'emp_age', 45))
print(getattr(e, 'emp_age_other', 45))
print(getattr(e, 'emp_age_other', e.default_age))


e1, e2 = Employee(), Employee()
print(hasattr(e1, 'emp_comp'))
print(hasattr(e1, 'emp_name'))
setattr(e1, "emp_address", "UK")
print(hasattr(e1, "emp_address"))
print(hasattr(e2, 'emp_address'))

print('=' * 35)

delattr(Employee, 'emp_comp')

print(hasattr(e, 'emp_comp'))
print(hasattr(e1, 'emp_comp'))



