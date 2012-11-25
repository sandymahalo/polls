import unittest
import mock
from polls.models import *

class SampleTests(unittest.TestCase):

	def test_filters_by_poll(self):
		poll = mock.Mock()
		manager = mock.Mock(spec=PollManager)
		PollManager.get_by_poll(manager, poll)
		manager.filter.assert_called_with(poll=poll)


	# Test the result of one query in the args of another
        @mock.patch('polls.models.PollManager.get_pub_date')
	@mock.patch('polls.models.PollManager.get_question') 
	def test_get_question_and_pub_date(self, get_question, get_pub_date): 
		id = mock.Mock()
		result = Poll.objects.get_poll_question_and_pub_date(id)
		self.assertEqual((get_question.return_value, get_pub_date.return_value), result)
