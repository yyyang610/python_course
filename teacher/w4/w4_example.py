#pip install gspread oauth2client
import gspread

gc = gspread.service_account(filename='python_course_access_cred.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1nqgiOHVyuIM1p4cBKUsi1HfmkaIhjIQdQYamGbkzOhE/edit#gid=0')

cell_range_pattern='c5:j12'
cell_range=sh.sheet1.get(cell_range_pattern)

print(cell_range)
print(type(cell_range))    

grade_list_data=list(cell_range)
print(type(grade_list_data))
