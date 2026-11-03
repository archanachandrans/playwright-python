import pytest 


def test_username(user_data):
    assert user_data["username"] == "testuser"
    assert user_data["password"] == "test@123"
    username = "admin"
    assert username == "admin"

def test_values():
    assert 10 > 5
    assert "Python" in "Python playwright"
    assert 5 != 3
    assert  [1,2,3] == [1,2,3]



# @pytest.mark.parametrize(
#     "number, expected",
#     [
#         (2, 4),
#         (3, 9),
#         (4, 16)
#     ]
# )
# def test_square(number, expected):
#     assert number * number == expected

# #Markers -- Organise tests into categories

@pytest.mark.smoke
@pytest.mark.regression
def test_smoke():
    number = 3
    assert number == 3