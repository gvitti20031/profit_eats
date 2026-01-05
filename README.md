# profit_eats
ProfitEats: Independent Contractor Profit Calculator
Giulio Vitti
November 13, 2025
https://www.profiteats.com
Introduction
Independent contracting has become the new way to make a quick buck, affording individuals the luxury of earning money at any time without any schedule commitments. Nonetheless, managing income and expenses efficiently is especially crucial for contractors to maximize earnings and avoid accepting unprofitable jobs that occasionally result in negative profits. This project demonstrates a practical tool built with Python (SymPy, Pandas, Flask), JavaScript, and HTML that allows users from any device to calculate estimated hourly profits for short-term contracts, as well as the sensitivity of the profit to a change in price, trip duration, gas mileage, distance traveled, and gas price. The tool is particularly useful to gig-economy drivers wanting to estimate their earnings in an hourly format and ways to improve profits. 
Project Overview
The website allows users to input relevant variables and quickly assess the profitability of a contract. The calculations are handled in Python, with the support of SymPy and Pandas, whereas the Flask framework package connects the formulas to the HTML render template that is displayed on the website. Two separate HTML scripts encapsulate the website design for the input and results pages, as well as the CSS design of those same pages, whereas a JavaScript file handles errors, ensuring valid inputs are submitted for calculation. 
Key Variables:
Input | Calculated by Python
	Price Offered (p): Amount the contractor is paid
	Trip duration (d): Minutes required to complete the job
	Distance traveled (t): Mileage covered over trip
	Zip code (z): Zip code of trip
	Gas mileage (m): Vehicle fuel efficiency (miles per gallon)
	Gas expense (e): Fuel cost (dollars per gallon)
Functionality:
	Estimates hourly profit based on the function P = 50.82p/d-et/m
	Gas expense, e, is extracted by matching the zip code to the corresponding state and returning the state average price from a CSV file, using Pandas. 
	The gradient vector (dP/dp,dP/dd,dP/dt,dP/dm,dP/de) is computed using the SymPy package to display the sensitivity of profit to changes in each of these variables. 
	HTML and CSS handle website design and layout, and Flask handles integration with Python. 
	JavaScript is used for error checking each inputted variable and preventing HTML form submission for any invalid input. 
	Allows users to modify inputs for each individual trip offer to receive an estimated profit figure and differential metrics within seconds
Technologies Used
	Python (SymPy, Pandas): Core calculations and logic
	Flask: Web application framework for user input and output
	HTML/CSS: Layout and design for website interface
	JavaScript: Handles error checking for user input variables
Conclusion
This project showcases practical applications of quantitative reasoning, multivariable calculus, algebra, programming, data science, and web development. It demonstrates the vast applications of mathematics, Python programming, and web frameworks to create a user-friendly tool for real-world decision-making. 
