import unittest
import mock
from polls.models import *

class SampleTests(unittest.TestCase):

	def test_filters_by_poll(self):
		poll = mock.Mock()
		manager = mock.Mock(spec=PollManager)
		PollManager.get_by_poll(manager, poll)
		manager.filter.assert_called_with(poll=poll)

