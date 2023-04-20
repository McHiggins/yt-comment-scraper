import yt_scraper
import yaml


# loading configuration file
def configloader(path: str):
    with open(path) as cfg:
        config = yaml.load(cfg, Loader=yaml.FullLoader)
    return config["ytcommentscraper"]


if __name__ == '__main__':
    yt_scraper.channellist_grabber(cfg_api_service_name: str, cfg_api_version: str, cfg_api_key: str, playlist_id: str,
    np_token: str)
    yt_scraper.youtubecomment_grabber(cfg_api_key: str, cfg_api_service_name: str, cfg_api_version: str, video_id=None,
                                                                                                                          video_title=None, channel_name=None, video_releasedate=None)
