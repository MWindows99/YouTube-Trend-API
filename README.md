# YouTube Trend API
## Fetch Top 10 Trending Videos
This program fetches the top 10 trending videos from the YouTube API and returns their URLs. It utilizes the YouTube API's "Trending Videos" endpoint to retrieve the required information.

### Prerequisites
Before running the program, make sure you have the following:
 - YouTube Data API v3 credentials: You need to create a project in the Google Developers Console, enable the YouTube Data API v3, and obtain the necessary API key.
 - Python libraries: Install the required Python libraries by running the following command:<br>```pip install -U -r requirements.txt```
 - Redis: This program caches results from the YouTube API for one hour. It uses Redis for storing that cache. It must be installed and running on your computer or server.

### Setup
Follow the steps below to set up the program:
1. Clone the repository or download the source code files.
2. Replace YOUR_API_KEY in the main.py file with your YouTube Data API v3 key.
3. Change the Redis port and host if necessary.

### Usage
To run the program, execute the following command in your terminal or command prompt:
```python main.py```

Access `http://localhost/trends` in your browser.

The program will make a request to the YouTube API and fetch the top 10 trending videos. It will then display the URLs of these videos.

### Example Output
```json
{
    "status": true,
    "cache": true,
    "data": [
       "https://www.youtube.com/watch?v=aaaaaaa",
       "https://www.youtube.com/watch?v=bbbbbbb",
       "https://www.youtube.com/watch?v=ccccccc",
       "https://www.youtube.com/watch?v=ddddddd",
       "https://www.youtube.com/watch?v=eeeeeee",
       "https://www.youtube.com/watch?v=fffffff",
       "https://www.youtube.com/watch?v=ggggggg",
       "https://www.youtube.com/watch?v=hhhhhhh",
       "https://www.youtube.com/watch?v=iiiiiii",
       "https://www.youtube.com/watch?v=jjjjjjj",
    ]
}
```

### Contributing
If you have any suggestions, improvements, or bug fixes, please feel free to contribute. You can fork the repository, make the changes, and submit a pull request.

### License
This program is licensed under the MIT License. Feel free to modify and use it according to your needs.

### Disclaimer
This program is provided as-is with no warranty or guarantee of its accuracy or effectiveness. The usage of this program is solely at your own risk.
