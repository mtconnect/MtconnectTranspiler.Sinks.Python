from enum import Enum

class MTCEnum(Enum):
	def __str__(self):
		"""Return the string representation of the MTCEnum."""
		return f"{self.name}: {self.value}"