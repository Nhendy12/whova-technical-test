#import_agenda.py

import db_table as db
import xlrd
from xlrd import open_workbook
import sys

database = db.db_table("Agenda", { "date": "text" , "time_start": "text" , "time_end": "text" , "title": "text" , "location": "text" , "description": "text"})

if __name__ ==  '__main__':

	#checks for proper input and gets excel file name
	if len(sys.argv) == 2:
		ExcelFileName = str(sys.argv[1])
	else:
		print("Run program as follows: ./import_agenda.py 'filename'.xls", file=sys.stderr)
		sys.exit(1)

	#opens the excel file 
	workbook = xlrd.open_workbook(ExcelFileName)
	worksheet = workbook.sheet_by_index(0)

	#create the table
	#{date, time_start, time_end, title, location, description}
	database = db.db_table("Agenda", { "date": "text" , "time_start": "text" , "time_end": "text" , "title": "text" , "location": "text" , "description": "text"})

	nrows = worksheet.nrows
	ncols = worksheet.ncols
	dates = ''
	start_time = ''
	end_time = ''
	title = ''
	rooms = ''
	description = ''

	#loop through the excel file row by row and put values into our table
	for y in range(13,nrows):
		dates = worksheet.cell_value(y,0)
		start_time = worksheet.cell_value(y,1)
		end_time = worksheet.cell_value(y,2)
		title = worksheet.cell_value(y,3)
		title = title.replace("'", "")
		rooms = worksheet.cell_value(y,4)
		description = worksheet.cell_value(y,5)
		description = description.replace("'", "")
		database.insert({ "date": dates, "time_start": start_time, "time_end": end_time, "title": title, "location": rooms, "description": description })

	print("Agenda successfully imported")