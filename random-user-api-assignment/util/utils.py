from enum import Enum


class SortBy(Enum):
    ID, FIRST_NAME, LAST_NAME, USERNAME, EMAIL, ADDRESS = range(6)
