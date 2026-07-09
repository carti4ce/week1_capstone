"""
Load and add items to the database, db.pkl
"""

import pickle

def load() -> dict:
    try:
        with open("db.pkl", mode = "rb") as opened_file:
            return pickle.load(opened_file)
    except EOFError:
        a = {}
        return a

def loadSongs() -> dict:
    try:
        with open("songs.pkl", mode = "rb") as opened_file:
            return pickle.load(opened_file)
    except EOFError:
        a = {}
        return a

def export(d: dict):   
    with open("db.pkl",mode="wb") as opened_file:
        pickle.dump(d,opened_file)

def exportSongs(d: dict):   
    with open("songs.pkl",mode="wb") as opened_file:
        pickle.dump(d,opened_file)

def add(fanout: list[tuple[tuple[float,float,float],float]], song_ID: str, song_name: str):
    d = load()
    for pair in fanout:
        if pair[0] not in d:
            d[pair[0]] = []
        d[pair[0]].append((song_ID, pair[1]))
    export(d)

    songs = loadSongs()
    songs[song_ID] = song_name
    exportSongs(songs)
    

def remove(songID: str):
    d = load()
    for key in d:
        d[key] = [pair for pair in d[key] if pair[0] != songID]
    export(d)

    songs = loadSongs()
    songs.pop(songID,None)
    exportSongs(songs)


def view():
    print(load())

def viewSongs():
    print(loadSongs())

def reset():
    a = {}
    export(a)

