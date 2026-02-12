 # Ultimate Tic-Tac-Toe Model Architecture

## 1. User
 - **Player Statistics**  Stores status such as W/L
 - **Marker** Given X or O
  
## 3. Board
- **Description:** The global game board encompassing the entire match.
- **Structure:** A list containing 9 **BoardSections**.

## 4. BoardSection
- **Description:** The primary gameplay layer (the "Local" board).
- **Win Condition:** User must align 3 squares in a row to capture the sector.
- **State:** Once a sector is won, it becomes unplayable.
- **Flow Control:** The square index chosen by the current player determines the **BoardSection** index for the next player.
    * *Logic Example:* Choosing the **bottom-right** square forces the opponent to play in the **bottom-right** board section.
- **Structure:** A 3x3 2D array.
- **Data:** Integer Board Section (2) for top right BoardSection

## 5. Square
- **Hidden_State** True or False if you can see any BoardSection, when other player wins a BoardSection
- **Marker** X or O
- **Data** Integer for Square number (05) for top left BoardSection 5th square

## 6. Marker
- **User** Account associated with Marker in Game
- **Value** 1 or 0 -> X or 0 (respectively) 

## 7. Player Statistics
- **Win/Loss**
- **Joined**
- **Color** User Collor

## 8. Game
- **Winner** UserID 
- **GameState** State of the game
- **Board** The Board
- **User1** Player 1 
- **User2** Player 2

https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Models/local_library_model_uml.svg
 
from django.db import models
from django.urls import reverse

class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    # …

    # Metadata
    class Meta:
        ordering = ['-my_field_name']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name

if you like piña coladas, and getting caught in the rain
⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣤⣶⣶⣦⣄⠙⣿⣿⣿⣇⣠⣶⣾⣿⣷⣶⣶⠄⠀⠀⠀⠀⠀
⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣷⣼⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⠛⠉⠉⠉⠁⠉⠉⠛⢿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣤⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠿⠛⢿⣿⣿⣿⣿⣟⠛⠻⢿⣷⣦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⠁⠀⠀ ⢸⣿⣿⡿⠻⣿⣷⡀ ⠀⠉⠻⢷⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⠁⠀⠀ ⠀⠸⣿⡿⠁⠀ ⠈⢿⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠁⠀⠀⠀ ⠀⠀⠉⠀⠀⠀⠀ ⠀⠀⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠛⠉