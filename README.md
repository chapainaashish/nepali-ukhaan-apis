# nepali-ukhaan-apis


**Hang on tight, This is currently in a development stage**

# Ukhaan Tukka API

The UkhaanTukka API provides access to a list of Nepali idioms, known as *ukhaans* in Nepali, along with their Roman transliteration, English meaning, and an example sentence. The API makes a request to the **`README.md`** file from <a href = ''>nepali-ukhaan</a> repository to the fetch data and can be used to fetch the full list of *ukhaan* or to search for a particular *ukhaan* based on its Nepali name, Roman transliteration, or meaning.


# Endpoints

- **`/ukhaantukka`**: Retrieves a paginated list of all *ukhaan*.<br>
- **`/ukhaantukka/nepali`**: Retrieves a paginated list of *ukhaan* sorted by Nepali text.<br>
- **`/ukhaantukka/roman`**: Retrieves a paginated list of *ukhaan* sorted by Roman text.<br>
- **`/ukhaantukka/meaning`**: Retrieves a paginated list of *ukhaan* sorted by their meaning.<br>
- **`/ukhaantukka/example`**: Retrieves a paginated list of *ukhaan* sorted by example usage.<br>

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

To retrieve all *ukhaan* at once, withouth pagination:
```python
http://localhost:8000/ukhaantukka?show_all=true
```

To retrieve the first 50 *ukhaan* sorted by Nepali text:
```python
http://localhost:8000/ukhaantukka/nepali?limit=10&offset=0
```

# License

The *ukhaan* data used in this API is collected and forked from the <a href = "https://github.com/chapainaashish/nepali-ukhaan">nepali-ukhaan</a> repository on GitHub and is free to use and modify under MIT license. We would like to thank <a href = "https://github.com/chapainaashish">Aashish Chapain</a> and the entire community for contributing to this repository and making this API possible.
