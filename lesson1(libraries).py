
print("Введите имя, отчество и фамилию")
s = input()
n = s.find(" ")
name = s[:n]
s = s[n+1:]
n = s.find(" ")
name2 = s[:n]
s = s[n+1:]
s = s + " " + name[0] + "." + name2[0] + "."
print(s) 
