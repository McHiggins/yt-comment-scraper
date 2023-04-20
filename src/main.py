import yt_comment_scraper
import yaml


# loading configuration file
def configloader(path: str):
    with open(path) as cfg:
        config = yaml.load(cfg, Loader=yaml.FullLoader)
    return config["ytcommentscraper"]


if __name__ == '__main__':
    yt_comment_scraper.channellist_grabber()
