# nepali-ukhaan-apis


**Hang on tight, This is currently in a development stage.**

# Ukhaan Tukka API

The *UkhaanTukka* API provides access to a list of Nepali idioms, known as *ukhaan* in Nepali, along with their Roman transliteration, English meaning, and an example sentence. The API makes a request to the **`README.md`** file from <a href = 'https://github.com/chapainaashish/nepali-ukhaan'>nepali-ukhaan</a> repository to the fetch data and can be used to fetch the full list of *ukhaan* ~~or to search for a particular *ukhaan* based on its Nepali name, Roman transliteration, or meaning~~

This API is built using FastAPI, a modern, fast, web framework for building APIs with Python. 

# Endpoints

- **`/ukhaantukka`**: Retrieves a paginated list of all *ukhaan*.<br>
- **`/ukhaantukka/nepali`**: Retrieves a paginated list of *ukhaan* sorted by Nepali text.<br>
- **`/ukhaantukka/roman`**: Retrieves a paginated list of *ukhaan* sorted by Roman text.<br>
- **`/ukhaantukka/meaning`**: Retrieves a paginated list of *ukhaan* sorted by their meaning.<br>
- **`/ukhaantukka/example`**: Retrieves a paginated list of *ukhaan* sorted by example usage.<br>
- **`/random-ukhaan`**: Retrieves a random *ukhaan* from the list.
- **`/random-ukhaan/nepali`**: Retrieves a random Nepali *ukhaan* from the list.
- **`/random-ukhaan/roman`**: Retrieves a random Roman *ukhaan*.
- **`/random-ukhaan/meaning`**: Retrieves a random *ukhaan* along with its meaning.
- **`/random-ukhaan/example`**: Retrieves a random *ukhaan* along with an example sentence.

# Query Parameters

The following query parameters can be used to modify the results returned by the API:

- **`limit`**: The number of *ukhaan* to retrieve (default: 100).<br>
- **`offset`**: The starting index of the *ukhaan* to retrieve (default: 0).<br>
- **`show_all`**: Whether to retrieve all *ukhaan* at once, without pagination (default: **`False`**).<br>

# Example Usage

To retrieve a list of *ukhaan*, make a GET request to the following endpoint:
```python
http://localhost:8000/ukhaantukka
```
The response will be a JSON object containing a list of *ukhaan*. You can use the **`limit`** and **`offset`** query parameters to paginate the results. For example, to retrieve the first 10 *ukhaan*, you can make the following request:
```python
http://localhost:8000/ukhaantukka?limit=10&offset=0
```

To retrieve all *ukhaan* at once, without pagination:
```python
http://localhost:8000/ukhaantukka?show_all=true
```
To retrieve all the random *ukhaan* with its Nepali and Roman transliteration along with meaning.
```python
http://localhost:8000/random-ukhaan
```
Output
```json
{
    "Nepali": "नजाने गाउँको बाटो नसोध्नु",
    "Roman": "Najaane gau ko bato nasodhnu.",
    "Meaning": "Don't waste time on things that do not concern you.",
    "Example": ""
}

```

# Swagger Documentation

This API is documented using Swagger, an open source platform for building, documenting, and consuming RESTful web services. The Swagger documentation provides detailed information on the available endpoints, parameters, and responses, as well as examples of how to use the API.

To view the Swagger documentation for this API, open your browser and navigate to **`http:localhost:8000/docs`** or **`http://localhost:8000/redoc`**. From there, you can interact with the API directly from your browser, and also try out different requests and see their responses.

# License

The *ukhaan* data used in this API is collected and forked from the <a href = "https://github.com/chapainaashish/nepali-ukhaan">nepali-ukhaan</a> repository on GitHub and is free to use and modify under MIT license. We would like to thank <a href = "https://github.com/chapainaashish">Aashish Chapain</a> and the entire community for contributing to this repository and making this API possible.
