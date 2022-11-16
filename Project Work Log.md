
## Part 1

pip install dash jupyter-dash

use python file instead of jupyter notebook


challenge:
- Genre: one song may have different genres, not suitable to use color to show

- Features are chosen with a range, instead of exact value, so, popularity can't be predicted directly.

- Use min/max or legally min/max to describe range?

- Not linear-related, it's hard to find relations between features and related popularity



'duration_ms', 'year',
'popularity', 'danceability', 'energy', 'key', 'loudness', 'mode',
'speechiness', 'acousticness', 'instrumentalness', 'liveness',
'valence', 'tempo'


'artist', 'song', 'explicit', 'genre'

Params in left side:

duration_ms: int 113k-484k
year: int 1998-2020
popularity: int 0-100 
danceability: float 0-1
energy: float 0-1
key: int 0-11
loudness: -20.5--0.28
speechiness: 0.02-0.58
acousticness: 0-0.98
instrumentalness: 0-0.98
liveness: 0.02-0.85
valence: 0.04-0.97
tempo: 60-211

genre: contain pop, hiphop, R&B
explicit: True/False
mode: 0/1


### TODO
- paiwise correlation of columns

- Feature Distribution

- Total songs based on genres
- Popular genres based on pouplarity
  
- List of Songs Recorded by Each Singer
- Top 30 Popular Singers
找到与自己曲风相近的歌手


