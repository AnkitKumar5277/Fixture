# 4. Create a BOOKING, Delete It


import pytest
import requests

base_url = "https://restful-booker.herokuapp.com"
headers = { "Content-Type" : "application/json" }

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

"""
Yeh Python code ek REST API test karta hai jismein hum ek **booking create**, phir **delete** karte hain, aur verify karte hain ki woh successfully delete hui ya nahi — yeh sab `pytest` framework ka use karke hota hai.

### Code Explanation (Hinglish):

#### 🔹 `get_token()` function:

* Is function ka kaam hai **login karke token lena**.
* API endpoint `/auth` pe POST request bhejta hai `username` aur `password` ke saath.
* Agar response code `200` hai, toh response se `token` nikala jata hai aur return kiya jata hai.
* **Token** authorization ke liye use hota hai jab hum delete request bhejte hain.

#### 🔹 `get_bookingid()` function:

* Iska kaam hai ek **nayi booking create karna**.
* `/booking` endpoint pe POST request bhejta hai ek JSON body ke saath (jismein name, price, dates, etc. hote hain).
* Response se `bookingid` nikala jata hai aur print karke return hota hai.

#### 🔹 `test_delete()` function:

* Sabse pehle ek booking create karta hai (`get_bookingid()` call karke).
* Phir `get_token()` call karke token nikalta hai.
* Fir `/booking/<bookingid>` pe DELETE request bhejta hai token ke sath.
* Agar response ka status code `201` hai (successfully deleted), toh success message print karta hai.

---

### 🔁 Summary:

* **Step 1:** Token generate hota hai
* **Step 2:** Booking create hoti hai
* **Step 3:** Booking ko delete kiya jata hai using token
* **Step 4:** Status code `201` hone par confirm hota hai ki booking delete ho gayi

---

Agar tum chaaho toh isme ek aur step add kar sakte ho — booking delete hone ke baad usko GET karke verify karna ki `404 Not Found` aaye (matlab booking ab exist nahi karti).

"""
