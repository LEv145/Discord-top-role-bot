from dataclasses import dataclass


@dataclass
class Message():
    user_id: int
    content: str
