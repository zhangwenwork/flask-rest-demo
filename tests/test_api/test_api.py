import requests


#Start the api to do the api Test
def test_posts_api():
    r = requests.get()
    assert r == 'Hello, World!'



#Test rest API which depends on third-party gRPC API
def test_calculator_api():
    pass

#Test resr API which depends on third-party rest API
def test_posts_api():
    pass