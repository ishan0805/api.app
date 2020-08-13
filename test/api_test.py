import pytest
import requests
url="http://127.0.0.1:5000/"


def test_get_api_valid():
    test1="api/v1/resources/books/all"
    test2="api/v1/resources/books?id=0"

    response1=requests.get(url+test1)
    response2=requests.get(url+test2)
    
    assert response1.status_code == 200
    assert response2.status_code == 200

def test_delete_api_valid():
   
    test1="api/v1/resources/books?id=2"

    response1=requests.delete(url+test1)
   
    
    assert response1.status_code == 200
   

def test_post_api_valid():
   
    test1="api/v1/resources/books"
    ob={"author" : "Ishan","published" :"2020"}
    response1=requests.post(url+test1,data=ob)
   
    
    assert response1.status_code == 200

def test_put_api_valid():
   
    test1="api/v1/resources/books"
    ob={"id":0,"author" : "Ishan","published" :"2020"}
    response1=requests.post(url+test1,data=ob)
   
    
    assert response1.status_code == 200    