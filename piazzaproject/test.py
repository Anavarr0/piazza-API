
import requests
"""
url = "http://10.61.64.132:8000/authentication/register/"

nick = {
		'username': 'nick',
		'password': '1234'
	}
nick_response = requests.post(url, data=nick)
nick_response = nick_response.json()
print(nick_response)

"""
olga = {
		'username': 'olga',
		'password': '1234'
	}
"""
olga_response = requests.post(url, data=olga)
olga_response = olga_response.json()
print(olga_response)

mary = {
		'username': 'mary',
		'password': '1234'
	}
mary_response = requests.post(url, data=mary)
mary_response = mary_response.json()
print(mary_response)

nestor = {
		'username': 'nestor',
		'password': '1234'
	}
nestor_response = requests.post(url, data=nestor)
nestor_response = nestor_response.json()
print(nestor_response)

"""

url = "http://10.61.64.132:8000/api/posts-list/"
"""
olga_response = requests.post(url,data = olga)
print(olga_response.json())
"""
token_url = "http://10.61.64.132:8000/authentication/token/"

olga_response_token = requests.post(token_url, data = olga)
print(olga_response_token.json())

olga_token = olga_response_token.json()['access_token']

post_new_url = "http://10.61.64.132:8000/post-new/"
headers = {'Authorization': 'Bearer '+str(olga_token)}
post = {"title" : "my post",
        "body": "Hello World 4",
        "topic": "Health",
        "expiration_time": "00:02:00"
        }

olga_response_post = requests.post(post_new_url, headers=headers, data = post)
