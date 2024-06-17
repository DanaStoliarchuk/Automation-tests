import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection(db):
    assert db.test_connection() is not None


@pytest.mark.database
def test_check_all_users(db: Database):
    users = db.get_all_users()

    assert len(users) != 0


@pytest.mark.database
def test_check_user_sergii(db: Database):
    user = db.get_user_address_by_name("Sergii")

    assert user.get("address") == "Maydan Nezalezhnosti 1"
    assert user.get("city") == "Kyiv"
    assert user.get("postalCode") == "3127"
    assert user.get("country") == "Ukraine"


@pytest.mark.database
def test_product_quantity_update(db: Database, update_product_quantity):
    db.update_product_qnt_by_id(**update_product_quantity)
    water_qnt = db.select_product_qnt_by_id(product_id=update_product_quantity.get("product_id"))

    assert water_qnt.get("quantity") == 2update_product_quantity.get("qnt")


@pytest.mark.database
def test_create_new_product(db: Database, create_random_product):
    db.add_new_product(**create_random_product)
    new_product = db.get_product_by_id(product_id=create_random_product.get("product_id"))

    assert new_product.get("id") == create_random_product.get("product_id")
    assert new_product.get("name") == create_random_product.get("name")
    assert new_product.get("description") == create_random_product.get("description")
    assert new_product.get("quantity") == create_random_product.get("qnt")


@pytest.mark.database
def test_get_all_data(db: Database):
    users = db.get_all_users()
    products = db.get_all_products()

    print(users)
    print(products)
