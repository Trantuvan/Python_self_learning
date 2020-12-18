from Regular_expression import isPhoneNumber

msg = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office"

for i in range(len(msg)):
    chunk = msg[i:i+12]

    if isPhoneNumber(chunk):
        print('Phone number found:' + chunk)

print('done')


# import unittest

# class TestRegularExpression(unittest.TestCase):
#     """TestRegularExpression str 444-555-9099 co phai sdt"""

#     def test_sdt(self):
#         sdt = isPhoneNumber('444-555-9099')
#         self.assertEqual(sdt,True)

# unittest.main()

