from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message="Hello from Flask on Vercel!")

# If the app is running within Vercel's serverless function, it should be wrapped like this:
def handler(event, context):
    from werkzeug.serving import run_simple
    return run_simple("0.0.0.0", 5000, app)
