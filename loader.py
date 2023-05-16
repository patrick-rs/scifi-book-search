import csv
from elasticsearch import Elasticsearch
import os


file_book_type = {
    'Aliens': 'sf_aliens.csv',
    'Alternate History':'sf_alternate_history.csv',
    'Alternate Universe':'sf_alternate_universe.csv',
    'Apocalyptic':'sf_apocalyptic.csv',
    'Cyberpunk':'sf_cyberpunk.csv',
    'Dystopia':'sf_dystopia.csv',
    'Military':'sf_military.csv',
    'Robots':'sf_robots.csv',
    'Space Opera':'sf_space_opera.csv',
    'Steampunk':'sf_steampunk.csv',
    'Time Travel':'sf_time_travel.csv'
}


es = Elasticsearch(
        os.environ["ELASTIC_URL"],
        verify_certs=False,
        basic_auth=('elastic', os.environ['ELASTIC_PASSWORD'])
        )


for book_type, file_name in file_book_type.items():
    with open(f'books/{file_name}') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            unique_key = f"{row['Author_Name']}#{row['Book_Title']}"
            row.pop('Original_Book_Title')
            row.pop('Genres')
            row['Book_Type'] =book_type
            row.pop('Review_number')

            row['URL'] = row['url']
            row.pop('url')
            res = es.index(index="scifi_books", id=unique_key, document=row)