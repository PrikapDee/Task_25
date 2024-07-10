from IMDB_PAGE import Imdb
import pytest

url = "https://www.imdb.com/search/name/"

imdb_obj1 = Imdb(url)


# Test to verify login functionality
def test_login():
    assert imdb_obj1.login() == True
    print("Test case Pass")


# test to verify search functionality

def test_search_name():
    assert imdb_obj1.search_name_Birthdate() == True
    print("Test case pass")
