#lookup_agenda.py

import sys
import import_agenda

valid_columns = ["date", "time_start", "time_end", "title", "location", "description"]

#checks for proper input
if len(sys.argv) == 3:
	column = str(sys.argv[1])
	value = str(sys.argv[2])
elif(len(sys.argv) > 3):
	print("Too many args. If the 'value' is more than one word then put quotes around it.", file=sys.stderr)
	sys.exit(1)
else:
	print("Run program as follows: ./lookup_agenda.py column value", file=sys.stderr)
	sys.exit(1)

#column input check
if(column not in valid_columns):
	print("column must be one of the following: date, time_start, time_end, title, location, description", file=sys.stderr)
	sys.exit(1)

#queries database and prints all the values it finds
selected = import_agenda.database.select(where={ column: value })
for x in selected:
	for a, b in x.items():
		print(b, end=" ")
	print()
print("------------------------------------------------")
print("All results found.")
