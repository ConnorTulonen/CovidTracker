import concurrent.futures
#this section is devoted to the algorithm itself
e = 2.718281828459045
pi = 3.14159265359
def multiply(a,b):
	return a * b
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
weights = [[2.7123,5.678,9.5],[1.3,7.1,0.2],[2,1,1]]
