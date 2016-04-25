from pymongo import MongoClient
client = MongoClient()

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
        for p in posts.find():
        	print (p)
        	print '\ns'


    
	
