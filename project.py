import scraper
import preprocessor
import similarity
import pandas as pd
import argparse
from config import CSV_FILE_PATH

def main(args):
    if args.read_csv:
        # Read from CSV
        df = pd.read_csv(CSV_FILE_PATH)
        preprocessed_articles = df.to_dict(orient='records')
    elif args.process_csv:
        # Preprocess the CSV
        df = pd.read_csv(CSV_FILE_PATH)
        output_csv_path = 'csv/processed_file.csv'
        preprocessed_articles = []

        for _, row in df.iterrows():
            article = {'link': row['link'], 'content': row['content']}
            preprocessed_article = preprocessor.preprocess_article(article)
            preprocessed_articles.append(preprocessed_article)

        # Save the preprocessed data to a new CSV file
        df_preprocessed = pd.DataFrame(preprocessed_articles)
        df_preprocessed.to_csv(output_csv_path, index=False)
        print(f"Saved preprocessed data to {output_csv_path}")
    else:
        # Scrape
        articles = scraper.scrape()
        # Preprocess
        preprocessed_articles = [preprocessor.preprocess_article(article) for article in articles]
        # Save to CSV
        df = pd.DataFrame(preprocessed_articles)
        df.to_csv(CSV_FILE_PATH, index=False)
        print(f"Saved preprocessed articles to {CSV_FILE_PATH}")

    # For demonstration, let's use the links of the first 5 articles as input_articles_links
    input_articles_links = [article['link'] for article in preprocessed_articles[:5]]

    recommendations = similarity.get_recommendations(preprocessed_articles, input_articles_links, top_n=5)

    for rec in recommendations:
        print(f"Based on {rec['original']}, we recommend {rec['recommended']} with a score of {rec['score']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Wikipedia Article Recommender System')
    parser.add_argument('--read-csv', action='store_true', help='Use this flag to read data from CSV instead of scraping again')
    parser.add_argument('--process-csv', action='store_true', help='Use this flag to preprocess an existing CSV')
    args = parser.parse_args()
    main(args)
