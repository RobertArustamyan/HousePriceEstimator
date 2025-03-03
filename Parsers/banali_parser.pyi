from typing import Union, List,Literal


class BanaliParser:
    regions: dict[str, int]

    def __init__(self, trade_type: Literal["buy/sell", "rent"], regions: Union[Literal["all"], List[str]]) -> None: ...

    def __get_url(self) -> str: ...

    def __get_page_url(self, page: int) -> str: ...