import pytest
@pytest.fixture()
def is_married_before_run():
    return True

def test_update(is_married_before_run):
    assert is_married_before_run == False      

# Is code mein `@pytest.fixture()` ek **fixture function** banata hai jiska naam hai `is_married_before_run`. 
# Ye function test se pehle automatically chalega aur `True` return karega. 
# Fir `test_update` naam ka test function likha gaya hai jo `is_married_before_run` ko input leta hai.
# Lekin test ke andar `assert is_married_before_run == False` likha hai, jo galat hai, 
# kyunki fixture `True` return karta hai. Is wajah se test fail hoga. Ye code mainly yeh dikhata hai ki **fixture se value kaise pass hoti hai**,
# aur agar expected value match nahi karti, to test kaise fail hota hai. Ye pytest mein reuse ke liye helpful hota hai.

