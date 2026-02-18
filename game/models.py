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

### 2. Board (Tristan)
    # Fields
    # Determines which BoardSection (0–8) the next player must play in.
    # If null, the player may choose any available section.
    active_section = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        help_text="0-8 index of the active BoardSection"
    )

    # Stores which Marker (X or O) won the entire board.
    winner_marker = models.ForeignKey(
        'Marker',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    # Metadata
    class Meta:
        ordering = ['id']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of Board."""
        return reverse('board-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Board object."""
        if self.winner_marker:
            return f"Board {self.id} (Winner: {self.winner_marker})"
        return f"Board {self.id} (In Progress)"

### 3. BoardSection (Maci) 
# The primary gameplay layer (the "Local" board).
class BoardSection(models.Model):
        # ForeignKey linking this BoardSection to its parent Board.
        # If the Board is deleted, all its sections are deleted as well.
    board = models.ForeignKey('Board', on_delete=models.CASCADE, related_name="sections")
    position = models.PositiveSmallIntegerField(help_text="0-8 index of this section on the global board") # Position of this section within the global board (0–8).
        # Stores which Marker (X or O) won this section. If null, the section has not been won yet.
        # SET_NULL keeps the section if a Marker is deleted.
    winner_marker = models.ForeignKey('Marker', on_delete=models.SET_NULL, null=True,related_name="won_sections")
    
    class Meta:
        ordering = ["board", "position"]
        constraints = [models.UniqueConstraint(fields=["board", "position"], name="unique_section_per_board_position"),]  # Ensures you cannot have two sections with the same position on one board
    def get_absolute_url(self):
        return reverse('boardsection-detail', args=[str(self.id)])
    def __str__(self):
        return f"BoardSection(board_id={self.board_id}, pos={self.position}, winner={self.winner_marker})"


## 4. Square (Maci)
class Square(models.Model):
    section = models.ForeignKey('BoardSection', on_delete=models.CASCADE, related_name="squares")  # Links square to its parent BoardSection. If the section is deleted, its squares are deleted.
    position = models.PositiveSmallIntegerField(help_text="0-8 index of this section on the global board") # Position of this section within the global board (0–8).
    marker = models.ForeignKey('Marker', on_delete=models.SET_NULL, null=True, related_name="marked_squares")
    hidden_state = models.BooleanField(default=False)  # True if this square should be hidden/unplayable.
    
    class Meta:
        ordering = ["section", "position"] 
        constraints = [models.UniqueConstraint(fields=["section", "position"], name="unique_square_per_section_position"),] # Prevents duplicate square positions within same section
    def get_absolute_url(self):
        return reverse("square-detail", args=[str(self.id)])
    def __str__(self):
        return f"Square(section_id={self.section_id}, pos={self.position}, marker={self.marker}, hidden={self.hidden_state})"

### 5. Marker (Tristan) 
class Marker(models.Model):

    # Fields
    user = models.ForeignKey(
        'User',
        on_delete=models.SET_NULL,
        null=True
    )

    # 1 = X, 0 = O
    value = models.IntegerField(
        choices=((0, 'O'), (1, 'X'))
    )

    # Metadata
    class Meta:
        ordering = ['value']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of Marker."""
        return reverse('marker-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Marker object."""
        return 'X' if self.value == 1 else 'O'

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
    

# 7. Game (Jacob)
class game(models.Model):

    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    gameState = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    board = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    user1 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    user2 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def get_absolute_url(self):
        """Returns the URL to access a particular instance of game."""
        return reverse('game-detail', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the game object (in Admin site etc.)."""
        return f"{self.user1.username} vs {self.user2.username} -> winner: {self.winner.username}"
    
