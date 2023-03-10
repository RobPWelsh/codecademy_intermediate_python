# Creating Sets and Frozensets
"""
genre_results = ['rap', 'classical', 'rock', 'rock', 'country', 'rap', 'rock', 'latin', 'country', 'k-pop', 'pop', 'rap', 'rock', 'k-pop',  'rap', 'k-pop', 'rock', 'rap', 'latin', 'pop', 'pop', 'classical', 'pop', 'country', 'rock', 'classical', 'country', 'pop', 'rap', 'latin']

survey_genres = set(genre_results)

print(survey_genres)  # Prints {'k-pop', 'latin', 'rap', 'country', 'pop', 'classical', 'rock'}

survey_abbreviated = {genre[0:3] for genre in survey_genres}
print(survey_abbreviated)  # Prints {'rap', 'cla', 'roc', 'pop', 'k-p', 'cou', 'lat'}

top_genres = ['rap', 'rock', 'pop']

frozen_top_genres = frozenset(top_genres)  # Can only create a frozenset using its constructor
print(frozen_top_genres)

# _______________________________________________
# Adding to a Set

song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}

user_tag_1 = 'warm'
user_tag_2 = 'exciting'
user_tag_3 = 'electric'

tag_set = set(song_data['Retro Words'])
tag_set.add(user_tag_1)
tag_set.add(user_tag_2)
tag_set.add(user_tag_3)
print(tag_set)  # Prints {'happy', 'warm', 'electric', 'exciting', 'pop'}

song_data = {'Retro Words': tag_set}
print(song_data)  # Prints {'Retro Words': {'pop', 'happy', 'exciting', 'warm', 'electric'}}

# _______________________________________________
# Removing from a Set
song_data_users = {'Retro Words': ['pop', 'onion', 'warm', 'helloworld', 'happy', 'spam', 'electric']}

tag_set = set(song_data_users['Retro Words'])

tag_set.remove('onion')
tag_set.remove('helloworld')
tag_set.remove('spam')

song_data_users['Retro Words'] = tag_set

print(song_data_users)  # Prints {'Retro Words': {'electric', 'warm', 'happy', 'pop'}}

# _______________________________________________
# Finding elements in a Set
allowed_tags = ['pop', 'hip-hop', 'rap', 'dance', 'electronic', 'latin', 'indie', 'alternative rock', 'classical', 'k-pop', 'country', 'rock', 'metal', 'jazz', 'exciting', 'sad', 'happy', 'upbeat', 'party', 'synth', 'rhythmic', 'emotional', 'relationship', 'warm', 'guitar', 'fiddle', 'romance', 'chill', 'swing']

song_data_users = {'Retro Words': ['pop', 'explosion', 'hammer', 'bomb', 'warm', 'due', 'writer', 'happy', 'horrible', 'electric', 'mushroom', 'shed']}

tag_set = set(song_data_users['Retro Words'])

bad_tags = []
for tag in tag_set:
    if tag not in allowed_tags:
        bad_tags.append(tag)

for tag in bad_tags:
    if tag in tag_set:
        tag_set.remove(tag)

song_data_users['Retro Words'] = tag_set

print(song_data_users)

# _______________________________________________
# Set Union
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth']}

user_tag_data = {'Lowkey Space': ['party', 'synth', 'fast', 'upbeat'],
                 'Retro Words': ['happy', 'electronic', 'fun', 'exciting'],
                 'Wait For Limit': ['romance', 'chill', 'rap', 'rhythmic'],
                 'Stomping Cue': ['country', 'swing', 'party', 'instrumental']}

new_song_data = {}

for key, value in song_data.items():
    song_data_set = set(song_data[key])
    user_tag_set = set(user_tag_data[key])
    new_song_data[key] = song_data_set | user_tag_set
print(new_song_data)  # Prints a dictionary with same keys as two dicts above with combined values (no duplicates)

# _______________________________________________
# Set Intersection
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_recent_songs = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat']}

tags_int = set(user_recent_songs['Retro Words']) & set(user_recent_songs['Lowkey Space'])

print(tags_int)  # Prints {'synth', 'electronic'}

recommended_songs = {}

for key, value in song_data.items():
    if key != 'Retro Words' and key != 'Lowkey Space':
        for tag in tags_int:
            if tag in value:
                recommended_songs[key] = value

print(recommended_songs)  # Prints {'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

# _______________________________________________
# Set Difference
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_liked_song = {'Back To Art': ['pop', 'sad', 'emotional', 'relationship']}
user_disliked_song = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth']}

tag_diff = set(user_liked_song['Back To Art']) - set(user_disliked_song['Retro Words'])

print(tag_diff)  # Prints {'relationship', 'sad', 'emotional'}

recommended_songs = {}

for key, value in song_data.items():
    if key != 'Back To Art' and key != 'Retro Words':
        for tag in tag_diff:
            if tag in value:
                recommended_songs[key] = value

print(
    recommended_songs)  # Prints {'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'], 'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional']}

# _______________________________________________
# Symmetric Difference
user_song_history = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Stomping Cue': ['country', 'fiddle', 'party'],
                     'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

friend_song_history = {'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
                       'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
                       'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
                       'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_tags = set()
friend_tags = set()

for song in user_song_history:
    for tag in user_song_history[song]:
        user_tags.add(tag)

for song in friend_song_history:
    for tag in friend_song_history[song]:
        friend_tags.add(tag)

unique_tags = user_tags ^ friend_tags

print(unique_tags)  # Prints {'party', 'sad', 'happy', 'warm', 'fiddle', 'pop', 'rap', 'intense', 'romance', 'dance', 'moving', 'emotional', 'country', 'upbeat', 'fast'}

"""
# _______________________________________________
# Review
music_tags = {'pop', 'warm', 'happy', 'electronic', 'synth', 'dance', 'upbeat'}

my_tags = frozenset(['pop', 'electronic', 'relaxing', 'slow', 'synth'])

frozen_tag_union = my_tags.union(music_tags)  # Prints frozenset({'slow', 'happy', 'warm', 'relaxing', 'synth', 'pop', 'electronic', 'upbeat', 'dance'})

regular_tag_intersect = music_tags.intersection(my_tags)  # Prints {'pop', 'electronic', 'synth'}

frozen_tag_difference = my_tags.difference(music_tags)  # Prints frozenset({'slow', 'relaxing'})

regular_tag_sd = music_tags.symmetric_difference(my_tags)  # Prints {'slow', 'dance', 'happy', 'upbeat', 'warm', 'relaxing'}

print(frozen_tag_union)
print(regular_tag_intersect)
print(frozen_tag_difference)
print(regular_tag_sd)

