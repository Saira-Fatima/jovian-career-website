from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru India',
  'salary': 'Rs.10,00,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Dehli India',
  'salary': 'Rs.50,00,000'
}, {
  'id': 3,
  'title': 'Backend Engineer',
  'location': 'Remote',
  'salary': 'Rs.12,00,000'
}, {
  'id': 4,
  'title': 'Frontend Engineer',
  'location': 'San Francisco,USA',
}]


@app.route("/")
def hello_jovians():
  return render_template('home.html', jobs=JOBS, company_name="Jovians")

@app.route("/api/JOBS")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
