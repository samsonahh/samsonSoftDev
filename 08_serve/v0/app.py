# Worship Warships: Samson, Aahan, Joshua
# SoftDev
# Oct 2022

'''
Notes:
print(__name__) shows up only on the terminal
return shows the string on the website

QCC:
what is the purpose of setting app = Flask(__name__)?
Why does __name__ end up as __main__?
'''

from flask import Flask
app = Flask(__name__) # This is a standard when importing Flask

@app.route("/") # Goes to main page of site Ex: localhost:5000/
def hello_world():
    print(__name__) # Prints __main__
    return "No hablo queso!"  # Shows up on the website

app.run()  # Without this, the website doesnt run at all
                
