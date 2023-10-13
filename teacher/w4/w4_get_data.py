import gspread

gc = gspread.service_account(filename='python_course_access_cred.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1nqgiOHVyuIM1p4cBKUsi1HfmkaIhjIQdQYamGbkzOhE/edit#gid=0')

print(sh.sheet1.get('A1:b15'))

