from typing import Union, List, Literal


class BanaliParser:
    regions: dict[str, int]

    def __init__(self, trade_type: Literal["buy/sell", "rent"], regions: Union[Literal["all"], List[str]]) -> None: ...

    def __get_url(self) -> str: ...

    def get_page_url(self, page: int) -> str: ...


class Regions:
    _regions_by_id: dict[str, int]


class GetCardsURL(Regions):
    __json_data: dict[str, dict]
    __params: dict[str, str]

    def __init__(self, regions: Union[Literal["all"], List[str]]) -> None: ...

    def __get_response(self, page: int) -> str: ...
