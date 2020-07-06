import requests


#Start the api to do the api Test
def test_posts_api():
    r = requests.get()
    assert r == 'Hello, World!'