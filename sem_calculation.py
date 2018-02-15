# imports
import csv
from collections import OrderedDict

# define a class object to handle all the calculation
class SemPerformance:
	def __init__(self, csv_file):
		self.csv_file = csv_file

	# helper method for ignoring headers
	def ignore_headers(self, line, headers):
		new_line = {header:line[header] for header in line if header not in headers}
		return new_line

	# helper method to group the data by Search keywords
	def group_by_keywords(self, data):
		keywords = OrderedDict()
		for row in data:
			if not row['Search keyword'] in keywords:
				keywords[row.get('Search keyword')] = [row]
			else:
				keywords[row.get('Search keyword')].append(row)
		return keywords

	# helper method for value greater than or equal to 10
	def greater_than_10(self, csv_writer, value, new_value, i):
		if int(value[i].get('Position')) <= 3:
			price = int(value[1].get('Position')) / float(value[i].get('CTR')) + 0.01
			new_value['Price to pay for Ad'] = price
			new_value['Performance'] = 'Very Good'
			print(
				'Search keyword: ', new_value.get('Search keyword'), ': ', 
				'Company Name: ', new_value.get('Company'), ': ',
				'Performance: ', new_value.get('Performance')
				)
			csv_writer.writerow(new_value)
		elif int(value[i].get('Position')) <= 5:
			price = int(value[1].get('Position')) / float(value[i].get('CTR')) + 0.01
			new_value['Price to pay for Ad'] = price
			new_value['Performance'] = 'Good'
			print(
				'Search keyword: ', new_value.get('Search keyword'), ': ',
				'Company Name: ', new_value.get('Company'), ': ',
				'Performance: ', new_value.get('Performance')
				)
			csv_writer.writerow(new_value)
		else:
			price = int(value[1].get('Position')) / float(value[i].get('CTR')) + 0.01
			new_value['Price to pay for Ad'] = price
			new_value['Performance'] = 'Bad'
			print(
				'Search keyword: ', new_value.get('Search keyword'), ': ',
				'Company Name: ', new_value.get('Company'), ': ',
				'Performance: ', new_value.get('Performance')
				)
			csv_writer.writerow(new_value)

	# helper method for value less than 10
	def less_than_10(self, csv_writer, value, new_value, i):
		if int(value[i].get('Position')) <= 2:
			price = int(value[1].get('Position')) / float(value[i].get('CTR')) + 0.01
			new_value['Price to pay for Ad'] = price
			new_value['Performance'] = 'Very Good'
			print(
				'Search keyword: ', new_value.get('Search keyword'), ': ',
				'Company Name: ', new_value.get('Company'), ': ',
				'Performance: ', new_value.get('Performance')
				)
			csv_writer.writerow(new_value)
		elif int(value[i].get('Position')) <= 4:
			price = int(value[1].get('Position')) / float(value[i].get('CTR')) + 0.01
			new_value['Price to pay for Ad'] = price
			new_value['Performance'] = 'Good'
			print(
				'Search keyword: ', new_value.get('Search keyword'), ': ',
				'Company Name: ', new_value.get('Company'), ': ',
				'Performance: ', new_value.get('Performance')
				)
			csv_writer.writerow(new_value)
		else:
			price = int(value[1].get('Position')) / float(value[i].get('CTR')) + 0.01
			new_value['Price to pay for Ad'] = price
			new_value['Performance'] = 'Bad'
			print(
				'Search keyword: ', new_value.get('Search keyword'), ': ',
				'Company Name: ', new_value.get('Company'), ': ',
				'Performance: ', new_value.get('Performance')
				)
			csv_writer.writerow(new_value)

    # method to write the performance result to a new file
	def write_result(self):
		# let the user know the program is generating a file
		print('Generating results to a file "performance_results.csv"........')
		# get the data as OrderedDict
		data = csv.DictReader(self.csv_file)

		with open('performance_results.csv', 'w') as result_file:
			headers = [
			    'Search keyword', 'Company',
			    'Price to pay for Ad', 'Performance'
			]
			csv_writer = csv.DictWriter(result_file, headers)
			csv_writer.writeheader()
			# loop through the keywords OrderedDict
			for _, value in self.group_by_keywords(data).items():
				i = 0
				while i < len(value):
					new_value = self.ignore_headers(
						value[i],
						['Impressions', 'CTR', 'Position', 'Cost', 'Revenue'])
					if len(value) >= 10:
						self.greater_than_10(csv_writer, value, new_value, i)
					else:
						self.less_than_10(csv_writer, value, new_value, i)
					i += 1


if __name__ == '__main__':
	with open('take_home_test_data.csv', 'r') as csv_file:
		performance = SemPerformance(csv_file)
		performance.write_result()