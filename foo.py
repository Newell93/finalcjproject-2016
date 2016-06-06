from operator import itemgetter
import csv
VACCINE_FNAME = './static/data/master_data.csv'

def filter_by_city(state, datarows):
    matches = []
    for c in datarows:
        # find all house members
        # that match given z['district'] and z['state']
        if c['title'] == 'Rep' or c['title'] == 'Sen':
            if state.upper() == c['state']: # upcase the state, so that `ca` resolves to `CA`
                matches.append(c)
    return matches



def filter_by_county(zipcode, datarows, ziplookups):
    matches = []
    zrows = [z for z in ziplookups if z['zipcode'] == zipcode]
    for z in zrows:
        for c in datarows:
            # find all house members
            # that match given z['district'] and z['state']
            if c['title'] == 'Rep':
                if c['district'] == z['district'] and c['state'] == z['state']:
                    matches.append(c)
            # find all senators that match z['state']
            elif c['title'] == 'Sen':
                if c['state'] == z['state']:
                    matches.append(c)
    return matches

