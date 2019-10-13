# custom_errors.py
# Custom exceptions that may be raised


class TrackingTestCaseError(Exception):
	# Base class for other exceptions
	def __init__(self, error_message):
		Exception.__init__(self, error_message)
		self.error_message = error_message


class ValueTooSmall(TrackingTestCaseError):
	ERROR_MESSAGE = "The value is too small."

	# When the value Input is small
	def __init__(self):
		super(self.ERROR_MESSAGE)


class ValueTooLarge(TrackingTestCaseError):
	ERROR_MESSAGE = "The value is too large."

	# When the value is too large
	def __init__(self):
		super(self.ERROR_MESSAGE)


class InvalidFileName(TrackingTestCaseError):
	ERROR_MESSAGE = "The filename is Invalid. Please check the filename."

	# When the file name is invalid or the file is not available.
	def __init__(self):
		super(self.ERROR_MESSAGE)
