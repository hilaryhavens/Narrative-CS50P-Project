import pytest
from project import format_check, inum_count, nar_type


def test_format_check():
    assert format_check("test.txt") == True
    assert format_check("test") == None
    assert (
        format_check("https://www.gutenberg.org/cache/epub/6346/pg6346-images.html")
        == True
    )
    assert format_check("tenberg.org/123") == None


def test_inum_count():
    assert inum_count(" I am feeling good. I am happy.") == 2
    assert inum_count("What I've got to do.") == 1
    assert inum_count("The crows and clouds are circling in the sky.") == 0


def test_nar_type():
    assert nar_type(0.024) == "ambiguously first-person or epistolary"
    assert nar_type(0.001) == "unlikely first-person or epistolary"
    assert nar_type(0.03) == "probably first-person or epistolary"
