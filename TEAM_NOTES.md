 # Ultimate Tic-Tac-Toe Model Architecture

## 1. User 1
- **Player Statistics:** Stores stats such as W/L.
- **Marker:** Given an X marker.
- **ID** Username
- **Color** User Collor

## 2. User 2
- **Player Statistics:** Stores stats such as W/L.
- **Marker:** Given an O marker.

## 3. Board
- **Description:** The global game board encompassing the entire match.
- **Structure:** A 3x3 2D array containing 9 **BoardSections**.
- **Data:** `board[3][3]`

## 4. BoardSection
- **Description:** The primary gameplay layer (the "Local" board).
- **Win Condition:** User must align 3 squares in a row to capture the sector.
- **State:** Once a sector is won, it becomes unplayable.
- **Flow Control:** The square index chosen by the current player determines the **BoardSection** index for the next player.
    * *Logic Example:* Choosing the **bottom-right** square forces the opponent to play in the **bottom-right** board section.
- **Structure:** A 3x3 2D array.
- **Data:** `square[3][3]

## 5. Square
- **Hidden_State** True or False if you can see any BoardSection, when other player wins a BoardSection
- **Marker** X or O
- **X** Integer for X-Coordinate
- **Y** Integer for Y-Coordinate

## 6. Marker
- **User** Account associated with Marker in Game
- **Value** 1 or 0 -> X or 0 (respectively) 

## 7. Player Statistics
- **Win/Loss**
- **Joined**
- **Color** User Collor

## 8. GameManager
- **ValidateMove** Checks if a current move is Valid
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