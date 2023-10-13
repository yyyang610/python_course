grade_list = [['John', 72, 88, 88, 84, 0, 0, 0], 
              ['Eric', 88, 82, 77, 80, 0, 0, 0], 
              ['Rick', 63, 49, 55, 68, 0, 0, 0], 
              ['Mary', 72, 64, 82, 74, 0, 0, 0], 
              ['Alice', 92, 79, 93, 89, 0, 0, 0], 
              ['Match', 81, 72, 62, 70, 0, 0, 0], 
              ['Sunny', 78, 77, 51, 72, 0, 0, 0]]
sorted_data=[]
data=[]
print('姓名\t國文\t英文\t數學\t理化\t總分\t平均\t名次')
print('------------------------------------------------------------')
for i in range(len(grade_list)):
    for j in range(1, len(grade_list[i])-3):
        grade_list[i][5]+=grade_list[i][j]
    grade_list[i][6]+=grade_list[i][5]/4  
    data.append(grade_list[i][6])
    data_sorted=sorted(data)  
for i in range(len(data)):
    for j in range(len(data_sorted)):
        if data[i]==data_sorted[j]:
           grade_list[i][7]=str(len(data)-j)
           
       
for i in range(len(grade_list)):
    print(grade_list[i][0], end='\t')
    for j in range(1, len(grade_list[i])):
        print(grade_list[i][j], end='\t')        
    print()