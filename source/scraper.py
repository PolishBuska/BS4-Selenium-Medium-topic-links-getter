"""Factory function to get a bs4 object"""

from bs4 import BeautifulSoup


def bs4_factory(source):
    """source: html content"""
    return BeautifulSoup(source, 'lxml')
