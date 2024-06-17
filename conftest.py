import pytest
from modules.api.clients.github import GitHub
from faker import Faker
from modules.common.database import Database

fake = Faker()


class User:
    def __init__(self):
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Dana"
        self.second_name = "Stoliarchuk"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()
    yield user

    user.remove()

@pytest.fixture
def db():
    db = Database()
    yield db

@pytest.fixture
def github_api_client():
    api = GitHub()
    yield api


@pytest.fixture
def create_random_product():
    yield {
        "product_id": fake.random_int(),
        "name": fake.name(),
        "description": fake.last_name(),
        "qnt": fake.random_int()
    }


@pytest.fixture
def update_product_quantity():
    yield {
        "product_id": fake.random_int(),
        "qnt": fake.random_int()
    }