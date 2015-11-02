#I_AM_THE_REAL_KEVIN
#conversationbot


import praw
from Markov import Markov
import time
import pickle
from cStringIO import StringIO


username = "I_AM_THE_REAL_KEVIN"
password = "conversationbot"
kevin = praw.Reddit(user_agent="Hi, my name is Kevin")
kevin.login(username, password, disable_warning=True) 

def main():
	submissions = kevin.get_subreddit("AskReddit").get_hot(limit=1000)
	commentList = list()
	grababunchofcomments(submissions)
	# markov = Markov(4)

	# for submission in submissions:
	# 	for comment in submission.comments:
	# 		if type(comment) is praw.objects.Comment:
	# 				markov.trainingComment(comment.body)


	# for i in range(10):
	# 	print "%d: %s" % (i,markov.generateComment())



def grababunchofcomments(submissions):


	output = open('data.pkl', 'wb')

	for submission in submissions:
		for comment in submission.comments:
			if type(comment) is praw.objects.Comment:
				pickle.dump(comment, output)









main()

