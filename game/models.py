from django.db import models

#
from django.db import models
from django.urls import reverse
### 1. User (Nicholas) 
# **Player Statistics**  Stores status such as W/L 
# **Marker** Given X or O 
class User(models.Model):

    """A typical class defining a model, derived from the Model class."""

    # Fields
    username = models.CharField(max_length=200)
    statistics = models.ForeignKey(PlayerStatistics, on_delete=models.SET_NULL, null=True)
    marker = models.ForeignKey(Marker, on_delete=models.SET_NULL, null=True)

    # Metadata
    class Meta:
        ordering = ['username']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of User."""
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the User object (in Admin site etc.)."""
        return self.username

### 6. User Statistics (Nicholas)
# - **Win/Loss**
# - **Games** number of games played
# - **Color** User Collor
class UserStatistics(models.Model):

    # Fields
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    win = models.IntegerField(default=0)
    loss = models.IntegerField(default=0)
    games = models.IntegerField(default=0)
    user_color = models.CharField(max_length=20, default='Purple')

    # Metadata
    class Meta:
        ordering = ['user']

    # Methods

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of UserStatistics."""
        return reverse('userstatistics-detail', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the UserStatistics object (in Admin site etc.)."""
        return f"{self.user.username}: {self.win} - {self.loss} - {self.user_color}"
    