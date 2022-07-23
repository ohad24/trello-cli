from datetime import date
from pydantic import BaseModel
from typing import Optional


class TrelloList(BaseModel):
    id: str
    name: str


class TrelloAction(BaseModel):
    id: str
    idMemberCreator: str
    memberCreator: dict
    type: str
    date: str


class TrelloCard(BaseModel):
    id: str
    name: str
    desc: Optional[str] = None
    idChecklists: Optional[list] = None
    idLabels: Optional[list] = None
    # labels: Optional[list] = None
    idList: str
    idMembers: Optional[list] = None
    # url: str
    # shortLink: str
    shortUrl: str
    due: Optional[str] = None
    subscribed: bool
    dateLastActivity: str
    # actions: list[TrelloAction] = None
