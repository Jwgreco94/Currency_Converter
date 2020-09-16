"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Jonathan Greco
Date:   9/6/2020
"""

import introcs
import currency


def test_before_space():
    """Test procedure for before_space"""
    print('Testing before_space')
    
    #Test Case #1
    result = currency.before_space('Hello World')
    introcs.assert_equals('Hello',result)
    
    #Test Case #2
    result = currency.before_space('Hello  World')
    introcs.assert_equals('Hello',result)
    
    #Test Case #3
    result = currency.before_space(' Hello')
    introcs.assert_equals('',result)
    
    #Test Case #4
    result = currency.before_space('He llo World')
    introcs.assert_equals('He',result)
    
    
def test_after_space():
    """Test procedure for after_space"""
    print('Testing after_space')
    
    #Test Case #1
    result = currency.after_space('Hello World')
    introcs.assert_equals('World',result)
    
    #Test Case #2
    result = currency.after_space('Hello  World')
    introcs.assert_equals(' World',result)
    
    #Test Case #3
    result = currency.after_space('Hello ')
    introcs.assert_equals('',result)
    
    #Test Case #4
    result = currency.after_space('He llo World')
    introcs.assert_equals('llo World',result) 
    

def test_first_inside_quotes():
    """Test procedure for first_inside_quotes"""
    print('Testing first_inside_quotes')
    
    #Test Case #1
    result = currency.first_inside_quotes('Hello "World"')
    introcs.assert_equals('World',result)
    
    #Test Case #2
    result = currency.first_inside_quotes('""Hello World""')
    introcs.assert_equals('',result)
    
    #Test Case #3
    result = currency.first_inside_quotes('" "')
    introcs.assert_equals(' ',result)
    
    #Test Case #4
    result = currency.first_inside_quotes('"Hello" "World"')
    introcs.assert_equals('Hello',result) 
    
    
def test_get_src():
    """Test procedure for get_src"""
    print('Testing get_src')
    
    #Test Case #1
    result = currency.get_src('{"success":false,'+
                              '"src":"","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals('',result)
    
    #Test Case #2
    result = currency.get_src('{"success": false,'+
                              '"src": "","dst": "","error":"Source currency code is invalid."}')
    introcs.assert_equals('',result)
    
    #Test Case #3
    result = currency.get_src('{"success": true,'+
                              ' "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars',result)
    
    #Test Case #4
    result = currency.get_src('{"success":true,'+
                              ' "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('2 United States Dollars',result)
    
    
def test_get_dst():
    """Test procedure for get_dst"""
    print('Testing get_dst')
    
    #Test Case #1
    result = currency.get_dst('{"success": true,'+
                              ' "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros',result)
    
    #Test Case #2
    result = currency.get_dst('{"success":false,'+
                              '"src":"","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals('',result)
    
    #Test Case #3
    result = currency.get_dst('{"success":true,'+
                              ' "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('1.772814 Euros',result)
    
    #Test Case #4
    result = currency.get_dst('{"success": false,'+
                              '"src": "","dst": "","error": "Source currency code is invalid."}')
    introcs.assert_equals('',result)
    
    
def test_has_error():
    """Test procedure for has_error"""
    print('Testing has_error')
    
    #Test Case #1
    result = currency.has_error('{"success":false,'+
                                '"src":"","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals(True,result)
    
    #Test Case #2
    result = currency.has_error('{"success": true,'+
                                ' "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals(False,result)
    
    #Test Case #3
    result = currency.has_error('{"success":true,'+
                                ' "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals(False,result)
    
    #Test Case #4
    result = currency.has_error('{"success": false,'+
                                '"src": "","dst": "","error": "Source currency code is invalid."}')
    introcs.assert_equals(True,result)
    
    
def test_service_response():
    """Test procedure for service_response"""
    print('Testing service_response')
    
    #Test Case #1
    result = currency.service_response('USD','EUR',2.5)
    introcs.assert_equals('{"success": true, "src": "2.5 United States Dollars",'+
                          ' "dst": "2.2160175 Euros", "error": ""}',result)
    
    #Test Case #2
    result = currency.service_response('USD','EUR',-2.5)
    introcs.assert_equals('{"success": true, "src": "-2.5 United States Dollars",'+
                          ' "dst": "-2.2160175 Euros", "error": ""}',result)
    
    #Test Case #3
    result = currency.service_response('US','EUR',2.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error":'+
                          ' "The rate for currency US is not present."}',result)
    
    #Test Case #4
    result = currency.service_response('USD','EU',2.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error":'+
                          ' "The rate for currency EU is not present."}',result)
    
    
def test_iscurrency():
    """Test procedure for iscurrency"""
    print('Testing iscurrency')
    
    #Test Case #1
    result = currency.iscurrency('USD')
    introcs.assert_equals(True,result)
    
    #Test Case #2
    result = currency.iscurrency('US')
    introcs.assert_equals(False,result)
    
    
def test_exchange():
    """Test procedure for exchange"""
    print('Testing exchange')
    
    #Test Case #1
    result = currency.exchange('USD','EUR',-2.5)
    introcs.assert_floats_equal(-2.2160175,result)
    
    #Test Case #2
    result = currency.exchange('EUR','USD',2.5)
    introcs.assert_floats_equal(2.8203748390976155,result)
    
    
# Function Calls
test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()
print("All tests completed successfully.")