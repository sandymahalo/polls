import unittest
import mock
from polls.models import *

class SampleTests(unittest.TestCase):

	def test_filters_by_id(self):
		id = mock.Mock()
		manager = mock.Mock(spec=PollManager)
		PollManager.get_by_id(manager, id)
		manager.filter.assert_called_with(id=id)

	def test_filters_by_question(self):
		question = mock.Mock()
		manager = mock.Mock(spec=PollManager)
		PollManager.get_by_question(manager, question)
		manager.filter.assert_called_with(question=question)

