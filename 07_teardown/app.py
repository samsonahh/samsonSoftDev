# your heading here

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
*There is an @ right next to app.route("/") in line 7.
*We can't directly run the code yet.
*Apparently we can setup a virtual environment so that certain libraries can only be used in a certain directory.
*We can install Flask with pip install Flask.
*"No hablo queso!" does show on the website. Kevin was right.
*You can CTRL + C to quit.

QCC:
0. We have never seen the underscore syntax in any other languages.
1. We think the '/' refers to the current directory the file is in.
2. We think that it will probably print to the console.
3. 
4. Kevin thinks that the string will show on the website when you goto the '/' directory because of the app.route('/') above it. 
Samson thinks that nothing will appear at all because it is simply a return.
5. We have seen something similar in Java when working with objects.

*What is a localhost?
*What is a virtual environment and why is it important to Flask?
*What is favicon.ico?
*What does the 200 and 404 mean at the end of each line?
...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
1) We initially tried running the code but nothing happened. 
2) We will now look up the Flask documentation. Specifically the installation process because we cannot run the code.
3) We figured out how to unstall Flask with pip install Flask.
4) Running the code gives us a clickable url.
'''
