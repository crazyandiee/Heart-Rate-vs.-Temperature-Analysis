# 🧠 Heart Rate vs. Temperature Analysis Across Six Months
This project investigates the relationship between heart rate (HR) and ambient temperature using real-world physiological and environmental data collected over six months. By combining wearable device data from Apple Watches with historical weather records from OpenWeatherMap, we analyze whether temperature drops correlate with cardiovascular responses across different individuals and contexts.

🧰 Tech Stack
Python 3

Pandas – Data manipulation

Matplotlib & Seaborn – Data visualization

NumPy – Data processing

OpenWeatherMap API – Historical temperature data source

Apple HealthKit (exported XML) – Heart rate monitoring


📁 Project Structure
heart-weather-analysis/

├── data/

│   └── combined.xlsx

├── src/

│   └── main_code.py

│   └── changing the xml files.py

├── README.md

├── docs/



📌 Key Features
Integrates 6 months of heart rate and temperature data across multiple participants

Performs correlation, regression, time series, and machine learning analysis

Categorizes temperature drops into severity ranges and links to physiological response

Contextual analysis (indoor vs outdoor, time of day, rest vs activity)

🔍 Research Questions
Do temperature drops trigger a significant change in heart rate?

Are there thresholds of cold exposure that elicit stronger physiological responses?

How does individual variation (e.g., fitness, environment) affect sensitivity?

Can consumer-grade wearable devices be used for population-level health monitoring?


📊 Methodology Overview
Heart rate data was collected every 5–10 minutes using Apple Watch devices

Environmental data was pulled hourly via the OpenWeatherMap API

Preprocessing was done to align time-series datasets and filter noise

Analytical methods included Pearson correlation, linear regression, time-lagged analysis, ARIMA models, and random forest regression


📉 Key Findings
Most participants showed weak or no correlation between temperature drops and immediate heart rate changes

One participant (P3) exhibited a strong positive response to cold exposure, indicating individual variability

Heart rate response was more visible during nighttime, rest periods, and outdoor exposure

Machine learning models (Random Forest) had low predictive power, suggesting other factors influence HR more significantly than temperature alone

📚 Report
A detailed research dissertation is available in the /docs/ folder [or linked here if hosted elsewhere], including:

Literature review

Methodology

Statistical and machine learning analysis

Visualizations

Limitations and recommendations


🚀 How to Run
Clone the repo:

git clone https://github.com/your-username/heart-weather-analysis.git
cd heart-weather-analysis

Install required libraries:
pip install -r requirements.txt

Open the Viusal Studio Code and run:
Main_code.py

🧠 Learning Outcomes
Hands-on experience with wearable health data

Fusion of environmental APIs with physiological time-series

Use of statistical and machine learning tools to analyze real-world health data

Practical insights into human adaptation to climate stressors
