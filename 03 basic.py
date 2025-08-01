import pytest

@pytest.fixture()
def create_token():
    return "abc"

@pytest.fixture()
def create_booking_id():
    return 123

def test_update_req_1(create_token, create_booking_id):
    print("Token ->", create_token)
    print("Booking ID -> ", create_booking_id)

# Is code mein hum pytest ka use kar rahe hain testing ke liye. Yahaan fixture ek special function hota hai 
# jo test case chalne se pehle kuch data ya setup provide karta hai.
# 🔹 @pytest.fixture() decorator se create_token() aur create_booking_id() functions define kiye gaye hain.
# 🔹 create_token() function "abc" return karta hai aur create_booking_id() 123 return karta hai.
# 🔹 test_update_req_1() ek test function hai jo in dono fixtures ka use karta hai.
# 🔹 Test ke dauraan print() ke through token aur booking ID screen par show ki jati hai.
# Fixtures se reusable test data milta hai, aur code clean rehta hai.
