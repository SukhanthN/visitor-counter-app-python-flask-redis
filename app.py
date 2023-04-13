from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    counter = str(redis.get('hits'),'utf-8')
    # return "Hello world! this sukhanth, This webpage has been viewed "+counter+" time(s)"
    # return "<h1 style='color:red'>Hello world! This is sukhanth</h1><h2> This webpage has been viewed <span style='color:red'>" + counter + "</span> time(s).</h2>"
    # return "<div style='background-color:lightblue;padding:20px'><h1 style='color:red'>Hello world! This is sukhanth</h1><h4 style='color:green'>this webpage has been viewed <span style='color:red'>" + counter + "</span> time(s).</h4></div>"
    # return "<html><head><title>Hello World</title></head><body style='background-color:lightblue;padding:20px'><h1 style='color:white'>Hello world!</h1><p style='color:black'>This is sukhanth, and this webpage has been viewed <span style='color:red'>" + counter + "</span> time(s).</p></body></html>"
    return "<html><head><title>Hello World</title><style>html,body {height:100%;margin:0;}head {display:flex;align-items:center;justify-content:center;flex-direction:column;}</style></head><body style='background-color:lightblue;padding:20px'><h1 style='color:green;text-align:center'>Hello world! </h1><h2 style='color:#00008B;text-align:center'> This is Sukhanth, This webpage has been viewed <span style='color:red'>" + counter + "</span> time(s).</h2></body></html>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
