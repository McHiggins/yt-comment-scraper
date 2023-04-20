import yt_scraper
import yaml


# loading configuration file
def configloader(path: str):
    with open(path) as cfg:
        config = yaml.load(cfg, Loader=yaml.FullLoader)
    return config["ytcommentscraper"]


if __name__ == '__main__':
    cfg = configloader(path="..\\data\\config\\config.yaml")
    yt_scraper.channellist_grabber(cfg_api_service_name=cfg["api_service_name"], cfg_api_version=cfg["api_version"],
                                   cfg_api_key=cfg["APIKey"], playlist_id="", np_token="")
    yt_scraper.youtubecomment_grabber(cfg_api_key=cfg["APIKey"], cfg_api_service_name=cfg["api_service_name"],
                                      cfg_api_version=cfg["api_version"], video_id="", video_title="",
                                      channel_name="", video_releasedate="")
