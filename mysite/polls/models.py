from django.db import models

class Poll(models.Model):

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


class PollManager(models.Manager):
	def get_by_id(self, id):
		self.filter(id=id)

	def get_by_question(self, question):
		self.filter(question=question)
