from fastapi import FastAPI
from tools import RetrieveUkhaanAPI

# TODO: return response in dictionary format with key value pair


# Create instances of UkhaanTable and UkhaanFunctionalities classes:
ukhaan = RetrieveUkhaanAPI()

# Initialize a FastAPI instance:
app = FastAPI()


# Define a route to get all ukhaan
@app.get("/")
def get_ukhaan(limit: int = 100, offset: int = 0, show_all: bool = False):
    result = ukhaan.retrieve_ukhaan(limit, offset, show_all)
    return {**result}


# Endpoint and routes to get Nepali, Romanized version, example usage of Ukhaan based on the given parameters:
@app.get("/nepali")
def nepali(limit: int = 100, offset: int = 0, show_all: bool = False):
    result = ukhaan.retrieve_nepali(limit, offset, show_all)
    return {**result}


@app.get("/roman")
def roman(limit: int = 100, offset: int = 0, show_all: bool = False):
    result = ukhaan.retrieve_roman(limit, offset, show_all)
    return {**result}


@app.get("/example")
def example(limit: int = 100, offset: int = 0, show_all: bool = False):
    result = ukhaan.retrieve_example(limit, offset, show_all)
    return {**result}


# Endpoint and routes to get random Nepali ukhaan, romanized version and example


@app.get("/random/ukhaan")
def random_ukhaan():
    result = ukhaan.retrieve_random_ukhaan()
    return {result}


@app.get("/random/roman")
def random_roman():
    result = ukhaan.retrieve_random_roman()
    return {result}


@app.get("/random/example")
def random_example():
    result = ukhaan.retrieve_random_example()
    return {result}
