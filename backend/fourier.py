import concurrent.futures
import soundfile as sf
import math
pi = 3.14159265359
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