from django.db import models

class PollManager(models.Manager):

        def get_by_poll(self, poll):
                self.filter(poll=poll)

        def get_question(self, id):
		poll = self.filter(id=id)
		return poll.question
        def get_pub_date(self, id):
		poll = self.filter(id=id)
		return poll.pub_date
        def get_poll_question_and_pub_date(self, id):
                return self.get_question(), self.get_pub_date()

class Poll(models.Model):

    objects = PollManager()

    def __unicode__(self):
            return self.question

    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):

    def __unicode__(self):
            return self.choice_text

    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()

