import sqlite3
from database import get_data

def predict():
    RENO_COST_SF = 138
    ROI = 0.2

    con = sqlite3.connect('database/properties.db')
    cur = con.cursor()

    listings = get_data.get_act(cur)

    possible_investments = []
    for line in listings:
        if line[14] == 'Y':
            continue
        else:
            # gets the potenital value per sqft
            vals = get_data.get_comps(line, 402.34, cur)
            value_sqft = get_data.get_avg_val(vals)
            # sf * potential_value per sf
            potential_value = float(line[10]) * value_sqft
            # sf * constant reno cost per sf
            reno_cost = float(line[10]) * RENO_COST_SF

            strike_price = (potential_value - reno_cost - 0.015 * potential_value - 5000 - ROI * reno_cost - ROI * 0.015 * potential_value - 5000 * ROI) / (1 + ROI + 0.025 + 0.025 * ROI)
            # strike_price - original price
            difference = float(line[8]) - strike_price

            if difference <= 0:
                possible_investments.append([line, difference])

    con.close()

    return possible_investments

if __name__ == "__main__":

    print(predict())
