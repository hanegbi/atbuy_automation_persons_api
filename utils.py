from typing import List, Union

import requests
from person import Person

from consts import RANDOMMER_API_NAME_URL, NATIONALITY_HIGHEST_PROBABILITY_INDEX, NATIONALITY_API, COUNTRY_ID, NAME, \
    COUNTRY, AGE, AGE_API, NATIONALITY, GENDER_API, GENDER, OK, RANDOMMER_HEADER, DEFAULT_QUANTITY, NAME_TYPE, QUANTITY, \
    FIRSTNAME, BAD_REQUEST, BAD_REQUEST_MESSAGE, UNAUTHORIZED, UNAUTHORIZED_MESSAGE, ERROR_MESSAGE


def generate_persons_names(quantity: int = DEFAULT_QUANTITY) -> List[str]:
    """
    Generate random names of persons via Randommer API.

    :param quantity: Number of names.
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


def generate_persons_data(persons_names: list) -> List[Person]:
    """
    Get age, gender and nationality for each person and store the data on list with Person objects.

    :param persons_names: List of persons names.
    :return: List of Person objects.
    """
    persons_data = []
    for name in persons_names:
        person = Person()
        person.name = name
        person.age = get_person_data(name, AGE)
        person.gender = get_person_data(name, GENDER)
        person.nationality = get_person_data(name, NATIONALITY)
        persons_data.append(person)

    return persons_data


def get_person_data(name: str, data_type: str) -> Union[str, int]:
    """
    Get data from Api about a person.

    :param name: Name of a person.
    :param data_type: Age or gender or nationality.
    :return: Age or gender or nationality.
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
