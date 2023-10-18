import sys


grade_list = [['John', 72, 88, 88, 84, 0, 0, 0],
              ['Eric', 88, 82, 77, 80, 0, 0, 0],
              ['Rick', 63, 49, 55, 68, 0, 0, 0],
              ['Mary', 72, 64, 82, 74, 0, 0, 0],
              ['Alice', 92, 79, 93, 89, 0, 0, 0],
              ['Match', 81, 72, 62, 70, 0, 0, 0],
              ['Sunny', 78, 77, 51, 72, 0, 0, 0]]


print('姓名\t國文\t英文\t數學\t理化\t總分\t平均\t名次')
print('------------------------------------------------------------')

rankList = []

for i in range(7):
    for j in range(1,5):
        grade_list[i][5] += grade_list[i][j]
    rankList.append(grade_list[i][5])
    grade_list[i][6] = grade_list[i][5] / 4

rankList.sort()
for i in range(7):
    grade_list[i][7] = rankList.index(grade_list[i][5]) + 1

for i in range(7):
    for j in range(8):
        print(grade_list[i][j], end='\t')
    print()