from flask import Flask
app = Flask(__name__)

flute = dict(apple='アップル',orange='オレンジ',banana='バナナ')

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/flute/<flute_name>/')
def what_flute(flute_name):
    return flute.get(flute_name,'何か食べる')

if __name__ == '__main__':
    app.run()
