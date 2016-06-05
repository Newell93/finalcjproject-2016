from flask import Flask, render_template, request 
from operator import itemgetter
import csv

VACCINE_FNAME = './static/data/master_data.csv'

app = Flask(__name__)

def get_data():
	with open(VACCINE_FNAME, encoding='latin1') as f:
		newrows = []
		for row in csv.DictReader(f):
			if row['pbe_per'] != '':
				row['pbe_per'] = float(row['pbe_per'])
				newrows.append(row)
	return newrows

def filter_data(city='', sortby=None):
    upcity = city.upper()
    rows = [d for d in get_data() if upcity in d['city']]
    if sortby == 'Highest_PBE_Rates':
        return sorted(rows, key=itemgetter('pbe_per'), reverse=True)
    elif sortby == 'Lowest_PBE_Rates':
        return sorted(rows, key=itemgetter('pbe_per'))
    else:
        return sorted(rows, key=itemgetter('city'))

@app.route("/")
def homepage():
    html = render_template('index.html')
    return html

@app.route("/results")
def results():
    _sortby =  request.args.get('sortby')
    _city =  request.args.get('city')
    schools = filter_data(city=_city, sortby=_sortby)
    html = render_template('results.html', city=_city,
                           master_data=schools, sortby=_sortby)
    return html


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)