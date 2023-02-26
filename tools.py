import random
import markdown
import requests
import itertools
from bs4 import BeautifulSoup


# This little function to avoid nested lists:
def flat_lists(d_lists):
    return list(itertools.chain(*d_lists))


# This function retrieves a list of ukhaan and their iteration based on parameters such as limit and offset:
def get_language_list(language_name, language_list, limit: int = 100, offset: int = 0, show_all: bool = False):
    if show_all:
        return {
            language_name: language_list,
        }
    else:
        return {
            language_name: language_list[offset: offset + limit],
            }


# This class retrieves data from a Nepali proverb table:
class UkhaanTable:    
    def __init__(self): 
        # Retrieve the raw markdown text from the `nepali-ukhaan` repository on GitHub and convert to HTML for parsing purposes.         
        req = requests.get('https://raw.githubusercontent.com/chapainaashish/nepali-ukhaan/main/README.md')
        html = markdown.markdown(req.text)
        
        # Making a soup to parse the HTML to retrieve the Nepali proverb table
        soup = BeautifulSoup(html, 'html.parser')

        for span_tag in soup.find_all(['span', 'br']): span_tag.decompose()
        self.table = soup.find_all('p')[-1]

        nested_lists = [tab.text.split("\n") for tab in self.table]
        # Filtering the list that give an empty string in a newline
        filtered_lists = [[item for item in sublist if item != ''] for sublist in nested_lists]
        # Flattening the nested/multi-dimensional list
        self.ukhaan_tables = flat_lists(filtered_lists[1:])        
    
    # This method extracts the Nepali or Roman list from the Nepali proverb table based on the given index.
    def extract_phase_one(self, indexes):        
        into_list_comprehension = [tab.split("|")[indexes].strip() for tab in self.ukhaan_tables]        
        return into_list_comprehension        
            
    # This method extracts the meaning and example lists from the Nepali proverb table:
    def extract_phase_two(self):        
        # This code snippet extracts the meaning and example lists from self.ukhaan_tables using list comprehension method.

        # If a row in self.ukhaan_tables has 4 fields (i.e. separated by '|'), the second-to-last field is assumed to be the meaning
        # and the last field is assumed to be the example. If a row has 3 fields, only the last field is assumed to be the meaning.
        # If a row has less than 3 fields, both meaning and example are set to empty string.
        # The resulting meaning and example lists are returned as a tuple.
        meaning_lists = [
                            row.split("|")[-2].strip() if len(row.split("|")) == 4 else
                            row.split("|")[-1].strip() if len(row.split("|")) == 3 else
                            "" for row in self.ukhaan_tables    
                        ]
        example_lists = [
                            row.split("|")[-1].strip() if len(row.split("|")) == 4 else
                            "" for row in self.ukhaan_tables        
                        ]
        
        return meaning_lists, example_lists        
        
    # Below methods return a list of nepali, romanized version, meaning and an example usage of ukhaan.
    
    def nepali(self):        
        return [nep.strip() for nep in self.extract_phase_one(0)]
    
    def roman(self):        
        return [rom.strip() for rom in self.extract_phase_one(1)]  
    
    def meaning(self):        
        return self.extract_phase_two()[0]
    
    def example(self):        
        return self.extract_phase_two()[-1]


# This class provides additional functionalities for the ukhaan table.
class UkhaanFunctionalities(UkhaanTable):    
    def __init__(self):
        super().__init__()        

    # This method returns a random ukhaan along with its corresponding romanization, meaning, and example as a dictionary.
    def random_ukhaan(self):      
        indexes = random.randint(0, len(self.extract_phase_one(0)))       

        data = {
                'Nepali': self.extract_phase_one(0)[indexes].strip(),
                'Roman': self.extract_phase_one(1)[indexes].strip(),
                'Meaning': self.extract_phase_two()[0][indexes].strip(),
                'Example': self.extract_phase_two()[-1][indexes].strip(),
            }
        
        return data
    
    # Below methods returns a Nepali, romanized version, meaning and an example usage of a random Nepali ukhaan.
        
    def random_nepali(self):        
        indexes = random.randint(0, len(self.extract_phase_one(0)))
        return self.extract_phase_one(0)[indexes]

    def random_roman(self):    
        indexes = random.randint(0, len(self.extract_phase_one(1)))
        return self.extract_phase_one(1)[indexes]
    
    def random_meaning(self):        
        indexes = random.randint(0, len(self.extract_phase_two()[0]))
        return self.extract_phase_two()[0][indexes]
    
    def random_example(self):    
        indexes = random.randint(0, len(self.extract_phase_two()[-1]))
        return self.extract_phase_two()[-1][indexes]

