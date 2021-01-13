from pymongo import MongoClient
import requests, datetime, pprint

client = MongoClient()
db = client.githubusers

# db.drop_collection("classmates")
collection = db.classmates

classmate_one = requests.get('https://api.github.com/users/swolepenguin')
classmate_two = requests.get('https://api.github.com/users/jreeves')
classmate_three = requests.get('https://api.github.com/users/alanavery')

obj_one = {
    'github_id': classmate_one.json().get('id'),
    'name': classmate_one.json().get('name'),
    'email': classmate_one.json().get('email'),
    'bio': classmate_one.json().get('bio'),
    'followers': classmate_one.json().get('followers_url'),
    'repos': classmate_one.json().get('public_repos'),
    'date': datetime.datetime.now()
}
obj_two = {
    'github_id': classmate_two.json().get('id'),
    'name': classmate_two.json().get('name'),
    'email': classmate_two.json().get('email'),
    'bio': classmate_two.json().get('bio'),
    'followers': classmate_two.json().get('followers_url'),
    'repos': classmate_two.json().get('public_repos'),
    'date': datetime.datetime.now()
}
obj_three = {
    'github_id': classmate_three.json().get('id'),
    'name': classmate_three.json().get('name'),
    'email': classmate_three.json().get('email'),
    'bio': classmate_three.json().get('bio'),
    'followers': classmate_three.json().get('followers_url'),
    'repos': classmate_three.json().get('public_repos'),
    'date': datetime.datetime.now()
}


print(db.classmates.find_one(obj_one.github_id))
# classmate_one_id = db.c
# lassmates.find_one('github_id')
# print(classmate_one_id)

# db.classmates.insert_many([obj_one, obj_two, obj_three])


