from TrelloAPIclient import TrelloClient
import fire
from tabulate import tabulate
from . import __version__


class TrelloCLI:
    # def __init__(self, **data):
    #     self.version = __version__

    def _format_data_table(self, data: list):
        headers = list(data[0].dict().keys())
        rows = [row.dict().values() for row in data]
        print(tabulate(rows, headers, tablefmt="grid"))

    def get_lists(self, board_id: str):
        """
        Get all lists from a board
        """
        client = TrelloClient()
        status, res = client.get_lists(board_id=board_id)
        if status == 200:
            self._format_data_table(res)
        else:
            print(res)

    def get_cards(self, list_id: str):
        """
        Get all cards from a list
        """
        client = TrelloClient(list_id=list_id)
        status, res = client.get_cards(list_id)
        if status == 200:
            self._format_data_table(res)
        else:
            print(res)

    def version(self):
        """
        Prints the version of the CLI
        """
        print(__version__)


def main():
    fire.Fire(TrelloCLI)


if __name__ == "__main__":
    main()
