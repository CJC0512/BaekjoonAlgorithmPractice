from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_total = defaultdict(int)
    songs = defaultdict(list)
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        genre_total[genre] += play
        songs[genre].append((play, i))
        
    sorted_genres = sorted(genre_total.keys(), key=lambda x: genre_total[x], reverse = True)
    
    for genre in sorted_genres:
        sorted_songs = sorted(songs[genre], key=lambda x: (-x[0], x[1]))
        answer.extend([song[1] for song in sorted_songs[:2]])
    
    return answer