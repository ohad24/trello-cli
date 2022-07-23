import requests
from pprint import pprint
from typing import Union, Tuple
from dotenv import load_dotenv
import os
from pydantic import BaseModel, PrivateAttr
from models import TrelloList, TrelloCard

# class TrelloClient:
#     # https://stackoverflow.com/questions/63492123/how-do-add-an-assembled-field-to-a-pydantic-model
#     def __init__(self, API_KEY, API_TOKEN, BOARD_ID):
#         self.params = {"key": API_KEY, "token": API_TOKEN}
#         self.board_id = BOARD_ID
#         self.api_url = "https://api.trello.com/1/"
class TrelloClient(BaseModel):
    API_KEY: str
    API_TOKEN: str
    # BOARD_ID: str
    _query_params: dict = PrivateAttr()
    _api_url: str = PrivateAttr(default="https://api.trello.com/1/")

    def __init__(self, **data):
        # print(data)
        super().__init__(**data)
        self._query_params = {
            "key": data.get("API_KEY"),
            "token": data.get("API_TOKEN"),
        }

    def _make_requests(self, url: str) -> Tuple[int, Union[dict, str]]:
        response = requests.get(url, params=self._query_params)
        if response.status_code == 200:
            return response.status_code, response.json()
        else:
            return response.status_code, response.text

    def get_lists(self, board_id) -> Tuple[int, Union[TrelloList, str]]:
        url = self._api_url + "boards/" + board_id + "/lists"
        status, res = self._make_requests(url)
        if status == 200:
            return status, [TrelloList(**list_) for list_ in res]
        return status, res

    def get_cards(self, list_id: str) -> Tuple[int, Union[dict, str]]:
        url = self._api_url + "lists/" + list_id + "/cards"
        status, res = self._make_requests(url)
        if status == 200:
            return status, [TrelloCard(**card) for card in res]
        return status, res


if __name__ == "__main__":
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    API_TOKEN = os.getenv("API_TOKEN")
    BOARD_ID = os.getenv("BOARD_ID")
    client = TrelloClient(
        API_KEY=API_KEY,
        API_TOKEN=API_TOKEN,
    )
    pprint(client.dict())
    # client.get_lists()
    status, res = client.get_lists(board_id=BOARD_ID)
    if status == 200:
        for list in res:
            print(list.id, list.name)
            status, res = client.get_cards(list.id)
            if status == 200:
                for card in res:
                    pprint(card.dict())
    else:
        print(status, res)
