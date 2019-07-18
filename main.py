#!/usr/bin/env python
import fire
import requests

DATA = "data"
NAME = "name"
PRINTS_SEARCH_URI = "prints_search_uri"
SET_NAME = "set_name"


class Card:

    @staticmethod
    def search(name):
        # TODO: Need to figure out how to deal with spaces.
        response = requests.get("https://api.scryfall.com/cards/named?fuzzy=%s" % name)

        # TODO: Maybe consider refactoring the print items into a separate method or at least pretty it up with tabs.
        print(Card.__get_card_name(response))

        for set_name in Card.__get_card_set_names(response):
            print("\t" + set_name)

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


if __name__ == '__main__':
    fire.Fire(Card)
