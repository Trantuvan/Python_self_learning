class Employee(object):

	def __init__(self, name):
		self.name = name

	def emp_info(self):
		return '{}'.format(self.name)

class Manager(Employee):
	# Con 1 cach nua sua loi mutanle trong class
	# khong define list_staff trc trong init
	# chi set self.list_staff = []

	def __init__(self, name, list_staff = None):
		super().__init__(name)
		if list_staff is None:
			self.list_staff = []
		else:
			self.list_staff = list_staff

	def add_staff(self, emp):
		if emp not in self.list_staff:
			self.list_staff.append(emp)

	def remove_staff(self,emp):
		if emp in self.list_staff:
			self.list_staff.remove(emp)

	def mana_info(self):
		# super().emp_info()
		print('List_staff: ')
		for emp in self.list_staff:
			print('-->', emp.emp_info())

emp_1 = Employee('van')
man_1 = Manager('Am')
# man_2 = Manager('Thanh')
print(emp_1.name)
# man_1.add_staff(emp_1)
# print(man_1.mana_info())


