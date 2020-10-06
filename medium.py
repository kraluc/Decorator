#!/bin/env python

import requests
import json
from functools import wraps
import unittest

from api import API

URL_BASE = "https://api.publicapis.org"
URL_GET_CATEGORY = 'entries'
URL_GET_RANDOM = 'random'
URL_GET_ALL_CATEGORIES = 'categories'

# Defines
def disableAPIcall(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        flagValue = self.objAIP.enableAPICall
        self.objAPI.enableAPICall = False
        print('Disabling API calls...')
        retVal = func(self, *args, **kwargs)
        print('Re-enabling API calls...')
        self.objAPI.enableAPICall = flagValue
        return retVal
    return wrapper


def disableStdout(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        stdOut = self.API.objAPI.enableStdout
        self.objAPI.enableStdout = False
        print('Disabling class STDOUTs...')
        retVal = func(self, *args, **kwargs)
        print('Re-enabling class STDOUTs...')
        self.objAPI.enableStdout = stdOut
        return retVal
    return wrapper


class test_API(unittest.TestCase):
    def setUp(self):
        print('\n---------------------------')
        self.objAPI = API()

    @disableAPICall
    @disableStdout
    def testConfig_getRandom(self):
        print('Testing config: getRandom')
        self.objAPI.getRandom()
        self.assertEqual(self.objAPI.apiURL,'https://api.publicapis.org/random')
        self.assertDictEqual(self.objAPI.apiPayload, {'auth' : 'null' })


    @disableAPICall 
    @disableStdout
    def testConfig_getAllCategories(self):
        print('Testing config: getAllCategories')
        self.objAPI.getAllCategories()
        self.assertEqual(self.objAPI.apiURL, 'https://api.publicapis.org/categories')

    @disableAPICall 
    @disableStdout 
    def testConfig_getEntry(self):
        print('Testing config with category: Business')
        self.objAPI.getEntry('business')
        self.assertEqual(self.objAPI.apiURL, 'https://api.publicapis.org/entries'
        self.assertDictEqual(self.objAPI.apiPayload,{'category':'business', 'https':True})

    def testResponse_getAllCategories(self):
        print('Testing response: getAllCategories')
        categories = self.objAPI.getAllCategories()
        print(' - Validating number of categories returned = 46')
        self.assertEqual(len(categories),46)

    @disableStdout
    def testResponse_getEntry_Business(self):
        print('Testing response for category: Business')
        self.objAPI.getEntry('business')
        responseJSON = json.loads(self.objAPI.response.text)
        print(' - Asserting keys in response JSON...')
        self.assertIn('count', responseJSON.keys())
        self.assertIn('entries', responseJSON.keys())


class API:
    def __init__(self):
        print('Setting up API...')

        # control Parameters
        self.enableAPICall = True
        self.enableStdout = True

        # API Parameters
        self.apiURL = None
        self.apiHeader = None
        self.apiPayLoad = None
        self.response = None

        
    def getEntry(self, categoryName):
        if self.enableStdout:
            print('\nFetching Category:', categoryName)
        self.apiURL = URL_BASE + URL_GET_CATEGORY
        self.apiPayLoad = {'category': categoryName, 'https': True}

        if self.enableAPICall is True:
            self.response = requests.get(url=self.apiURL, params=self.apiPayLoad)
            responseJSON = json.loads(self.response.text)
            for key, value in responseJSON.items():
                if self.enableStdout:
                    print(' -', key, '=', value)


if __name__ == "__main__":
    unittest.main()