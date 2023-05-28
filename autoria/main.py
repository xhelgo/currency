import csv
import random
from time import sleep

import requests
from bs4 import BeautifulSoup

from sql_writer import autoria_sql_writer


def random_sleep():
    sleep(random.randint(1, 5))


def get_page_content(page: int, size: int = 100) -> str:
    query_parameters = {
        'indexName': 'auto,order_auto,newauto_search',
        'country.import.usa.not': '-1',
        'price.currency': 1,
        'abroad.not': '-1',
        'custom.not': '-1',
        'page': page,
        'size': size
    }
    base_url = 'https://auto.ria.com/uk/search/'
    response = requests.get(base_url, params=query_parameters)
    response.raise_for_status()
    return response.text


def get_car_features(slug: str) -> dict:
    base_url = 'https://auto.ria.com/uk'
    response = requests.get(base_url + slug)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, features="html.parser")

    if not soup.find("div", {"id": "autoDeletedTopBlock"}):

        technical_info = soup.find("div", {"class": "technical-info"})

        labels = technical_info.find_all("span", {"class": "label"})[:3]
        arguments = technical_info.find_all("span", {"class": "argument"})[:3]

        car_features = dict(
            zip(
                [label.get_text() for label in labels],
                [argument.get_text() for argument in arguments]
            )
        )
    else:
        car_features = {}

    return car_features


class CSVWriter:
    def __init__(self, filename, headers=None):
        self.filename = filename
        self.headers = headers

        if self.headers:
            with open(self.filename, 'w', encoding='UTF8') as f:
                writer = csv.writer(f)
                writer.writerow(self.headers)

    def write(self, row: list):
        with open(self.filename, 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(row)


def main():

    writers = [
        CSVWriter('cars.csv', ['car_id', 'data_link_to_view', 'model and year', 'engine', 'color']),
        CSVWriter('cars_no_header.csv')
    ]

    page = 2450

    while True:

        print(f"Page: {page}")

        page_content = get_page_content(page)

        page += 1

        soup = BeautifulSoup(page_content, features="html.parser")

        search_results = soup.find("div", {"id": "searchResults"})
        ticket_items = search_results.find_all("section", {"class": "ticket-item"})

        if not ticket_items:
            break

        for ticket_item in ticket_items:
            car_details = ticket_item.find("div", {"class": "hide"})
            car_id = car_details["data-id"]
            data_link_to_view = car_details["data-link-to-view"]
            car_features = get_car_features(data_link_to_view)

            for writer in writers:
                info_to_write = [car_id, data_link_to_view] + list(car_features.values())
                writer.write(info_to_write)

        random_sleep()

    autoria_sql_writer()


if __name__ == '__main__':
    main()
