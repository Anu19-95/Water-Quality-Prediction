🧪 Water Quality Prediction Using ML (India — Lakes & Rivers)

This project predicts water quality for lakes and rivers in India using machine learning, based on historical water-quality parameters collected from government and environmental datasets.

The dataset has been enhanced by replacing station IDs with lake and river names, so users can easily search locations instead of cryptic codes.

The goal is to support:

environmental researchers

urban planners

pollution control boards

students & public stakeholders

by providing interpretable, location-based water quality insights.

🌍 Problem Statement

Water quality data in India is often:

fragmented across stations

difficult to interpret for public use

stored using numeric station IDs instead of real locations

As a result, it becomes hard to answer questions like:

“What is the water quality trend of this particular lake or river?”

This project converts raw monitoring data into:

✔ meaningful lake & river names
✔ structured dataset
✔ ML-based predictive analytics
✔ user-friendly interface (optional Streamlit app)

📂 Dataset Description

The dataset consists of multiple years of water quality observations.

Typical features include:

Location Name (Lake / River)

State / Region

Latitude / Longitude

Year / Season

pH

Dissolved Oxygen (DO)

Biological Oxygen Demand (BOD)

Chemical Oxygen Demand (COD)

Nitrate

Phosphate

TDS / EC

Turbidity

Temperature

Wherever possible, values are retained exactly as recorded to maintain scientific validity.

❗ No artificial or assumed values were added.

Only verified observations are used.

🎯 Project Objectives

✔ Replace anonymous station IDs with real water body names
✔ Clean and standardize dataset
✔ Perform exploratory analysis
✔ Train ML models to predict water quality indicators
✔ Provide interpretable results
✔ Make dataset searchable by lake/river name
✔ Support future expansion with new locations

🧠 Machine Learning Approach

The project focuses on supervised regression models to predict critical parameters such as:

BOD

DO

pH

Overall Water Quality Index (optional)

Models explored:

Random Forest Regressor

Linear Regression

Gradient Boosting

Decision Tree Regressor

Model selection is based on:

Mean Absolute Error (MAE)

RMSE

R² Score

Generalization performance

Reliability is prioritized over overfitting or inflated accuracy claims.

🛠️ Tech Stack

Languages

Python

Libraries

pandas

numpy

scikit-learn

joblib

matplotlib / seaborn (for analysis)

streamlit (for optional web app)

Tools

Jupyter / VS Code

GitHub

CSV-based dataset workflow

🚀 How the System Works
🔹 Input

User selects or searches:

Lake / River name

Location / Region

Year (or future prediction)

Machine learning model uses:

historical concentration values

temporal trends

environmental parameters

🔹 Output

The system provides:

Predicted water quality parameter values

Possible alert category (optional, non-medical)

Trend interpretation

Comparison with past values

Example outputs include:

“BOD is likely to increase in this lake based on past trend”

“DO levels are stable”

“Water quality may require monitoring attention”

Outputs are descriptive — not regulatory classifications.

📊 Use-Case Relevance

This project can support:

research projects

environmental monitoring studies

student innovation / hackathons

academic presentations

early-warning analytics exploration

It is not a replacement for laboratory testing, but a data-driven decision-support tool.

⚖️ Ethical & Data Integrity Notes

To maintain accuracy:

No synthetic values were inserted

No unrealistic generalizations applied

Missing values handled cautiously

Predictions interpreted with context

Water quality has real-world environmental impact, so correctness is prioritized over dataset size.

▶️ How to Run the Project
Install dependencies
pip install pandas numpy scikit-learn joblib streamlit matplotlib seaborn

Train / retrain model
python train_model.py

Run Streamlit app (optional)
streamlit run app.py

🔮 Future Enhancements

Planned improvements:

Add more verified lakes / rivers from official datasets

Introduce seasonal & hydrological features

Support GIS visualization

Add anomaly detection for pollution spikes

Build mobile-friendly interface

Only validated environmental data will be included.

✨ Project Outcomes

This project demonstrates:

dataset cleaning & feature engineering

ML-based environmental prediction

real-world domain mapping (station → location name)

user-oriented dataset usability

responsible scientific application of AI
