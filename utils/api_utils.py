'''
Utilities to perform api related operations

    Author: Sachin Chaudhary
    Created on: 29th Dec 2021
    Last Modified on: 29th Dec 2021
'''

import requests
import config


class ApiUtils:
    '''api utilities class'''

    def call_endpoint(self, endpoint=config.star_data_endpoint):
        '''Calls the endpoint and returns the json formatted data.
            Parameters
            ----------
            endpoint : string
                Endpoint to call. Default is picked from config.py.

            Returns
            -------
            string
                Response returned by the endpoint.'''

        return requests.get(endpoint).json()

    def validate_response_schema(self,data):
        '''Validates that the passed data conforms to the expected schema.
            Parameters
            ----------
            data : string
                api response data.

            Returns
            -------
            boolean
                Returns 'True' if schema matches else 'False' is returned.'''
        validate_result = [self.validate_keys(data), self.validate_signature_key(data)]
        if False in validate_result:
            return False
        else:
            return True

    def validate_keys(self, data):
        '''Validates that the passed data conforms to the expected schema.
            Parameters
            ----------
            data : string
                api response data.

            Returns
            -------
            boolean
                Returns 'True' if schema matches else 'False' is returned.'''
        keys_list = list(data.keys())
        expected_keys_list = ['signature', 'count', 'fields', 'data']
        return True if keys_list == expected_keys_list else False

    def validate_signature_key(self, data):
        '''Validates that the passed data conforms to the expected schema.
            Parameters
            ----------
            data : string
                api response data.

            Returns
            -------
            boolean
                Returns 'True' if schema matches else 'False' is returned.'''
        keys_list = list(data.get('signature').keys())
        expected_keys_list = ['source', 'version']
        return True if keys_list == expected_keys_list else False
