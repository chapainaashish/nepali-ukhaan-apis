
# Nepali-Ukhaan-APIs
The *Nepali-Ukhaan* API provides access to a list of Nepali idioms, known as *ukhaan* in Nepali, along with their Roman transliteration, English meaning, and an example sentence. The API makes a request to the **`README.md`** file from <a href = 'https://github.com/chapainaashish/nepali-ukhaan'>nepali-ukhaan. </a> 

**UPDATE: API IS LIVE**

https://nepaliukhaan.onrender.com/



This API is built using FastAPI, a modern, fast, web framework for building APIs with Python



# How to Set up?

1. Clone the reposistory `https://github.com/chapainaashish/nepali-ukhaan-apis.git` on your machine
   
2. Install poetry, if not installed `curl -sSL https://install.python-poetry.org | python3 -`

3. Install dependencies `poetry install`

4. Activate the virtual environment `poetry shell`

5. Run the server using uvicorn, `uvicorn ukhaan_api.app:app`

6. Navigate to `http://127.0.0.1:8000/`

7. Read the documentation `http://127.0.0.1:8000//docs`
   


# Endpoints

- **`/`**: Retrieves a paginated list of all *ukhaan*.<br>
- **`/nepali`**: Retrieves a paginated list of *ukhaan* sorted by Nepali text.<br>
- **`/roman`**: Retrieves a paginated list of *ukhaan* sorted by Roman text.<br>
- **`/example`**: Retrieves a paginated list of *ukhaan* sorted by example usage.<br>

- **`/random/ukhaan`**: Retrieves a random *ukhaan* from the list.
- **`/random/nepali`**: Retrieves a random Nepali *ukhaan* in Nepali language
- **`/random/roman`**: Retrieves a random *ukhaan* in Roman Nepali.
- **`/random/example`**: Retrieves a random *example usage* of an ukhaan.

# Query Parameters

The following query parameters can be used to modify the results returned by the API:

- **`limit`**: The number of *ukhaan* to retrieve (default: 100).<br>
- **`offset`**: The starting index of the *ukhaan* to retrieve (default: 0).<br>
- **`show_all`**: Whether to retrieve all *ukhaan* at once, without pagination (default: **`False`**).<br>

# Example Usage

To retrieve a list of *ukhaan*, make a GET request to the following endpoint:
```python
http://localhost:8000/
```

The response will be a JSON object containing a list of *ukhaan*. You can use the **`limit`** and **`offset`** query parameters to paginate the results. For example, to retrieve the first 10 *ukhaan*, you can make the following request:
```python
http://localhost:8000?limit=10&offset=0
```

To retrieve all *ukhaan* at once, without pagination:
```python
http://localhost:8000?show_all=true
```