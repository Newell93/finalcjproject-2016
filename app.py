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
                row['enrollment'] = float(row['enrollment'])
                newrows.append(row)
    return newrows


def filter_data(city='', sortby=None):
    upcity = city.upper()
    rows = [d for d in get_data() if upcity in d['city']]
    if sortby == 'Highest_PBE_Rates':
        return sorted(rows, key=itemgetter('pbe_per'), reverse=True)
    elif sortby == 'Lowest_PBE_Rates':
        return sorted(rows, key=itemgetter('pbe_per'))
    elif sortby == 'Highest_Enrollment':
        return sorted(rows, key=itemgetter('enrollment'))
    elif sortby == 'Lowest_Enrollment':
        return sorted(rows, key=itemgetter('enrollment'))
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


@app.route('/<row_school_code>/')
def detail(row_school_code):
    template = 'detail.html'
    object_list = get_data()
    for row in object_list:
        if row['school_code'] == row_school_code:
            return render_template(template, object=row)
    abort(404)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)