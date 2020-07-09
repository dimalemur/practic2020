from flask import Flask, render_template

app = Flask(__name__, static_folder="static")


@app.route("/", defaults={"path": ""})
@app.route("/<string:path>")
@app.route("/<path:path>")
def main(path):
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host="localhost")
