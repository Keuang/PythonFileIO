# s = open('studentnames.txt', 'r')
# print(s.readline().rstrip('\n'))
# print(s.readline().rstrip('\n'))
# print(s.readline().rstrip('\n'))
# print(s.readline().rstrip('\n'))
# print(s.readline().rstrip('\n'))
# print(s.readline().rstrip('\n'))
# s.close()


studentData = open('studentnames.txt','r')
count = 0
for student in studentData:
    name = student.rstrip("\n")
    print(name)
    count += 1
print(count)
studentData.close()



