import pickle

mydata = [1,2,3,4,5,6,7,8,9,0]

# for writing into file that is in bytes 'wb'
with open('dummyFile.txt' , 'wb') as fl:
	pickle.dump(mydata , fl)

# for reading data from file that is in bytes 'rb'
with open('dummyFile.txt' , 'rb') as fl:
	returned = pickle.load(fl)

print(returned)


#dekh 1 file aa gai hn es ko us mai use kese krein gy q k hum ne jo recursion ;agi hoi ha usko eska koi reference pass ni kia ?
# abhi files bn rai hain iski agli iteration may code dubara edit ho ga .. abhi file write ho rai hain us may baad hum read krain gain
# abhi sirf wirte hon gi .. jab read krain gain to data variables may save krain gain ok ye masla tha rat ko mai dono ko ek e dafa dy raha tha wo chal e ni raha tha :P
# bs isi chez k lea main hazir hu :D hahahahha very very thankful to you really :) <3 hahah koi gal nai yaar .. coding ka shok hay mujhy :D hahahaha yrrrr ye bs shok e to paida ni hota :D
# hahaha chor acha hay k paida nai hota :D kia krta hay avin demang khapai hay xP hn ye to ha bs yrrr ab to guzar gai ha itna k seekh lia ha k time lagaon to o jata ha bs ye e kaafi ha wallah
# han exactly 
#ye dekh yrrrr from 1% data we are predicting 99% data but omar usman said k error ziada q hahahahah
#
