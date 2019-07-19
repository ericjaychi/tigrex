#!/usr/bin/env python
import fire
import requests

DATA = "data"
DOLLAR_SIGN = "$"
EMPTY_STRING = ""
FORWARD_SLASH = "/"
FUZZY_SEARCH = "https://api.scryfall.com/cards/named?fuzzy=%s"
NAME = "name"
PLUS = "+"
PRICES = "prices"
PRINTS_SEARCH_URI = "prints_search_uri"
SET_NAME = "set_name"
SPACE = " "
TAB = "\t"
USD = "usd"
USD_FOIL = "usd_foil"


class Card:

    @staticmethod
    def search(*args):
        plus_delimited_card_name = Card.__get_plus_delimited_card_name(*args)

        response = requests.get(FUZZY_SEARCH % plus_delimited_card_name)

        # TODO: Refactor all the print statements into a separate method.
        print(Card.__get_card_name(response))

        for set_name, card_prices_usd in Card.__get_card_set_names(response).items():
            normal_price = None
            foil_price = None

            print(TAB + set_name)

            if not card_prices_usd[0] is None:
                normal_price = card_prices_usd[0]
            else:
                normal_price = "N/A"

            if not card_prices_usd[1] is None:
                foil_price = card_prices_usd[1]
            else:
                foil_price = "N/A"

            print(TAB + TAB + DOLLAR_SIGN + normal_price + SPACE + FORWARD_SLASH + SPACE + DOLLAR_SIGN + foil_price)

    @staticmethod
    def __get_card_name(response):
        return response.json()[NAME]

    @staticmethod
    def __get_card_set_names(response):
        card_set_list = dict()
        prints_search_uri = response.json()[PRINTS_SEARCH_URI]

        card_sets_response = requests.get(prints_search_uri)

        for json in card_sets_response.json()[DATA]:
            set_name = json[SET_NAME]
            normal_price = json[PRICES][USD]
            foil_price = json[PRICES][USD_FOIL]

            card_set_list.update({set_name: [normal_price, foil_price]})

        return card_set_list

    @staticmethod
    def __get_plus_delimited_card_name(*args):
        plus_delimited_card_name = EMPTY_STRING

        for index, argument in enumerate(args):
            if index == len(args) - 1:
                plus_delimited_card_name = plus_delimited_card_name + argument
            else:
                plus_delimited_card_name = plus_delimited_card_name + argument + PLUS

        return plus_delimited_card_name


if __name__ == '__main__':
    fire.Fire(Card)
