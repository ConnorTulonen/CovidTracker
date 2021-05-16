import requests
import ML
import fourier
from flask import render_template
x = requests.get(url)
z = fourier.fastfouriertransform(x.data)
perc = 100*ML.feedforward(z,ML.weights)
out = round(perc)
render_template('htmltemp',prob = out)

