"""
---PLAN---

>   calculate value given: artist density of the song, popularity && correlation 
    with the song at pivot position

>   track-artist data in a graph to determine artist density + correlation

>   quicksort: the highest value are the ones with higher correlation

*** In case with many data points, keep the sample data to a 

"""

# FUNCTION: create graph (x: artists, y: tracks)
# NOTE: tracks are referred to by IDs (their index)

# CLASS: Track Criteria
# FUNCTION: artist density calculatiion
# FUNCTION: get popularity (EASY -> just extract from track list)
# FUNCTION: correlation to startings point (same artist?, popularity?)
# This is the function that will indicate how we sort things out

# FUNCTION: random seed

# MIN_HEAP:
# generate list of tracks(ID) to be played

# NOTE: No modifications to array, only refer to index to avoid any resizing, reallocation

import random as rand
from random import randrange, sample
from sample import playlist
from heap import *
import numpy as np


""" GRAPH """

# playlist only contains list of artists


class graph:
    playlist = []
    artists = {}
    density = []
    popularity = []
    correlation = []
    total_track = 0

    def __init__(self, playlist=None, popularity=None):
        if playlist == None:
            pass
        else:
            self.popularity = popularity
            self.total_track = len(playlist)
            self.playlist = playlist
            for i, artist in enumerate(playlist):
                found = False
                for a in artist:
                    if a in self.artists:
                        self.artists[a].append(i)
                        found = True
                    break
                if not found:
                    self.artists.setdefault(artist[0], [])
                    self.artists[artist[0]].append(i)

    # density = artist_appeared/total_tracks
    def get_density(self):
        for a in playlist:
            a = a[0]
            if a in self.artists:
                self.density.append(len(self.artists[a])/self.total_track)
            else:
                self.density.append(1/self.total_track)
        return self.density

    # calculate from seed track
   def get_correlation(self, track):
        pivot_artist = playlist[track]
        # count tracks with significant density
        self.get_density()
        density_condition = np.quantile(self.density, 0.75)
        count = sum(1 for i in self.density if i > density_condition)
        step = 1/count
        step_count = 1
        for i, a in enumerate(playlist):
            if pivot_artist == a:
                corr = 1
            else:
                # calculate correlation for track with significant popularity difference
                diff = self.popularity[track] - self.popularity[i]
                diff = abs(diff)
                corr = (diff/self.popularity[track])

                if self.density[i] > 0.02:
                    corr = corr + step * step_count
                    step_count = step_count + 1
            self.correlation.append([corr, i])
        return self.correlation


""" SHUFFLE FUNCTIONS """

# Fisher-Yates


def fisher_yates(bucket):
    size = len(bucket)
    for x in range(0, size - 1):    # range [x, y)
        j = rand.randint(x, size - 1)    # randint [x, y]
        bucket[x], bucket[j] = bucket[j], bucket[x]


""" HELPER FUNCTIONS """

# Modify Playlist


def mod_playlist(playlist):
    mod_playlist = []
    popularity = []
    for track in playlist:
        track.pop('name')
        track.pop('image_url')
        track.pop('preview_url')
        popularity.append(track['popularity']/100)
        track.pop('popularity')
        mod_playlist.append(track['artists'])
    return mod_playlist, popularity


# Example:

"""
HOW-TO

1. get 'playlist' and 'popularity' from mod_playlist(input)
2. create an array of int, shuffle using fisher_yates() to generate random seed
3. create a graph using (inputs are playlist & popularity)
4. use get_correlation with the input of seed
5. create min heap with the size of the playlist
6. insert score array in min heap

"""


playlist, popularity = mod_playlist(playlist)

seed = list(range(0, 100))
fisher_yates(seed)
print(seed)
g = graph(playlist, popularity)
corr = g.get_correlation(seed[4])  # input base index

# Min_heap uses
heap = Min_Heap(g.total_track)

for item in corr:
    heap.insert(item)

shuffled = []
data = []
for j in range(g.total_track):
    tmp, index = heap.pop()  # return score, index
    shuffled.append(index)
    data.append(tmp)
print(shuffled[3])  # shuffled index
