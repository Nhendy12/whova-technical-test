# whova-technical-test

Requirements:
  - pip install xlrd
  
import_agenda.py:
  - Takes the specified columns and rows from agenda.xls, creates a local SQLite Database table and stores values into it
  
lookup_agenda.py:
  - Quereies local database based off of input and prints all rows that match

How to run:
  - Run program as follows: python ./import_agenda.py 'filename'.xls
  - Run program as follows: python ./lookup_agenda.py column value
