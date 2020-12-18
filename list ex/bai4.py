webs = ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]

spam = [i.split(".",-1)[2] for i in webs]
print(spam)
