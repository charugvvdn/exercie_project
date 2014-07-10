import csv
import unittest
import os
class CSVReader():
	def __init__(self,filename):
		cwd = os.path.dirname(__file__)	# to fetch the current working directory
		fileobj =os.path.join(cwd, filename)	# creating a file object that need to be opened 
		self.csvreader = csv.reader(open(fileobj))	# opening the file object using csv.reader
		self.headers = self.csvreader.next()[2:]	 #getting the header info from the csv file
		self.company = {}
	
	def getheader(self):
		count = 0
		""" creating a dictionary for unique company names with initial year, month, price and a counter to 
		 show which column does its value belong to """
		for title in self.headers:
			count += 1
			if title not in self.company:
				self.company[title]={"year":'',"month":'',"price":0,"comp_count":count}
	
	def max_price(self):
		# reading the csv file per row 
		try:
			self.getheader()
			for row in self.csvreader:
				# find the maximum share proice value for respective company saved in dictionary
				for title in self.company:
					# check if the corresponding column contains a data and data is > 0 
					if row[self.company[title]['comp_count']+1].isdigit() and  int(row[self.company[title]['comp_count']+1]) > 0:
						if self.company[title]["price"] < int(row[self.company[title]['comp_count']+1]) :
							self.company[title]["price"] = int(row[self.company[title]['comp_count']+1])
							self.company[title]["year"] = row[0]
							self.company[title]["month"]= row[1]
			# deleting the non required key value pair of count
			for c in self.company:
				del(self.company[c]['comp_count'])
			return self.company
		except Exception as error:
			print error 
			return False

class CSVTest(unittest.TestCase):
	# test case to verify the expected output of the given csv file
	def testcsv(self):
		filename = "test_shares_data.csv"
		csvread = CSVReader(filename)
		result = csvread.max_price()
		expected = {'Company-E': {'price': 997, 'month': 'Oct', 'year': '2008'}, 'Company-D': {'price': 999, 'month': 'Apr', 'year': '2002'}, 'Company-C': {'price': 995, 'month': 'Jun', 'year': '1993'}, 'Company-B': {'price': 986, 'month': 'Mar', 'year': '2007'}, 'Company-A': {'price': 1000, 'month': 'Mar', 'year': '2000'}}
		assert result ==  expected

if __name__ == "__main__":
        unittest.main()

	

	
	