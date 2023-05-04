from fastapi import FastAPI
from tools import RetrieveUkhaanAPI

# Create instances of UkhaanTable and UkhaanFunctionalities classes:
ukhaan = RetrieveUkhaanAPI()

# Initialize a FastAPI instance:
app = FastAPI()


# Define a route to get all ukhaan
@app.get("/")
def get_ukhaan(limit: int = 100, offset: int = 0, show_all: bool = False):
    result = ukhaan.retrieve_ukhaan(limit, offset, show_all)
    return {**result}


# Below defined endpoint and routes to get Nepali, Romanized version, meaning and and example usage of Ukhaan based on the given parameters:
@app.get("/nepali")
def nepali(limit: int = 100, offset: int = 0, show_all: bool = False):
    result = ukhaan.retrieve_nepali(limit, offset, show_all)
    return {**result}


@app.get("/roman")
def roman(limit: int = 100, offset: int = 0, show_all: bool = False):
    result = ukhaan.retrieve_roman(limit, offset, show_all)
    return {**result}


@app.get("/meaning")
def meaning(limit: int = 100, offset: int = 0, show_all: bool = False):
    result = ukhaan.retrieve_meaning(limit, offset, show_all)
    return {**result}


@app.get("/example")
def example(limit: int = 100, offset: int = 0, show_all: bool = False):
    result = ukhaan.retrieve_example(limit, offset, show_all)
    return {**result}
