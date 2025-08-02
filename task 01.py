# 1. Verify that Create Booking -> Put/Patch Request - Verify that firstName is updated.


import pytest
import allure
import requests

base_url = "https://restful-booker.herokuapp.com"
headers = { "Content-Type" : "application/json" }

@allure.title("TC01 - Create and Update Booking.1")
@allure.description("Verify that a token&booking id is created and then first name is updated")
def get_token():
    path_post = "/auth"
    full_url = base_url + path_post
    json_payload = {
        "username" : "admin",
        "password" : "password123"
    }

    response_data = requests.post(url = full_url, headers= headers, json = json_payload)
    response_data_json = response_data.json()
    token = response_data_json["token"]
    assert  response_data.status_code == 200
    return token

def get_bookingid():
    path_post = "/booking"
    full_url = base_url + path_post
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_data = requests.post(url = full_url, headers = headers, json = payload)
    response_data_json = response_data.json()
    bookingid = response_data_json["bookingid"]
    return bookingid

def test_put_reuest():
    token = get_token()
    bookingid = get_bookingid()

    print(token)
    print(bookingid)

    base_path = "/booking/" + str(bookingid)
    full_url_put = base_url + base_path
    cookie = "token=" + token

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": cookie

    }

    json_payload = {
        "firstname": "Damini", #Updating First Name.
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=full_url_put, headers=headers, json=json_payload)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Damini"
    print(response.json()["firstname"])

"""" 
Yeh code RESTful Booker API ke through ek booking create karta hai, uske baad us booking ka **firstname** update karta hai using **PUT request**. Chaliye step-by-step samajhte hain Hinglish mein:

---

### 🔹 Step 1: Import Libraries

```python
import pytest
import allure
import requests
```

Yeh sab libraries testing aur API calls ke liye use hoti hain.

---

### 🔹 Step 2: Global Variables

```python
base_url = "https://restful-booker.herokuapp.com"
headers = { "Content-Type" : "application/json" }
```

Yahaan base API URL aur headers define kiye gaye hain.

---

### 🔹 Step 3: Token Generate Karna

```python
def get_token():
    ...
```

* `/auth` endpoint pe POST request bheji gayi hai.
* `username` and `password` se ek **token** banaya ja raha hai.
* Token verify bhi kiya gaya hai (status code 200 hona chahiye).

---

### 🔹 Step 4: Booking ID Create Karna

```python
def get_bookingid():
    ...
```

* `/booking` endpoint pe POST request se booking ban rahi hai.
* `"Jim"` naam ka customer hai initially.
* Response se `bookingid` return ho raha hai.

---

### 🔹 Step 5: PUT Request (Firstname Update Karna)

```python
def test_put_reuest():
    ...
```

#### 🟠 Kya ho raha hai is function mein:

1. **Token aur Booking ID** generate kar rahe hain.
2. URL bana rahe hain booking ko update karne ke liye (`/booking/<id>`).
3. PUT request ke headers mein `Cookie` ke through token pass kar rahe hain.
4. `json_payload` mein `firstname` ko `"Damini"` se update kar diya gaya hai.
5. PUT request bhej kar:

   * Check kar rahe hain status code 200 ho.
   * Response ka `firstname` check kar rahe hain ki wo `"Damini"` hai ya nahi.

---

### 🔚 Output

* Agar update sahi se ho gaya, toh print karega: `Damini`

---

### 🔑 Summary:

> Pehle ek booking banayi ja rahi hai (Jim), fir us booking ka `firstname` PUT request se `"Damini"` se update kiya ja raha hai. Last mein confirm kiya ja raha hai ki update successful tha ya nahi.

Agar chaho toh main isme **allure report ke tags** ya fixtures bhi add karwa sakta hoon for better pytest structure.
"""
