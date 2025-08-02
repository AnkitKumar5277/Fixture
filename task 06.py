# 6. Trying to Update on a Delete ID -> 404


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


def test_put_reuest():
    token = get_token()
    bookingid = test_delete()

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

    response = requests.patch(url=full_url_put, headers=headers, json=json_payload)
    assert response.status_code == 405
    assert response.text == "Method Not Allowed"
    print("Booking Id : "+str(bookingid)+ " is Deleted. So, updation isn't allowed.")

"""
# 6. Trying to Update on a Delete ID -> 404


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


def test_put_reuest():
    token = get_token()
    bookingid = test_delete()

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

    response = requests.patch(url=full_url_put, headers=headers, json=json_payload)
    assert response.status_code == 405
    assert response.text == "Method Not Allowed"
    print("Booking Id : "+str(bookingid)+ " is Deleted. So, updation isn't allowed.")
    """
