from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Petition(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="petitions")
    created_at = models.DateTimeField(auto_now_add=True)

    def yes_votes(self):
        return self.votes.filter(vote_type="yes").count()

class Vote(models.Model):
    VOTE_CHOICES = [("yes", "Yes")]
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE, related_name="votes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=10, choices=VOTE_CHOICES)

    class Meta:
        unique_together = ("petition", "user")