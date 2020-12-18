gadgets = ['Mobile','Laptop', 100, 'Camera', 310.28, 'Speakers', 27.00,
'Television', 1000, 'Laptop Case', 'Camera Lens']

# numbers = [i for i in gadgets if isinstance(i,(int,float))]
# strings = [a for a in gadgets if isinstance(a,str)]

numbers = [i for i in gadgets if isinstance(i,(int,float)) == True]
strings = [i for i in gadgets if isinstance(i,str) == True]

print(numbers)
print(strings)

# and not isinstance(x,bool) cho truong hop co True or False in list, boolean la sub class cua int
# neu chi su dung isinstance(x,int) no se in luon True or False
# [x for x in testList if (isinstance(x, int) and not isinstance(x, bool))]

strings.sort(reverse = True)
numbers.sort()
print(numbers)
print(strings)
#Muon tao 1 copy cho string voi number roi sort gan copy cho 1 bien ma in ra none ??