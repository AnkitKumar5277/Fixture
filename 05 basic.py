import pytest

@pytest.fixture()
def launch_browser():
    print("Browser Launched")
    return

@pytest.fixture()
def close_browser():
    print("Browser Closed")
    return

def test_selenium(launch_browser, close_browser):
    print("Do Tc")

# इस कोड में `pytest` का इस्तेमाल किया गया है, जिसमें दो fixtures बनाए गए हैं – `launch_browser()` और `close_browser()`।
# Is code mein `@pytest.fixture()` ka use karke do functions define kiye gaye hain – `launch_browser()` aur `close_browser()`. 
# Jab `test_selenium()` run hota hai, tab ye dono fixtures automatically call ho jaate hain. 
# Pehle `launch_browser()` execute hota hai, jismein "Browser Launched" print hota hai.
# Fir `test_selenium()` ka main body execute hota hai jismein "Do Tc" print hota hai. 
# Last mein `close_browser()` execute hota hai, jismein "Browser Closed" print hota hai. 
# Fixtures testing setup aur teardown ke liye use hote hain. Lekin yahan teardown (close) automatic nahi chal raha, 
# kyunki pytest fixture ko return ya yield ke through properly manage nahi kiya gaya hai.
