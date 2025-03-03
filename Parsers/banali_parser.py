"""
This file is used for https://banali.am/ data collection.
"""
from typing import Union, List
import requests

class BanaliParser:
    regions_by_id: dict[str, int] = {
        "yerevan": 1,
        "gexarquniq": 2,
        "shirak": 3,
        "lori": 4,
        "vayoc-dzor": 5,
        "armavir": 6,
        "syuniq": 7,
        "tavush": 8,
        "aragacotn": 9,
        "kotayk": 10,
        "ararat": 11
    }

    def __init__(self, trade_type, regions):
        self.__trade_type = trade_type
        self.__regions = regions
        self.__base_url = self.__get_url

    @property
    def __get_url(self):
        base_url = "https://banali.am/en"
        # Url making part from our request
        if self.__trade_type not in ['buy/sell', 'rent']:
            raise ValueError(f"Invalid trade type: {self.__trade_type}. Must be 'buy/sell' or 'rent'.")
        url_trade_type = "sell" if self.__trade_type == "buy/sell" else "rent"

        # Making URL for each region separately
        if self.__regions == "all":
            return base_url + "/" + url_trade_type
        elif isinstance(self.__regions,list) and all(region.lower() in self.regions_by_id for region in self.__regions):
            url_regions = "&".join(f"state={str(self.regions_by_id[region.lower()])}" for region in self.__regions)
            return base_url + "/" + url_trade_type + "?" + url_regions
        else:
            raise ValueError(f"Invalid regions: {self.__regions}. Must be 'all' or a list of valid regions.")

    def _get_page_url(self, page):
        # Adding page to url of https://banali.am/vachark format
        if "?" in self.__base_url:
            return self.__base_url + f"&page={page}"
        else:
            return self.__base_url + f"?page={page}"

if __name__ == '__main__':
    parser = BanaliParser("buy/sell", "all")
    print(parser._get_page_url(2))