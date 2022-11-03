# TNPG: Steve, Roster: Samson, Joseph, Ryan

from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = b'_MinecraftSTEVE'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# def display_login_page():
#     print("\n\n\n")
#     print("***DIAG: this Flask obj ***")
#     print(app)
#     print("***DIAG: request obj ***")
#     print(request)
#     print("***DIAG: request.args ***")
#     print(request.args)
#     print("***DIAG: request.headers ***")
#     print(request.headers)
#     return render_template( "login.html" )

# @app.route("/auth", methods=['POST'])
# def authenticate():
#     print("\n\n\n")
#     print("***DIAG: this Flask obj ***")
#     print(app)
#     print("***DIAG: request obj ***")
#     print(request)
#     print("***DIAG: request.args ***")
#     #print(request.args)
#     print("***DIAG: request.form ***")
#     print(request.form)
#     print("***DIAG: request.args['username']  ***") #Works only when its uncommented here
#     #print(request.args['username']) #prints the inputted user
#     username = request.form['username']
#     print("***DIAG: request.headers ***")
#     print(request.headers) #Accesses the args and puts them in a list
#     return render_template( "response.html", user=username )  #response to a form submission

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()