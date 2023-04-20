import yt_scraper
import yaml


# loading configuration file
def configloader(path: str):
    with open(path) as cfg:
        config = yaml.load(cfg, Loader=yaml.FullLoader)
    return config["ytcommentscraper"]


if __name__ == '__main__':
    cfg = configloader(path="..\\data\\config\\config.yaml")
    yt_scraper.channellist_grabber(cfg_api_service_name=cfg[""], cfg_api_version=cfg[""], cfg_api_key=cfg[""],
                                   playlist_id=cfg[""], np_token="")
    yt_scraper.youtubecomment_grabber(cfg_api_key=cfg[""], cfg_api_service_name=cfg[""], cfg_api_version=cfg[""],
                                      video_id=cfg[""], video_title=None, channel_name=None, video_releasedate=None)
