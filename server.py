from flask import Flask, render_template

app = Flask(__name__)    

@app.route('/')          
def hello_world():
    userz = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    tots = len(userz)


    return render_template('index.html', users = userz, total = int(tots)) 




if __name__=="__main__":  
    app.run(debug=True)    
