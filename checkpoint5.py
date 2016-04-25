from pymongo import MongoClient
client = MongoClient()
from random import randint


def random_word_requester(posts):
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    count = 0;
    for p in posts.find():
   		count+=1

   	rand = random.randint(0,count)
   	i = 0
   	for p in posts.find():
   		if(i == rand):
   			a = p.author
   			db.posts.update({"author": a}, { $push: { "date" : datetime.datetime.utcnow() } })
   			print a
   			print p
   			print '\n'
   			return

   		i++

if __name__ == '__main__':
	db = client.test_database
	collection = db.test_database
	import datetime
	post = {"author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"], "date": datetime.datetime.utcnow()}
        posts = db.posts
        post_id = posts.insert_one(post).inserted_id
        post_id
        db.collection_names(include_system_collections=False)
        posts.find()
        print (posts.find_one({"author": "Mike"}))
        print (posts.find_one({"author": "Eliot"}))
        print (post_id)
        post_id_as_str = str(post_id)
        print (posts.find_one({"_id": post_id_as_str}))
        print (posts.count())
    	random_word_requester(posts)

