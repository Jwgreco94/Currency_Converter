"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Jonathan Greco
Date:   09/06/2020
"""

import introcs

# Create global variable to hold the API key.
APIKEY = 'InLoHFJsp52kVNRMsMp2w5boLodI0CB2HnO6tTDI4uge'


def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    
    # Enforce the precondition
    assert type(s) == str, repr(s)+' is not a string'
    assert ' ' in s, repr(s)+' is missing a space'
    
    # Get the position of the first space.
    pos = introcs.find_str(s,' ')
    
    # Slice the string.
    before = s[:pos]
    
    # Return the value.
    return before


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    
    # Enforce the precondition
    assert type(s) == str, repr(s)+' is not a string'
    assert ' ' in s, repr(s)+' is missing a space'
    
    # Get the position of the first space.
    pos = introcs.find_str(s,' ')
    
    # Slice the string.
    after = s[pos+1:]
    
    # Return the value.
    return after


def double_quotes(s):
    """
    Returns True if the string s contains two quotation marks.

    Double quotation marks in a string is defined of containing two quotation
    characters in a string. Anything can be inbetween the two quoation marks.

    Example: double_quotes('"Hello World"') returns True
    Example: double_quotes('"Hello World' returns False

    Parameter s: The string to check
    Precondition: s is a string (possibly empty)
    """
    
    # Enforce the precondition
    assert type(s) == str, repr(s)+' is not a string'
    
    # Search for the first quote '"'.
    cond1 = introcs.find_str(s, '"')
    
    # Search for the second quote '"' AFTER the first quote.
    cond2 = introcs.find_str(s, '"', cond1 + 1)
    
    # Compare both searches to -1 and return True if BOTH are not -1
    result = cond1 > -1 and cond2 > -1 and cond2 > cond1
    
    # Return result
    return result


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a 
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only 
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """
    
    # Enforce the precondition
    assert type(s) == str, repr(s)+' is not a string'
    assert double_quotes(s) == True, repr(s)+' is missing double quotation marks'
    
    # Find the first '"'.
    cond1 = introcs.find_str(s,'"')
    
    # Find the second '"' AFTER the first '"'.
    cond2 = introcs.find_str(s, '"', cond1 + 1)
    
    # Slice the string.
    result = s[cond1 + 1:cond2]
    
    # Return the string.
    return result


def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"src"'. For example,
    if the json is
    
        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '2 United States Dollars' (not '"2 United States Dollars"'). 
    On the other hand if the json is 
    
        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON
    
        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    
    # Enforce the precondition
    assert type(json) == str, repr(json)+' is not a JSON string!'
    
    # Find the first colon.
    cond1 = introcs.find_str(json, ':')
    
    # Find the second colon.
    cond2 = introcs.find_str(json, ':', cond1 + 1)
    
    # Find the third colon.
    cond3 = introcs.find_str(json, ':', cond2 + 1)
    
    # Slice the string.
    slice = json[cond2 + 1 :cond3]
    
    # Call first_inside_quotes function to retrieve src.
    src = first_inside_quotes(slice)
    
    # Return src.
    return src 


def get_dst(json):
    """
    Returns the dst value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"dst"'. For example,
    if the json is
    
        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
    hand if the json is 
    
        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON
    
        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    
    # Enforce the precondition
    assert type(json) == str, repr(json)+' is not a JSON string!'
    
    # Find the last colon.
    cond1 = introcs.rfind_str(json, ':')
    
    # Find the second to last colon.
    cond2 = introcs.rfind_str(json, ':', 0, cond1-1)
    
    # Slice the string.
    slice = json[cond2:cond1]
    
    # Call first_inside_quotes function to retrieve dst.
    dst = first_inside_quotes(slice)
    
    # Return dst.
    return dst


def has_error(json):
    """
    Returns True if the response to a currency query encountered an error.

    Given a JSON string provided by the web service, this function returns True if the
    query failed and there is an error message. For example, if the json is
    
        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns True (It does NOT return the error message 
    'Source currency code is invalid'). On the other hand if the json is 
    
        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns False.

    The web server does NOT specify the number of spaces after the colons. The JSON
    
        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    
    # Enforce the precondition
    assert type(json) == str, repr(json)+' is not a JSON string!'
    
    # Search json string for the substring 'false'.
    status = introcs.find_str(json,'false')
    
    # Compare string to -1 and return True if status is not equal to -1, otherwise return False.
    result = status > -1
    
    # Return result.
    return result
   
    
def check_string(s):
    """
    Returns True if s is a string that is not empty and contains only alphabetic characters.
    
    Parameter: A string to check
    Precondition: s is a string that is not empty. 
    """
    
    # Enforce the preconditions
    assert type(s) == str, repr(s)+' is not a string'
    assert len(s) > 0, repr(s)+ ' is an empty string'
    
    # Check if string contains alphabetic characters only.
    check1 = introcs.isalpha(s)
    
    # Return True if string contains only alphabetic characters.
    return check1


def service_response(src, dst, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the currency dst. The response 
    should be a string of the form

        '{"success": true, "src": "<src-amount>", dst: "<dst-amount>", error: ""}'

    where the values src-amount and dst-amount contain the value and name for the src 
    and dst currencies, respectively. If the query is invalid, both src-amount and 
    dst-amount will be empty, and the error message will not be empty.

    There may or may not be spaces after the colon.  To test this function, you should
    chose specific examples from your web browser.

    Parameter src: the currency on hand
    Precondition src is a nonempty string with only letters

    Parameter dst: the currency to convert to
    Precondition dst is a nonempty string with only letters

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    
    # Enforce Preconditions
    assert check_string(src), repr(src)+' has the wrong format'
    assert check_string(dst), repr(dst)+' has the wrong format'
    assert type(amt) == float or type(amt) == int, repr(amt) 
    +'must be a float or an int value'
    
    # Create a variable to hold the url. 
    url = 'https://ecpyfac.ecornell.com/python/currency/fixed?src=' + src + '&dst=' +\
    dst + '&amt=' + str(amt) + '&key=' + APIKEY
    
    # Call the urlread function to return a json string from the url.
    json = introcs.urlread(url)
    
    # Return the json string.
    return json


def iscurrency(currency):
    """
    Returns True if currency is a valid (3 letter code for a) currency.

    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a nonempty string with only letters
    """
    
    # Enforce preconditions
    assert check_string(currency), repr(currency)+' has the wrong format'
    
    # Create a variable to check if the currency contains three letters.
    check1 = len(currency) == 3
    
    # Create a json string by calling function service_response and using currency as the
    # default parmeters values for src and dst and a default of 1 for amt.
    json = service_response(currency, currency, 1)
    
    # Create a variable to check if the paramters passed into service_response has prompted an error.
    check2 = has_error(json) == False 
    
    # Return True if all checks have passed.
    return check1 and check2


def exchange(src, dst, amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency src to the currency 
    dst. The value returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter src: the currency on hand
    Precondition src is a string for a valid currency code

    Parameter dst: the currency to convert to
    Precondition dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    
    # Enforce Preconditions
    assert iscurrency(src), repr(src)+' is not a valid currency'
    assert iscurrency(dst), repr(dst)+' is not a valid currency'
    assert type(amt) == float or type(amt) == int, repr(amt)
    +' must be a float or an int value'
    
    # Create a json string by passing paramters to the function service_response.
    json = service_response(src, dst, amt)
    
    # Create a variable to hold the dst string from the json string.
    result = get_dst(json)
    
    # Find the position of a space character in the dst string.
    pos = introcs.find_str(result, ' ')
    
    # Slice the remaining characters after the space in the dst string.
    slice = result[:pos]
    
    # Convert the sliced string into a float.
    exchanged = float(slice)
    
    # Return the calculated exchanged results.
    return exchanged