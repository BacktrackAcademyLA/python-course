from wifi import Cell
import os 
import time

print("R E D E S   D I S P O N I B L E S \n"
	+"-------------------------------------")
for x in xrange(1,5):
	cell = Cell.all('mon0')
	time.sleep(2)
	os.system('clear')
	print(cell)	