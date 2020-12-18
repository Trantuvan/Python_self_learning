class Employee(object):
    """Employee info"""
    # bien global raise_amt
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.full_name = self.first + ' ' + self.last

    def give_raise(self):
        # Chu y self. la dung cho ca class
        # bien local raise_amt
        # int() trong truong hop nay tra lai so nguyen
        self.pay = int(self.pay * self.raise_amt)
        return self.pay



emp_1 = Employee('van','tran',4000)
emp_2 = Employee('hoang','hai',3000)
emp_2.raise_amt = 1000
print(emp_1.give_raise())

# import unittest


# class TestEmployee(unittest.TestCase):
#     """Test for class Employee"""

#     def setUp(self):
#         # 1. nhap attribute cho class Employee
#         emp_1 = Employee('van','tran',4000)
#         emp_2 = Employee('thanh','hai',2000)
#         # 2 set custom raise self. la de var co the dung khap noi trong class
#         self.raise_amt = 1000
#         # 3 give_de_raise la bien chua method give_raise
#         self.give_de_raise = emp_1.give_raise
#         # 4 give_cu_raise la bien chua ket qua
#         self.give_cu_raise = emp_2.give_raise(self.raise_amt)

#     def test_default_raise(self):
#         self.assertEqual(self.give_de_raise(),9000)

#     def test_cus_raise(self):
#         self.assertEqual(self.give_cu_raise,3000)

# unittest.main()

