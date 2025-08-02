# 2. Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.

import pytest
import allure
import requests

base_url = "https://restful-booker.herokuapp.com"
headers = { "Content-Type" : "application/json" }

@allure.title("TC02 - Create, Delete and Verify")
@allure.description("Verify that a token&booking id is created and then verify the get response after deletion.")
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
    print(token)
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
    print("The Booking Id " + str(bookingid) + " is created.")
    return bookingid

def test_delete():
    base_url = "https://restful-booker.herokuapp.com/booking/"
    booking_id_del = get_bookingid()
    DELETE_URL = base_url + str(booking_id_del)
    cookie = "token=" + get_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    response = requests.delete(url=DELETE_URL, headers=headers)
    assert response.status_code == 201
    # assert response.status_code == 200
    print("The Booking Id " + str(booking_id_del) + " is deleted.")
    return booking_id_del


def test_get_request():
    base_url = "https://restful-booker.herokuapp.com/booking/"
    booking_id_get = test_delete()
    GET_URL = base_url + str(booking_id_get)
    response_data = requests.get(url = GET_URL)
    assert response_data.status_code != 200
    assert response_data.status_code == 404
    assert response_data.text == "Not Found"
    print("We are getting status code - 404 as " + str(booking_id_get) + " is now deleted.")

"""
Yeh code `pytest` aur `allure` ka use karke ek automation test bana raha hai jisme 3 kaam ho rahe hain:

---

### 🔸 **Test Steps (Samjhaane ke liye in Hinglish):**

#### **1. Token Create karna (`get_token`)**

* `/auth` API se `POST` request bhej ke token banaya ja raha hai.
* JSON payload mein username aur password diya gaya hai.
* Agar response `200` aata hai, to token valid hai.

#### **2. Booking Create karna (`get_bookingid`)**

* `/booking` endpoint par ek naya booking create kiya ja raha hai `POST` request se.
* Booking details jaise firstname, lastname, dates etc. bheji ja rahi hain.
* Response se `bookingid` nikala ja raha hai jo uniquely identify karta hai booking ko.

#### **3. Booking Delete karna aur Verify karna (`test_delete` + `test_get_request`)**

##### **test\_delete()**

* Pehle `get_bookingid()` se booking create hoti hai.
* Phir `get_token()` se token leke `DELETE` request bheja jata hai us booking id ko delete karne ke liye.
* Agar delete successful hota hai, to status code `201` aata hai.
* Delete hone ke baad booking id return kiya jata hai.

##### **test\_get\_request()**

* `test_delete()` ko call karke ek booking id delete ki jati hai.
* Fir usi booking id pe `GET` request bheja jata hai.
* Kyonki wo booking ab delete ho chuki hai, to `404 Not Found` status aana chahiye.
* Assertion se verify kiya jata hai ki response status code 404 ho aur body mein `"Not Found"` likha ho.

---

### 🔹 **Important Notes:**

* `test_get_request()` ke andar `test_delete()` call karna thoda **unconventional** hai. Better practice hoti agar `booking_id` aur `token` ko ek pytest fixture ke through share karte.
* Status code `201` for DELETE kaafi unusual hai, kyunki normal DELETE request ke liye `200` ya `204` expected hota hai. Shayad API ka custom behavior ho.

---

### ✅ **Output**

Agar sab kuch sahi hota hai to console par ye print hoga:

```
The Booking Id 1234 is created.
The Booking Id 1234 is deleted.
We are getting status code - 404 as 1234 is now deleted.
```

Aap chahe to main yeh code **pytest fixtures** ke sath aur better bana ke de sakta hoon. Batayein agar chahiye?

"""
