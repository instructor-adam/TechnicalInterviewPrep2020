
import requests

def getMovieTitles(substr):
    base = f"https://jsonmock.hackerrank.com/api/movies/search/?Title={substr}"
    req = requests.get(base).json()
    movie_titles = []
    total_pages = req["total_pages"]
    for page in range(1, total_pages+1):
        url = base + f"&page={page}"
        req = requests.get(url).json()
        data = req["data"]
        for movie in data:
            movie_titles.append(movie["Title"])
    return sorted(movie_titles)
