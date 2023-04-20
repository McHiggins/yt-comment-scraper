import yt_scraper
import yaml
import argparse


# loading configuration file
def configloader(path: str):
    with open(path) as cfg:
        configuration = yaml.load(cfg, Loader=yaml.FullLoader)
    return configuration["ytcommentscraper"]


def scraper_channelist(cfg: dict):
    channel_list = yt_scraper.channellist_grabber(cfg_api_service_name=cfg["api_service_name"], cfg_api_version=cfg["api_version"],
                                   cfg_api_key=cfg["APIKey"], playlist_id="", np_token="")
    return channel_list


def scraper_channelist(cfg: dict):
    channel_list = yt_scraper.channellist_grabber(cfg_api_service_name=cfg["api_service_name"], cfg_api_version=cfg["api_version"],
                                                  cfg_api_key=cfg["APIKey"], playlist_id="", np_token="")
    return channel_list


parser = argparse.ArgumentParser()
parser.add_argument("-a", "--action", help="Get data by channellist or video_id use -a ""channel_list"" or "
                                           """video_id""")
args = parser.parse_args()


if __name__ == '__main__':
    if args.action == "channel_list":
        config = configloader(path="..\\data\\config\\config.yaml")
        yt_scraper.channellist_grabber(cfg_api_service_name=config["api_service_name"],
                                       cfg_api_version=config["api_version"],cfg_api_key=config["APIKey"],
                                       playlist_id="", np_token="")
    if args.action == "video_id":
        config = configloader(path="..\\data\\config\\config.yaml")
        yt_scraper.youtubecomment_grabber(cfg_api_key=config["APIKey"], cfg_api_service_name=config["api_service_name"],
                                      cfg_api_version=config["api_version"], video_id="", video_title="",
                                      channel_name="", video_releasedate="")
