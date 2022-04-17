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
from math import floor
from sample import playlist
from heapq import heapify, heappush, heappop


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

    def get_density(self):
        for a in playlist:
            a = a[0]
            if a in self.artists:
                self.density.append(len(self.artists[a])/self.total_track)
            else:
                self.density.append(1/self.total_track)
        return self.density

    def get_correlation(self, track):
        pivot_artist = playlist[track]
        count = sum(1 for i in self.density if i > 0.02)
        step = 1/count
        step_count = 1
        for i, a in enumerate(playlist):
            if pivot_artist == a:
                self.correlation.append(1)
            else:
                diff = self.popularity[track] - self.popularity[i]
                if abs(diff) > 0.15:
                    corr = min(self.popularity[i], self.popularity[track]) / \
                        max(self.popularity[i], self.popularity[track])
                else:
                    corr = self.popularity[i]/self.popularity[track]

                if density[i] > 0.02:
                    corr = corr + step * step_count
                    step_count = step_count + 1
                self.correlation.append(corr)
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


playlist, popularity = mod_playlist(playlist)
g = graph(playlist, popularity)
density = g.get_density()
popularity = g.popularity
corr = g.get_correlation(1)  # input base index

""" TODO: sort corr and keep track of indexs (using heap?)"""
