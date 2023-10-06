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


#學生成績列表
grade_list = [['John', 72, 88, 88, 84, 0, 0, 7], 
              ['Eric', 88, 82, 77, 80, 0, 0, 0], 
              ['Rick', 63, 49, 55, 68, 0, 0, 0], 
              ['Mary', 72, 64, 82, 74, 0, 0, 0], 
              ['Alice', 92, 79, 93, 89, 0, 0, 0], 
              ['Match', 81, 72, 62, 70, 0, 0, 0], 
              ['Sunny', 78, 77, 51, 72, 0, 0, 0]]

#所有變數
height=len(grade_list) #7
weight=len(grade_list[1]) #8
sum=0
aver=0
sort=0
max=0
count=height
test=0

  
#計算總合和平均
for i in range(height):    
    for j in range(1, weight-3):
        sum=sum+grade_list[i][j]
        aver=sum/4
    grade_list[i][5]=sum
    grade_list[i][6]=aver
    sum=0
    aver=0

#計算排名    
for i in range(height):     
    for n in range(height):
        if grade_list[i][5]<grade_list[n][5]:
            count=count-1
        grade_list[i][7]=count
    count=height

#列印所有資訊
print('姓名\t國文\t英文\t數學\t理化\t總分\t平均\t名次')
print('------------------------------------------------------------')     
for i in range(height):    
    for j in range(weight):
        print(grade_list[i][j], end='\t')
    print()
