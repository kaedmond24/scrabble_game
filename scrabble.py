# Create lists for letters and point values
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Map letters to points in a dictionary
letter_to_points = {l:p for l,p in zip(letters,points)}
print(letter_to_points)
print(" ")

# Add consideration for 'blank' tiles
letter_to_points[" "] = 0
print(letter_to_points)
print(" ")

# Create function to calculate word score
def score_word(word):
  point_total = 0
  
  # Iterate through word chaarters and add points to score
  for char in word:
    point_total += letter_to_points.get(char, 0)

  return point_total

# Test score_word function
print(score_word("BROWNIE"))
print(" ")

# Dictionary mapping player to list of words played
player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"],
  "player2": ["EARTH", "EYES", "MACHINE"],
  "player3": ["ERASER", "BELLY", "HUSKY"],
  "player4": ["ZAP", "COMA", "PERIOD"]
}

# Dictionary to map player points
player_to_points = {
  "player1": 0,
  "player2": 0,
  "player3": 0,
  "player4": 0
}

# Loop through each player's word list
# and score the word then update score mapping
for player in player_to_words.keys():
  player_points = 0
  for word in player_to_words[player]:
    player_points += score_word(word)

  player_to_points[player] = player_points
  player_points = 0

# Display game scores
print(player_to_points)

# Function to take in a player and a word, and add that word to the list of words they’ve played
def play_word(player_name, word):
  player_to_word[player_name].append(word)

# def update_point_totals():
#   # Loop through each player's word list
#   # and score the word then update score mapping
#   for player in player_to_words.keys():
#     player_points = 0
#     for word in player_to_words[player]:
#       player_points += score_word(word)

#     player_to_points[player] = player_points
#     player_points = 0

#   # Display game scores
#   print(player_to_points)

