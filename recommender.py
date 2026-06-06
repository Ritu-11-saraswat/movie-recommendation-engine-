from movies import MOVIES

def recommend(genre=None, mood=None, industry=None):
    results = []

    for movie in MOVIES:
        score = 0

        if genre and genre in movie["genre"]:
            score += 2
        if mood and mood in movie["mood"]:
            score += 2
        if industry and industry != "Both" and movie["industry"] == industry:
            score += 1
        elif industry == "Both" or not industry:
            score += 0.5

        if score > 0:
            results.append({**movie, "score": score})

    # Sort by score then rating
    results.sort(key=lambda x: (x["score"], x["rating"]), reverse=True)
    return results[:8]
