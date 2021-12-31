'''
Utilities to perform api related operations

    Author: Sachin Chaudhary
    Created on: 29th Dec 2021
    Last Modified on: 29th Dec 2021
'''
import json
import jsonschema
import requests
import config, utils.api_schemas as expected_schemas


class ReqResApiUtils:
    '''api utilities class'''

    def list_users(self):
        r"""Sends a GET request to create list users on the server.
            :return: json formatted response
            """

        response = requests.get(url=config.reqres_url+config.reqres_users_path_param)
        return json.loads(response.text)

    def create_user(self, name, job):
        r"""Sends a POST request to create a new user on the server.

            :param name: name of the user to be created.
            :param job: job of the user
            :return: json formatted response
            """

        response = requests.post(url=config.reqres_url + config.reqres_users_path_param,
                                 data={"name": name, "job": job})
        return json.loads(response.text)

    def validate_list_users_response_schema(self, data):

        try:
            jsonschema.validate(instance=data, schema=expected_schemas.reqres_list_users_schema)
        except jsonschema.exceptions.ValidationError:
            return False
        return True

    def validate_create_user_response_schema(self, data):

        try:
            jsonschema.validate(instance=data, schema=expected_schemas.reqres_create_user_schema)
        except jsonschema.exceptions.ValidationError:
            return False
        return True

    def verify_user_in_list_users(self, user_data_dict, response):
        users = response.get('data')
        found = False
        for user in users:
            if user == user_data_dict:
                found = True
        return found

    def verify_user_in_create_user(self, name, job, response):
        if response.get('name') == name and response.get('job') == job:
            return True
        else:
            return False


    def save_response_to_file(self, response_data, location='response.json'):
        json_object = json.dumps(response_data, indent=4)
        with open(location, 'w') as response:
            response.write(str(json_object))

    def compare_response_to_expected(self, response, expected_file):
        self.save_response_to_file(response,
                                   expected_file)
        expected_file = open(expected_file)
        expected_json = json.load(expected_file)
        expected_file.close()
        if response == expected_json:
            return True
        else:
            return False
