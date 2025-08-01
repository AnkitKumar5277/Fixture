import pytest

@pytest.fixture()
def create_token():
    return "abc"

@pytest.fixture()
def create_booking_id():
    return 1

@pytest.fixture()
def read_excel_file():
    return "xyz"

def test_put(create_token, create_booking_id):
    print(create_token)
    print(create_booking_id)

def test_put_2(create_token, create_booking_id, read_excel_file):
    print(create_token)
    print(create_booking_id)
    print(read_excel_file)

# Is code mein **`pytest`** framework ka use kiya gaya hai jismein **fixtures** define kiye gaye hain. Fixtures test run se pehle kuch data ya setup provide karte hain.
# * `create_token()` fixture ek dummy token `"abc"` return karta hai.
# * `create_booking_id()` ek booking ID `1` return karta hai.
# * `read_excel_file()` ek file ka naam `"xyz"` return karta hai.
# Phir do test functions hain:
# 1. **`test_put()`**: ye `create_token` aur `create_booking_id` ko use karke unka print karta hai.
# 2. **`test_put_2()`**: ye teeno fixtures ko use karta hai aur unki values print karta hai.
# Fixtures automatically inject ho jaate hain test functions mein.
