#!/usr/bin/env python
import fire
import requests

CARD_FACES = "card_faces"
DATA = "data"
DOLLAR_SIGN = "$"
EMPTY_STRING = ""
FORWARD_SLASH = "/"
FUZZY_SEARCH = "https://api.scryfall.com/cards/named?fuzzy=%s"
LAYOUT = "layout"
MANA_COST = "mana_cost"
MELD = "meld"
NAME = "name"
NEW_LINE = "\n"
NORMAL = "normal"
NOT_AVAILABLE = "N/A"
ORACLE_TEXT = "oracle_text"
PARENTHESIS_LEFT = "("
PARENTHESIS_RIGHT = ")"
PLUS = "+"
PRICES = "prices"
PRINTS_SEARCH_URI = "prints_search_uri"
SAGA = "saga"
SET = "set"
SET_NAME = "set_name"
SPACE = " "
SPLIT = "split"
TAB = "\t"
TRANSFORM = "transform"
TRANSFORM_LINE_BREAK = "---------"
USD = "usd"
USD_FOIL = "usd_foil"


class Card:

    @staticmethod
    def search(*args):
        plus_delimited_card_name = Card.__get_plus_delimited_card_name(*args)

        response = requests.get(FUZZY_SEARCH % plus_delimited_card_name)
        card_layout = Card.__get_card_layout(response)

        # TODO: Refactor this logic into its own print method.
        print(Card.__get_card_name(response) + TAB + TAB +
              Card.__get_card_mana_cost(response, card_layout) + NEW_LINE)
        print(Card.__get_card_description(response, card_layout) + NEW_LINE)

    @staticmethod
    def price(*args):
        plus_delimited_card_name = Card.__get_plus_delimited_card_name(*args)

        response = requests.get(FUZZY_SEARCH % plus_delimited_card_name)
        card_layout = Card.__get_card_layout(response)

        print(Card.__get_card_name(response) + TAB + TAB +
              Card.__get_card_mana_cost(response, card_layout) + NEW_LINE)

        # TODO: Move this to a separate method that only brings up a card's price.
        for set_name, card_prices_usd in Card.__get_card_set_names(response).items():
            normal_price = None
            foil_price = None

            print(TAB + set_name)

            if not card_prices_usd[0] is None:
                normal_price = card_prices_usd[0]
            else:
                normal_price = NOT_AVAILABLE

            if not card_prices_usd[1] is None:
                foil_price = card_prices_usd[1]
            else:
                foil_price = NOT_AVAILABLE

            print(TAB + TAB + DOLLAR_SIGN + normal_price + SPACE + FORWARD_SLASH + SPACE + DOLLAR_SIGN + foil_price)

    @staticmethod
    def __get_card_description(response, card_layout):
        description = EMPTY_STRING

        if card_layout == NORMAL or card_layout == MELD or card_layout == SAGA:
            description = response.json()[ORACLE_TEXT]
        elif card_layout == TRANSFORM or card_layout == SPLIT:
            front_description = response.json()[CARD_FACES][0][ORACLE_TEXT]
            back_description = response.json()[CARD_FACES][1][ORACLE_TEXT]

            description = front_description + NEW_LINE + TRANSFORM_LINE_BREAK + NEW_LINE + back_description

        return description

    @staticmethod
    def __get_card_name(response):
        return response.json()[NAME]

    # TODO: Refactor this method name into something else since it is technically getting both set and prices.
    @staticmethod
    def __get_card_set_names(response):
        card_set_list = dict()
        prints_search_uri = response.json()[PRINTS_SEARCH_URI]

        card_sets_response = requests.get(prints_search_uri)

        for json in card_sets_response.json()[DATA]:
            set_name = json[SET_NAME]
            set_code = json[SET].upper()
            normal_price = json[PRICES][USD]
            foil_price = json[PRICES][USD_FOIL]

            set_name = set_name + SPACE + PARENTHESIS_LEFT + set_code + PARENTHESIS_RIGHT

            card_set_list.update({set_name: [normal_price, foil_price]})

        return card_set_list

    @staticmethod
    def __get_card_mana_cost(response, card_layout):
        mana_cost = EMPTY_STRING

        if card_layout == NORMAL or card_layout == MELD or card_layout == SAGA:
            mana_cost = response.json()[MANA_COST]
        elif card_layout == TRANSFORM:
            mana_cost = response.json()[CARD_FACES][0][MANA_COST]
        elif card_layout == SPLIT:
            mana_cost = response.json()[CARD_FACES][0][MANA_COST] + \
                        SPACE + FORWARD_SLASH + FORWARD_SLASH + SPACE + response.json()[CARD_FACES][1][MANA_COST]

        return mana_cost

    @staticmethod
    def __get_plus_delimited_card_name(*args):
        plus_delimited_card_name = EMPTY_STRING

        for index, argument in enumerate(args):
            if index == len(args) - 1:
                plus_delimited_card_name = plus_delimited_card_name + argument
            else:
                plus_delimited_card_name = plus_delimited_card_name + argument + PLUS

        return plus_delimited_card_name

    @staticmethod
    def __get_card_layout(response):
        return response.json()[LAYOUT]

    # TODO: Implement a str() method to print the card information out.


if __name__ == '__main__':
    fire.Fire(Card)
