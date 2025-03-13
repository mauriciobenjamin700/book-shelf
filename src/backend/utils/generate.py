from datetime import datetime
from uuid import uuid4


def id_generate() -> str:
    return str(uuid4())


def get_current_date() -> str:
    return str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))