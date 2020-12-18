def isPhoneNumber(text):
    "Nhan dien day so co phai sdt khong"
    "text duoc pass 1 sdt kieu str thi moi iterate duoc"

    if len(text) != 12:
        return False
    for i in range(3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False

    return True

print(isPhoneNumber('415-555-4242'))



