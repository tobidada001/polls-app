from django.db import models

# Create your models here.
class PollTitle(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class PollChoice(models.Model):
    
    choice_polltitle = models.ForeignKey(PollTitle, on_delete=models.CASCADE, related_name = 'relatedchoice')
    choice = models.CharField(max_length=50, default = 'First option')

    number_of_selection = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice


