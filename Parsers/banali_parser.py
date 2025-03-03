"""
This file is used for https://banali.am/ data collection.
"""
from typing import Union, List
import requests

class Regions:
    _regions_by_id: dict[str, int] = {
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

class BanaliLinkCreater(Regions):
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
        elif isinstance(self.__regions, list) and all(
                region.lower() in self._regions_by_id for region in self.__regions):
            url_regions = "&".join(f"state={str(self._regions_by_id[region.lower()])}" for region in self.__regions)
            return base_url + "/" + url_trade_type + "?" + url_regions
        else:
            raise ValueError(f"Invalid regions: {self.__regions}. Must be 'all' or a list of valid regions.")

    def get_page_url(self, page):
        # Adding page to url of https://banali.am/vachark format
        if "?" in self.__base_url:
            return self.__base_url + f"&page={page}"
        else:
            return self.__base_url + f"?page={page}"


class GetCardsURL(Regions):
    __json_data = {
        'params': {
            'filters': {
                'public_code': '',
                'renovation': [],
                'structure_type': '',
                'developer_name': '',
                'rooms': [],
                'rental_price_type': [],
                'property_type': [],
                'is_developer': [],
                'sqm_price': [],
                'price': [],
                'monthly_mortgage': [],
                'area': [],
                'heating': [],
                'furniture': [],
                'amenities': [],
                'bedrooms': [],
                'floor': [],
                'has_3D_tour': [],
                'building_name': '',
                'animals': [],
                'with_installment': [],
                'is_favorite': [],
                'deal': 'sell',
                'state_id': [],
                'district_id': [],
            },
            'sortBy': 'date_desc',
        },
    }
    __params = {'page': '1'}

    def __init__(self, regions):
        self.__regions = regions

    def __get_response(self, page):
        if self.__regions == 'all':
            self.__json_data['params']['filters']['state_id'] = []
        else:
            states = []
            for region in self.__regions:
                if region.lower() in self._regions_by_id.keys():
                    states.append(str(self._regions_by_id[region.lower()]))
                    self.__json_data['params']['filters']['state_id'] = states

        self.__params['page'] = str(page)
        response = requests.post('https://banali.am/api/search/filter-posts', params=self.__params,
                                 json=self.__json_data)
        return response



if __name__ == '__main__':
    link_creator = BanaliLinkCreater("buy/sell", ['yerevan','kotayk'])
    urls = GetCardsURL(['yerevan','kotayk'])
    urls.get_response(1)
