from flask import Flask, render_template, request
import pandas as pd
import sympy as sp


app = Flask(__name__)

# Load and preprocess zip code data
clean_zips = pd.read_csv("clean.csv")
zip_codes = clean_zips["zip"].to_list()
zip_codes_str = list(map(str,zip_codes))

clean_zips['zip'] = [i.zfill(5) for i in zip_codes_str]

# Dictionary mapping state names to their average gas prices, will be updated every month
state_gas_prices = {
    'Alabama': 2.56, 'Alaska': 3.56, 'Arizona': 3.04, 'Arkansas': 2.41, 'California': 4.27, 'Colorado': 2.42,
    'Connecticut': 2.95, 'Delaware': 2.78, 'Florida': 2.86, 'Georgia': 2.68, 'Hawaii': 4.42, 'Idaho': 2.84,
    'Illinois': 2.94, 'Indiana': 2.83, 'Iowa': 2.38, 'Kansas': 2.44, 'Kentucky': 2.60, 'Louisiana': 2.48,
    'Maine': 2.94, 'Maryland': 2.85, 'Massachusetts': 2.96, 'Michigan': 2.75, 'Minnesota': 2.66, 'Mississippi': 2.47,
    'Missouri': 2.47, 'Montana': 2.81, 'Nebraska': 2.52, 'Nevada': 3.38, 'New Hampshire': 2.88, 'New Jersey': 2.83,
    'New Mexico': 2.67, 'New York': 3.05, 'North Carolina': 2.65, 'North Dakota': 2.57,
    'Oregon': 3.43, 'Pennsylvania': 3.04, 'Rhode Island': 2.88, 'South Carolina': 2.55, 'South Dakota': 2.60, 'Tennessee': 2.53,
    'Texas': 2.44, 'Utah': 2.66, 'Vermont': 3.05, 'Virginia': 2.73, 'Washington': 3.86, 'West Virginia': 2.83,
    'Wisconsin': 2.45, 'Wyoming': 2.54, 'Puerto Rico': 3.15, 'Virgin Islands': 4.25, 'Guam': 4.85
}

# Populate estimated gas price fields based on the above dictionary
clean_zips["gas_price"] = clean_zips["state_name"].map(state_gas_prices)

# Save the updated DataFrame back to CSV if there is no gas price column or if there are any missing values
if "gas_price" not in clean_zips.columns or clean_zips["gas_price"].isnull().any():
    clean_zips.to_csv("clean.csv", index=False)

@app.route('/')
def index():
    return render_template('index.html')

# Main calculation route
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Retrieve inputs from the form
        p = float(request.form['p'])
        d = float(request.form['d'])
        t = float(request.form['t'])
        z = str(request.form['z'])

        # Check for a valid zip code
        if z in clean_zips['zip'].values:
            pass
        else:
            error_message = f"Zip code '{z}' not found in the existing database for the US. Please check your entry."
            return render_template('index.html', error=error_message)
        m = float(request.form['m'])

        # Removed gas price input from index.html and use the mapped value from the CSV
        e = round(clean_zips[clean_zips['zip'] == z]['gas_price'].values[0], 2)
    except ValueError:
        error_message = "Please ensure all fields are filled correctly with valid numbers."
        return render_template('index.html', error=error_message)

    try:
        # Calculate the hourly profit value

        # Write out a profit function using SymPy
        p1, d1, t1, m1, e1 = sp.symbols('p d t m e')
        P = (50.82 / d1) * (p1 - ((e1 * t1) / m1))

        # Calculate gradients
        dP_dp = round(float(sp.diff(P, p1).subs({p1: p, d1: d, t1: t, m1: m, e1: e})), 2)
        dP_dd = round(float(sp.diff(P, d1).subs({p1: p, d1: d, t1: t, m1: m, e1: e})), 2)
        dP_dt = round(float(sp.diff(P, t1).subs({p1: p, d1: d, t1: t, m1: m, e1: e})), 2)
        dP_dm = round(float(sp.diff(P, m1).subs({p1: p, d1: d, t1: t, m1: m, e1: e})), 2)
        dP_de = round(float(sp.diff(P, e1).subs({p1: p, d1: d, t1: t, m1: m, e1: e})), 2)

        # Compute profit value
        profit_val = round(float(P.subs({p1: p, d1: d, t1: t, m1: m, e1: e})),2)

        # Round gradients to the nearest hundredth
        p_grad_num = round(float(dP_dp), 2)
        d_grad_num = round(float(dP_dd), 2)
        t_grad_num = round(float(dP_dt), 2)
        m_grad_num = round(float(dP_dm), 2)
        e_grad_num = round(float(dP_de), 2)

    except ZeroDivisionError:
        error_message = "Duration (minutes), Gas Mileage (mpg), and Price cannot be zero."
        return render_template('index.html', error=error_message)


    formatted_profit = f"{profit_val:0.2f}"

    return render_template('result.html', profit=formatted_profit, p_grad_num=p_grad_num, d_grad_num=d_grad_num, t_grad_num=t_grad_num, m_grad_num=m_grad_num, e_grad_num=e_grad_num)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)  # Use 0.0.0.0 for external access

