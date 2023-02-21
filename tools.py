import markdown
import requests
from bs4 import BeautifulSoup


class UkhaanTable:
    def __init__(self):        
        req = requests.get('https://raw.githubusercontent.com/chapainaashish/nepali-ukhaan/main/README.md')
        html = markdown.markdown(req.text)
       
        soup = BeautifulSoup(html, 'html.parser')
        self.ukhaan_tables = soup.find_all('p')[-1].text.split("\n")[2:]
            
    
    # This method to extract Nepali and Roman lists:
    def extract_phase_one(self, indexes):
        into_list_comprehension = [tab.split("|")[indexes] for tab in self.ukhaan_tables]
        return into_list_comprehension

    
    # This method to extract Meaning and Example lists:
    def extract_phase_two(self):
        # Below snippet need more optimization, I am sure there's better aprroach than this:
        meaning_lists = []
        example_lists = []
        for contents in self.ukhaan_tables:
            split_contents = contents.split("|")
            if len(split_contents) == 2:     # length 2 ensure that the meaning and example column is empty:           
                meaning_lists.append("")
                example_lists.append("")
            elif len(split_contents) == 3:   # 3 ensure meaning column           
                meaning_lists.append(split_contents[-1].strip())
                example_lists.append("")
            elif len(split_contents) == 4:   # 4 ensure example column:        
                meaning_lists.append(split_contents[-2].strip())
                example_lists.append(split_contents[-1].strip())    
            else:
                continue
        
        return meaning_lists, example_lists
        

    def nepali(self):
        return [nep.strip() for nep in self.extract_phase_one(0)]
    
    def roman(self):
        return [rom.strip() for rom in self.extract_phase_one(1)]    
    

    def meaning(self):
        return self.extract_phase_two()[0]
    
    def example(self):
        return self.extract_phase_two()[-1]

