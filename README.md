## 💡 Inspiration

Covid-19 has caught us all by surprise. We have to find new ways to combat it. We need to be knowledgeable about our symptoms, as we can't rush to the hospital every time we have a cough. We need to learn how to track our symptoms and talk to our doctors will be **distant**. And with everyone being **distant** and quarantined we have to find ways to get what on our mind out and not bottle in. We also need to find ways to share our thoughts with our doctors & friends and family.

## 🏥  What it does

* Connects users with our C-19 Wristband. The Wristband collects data (coughing, body temperature, etc.) Also has a questionnaire that once completed tells you if you are most likely to have caught covid-19 while remaining **distant**.

* A log feature to write how your feeling and send it to doctors & friends far away, allowing you to maintain **distance**.

* A hospital map feature to help you find hospitals near you and with your preferences.

## 🔨 How we built it

We first brainstormed some hardware ideas and how to implement them with software.
We then broke into groups web/design and hardware. 
Then we came together to combine our work and make a pitch deck and devpost submission.

## 😢 Challenges we ran into

* We struggled to come up with an idea that adhered to the theme. 
* We also struggled to find a project that combined all of our team members strengths (hardware, software (frontend), and design)
* FInding data to use for our wristband.

## 🏆 Accomplishments that we're proud of

* Completing both the software & hardware component of our project
* Doing this hackathon, as it was the first for some of us.

## 📖 What we learned

* How to build a wristband that can track temperature & pulse.
* Coding our Figma design prototype.
* Finding data.

## 🚀 What's next for _CovidTracker_

* Connecting the C-19 wristband to our site to display data on our site.
* Design our wristband to be more attractive
* Make a mobile app (IOS + Android)

#Resources/References

* https://github.com/nshomron/covidpred/tree/master/data
* https://www.nature.com/articles/s41746-020-00372-6#data-availability
Documentation
Machine learning
The machine learning part of the program is implements via neural network (ML.py).
The weights have already been calculated using a separate file (‘machinelearning.py)
Fourier Transform
Given that the program needs to considers audio files of coughs a Fourier transform is implemented (fourier.py). All sound data was provided via freesound.org.
Api
The api (newapi.py) retrieves data from the server and analyzing producing a demo webpage
