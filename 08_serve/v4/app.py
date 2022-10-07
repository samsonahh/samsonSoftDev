# Worship Warships: Samson, Aahan, Joshua
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported / What does this mean?
    app.debug = True        # enable auto-reload upon code change / very useful for live updates
    app.run()
