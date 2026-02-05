# Ultimate Tic-Tac-Toe Model Architecture

## 1. User
* **Account Tracking:** Stores Win / Loss records.
* **Marker Assignment:** Each user is assigned a specific **Marker**.

## 2. Marker
* **Value:** Represents either **X** or **O**.

## 3. Board
* **Description:** The global game board encompassing the entire match.
* **Structure:** A 3x3 2D array containing 9 **BoardSections**.
* **Data:** `board[3][3]`

## 4. BoardSection
* **Description:** The primary gameplay layer (the "Local" board).
* **Win Condition:** User must align 3 squares in a row to capture the sector.
* **State:** Once a sector is won, it becomes unplayable.
* **Flow Control:** The square index chosen by the current player determines the **BoardSection** index for the next player.
    * *Logic Example:* Choosing the **bottom-right** square forces the opponent to play in the **bottom-right** board section.
* **Structure:** A 3x3 2D array.
* **Data:** `square[3][3]