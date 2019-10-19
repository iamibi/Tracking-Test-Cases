# file_reader.py
# Utility methods to perform operations on files


class FileReader:

	def __init__(self, filename):
		""" Initialize the module with filename """
		self.filename = filename

	def update_filename(self, filename):
		""" Updates the filename for re-usability """
		self.filename = filename

	def readfile_from_path(self, path: str) -> str:
		""" Read file from the 'path' """
		pass

	def writefile_to_path(self, path: str) -> bool:
		""" Write file to the given 'path' """
		pass
