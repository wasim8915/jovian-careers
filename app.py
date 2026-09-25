from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

Jobs = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bangalore, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Bangalore, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Developer',
        'location': 'Remote',
        'salary': '$120,000'
    },
    {
        'id': 4,
        'title': 'Backend Developer',
        'location': 'New York, USA',
        'salary': '$150,0000000000'
    }
]

@app.route('/')
def index():
    return render_template('home.html', jobs=Jobs)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(Jobs)

if __name__ == '__main__':
    app.run(debug=True)