import itertools
import random

import markdown
import requests
from bs4 import BeautifulSoup


class RetrieveUkhaan:
    """Retrieves latest ukhaan from source and store them pythonically"""

    def __init__(self) -> None:
        # pulling latest ukhaan
        _request = requests.get(
            "https://raw.githubusercontent.com/chapainaashish/nepali-ukhaan/main/README.md"
        )

        # parsing md to html
        _html = markdown.markdown(_request.text)
        _soup = BeautifulSoup(_html, "html.parser")

        # excluding <span>, <br> elements and processing ukhaan table only
        for span_tag in _soup.find_all(["span", "br"]):
            span_tag.decompose()
        _table = _soup.find_all("p")[-1]

        # grouping ukhaan in nested list
        _nested_ukhaan_lists = [tab.text.split("\n") for tab in _table]

        # excluding empty string from list
        _filtered_lists = [
            [item for item in sublist if item != ""] for sublist in _nested_ukhaan_lists
        ]

        # flattening list/combining nested list
        # [1:] for removing table heading
        self._ukhaan_tables = list(itertools.chain(*_filtered_lists[1:]))

    def nepali(self) -> list:
        """
        Retrieves a list of ukhaan in Nepali language
        """
        # looks for a ukhaan in nepali in first position (index 0)
        return [raw.split("|")[0].strip() for raw in self._ukhaan_tables]

    def roman(self) -> list:
        """
        Retrieves a list of ukhaan in Roman Nepali
        """
        # looks for a ukhaan in romanized nepali in second position (index 1)
        return [raw.split("|")[1].strip() for raw in self._ukhaan_tables]

    def meaning(self) -> list:
        """
        Retrieves a meaning for each Nepali ukhaan
        """

        # looks for a meaning in second-last and last position (index -2|-1) depending on the row length, else return empty string
        return [
            row.split("|")[-2].strip()
            if len(row.split("|")) == 4
            else row.split("|")[-1].strip()
            if len(row.split("|")) == 3
            else ""
            for row in self._ukhaan_tables
        ]

    def example(self) -> list:
        """
        Retrieves a example for each Nepali ukhaan
        """

        # looks for a example in last position (index -1), else return empty string
        return [
            row.split("|")[-1].strip() if len(row.split("|")) == 4 else ""
            for row in self._ukhaan_tables
        ]

    def ukhaan(self) -> list:
        """
        Retrieves a list of tuples containing ukhaan, its Romanized version, its meaning, and an example
        """
        return list(zip(self.nepali(), self.roman(), self.meaning(), self.example()))


class RetrieveUkhaanAPI(RetrieveUkhaan):
    """Helper class specifically made for API call"""

    def __init__(self) -> None:
        super().__init__()

    def _limit_ukhaan(
        self, category_name: str, ukhaan: list, limit: int, offset: int, show_all: bool
    ) -> dict:
        """Implements limit and offset for ukhaan"""
        if show_all:
            return {
                category_name: ukhaan,
            }
        else:
            return {
                category_name: ukhaan[offset : offset + limit],
            }

    def retrieve_ukhaan(self, limit: int, offset: int, show_all: bool) -> list:
        """
        Retrieves a list of ukhaan in tuples
        """
        ukhaan = super().ukhaan()
        return self._limit_ukhaan(
            "Ukhaan", ukhaan, limit=limit, offset=offset, show_all=show_all
        )

    def retrieve_nepali(self, limit: int, offset: int, show_all: bool) -> dict:
        """
        Retrieves a list of Nepali ukhaan in Nepali language
        """
        nepali_ukhaan = super().nepali()
        return self._limit_ukhaan(
            "Nepali", nepali_ukhaan, limit=limit, offset=offset, show_all=show_all
        )

    def retrieve_roman(self, limit: int, offset: int, show_all: bool) -> dict:
        """
        Retrieves a list of Nepali ukhaan in Roman Nepali
        """
        roman_ukhaan = super().roman()
        return self._limit_ukhaan(
            "Roman", roman_ukhaan, limit=limit, offset=offset, show_all=show_all
        )

    def retrieve_example(self, limit: int, offset: int, show_all: bool) -> dict:
        """
        Retrieves a list of Nepali ukhaan example
        """
        ukhaan_example = super().example()
        return self._limit_ukhaan(
            "Example", ukhaan_example, limit=limit, offset=offset, show_all=show_all
        )

    def retrieve_random_ukhaan(self) -> tuple:
        """
        Retrieves a random nepali ukhaan
        """
        index = random.randint(0, len(super().ukhaan()))
        return super().ukhaan()[index]

    def retrieve_random_nepali(self) -> str:
        """
        Retrieves a random nepali ukhaan in nepali language
        """
        index = random.randint(0, len(super().nepali()))
        return super().nepali()[index]

    def retrieve_random_roman(self) -> str:
        """
        Retrieves a random nepali ukhaan in roman nepali format
        """
        index = random.randint(0, len(super().roman()))
        return super().roman()[index]

    def retrieve_random_example(self) -> str:
        """
        Retrieves a random ukhaan example
        """
        index = random.randint(0, len(super().example()))
        return super().example()[index]
