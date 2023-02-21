from fastapi import FastAPI
from tools import UkhaanTable


ukhaan = UkhaanTable()

nepali_lists = ukhaan.nepali()
roman_lists = ukhaan.roman()
meaning_lists = ukhaan.meaning()
example_lists = ukhaan.example()


app = FastAPI()

@app.get("/ukhaantukka")
def main_page(limit: int = 100, offset: int = 0, show_all: bool = False):
    if show_all:
        return {
                'Nepali': nepali_lists,
                'Roman': roman_lists,
                'Meaning': meaning_lists,
                'Example': example_lists,
            }        
    else:
        return {
            'Nepali': nepali_lists[offset : offset + limit],
            'Roman': roman_lists[offset : offset + limit],
            'Meaning': meaning_lists[offset : offset + limit],
            'Example': example_lists[offset : offset + limit],
            }


@app.get("/ukhaantukka/nepali")
def nepali(limit: int = 100, offset: int = 0, show_all: bool = False):
    if show_all:
        return {
            "Nepali": nepali_lists,
        }
    else:
        return {
            "Nepali": nepali_lists[offset : offset + limit],
        }


@app.get("/ukhaantukka/roman")
def roman(limit: int = 100, offset: int = 0, show_all: bool = False):
    if show_all:
        return {
            'Roman': roman_lists,
        }
    else:
        return {
            'Roman': roman_lists[offset : offset + limit],
        }


@app.get("/ukhaantukka/meaning")
def meaning(limit: int = 100, offset: int = 0, show_all: bool = False):
    if show_all:
        return {
            'Meaning': meaning_lists,
        }
    else:
        return {
            'Meaning': meaning_lists[offset : offset + limit],
        }


@app.get("/ukhaantukka/example")
def example(limit: int = 100, offset: int = 0, show_all: bool = False):
    if show_all:
        return {
            'Example': example_lists,
        }
    else:
        return {
            'Example': example_lists[offset : offset + limit],
        }

