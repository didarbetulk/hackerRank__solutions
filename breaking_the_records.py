def breakingRecords(scores):
    # Initialize the counters for breaking max and min records
    max_breaks = 0
    min_breaks = 0
    
    # Set the initial highest and lowest score to the first game's score
    max_score = min_score = scores[0]
    
    # Iterate through the scores starting from the second game
    for score in scores[1:]:
        # Check if the score breaks the max record
        if score > max_score:
            max_score = score
            max_breaks += 1
        # Check if the score breaks the min record
        elif score < min_score:
            min_score = score
            min_breaks += 1
    
    return [max_breaks, min_breaks]


n = int(input())  # Number of games
scores = list(map(int, input().split()))  # Scores for each game
result = breakingRecords(scores)
print(*result)
