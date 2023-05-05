from flask import Flask, render_template
import csv


app = Flask(__name__)
@app.route('/')
def csv_data():
    with open('freespace.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        data = [row[0] for row in csvreader]
        new_data = [6 - int(x) for x in data]
    return render_template('dashboard.html', data=data, new_data=new_data)



if __name__ == '__main__':
    app.run(host ="localhost", port=int(5000))
