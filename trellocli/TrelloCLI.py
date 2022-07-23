from TrelloAPIclient import TrelloClient
import fire
from dotenv import load_dotenv
import os
from tabulate import tabulate


class TrelloCLI():
    def __init__(self, **data):
        load_dotenv()
        self.API_KEY = os.getenv("API_KEY")
        self.API_TOKEN = os.getenv("API_TOKEN")
        super().__init__(**data)

    def _format_data_table(self, data:list):
        headers = list(data[0].dict().keys())
        rows = [row.dict().values() for row in data]
        print(tabulate(rows, headers, tablefmt="grid"))

    def get_lists(self, board_id: str):
        client = TrelloClient(API_KEY=self.API_KEY, API_TOKEN=self.API_TOKEN)
        status, res = client.get_lists(board_id=board_id)
        if status == 200:
            self._format_data_table(res)
        else:
            print(res)

    def get_cards(self, list_id: str):
        client = TrelloClient(API_KEY=self.API_KEY, API_TOKEN=self.API_TOKEN, list_id=list_id)
        status, res = client.get_cards(list_id)
        if status == 200:
            self._format_data_table(res)
        else:
            print(res)

def main():
    cli = TrelloCLI()
    fire.Fire(cli)

if __name__ == '__main__':
    # load_dotenv()
    # API_KEY = os.getenv("API_KEY")
    # API_TOKEN = os.getenv("API_TOKEN")
    # BOARD_ID = os.getenv("BOARD_ID")
    # cli = TrelloCLI(API_KEY=API_KEY, API_TOKEN=API_TOKEN, BOARD_ID=BOARD_ID)
    # cli = TrelloCLI(API_KEY=API_KEY, API_TOKEN=API_TOKEN, BOARD_ID="")
    # cli = TrelloCLI()
    # fire.Fire(cli)
    main()