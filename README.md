# LCHRK_NLP_Training_2025
 A complete NLP Training by Chaitanya Rajkumar Limmala

## Pre-requisites

### NLTK
Natural language toolkit and commonly called the mother of all 
NLP libraries.
#### Syntax
```python
pip install nltk
```

### SpaCy
SpaCy is recently a trending library, as it comes with the added 
flavors of a deep learning framework.
#### Syntax
```python
pip install spacy
```

### TextBlob
This is one of the data scientist’s favorite library when it 
comes to implementing NLP tasks. It is based on both NLTK and Pattern.
```python
pip install textblob
```

### CoreNLP
It is a Python wrapper for Stanford CoreNLP. The toolkit 
provides very robust, accurate, and optimized techniques for tagging, 
parsing, and analyzing text in various languages.
```python
pip install CoreNLP
```

## Tutorial 1
### Extracting The Data
- [x] **Text data collection using APIs**
##### Required Libraries
**Tweepy**
```python
pip install tweepy
```
**Tweepy** works only with V2 API(paid version) of X platform. So, check it once before running this tutorial.

- [x] **Reading PDF file**
##### Required Libraries
**PyPDF2**
```python
pip install PyPDF2
```
###### Sample Output
![Read PDF File Output Sample](https://github.com/lchrk241721/LCHRK_NLP_Training_2025/blob/main/Results%20Area/read-pdf-file-output.png)

- [x] **Reading Word Document**
##### Required Libraries
**python-docx**
```python
pip install python-docx
```
###### Sample Output
![Read Word Document Output Sample](https://github.com/lchrk241721/LCHRK_NLP_Training_2025/blob/main/Results%20Area/read-word-document-output.png)

- [x] **Reading JSON Object**
##### Required Libraries
**JSON**
```python
pip install json
```
###### Sample Output
![Read JSON Object Output Sample](https://github.com/lchrk241721/LCHRK_NLP_Training_2025/blob/main/Results%20Area/read-json-output.png)

- [x] **Reading HTML Page & Parsing**
##### Required Libraries
**BS4**
```python
pip install bs4
```
###### Sample Output
![Read HTML Page Output Sample](https://github.com/lchrk241721/LCHRK_NLP_Training_2025/blob/main/Results%20Area/read-html-page-parse-output.png)

- [x] **Regular Expressions -> Basic Example**
##### Required Libraries
**re**
```python
pip install re
```
###### Sample Output
![Regular Expressions Output Sample](https://github.com/lchrk241721/LCHRK_NLP_Training_2025/blob/main/Results%20Area/regex-example-output.png)

- [x] **Regular Expressions -> Extract Data From EBook**
###### Sample Output 1
![RegEx Extract Data From Ebook Output Sample](https://github.com/lchrk241721/LCHRK_NLP_Training_2025/blob/main/Results%20Area/regex-extract-data-from-ebook-output.png)
- [x] **Exploratory Analysis**
- [x] **Finding Occurences**
###### Sample Output 2
![Exploratory Analysis and Finding Occurences Output Sample](https://github.com/lchrk241721/LCHRK_NLP_Training_2025/blob/main/Results%20Area/regex-extract-data-from-ebook-expl-analysis-finding-occurences-output.png)

- [x] **String Handling**

###### Sample Output
![String Handling Output Sample](https://github.com/lchrk241721/LCHRK_NLP_Training_2025/blob/main/Results%20Area/string-handling-output.png)

- [x] **Web Scraping**
##### Required Libraries
**bs4**
```python
pip install bs4
```
```python
pip install requests
```
```python
pip install ipywidgets
```
###### Sample Output
![Web Scraping Output Sample](https://github.com/lchrk241721/LCHRK_NLP_Training_2025/blob/main/Results%20Area/web-scraping-output.png)
## Tutorial 2
### Exploring & Processing Text Data
- [ ] **Lowercasing**

- [ ] **Punctuation Removal**

- [ ] **Stop Words Removal**

- [ ] **Text Standardization**

- [ ] **Spelling Correction**

- [ ] **Tokenization**

- [ ] **Stemming**

- [ ] **Lemmatization**

- [ ] **Exploratory Data Analysis**

- [ ] **End-to-End Processing Pipeline**


## Download and Run
1. Download the latest binary from [Releases](https://github.com/lchrk241721/LCHRK_NLP_Training_2025/releases).
2. Open CMD/Terminal and navigate to the downloaded file.
3. Run:
```bash
    ./read-pdf-file.exe  # Windows
    ./read-word-document.exe # Windows
```


---

### **Notes**
- **Dependencies**: Ensure all dependencies are correctly specified in `requirements.txt`. PyInstaller bundles them, but missing ones will cause runtime errors.
- **Anti-Virus False Positives**: Some antivirus tools may flag PyInstaller binaries. Consider adding a note about this in your README.
- **Debugging**: If the binary fails, run it in CMD to see errors or use `--debug` with PyInstaller.

This approach lets users run your NLP tutorial without installing Python or dependencies. Let me know if you'd like help with automation (e.g., GitHub Actions) or multi-platform support!