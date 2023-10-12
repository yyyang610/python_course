import sys;   


"""
姓名	國文	英文	數學	理化	總分	平均	名次
John	72	    88	    88	    84			
Eric	88	    82	    77	    80			
Rick	63	    49	    55	    68			
Mary	72	    64	    82	    74			
Alice	92	    79	    93	    89			
Match	81	    72	    62	    70			
Sunny	78	    77	    51	    72			
"""

grade_list = [['John', 72, 88, 88, 84, 0, 0, 0], 
              ['Eric', 88, 82, 77, 80, 0, 0, 0], 
              ['Rick', 63, 49, 55, 68, 0, 0, 0], 
              ['Mary', 72, 64, 82, 74, 0, 0, 0], 
              ['Alice', 92, 79, 93, 89, 0, 0, 0], 
              ['Match', 81, 72, 62, 70, 0, 0, 0], 
              ['Sunny', 78, 77, 51, 72, 0, 0, 0]]


print('姓名\t國文\t英文\t數學\t理化\t總分\t平均\t名次')
print('------------------------------------------------------------')


# 計算總分、平均分並排序
for student in grade_list:
    student[5] = sum(student[1:5]) #計算總分並將總分存到5的列表中，也就是第6列(總分)的位置
    student[6] = student[5]/4 #計算平均，將原本存到表格(總分)位置的值拿出來除4，再存到表格(平均)的位置

sorted_grade_list = sorted(grade_list, key=lambda x: x[5], reverse=True) #將學生總分(x[5])進行排序，把成績較高的學生排在前面

# 設定名次
for i, student in enumerate(sorted_grade_list):
    student[7] = i + 1 #將排好的名次存到7，也就是表格第8列(名次)的位置，因為通常名次是1開始，故i+1才會是1開始


# 列印學生成績和名次
for student in sorted_grade_list:
    print('\t'.join(map(str, student))) 


