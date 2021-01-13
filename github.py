from pymongo import MongoClient
import requests, datetime, pprint

classmate_one = requests.get('https://api.github.com/users/swolepenguin')
classmate_two = requests.get('https://api.github.com/users/jreeves')
classmate_three = requests.get('https://api.github.com/users/alanavery')

obj_one = {
    'name': classmate_one.json().get('name'),
    'email': classmate_one.json().get('email'),
    'bio': classmate_one.json().get('bio'),
    'followers': classmate_one.json().get('followers_url'),
    'repos': classmate_one.json().get('public_repos')
}
obj_two = {
    'name': classmate_two.json().get('name'),
    'email': classmate_two.json().get('email'),
    'bio': classmate_two.json().get('bio'),
    'followers': classmate_two.json().get('followers_url'),
    'repos': classmate_two.json().get('public_repos')
}
obj_three = {
    'name': classmate_three.json().get('name'),
    'email': classmate_three.json().get('email'),
    'bio': classmate_three.json().get('bio'),
    'followers': classmate_three.json().get('followers_url'),
    'repos': classmate_three.json().get('public_repos')
}


print(obj_one)
print(obj_two)
print(obj_three)