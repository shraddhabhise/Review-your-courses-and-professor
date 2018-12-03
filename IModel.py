from abc import ABCMeta, abstractmethod
# referred from Dominic's solution discussed on slack channel

class IModel:
	__metaclass__ = ABCMeta
	@abstractmethod
	def fetchall(self,data):
		pass


