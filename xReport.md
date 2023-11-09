**Title:** Wikipedia Recommender System
**Authors:** *Samuel Janas 151927, Michał Skrzypek 151766*
**Date:** 05.11.2023

##1.	Goal
Our project aims to create a recommendation system for similar articles based on users' previously visited articles in an effective and ethical way. The system comprises several key components: web scraping and crawling, text preprocessing, content similarity calculation, and article recommendations.

##2.	Data Collection (Crawling and Scraping)
The data collection process involves scraping content from fandom website about computer game Terraria. We choose this fandom Wikipedia because Terraria is superb.
config.py
```python
BASE_URL = 'https://terraria.fandom.com'
START_URL = 'https://terraria.fandom.com/wiki/Terraria_Wiki'
MAX_DEPTH = 4
MAX_ARTICLES = 2000
SLEEP_TIME = 0.3  # Time to sleep between scraping requests (in seconds)

CSV_FILE_PATH = "csv/preprocessed_articles.csv"
```
<!-- <!-- paste config file here> -->
Configuration parameters such as base, start URLs and the number of articles that we want to scrape are provided. We defined sleep rule to avoid  excessive and rapid requests that could overload the website's server, resulting in getting our IP address banned. Parameter ```MAX_DEPTH``` limits the depth of web page traversal during the web scraping process. Deeper levels may contain less relevant or sometimes even unrelated information.

scraper.py
With global variable ```VISITED_LINKS``` we keep track of already visited links so none of them overlap. We store scraped data in list called ```articles```. Functions ```fetch_robots_txt, parse_robots_txt, can_visit_url``` retrieve content of the file robots.txt then parse it and extract “Allow”/”Disallow” rules. This part ensures that we crawl through the website ethically and for instance we don’t scrape data about users. With ```get_links_from_url``` we extract all links from a given URL and then we know next websites to visit. We consider links starting with the ```BASE_URL``` only.  The ```scrape_content_from_link``` scrapes the main content from a given URL. We assume that the main content is located in a &lt;div&gt; with the class mw-parser-output. The ```dfs_crawl``` function performs a recursive depth-first traversal of the website. If the content of a page is successfully scraped, it is appended to the articles list.



##3.	Preprocessing
To preprocess the data we utilized Natural Language Toolkit and applied standard techniques.
- **Tokenization:** breaking the article content into sentences and further into separate words. Smaller units are easier to process and analyze, morover for computer games separate words are menaingful, we can have heroes or weapons names that are extremely informative.
- **Removing Stopwords and non-alphabetical tokens:** This step improves the quality of the data. Stopwords (e.g., the, I, in, and, is) and non-alphabetical tokens (e.g., punctuation) are typically not informative so we removed them to clean the data.
- **POS tagging and Lemmatization:** Tagging the words ensures that the lemmatizer understands the correct part of speech for each word. Lemmatization reduces words to their base or dictionary form.

##4.	Similarity Calculation & Recommendations
We use *“Term Frequency-Inverse Document Frequency”* because this technique takes into account two crucial factors:
- how often a term appears in a document,
- how unique a term is across documents.
<div>The next step is converting the article content into TF-IDF vectors and then matrix. We calculate the similarities with cosine-similarity formula. It calculates the cosine of the angle between vectors and recommends five with the best score.</div>



##The resulting recommendations are based on the content of the articles.
- show some charts about which words occur most often.
- show 1-3 recommendations mathermaticaly (e.g words that are similar here and there)
- 1-2 recommendations knowledge-based (ask sami)
