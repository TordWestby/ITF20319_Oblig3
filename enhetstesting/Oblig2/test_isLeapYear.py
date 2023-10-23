from Oblig2.isLeapYear import isLeapYear

def test_leap_year_dividable_by_4_but_not_100():
    assert isLeapYear(2004) == True

def test_leap_year_dividable_by_400():
    assert isLeapYear(2000) == True

def test_non_leap_year_not_dividable_by_4():
    assert isLeapYear(2005) == False

def test_non_leap_year_dividable_by_100_but_not_400():
    assert isLeapYear(1700) == False

def test_leap_year_dividable_by_4000():
    assert isLeapYear(8000) == False
