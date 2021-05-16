import concurrent.futures
import soundfile as sf
import math
import random
#this section is devoted to the algorithm itself
e = 2.718281828459045
pi = 3.14159265359
def minus(a,b):
	return a - b
def multiply(a,b):
	return a * b
def multiplyminus(vect,a,b):
	return vectorminus(vect,multiply(a,b))
def multiplyvectors(vect1,vect2):
	with concurrent.futures.ThreadPoolExecutor() as executor:
		returnvect = []
		i = 0
		k = 0
		threadarray = []
		while(i < len(vect1)):
			threadarray.append(executor.submit(multiply,vect1[i],vect2[i]))
			k = k + threadarray[i].result()
			i = i + 1
		return k
def setvectorindex(vect1,vect2,vect,index):
	vect[index] = multiplyvectors(vect1,vect2)
def multiplymatrix(vector,matrix):
	with concurrent.futures.ThreadPoolExecutor() as executor:
		j = 0
		k = 0
		returnvect = []
		threadarray = []
		for i in matrix:
			threadarray.append(executor.submit(multiplyvectors,vector,i))
			returnvect.append(threadarray[j].result())
			j = j + 1
		return returnvect
def vectorminus(vect,subtract):
	with concurrent.futures.ThreadPoolExecutor() as executor:
		threadarray = []
		returnvect = []
		j = 0
		for x in vect:
			threadarray.append(executor.submit(minus,vect[j],subtract))
			vect[j] = threadarray[j].result()
			j = j + 1
def power(input,exponent):
	i = 1
	temp = input
	while(i < exponent):
		temp = temp * input
		i = i + 1
	return temp
def negativepower(input,exponent):
	return 1/power(input,exponent)
def sigmoid(x):
	return 1/(1+negativepower(e,x))
def feedforward(vector,matrix):
	with concurrent.futures.ThreadPoolExecutor() as executor:
		tempvect = multiplymatrix(vector,matrix)
		k = 0
		for i in tempvect:
			k = k + i
		return sigmoid(k)
def loss(result,out):
	return power(minus(result,out),2)
def backpropogation(vectin,expected,weights):
	x = feedforward(vectin,weights)
	y = loss(expected,x)
	threadarray = []
	k = 0
	j = 0
	with concurrent.futures.ThreadPoolExecutor() as executor:
		for i in vectin:
			threadarray.append(executor.submit(multiplyminus,weights[j],2 * y * x * (1-x),i))
			j = j + 1

#this section converts audio files into two values for a vector
def fouriercomponent(x,n):
    k = 2*pi/n
    factor = math.sin(k)+math.cos(k)
    return x * factor
def fastfouriertransform(file):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        data, filerate = sf.read(file)
        threadarray = []
        returnarray = 0
        n = len(data)
        j = 0
        while(j < n):
            threadarray.append(executor.submit(fouriercomponent,data[j],n))
            returnarray = returnarray + threadarray[j].result()
            j = j + 1
        return returnarray
weights = [[random.randint(),random.randint(),random.randint(),],[random.randint(),random.randint(),random.randint(),],[random.randint(),random.randint(),random.randint(),]]
x = fastfouriertransform('512306__dobroide__20200402-throat-clearing.wav')
y = [0,97]
backpropogation(x + y,1,weights)
print(weights,flush = True)
a = fastfouriertransform("512358__krqluld__sounds-of-me-at-home-during-covid-19.wav")
b = [0,98]
backpropogation(a + b,1,weights)
print(weights,flush = True)
c = fastfouriertransform("517897__klankbeeld__calm-corona-evening-200324-0136.ogg")
d = [89,97]
backpropogation(c + d,1,weights)
print(weights,flush = True)
e = fastfouriertransform("527438__bruno-auzet__emergency-room-hospital.wav")
f = [90,98]
backpropogation(e + f,1,weights)
print(weights,flush = True)
g = fastfouriertransform("537150__dastudiospr__male-cough.mp3")
h = [80,97]
backpropogation(g + h,1,weights)
print(weights,flush = True)
i = fastfouriertransform("547491__714jimmy__covid-cough.wav")
j = [89,97]
backpropogation(i + j,0,weights)
print(weights,flush = True)
k = fastfouriertransform("19121__fratz__cough6.aiff")
l = [79,97]
backpropogation(k + l,0,weights)
print(weights,flush = True)
m = fastfouriertransform("84695__cmusounddesign__cough.wav")
n = [90,98]
backpropogation(m + n,0,weights)
print(weights,flush = True)
o = fastfouriertransform("151212__owlstorm__cough-2.wav")
p = [84,99]
backpropogation(o + p,0,weights)
print(weights,flush = True)
q = fastfouriertransform("208761__harris85__cough.wav")
r = [80,96]
backpropogation(q + r,0,weights)
print(weights,flush = True)
s = fastfouriertransform("256567__sjnewton__coughing.mp3")
t = [75,97]
backpropogation(s + t,0,weights)
print(weights,flush = True)
u = fastfouriertransform("431164__inspectorj__voice-request-33-sarcastic-coughing.wav")
v = [100,98]
backpropogation(u + v,0,weights)
print(weights,flush = True)
