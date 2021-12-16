import pytest

from consts import AGE, GENDER, NATIONALITY, PERSONS
from utils import generate_persons_names, generate_persons_data, get_person_data


class TestPersonsApi:
    """
    Validate the persons' data integrity against the APIs.
    """

    @pytest.fixture
    def generate_persons(self):
        """
        Generate random names of persons via Randommer API and then get data for each person.

        :return: List of Person objects.
        """
        persons_names = generate_persons_names()
        return generate_persons_data(persons_names)

    @pytest.mark.parametrize(PERSONS, [pytest.lazy_fixture("generate_persons")])
    def test_data_integrity(self, persons):
        """
        Validate if generated persons data are the same as Apis.

        :param persons: List of Person objects or list of person names.
        """
        if all(isinstance(p, str) for p in persons):
            persons = generate_persons_data(persons)

        for person in persons:
            name = person.name
            age = get_person_data(name, AGE)
            gender = get_person_data(name, GENDER)
            nationality = get_person_data(name, NATIONALITY)
            assert person.age == age and person.gender == gender and person.nationality == nationality
