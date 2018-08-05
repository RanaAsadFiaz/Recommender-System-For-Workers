from flask import Flask,render_template,request
from collections import defaultdict
from surprise import SVD
from surprise import Dataset
from surprise import BaselineOnly
from surprise import KNNBasic
from surprise import Reader
import os
import csv
import pandas as pd

app = Flask (__name__)

def get_top_n(predictions , n = 10  ):
	top_n = defaultdict(list)
	for uid, iid , true_r , est , _ in predictions:
		top_n[uid].append((iid , est))
	for uid , user_ratings in top_n.items():
		user_ratings.sort(key = lambda x:x[1] , reverse = True)
		top_n[uid] = user_ratings[:n]
	return top_n
# names = ['userID','itemID','rating']
# df = pd.read_csv('~/.surprise_data/ratings.csv', names  = names)
# reader = Reader(rating_scale = (1,5))
# data = Dataset.load_from_df(df[['userID','itemID','rating']],reader)

# trainset = data.build_full_trainset()

# sim_options = {'name':'cosine', 'user_based':False}
# algo = KNNBasic(k=40 , min_k = 1 ,sim_options = {})
# algo.fit(trainset)
# testset = trainset.build_anti_testset()
# predictions = algo.test(testset)
# top_n = get_top_n(predictions , n = 10)
# for uid , user_ratings in top_n.items():
# 	print(uid , [iid for (iid, _) in user_ratings])

# button pr click ho to ya fution sara dubara chaley ? g or jo result ho na wo powershell ki bajaye udr aye
# new page pr ? g ap wese e ek button e sirf dikha dein jis py click kr k ye results aa jaein mai phr usko connect kr ln ga baaki interface k sath.. ok


@app.route('/nindex')
def nindex():
	return("<a href='/results'>Show Results</a>")

@app.route('/results')
def results():
	names = ['userID','itemID','rating']
	df = pd.read_csv('~/.surprise_data/ratings.csv', names  = names )

	names1 = ['itemID','Profession','City']
	df1 = pd.read_csv('~/.surprise_data/workers1.csv', names  = names1 )


	reader = Reader(rating_scale = (1,5))
	data = Dataset.load_from_df(df[['userID','itemID','rating']],reader)


	trainset = data.build_full_trainset()

	sim_options = {'name':'cosine', 'user_based':False}
	algo = KNNBasic(k=40 , min_k = 1 ,sim_options = {})
	algo.fit(trainset)
	testset = trainset.build_anti_testset()

	predictions = algo.test(testset)
	top_n = get_top_n(predictions , n = 10)
	myArray = []
	for uid , user_ratings in top_n.items():
		abcd = []
		#abcd.append(iid for (iid, _) in user_ratings)
		for w in user_ratings:
				abcd.append(w)
		myArray.append([uid , abcd ])

	
	print(myArray)
	
	return render_template('secondpage.html' , returned={'data':myArray})
	return('results working')
if __name__ == '__main__':
	app.run(debug = True)