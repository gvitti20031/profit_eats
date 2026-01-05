ProfitEats: Independent Contractor Profit Calculator
Author: Giulio Vitti

Live Demo: profiteats.com

📌 Introduction
In the gig economy, independent contractors often struggle to assess the true profitability of a trip in real-time. Many offers, when factoring in expenses and taxes, result in earnings below minimum wage or even negative profits.

ProfitEats is a quantitative tool designed to solve this information asymmetry. Built with Python (SymPy, Pandas, Flask) and JavaScript, it allows contractors to calculate estimated hourly profits and perform sensitivity analysis via multivariable calculus to understand how different factors affect their bottom line.

⚙️ Project Overview
The application takes user inputs and processes them through a mathematical engine to determine net profitability.

Key Functionality:

Dynamic Gas Pricing: Automatically extracts state-average fuel costs by matching user-inputted zip codes against a CSV dataset using Pandas.

Gradient-Based Sensitivity: Utilizes the SymPy library to compute the gradient vector of the profit function. This shows the user the "volatility" of their profit—how a slight change in gas price or trip duration impacts their hourly take-home pay.

Full-Stack Integration: A Flask backend bridges the Python logic with a responsive HTML/CSS frontend, while JavaScript ensures data integrity through client-side validation.

📉 Mathematical Framework
The core of the project is a multivariable profit function P. The tool calculates the estimated post-tax hourly profit:

P(p,d,t,e,m)= 
d
p−( 
m
t
​	
 ⋅e)
​	
 ×60
Where:

p = Price Offered

d = Trip Duration (minutes)

t = Distance Traveled

e = Gas Expense (extracted via Zip Code)

m = Vehicle Fuel Efficiency (MPG)

To provide deeper insights, the tool computes the gradient vector ∇P:

∇P=⟨ 
∂p
∂P
​	
 , 
∂d
∂P
​	
 , 
∂t
∂P
​	
 , 
∂e
∂P
​	
 , 
∂m
∂P
​	
 ⟩
This allows the user to see which variables (like distance vs. time) have the highest impact on their specific trip's profitability.

🛠️ Technologies Used
Python: Core logic and symbolic mathematics.

SymPy: Symbolic computation of partial derivatives.

Pandas: Data manipulation for geographic fuel pricing.

Flask: Web framework for request handling and template rendering.

JavaScript: Real-time error handling and input validation.

HTML/CSS: Frontend layout and responsive UI design.

💡 Conclusion
This project is a practical application of quantitative reasoning and multivariable calculus translated into a functional software product. It demonstrates the ability to take a real-world economic problem, model it mathematically, and deploy it as a user-friendly tool for better decision-making.
