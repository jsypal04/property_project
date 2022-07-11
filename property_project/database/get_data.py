import sqlite3
from . import util
import math

# finds all of the properties a certain distance from the base property
# base is a list that contains the property data, range is the maximum distance from base measured in meters
# returns a list of the prices per sqft
# reference: 0.25 miles = 402.34 meters
def get_comps(base, range, cur):
    results = []

    for property in cur.execute("SELECT * FROM properties"):
        if property[3] == "ACT":
            continue
        elif property[3] == "CLS":
            p1 = (math.radians(base[1]), math.radians(base[2]))
            p2 = (math.radians(property[1]), math.radians(property[2]))
            if (util.hav(p1, p2, util.RADIUS) <= range) and (property[10] != 0):
                    results.append(property[8] / property[10])
        else:
            print("Error")

    results.sort(reverse=True)

    return results

# returns the average price per sqft of the list returned in get_comps
# vals is a list
def get_avg_val(vals):
    total = 0.0
    loops = 0

    for i in range(len(vals)):
        if i < 5:
            total += vals[i]
            loops = i + 1
        else:
            break

    if loops > 0:
        return total / loops
    else:
        return 0

# returns all of the active properties as a list of tuples
def get_act(cur):
    cur.execute("SELECT * FROM properties WHERE status=:stat", {"stat": "ACT"})
    return cur.fetchall()

def block(cur, con, base):
    cur.execute("UPDATE properties SET blocked = 'Y' WHERE mls_num=:num", {"num": base[0][0]})
    con.commit()


if __name__ == "__main__":
    con = sqlite3.connect('properties.db')
    cur = con.cursor()

    cur.execute("UPDATE properties SET blocked = 'N' WHERE mls_num = 'DCDC2022300'")
    con.commit()

    cur.execute("SELECT * FROM properties WHERE mls_num = 'DCDC2022300'")
    prop = cur.fetchall()
    print(prop)

    if prop[0][14] == "N":
        print("works")

    con.close()
