from typing import List

import pytest
from dataclasses import dataclass

# @pytest.mark.asyncio
import requests

from consts import RANDOMMER_API_NAME_URL, RANDOMMER_HEADER, FIRSTNAME, NAME_TYPE, BAD_REQUEST, OK, \
    UNAUTHORIZED, UNAUTHORIZED_MESSAGE, BAD_REQUEST_MESSAGE, ERROR_MESSAGE, QUANTITY, AGE_API, NAME, GENDER_API, \
    NATIONALITY_API, AGE, GENDER, NATIONALITY, NATIONALITY_HIGHEST_PROBABILITY_INDEX, COUNTRY, COUNTRY_ID


@dataclass
class Person:
    name: str = None
    age: int = 0
    gender: str = None
    nationality: str = None


class TestPersonsApi:
    """

    """

    def setup_class(self):
        """
        """
        persons_names = self._generate_persons_names(self)
        self.persons = self.generate_persons_data(self, persons_names)

    def setup_method(self):
        """
        """

    def teardown_method(self):
        """
        """

    def teardown_class(self):
        """
        """

    def test_a(self):
        print(self.persons)

    def _generate_persons_names(self, quantity: int = 5) -> list:
        """
        Generate random names of persons via Randommer API.

        :param quantity: Number of names
        :return: List of persons names.
        """
        res = requests.get(RANDOMMER_API_NAME_URL, headers=RANDOMMER_HEADER, params={NAME_TYPE: FIRSTNAME,
                                                                                     QUANTITY: quantity})
        if res.status_code == OK:
            return res.json()
        elif res.status_code == BAD_REQUEST:
            print(BAD_REQUEST_MESSAGE)
        elif res.status_code == UNAUTHORIZED:
            print(UNAUTHORIZED_MESSAGE)
        else:
            print(ERROR_MESSAGE.format(status_code=res.status_code))

    def generate_persons_data(self, persons_names: list) -> List[Person]:
        """
        Get age, gender and nationality for each person and store the data on list with Person objects.

        :param persons_names: List of persons names.
        :return: List of Person objects.
        """
        persons = []
        for name in persons_names:
            person = Person()
            person.name = name
            person.age = self.get_person_data(self, name, AGE)
            person.gender = self.get_person_data(self, name, GENDER)
            person.nationality = self.get_person_data(self, name, NATIONALITY)
            persons.append(person)

        return persons

    def get_person_data(self, name: str, data_type: str):
        """
        Get data from Api about a person.
        :param name: Name of a person.
        :param data_type: Age or gender or nationality.
        :return:
        """
        if data_type == AGE or data_type == GENDER:
            api_url = AGE_API if data_type == AGE else GENDER_API
            return requests.get(api_url, params={NAME: name}).json().get(data_type)
        elif data_type == NATIONALITY:
            try:
                return requests.get(NATIONALITY_API, params={NAME: name}).json().get(COUNTRY) \
                    [NATIONALITY_HIGHEST_PROBABILITY_INDEX][COUNTRY_ID]
            except IndexError:
                return None
