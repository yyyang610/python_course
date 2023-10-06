# 定義學生成績列表
grade_list = [
    ['John', 72, 88, 88, 84, 0, 0, 0], 
    ['Eric', 88, 82, 77, 80, 0, 0, 0], 
    ['Rick', 63, 49, 55, 68, 0, 0, 0], 
    ['Mary', 72, 64, 82, 74, 0, 0, 0], 
    ['Alice', 92, 79, 93, 89, 0, 0, 0], 
    ['Match', 81, 72, 62, 70, 0, 0, 0], 
    ['Sunny', 78, 77, 51, 72, 0, 0, 0]
]

# 計算每個學生的總分和平均分數
for student in grade_list:
    total_score = sum(student[1:5])
    average_score = total_score / 4
    student[5] = total_score
    student[6] = average_score

# 根據總分對學生進行排序，然後賦予他們名次
sorted_list = sorted(grade_list, key=lambda x: x[5], reverse=True)
for i, student in enumerate(sorted_list):
    student[7] = i + 1

# 列印更新後的表格
print('姓名\t國文\t英文\t數學\t理化\t總分\t平均\t名次')
print('------------------------------------------------------------')
for student in sorted_list:
    print('\t'.join(map(str, student)))
