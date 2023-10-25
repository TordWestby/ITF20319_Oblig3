from isLeapYear import isLeapYear

def test_leap_year_dividable_by_4_but_not_100():
    assert isLeapYear(2004) == True
    assert isLeapYear(2008) == True
    assert isLeapYear(2012) == True
    assert isLeapYear(2016) == True
    assert isLeapYear(2020) == True

def test_leap_year_dividable_by_400():
    assert isLeapYear(2000) == True
    assert isLeapYear(400) == True
    assert isLeapYear(800) == True
    assert isLeapYear(1600) == True
    

def test_non_leap_year_not_dividable_by_4():
    assert isLeapYear(2005) == False
    assert isLeapYear(2007) == False
    assert isLeapYear(2009) == False
    assert isLeapYear(2011) == False

def test_non_leap_year_dividable_by_100_but_not_400():
    assert isLeapYear(1700) == False

def test_leap_year_dividable_by_4000():
    assert isLeapYear(8000) == False
