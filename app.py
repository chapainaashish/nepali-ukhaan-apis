from fastapi import FastAPI
from tools import UkhaanTable, UkhaanFunctionalities, get_language_list


# Create instances of UkhaanTable and UkhaanFunctionalities classes:
ukhaan = UkhaanTable()
functionalities = UkhaanFunctionalities()

# Get the lists of Nepali, Roman, Meaning and Example words from the UkhaanTable instance:
nepali_lists = ukhaan.nepali()
roman_lists = ukhaan.roman()
meaning_lists = ukhaan.meaning()
example_lists = ukhaan.example()


# Initialize a FastAPI instance:
app = FastAPI()


# Define a route to get all UkhaanTukka:
@app.get("/ukhaantukka")
def get_ukhantukka(limit: int = 100, offset: int = 0, show_all: bool = False):
    # Get the lists of Nepali, Roman, Meaning, and Example words based on the given parameters:
    nepali_result = nepali(limit, offset, show_all)
    roman_result = roman(limit, offset, show_all)
    meaning_result = meaning(limit, offset, show_all)
    example_result = example(limit, offset, show_all)

    # Return the merged result
    return {
        **nepali_result,
        **roman_result,
        **meaning_result,
        **example_result
    }


# Below defined endpoint and routes to get Nepali, Romanized version, meaning and and example usage of Ukhaan based on the given parameters:

@app.get("/ukhaantukka/nepali")
def nepali(limit: int = 100, offset: int = 0, show_all: bool = False):
    return get_language_list("Nepali", nepali_lists, limit, offset, show_all)


@app.get("/ukhaantukka/roman")
def roman(limit: int = 100, offset: int = 0, show_all: bool = False):
    return get_language_list("Roman", roman_lists, limit, offset, show_all)


@app.get("/ukhaantukka/meaning")
def meaning(limit: int = 100, offset: int = 0, show_all: bool = False):
    return get_language_list("Meaning", meaning_lists, limit, offset, show_all)


@app.get("/ukhaantukka/example")
def example(limit: int = 100, offset: int = 0, show_all: bool = False):
    return get_language_list("example", example_lists, limit, offset, show_all)



# Define endpoint to get a random Ukhaan.
@app.get("/random-ukhaan")
def random_ukhaan():    
    return functionalities.random_ukhaan()



# Below are the defined endpoints ard routes get Nepali, Romanized version, meaning and an example usage of random ukhaan.

@app.get("/random-ukhaan/nepali")
def random_nepali():
    return {
        'Nepali': functionalities.random_nepali().strip()
    }


@app.get("/random-ukhaan/roman")
def random_roman():
    return {
        'Roman': functionalities.random_roman().strip()
    }


@app.get("/random-ukhaan/meaning")
def random_meaning():
    return {
        'Meaning': functionalities.random_meaning().strip()
    }


@app.get("/random-ukhaan/example")
def random_example():
    return {
        'Example': functionalities.random_example().strip()
    }

    