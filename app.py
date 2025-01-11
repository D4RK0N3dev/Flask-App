from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/')
def show_table():
    data = [
        {'name': 'John Doe', 'age': 30, 'city': 'New York'},
        {'name': 'Jane Smith', 'age': 25, 'city': 'Los Angeles'},
        {'name': 'Mike Johnson', 'age': 35, 'city': 'Chicago'},
        {'name': 'Emily Davis', 'age': 22, 'city': 'San Francisco'},
        {'name': 'David Wilson', 'age': 40, 'city': 'Seattle'}
    ]
    return render_template('table.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
