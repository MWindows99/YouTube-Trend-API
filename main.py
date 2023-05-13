import redis
import uvicorn
import requests
from fastapi import FastAPI
from datetime import timedelta

API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
CACHE_NAME = "YT_CACHE"

app = FastAPI()
r = redis.Redis(host="localhost", port=6379, db=0)

def get_video_url(video):
    return "https://www.youtube.com/watch?v=" + video["id"]

class ReturnResponse:
    def __init__(self, status, cache, data):
        self.status = status
        self.cache = cache
        self.data = data

@app.get("/trends", status_code=200)
async def getTrends():
    if r.exists(CACHE_NAME):
        return ReturnResponse(True, True, r.get(CACHE_NAME))
    else:
        URL = "https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&regionCode=JP&maxResults=10&key=" + API_KEY
        response = requests.get(URL)
        if response.status_code == 200:
            videos = response.json()["items"]
            urls = [get_video_url(video) for video in videos]
            r.set(CACHE_NAME, urls, timedelta(hours=1))
            return ReturnResponse(True, False, urls)
        else:
            return ReturnResponse(False, None, None)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=80)
