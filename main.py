#!/usr/bin/env python
import fire
import requests

DATA = "data"
DOLLAR_SIGN = "$"
FORWARD_SLASH = "/"
FUZZY_SEARCH = "https://api.scryfall.com/cards/named?fuzzy=%s"
NAME = "name"
PRICES = "prices"
PRINTS_SEARCH_URI = "prints_search_uri"
SET_NAME = "set_name"
SPACE = " "
TAB = "\t"
USD = "usd"
USD_FOIL = "usd_foil"


class Card:

    @staticmethod
    def search(name):
        # TODO: Need to figure out how to deal with spaces.
        response = requests.get(FUZZY_SEARCH % name)

        # TODO: Refactor all the print statements into a separate method.
        print(Card.__get_card_name(response))

        card_price_usd = TAB + TAB + DOLLAR_SIGN + Card.__get_card_prices_usd(response) + \
                         SPACE + FORWARD_SLASH + SPACE + DOLLAR_SIGN + Card.__get_card_prices_usd_foil(response)

        for set_name in Card.__get_card_set_names(response):
            print(TAB + set_name)
            print(card_price_usd)

    @staticmethod
    def __get_card_name(response):
        return response.json()[NAME]

    @staticmethod
    def __get_card_set_names(response):
        card_set_list = []
        prints_search_uri = response.json()[PRINTS_SEARCH_URI]

        card_sets_response = requests.get(prints_search_uri)

        for json in card_sets_response.json()[DATA]:
            card_set_list.append(json[SET_NAME])

        return card_set_list

    # TODO: This will need to account for each individual price of the card from whichever set its from.
    @staticmethod
    def __get_card_prices_usd(response):
        return response.json()[PRICES][USD]

    @staticmethod
    def __get_card_prices_usd_foil(response):
        return response.json()[PRICES][USD_FOIL]


if __name__ == '__main__':
    fire.Fire(Card)
