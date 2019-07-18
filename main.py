#!/usr/bin/env python
import fire
import requests


class Card:

    @staticmethod
    def search(name):
        # TODO: Need to figure out how to deal with spaces.
        response = requests.get("https://api.scryfall.com/cards/named?fuzzy=%s" % name)

        return response.json()['name']


if __name__ == '__main__':
    fire.Fire(Card)
