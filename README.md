# ProfitEats: Independent Contractor Profit Calculator
**Author:** Giulio Vitti  
**Live Demo:** [profiteats.com](https://www.profiteats.com)

## Introduction
Independent contracting offers the luxury of a flexible schedule, but it often hides systemic inefficiencies. Many gig-economy trips result in earnings below minimum wage—or even negative profit—once taxes, fuel, and vehicle wear are calculated.

**ProfitEats** is a quantitative tool built to solve this. It moves beyond simple arithmetic by using **multivariable calculus** to provide contractors with real-time profit estimations and sensitivity analysis.

---

## Project Overview
The application enables users to input trip variables and receive an immediate assessment of profitability. The logic is handled by a Python backend, using symbolic math and data manipulation libraries to provide a high level of accuracy.

### Key Functionalities:
* **Geospatial Data Extraction:** Using **Pandas**, the system maps user-inputted Zip Codes to state-level average gas prices stored in a CSV database.
* **Symbolic Profit Modeling:** Uses **SymPy** to define a profit function that accounts for price, duration, distance, and fuel efficiency.
* **Validation Layer:** A custom **JavaScript** engine handles client-side error checking to ensure mathematical integrity before the data reaches the Flask server.

---

## Mathematical Engine
The core of ProfitEats is the **Profit Function ($P$)**. The tool calculates the estimated post-tax hourly profit as follows:

$$P(p, d, t, e, m) = \frac{p - \left( \frac{t}{m} \cdot e \right)}{d} \times 60$$

### Sensitivity Analysis (The Gradient)
To help drivers understand which factors impact their wallet the most, I implemented a **Gradient Vector ($\nabla P$)**. By calculating the partial derivatives with respect to each variable, the tool identifies the "volatility" of a trip's profit.

$$\nabla P = \left[ \frac{\partial P}{\partial p}, \frac{\partial P}{\partial d}, \frac{\partial P}{\partial t}, \frac{\partial P}{\partial e}, \frac{\partial P}{\partial m} \right]$$

---

## Tech Stack
| Component | Technology | Role |
| :--- | :--- | :--- |
| **Language** | Python 3.x | Logic & Mathematical Modeling |
| **Math Engine** | SymPy | Symbolic differentiation and gradients |
| **Data** | Pandas | CSV parsing and Zip Code mapping |
| **Backend** | Flask | Routing and Template Rendering |
| **Frontend** | HTML5 / CSS3 | Responsive UI Design |
| **Client Logic** | JavaScript | Input validation and Error handling |

---

## Conclusion
This project demonstrates the intersection of **quantitative reasoning, data science, and web development.** It showcases my ability to take a handwritten math equation and scale it into a transformative, user-facing system—aligning perfectly with the "builder" mindset required for the OpenAI Residency.
