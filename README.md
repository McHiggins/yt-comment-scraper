# YouTube Comment Scraper
___

The YouTube Comment Scraper is a program to fetch all comments
from a given playlist_id or a given video_id. You can retrieve
and save all the comments from your video via Google-API. After
this you can analyze the content of the comments and link them
to the retrieved metadata and analyze correlations. 


## Usage

1. Get a Google-API-Key and safe it to the config.yaml file.
2. Install all the requirements.txt
3. Get a video_id or playlist_id and start fetching data via
the youtubecomment_grabber() or channellist_grabber().
4. This will save you a dataframe with all the comments and it's 
meta-data to a .csv-file or all the video_ids from a specified 
   playlist.
   
You can use the playlist_id file to get all the single video_ids
from the playlist and download all comment data for each video.

