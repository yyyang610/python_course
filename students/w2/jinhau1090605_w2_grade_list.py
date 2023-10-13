grade_list = [['John', 72, 88, 88, 84, 0, 0, 0], 
              ['Eric', 88, 82, 77, 80, 0, 0, 0], 
              ['Rick', 63, 49, 55, 68, 0, 0, 0], 
              ['Mary', 72, 64, 82, 74, 0, 0, 0], 
              ['Alice', 92, 79, 93, 89, 0, 0, 0], 
              ['Match', 81, 72, 62, 70, 0, 0, 0], 
              ['Sunny', 78, 77, 51, 72, 0, 0, 0]]

print('姓名\t\t國文\t英文\t數學\t理化\t總分\t平均\t\t名次')
print('------------------------------------------------------------')

for i in range(0,7):
    grade_list[i][5] = grade_list[i][1] + grade_list[i][2] + grade_list[i][3] + grade_list[i][4]
    grade_list[i][6] = (grade_list[i][1] + grade_list[i][2] + grade_list[i][3] + grade_list[i][4])/4

data = [(1,grade_list[0][5] ), (2,grade_list[1][5]), (3,grade_list[2][5]), (4,grade_list[3][5]), (5,grade_list[4][5]), (6,grade_list[5][5]), (7,grade_list[6][5])]
sorted_data = sorted(data, key=lambda x: x[1])

x=sorted_data[0][0]
grade_list[x-1][7]=7
for i in range(0,7):
    x = sorted_data[i][0]
    grade_list[x - 1][7] = 7-i




for i in range(len(grade_list)):
    print(grade_list[i][0], end='\t')
    for j in range(1, len(grade_list[i])):
        print(grade_list[i][j], end='\t')
    print()



