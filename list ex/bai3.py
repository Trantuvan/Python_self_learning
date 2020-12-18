scores =  [86,86,85,85,87,85,83,23,45,84,93,86,87]

scores.sort()
frist = max(scores)

temp = [k for k in scores if k != frist]
second = temp[-1]

temp = [k for k in scores if k != frist and k != second]
third = temp[-1]

print(second)
print(third)







   




    


   

