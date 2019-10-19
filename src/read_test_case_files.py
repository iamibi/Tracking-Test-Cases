# read_test_case_files.py

from Utils import file_reader
from Exceptions import InvalidFileName


class ReadTestCaseFiles:

	def get_list_of_files(self, in_directory):
		return []

	def get_list_of_test_case_files(self, in_directory, extra_params=None):
		try:
			file_list = self.get_list_of_files(in_directory)
			test_files = [filename for filename in file_list if ".feature" in filename]
			return test_files
		except InvalidFileName as invalid_file_error:
			print("Error occurred: " + str(invalid_file_error))
