# 🌍 Air Quality Analysis & Forecasting Dashboard

## 🧠 Project Overview
This project focuses on analyzing air quality data across major Indian cities using geospatial and temporal techniques. It also includes a basic forecasting model to predict short-term pollution levels.

The goal is to understand pollution trends, identify high-risk areas, and support data-driven environmental decision-making.

---

## ❓ Business / Analytical Questions

- How does air pollution vary across different cities?
- What are the trends of pollutants over time?
- Which areas show consistently high pollution levels?
- Are there noticeable spikes in pollution during specific periods?
- Can we predict short-term pollution levels using historical data?

---

## 📁 Dataset Information

- Source: Air quality dataset (India)
- Data includes:
  - City names
  - Geographic coordinates (latitude, longitude)
  - Date-wise pollutant levels (NO2, etc.)

---

## 📊 Dashboard Features

- 📈 Time-series analysis of pollutant levels
- 🗺️ Geospatial visualization using interactive maps
- 🎛️ Dynamic filtering (city, pollutant, date range)
- 🤖 Short-term forecasting using Linear Regression
- 📉 Model performance evaluation using RMSE

---

## 🖼️ Dashboard Preview

### 📈 Pollution Trend
![Trend](https://github.com/sanchit-2511/Air-Quality-Analysis-Dashboard/blob/eaec30423dff9d77ef463d0a6e62122cd410cc63/Images/Screenshot%20(83).png)

### 🗺️ Geospatial Map
![Map](https://github.com/sanchit-2511/Air-Quality-Analysis-Dashboard/blob/eaec30423dff9d77ef463d0a6e62122cd410cc63/Images/Screenshot%20(84).png)

### 🤖 Forecast Output
![Forecast](https://github.com/sanchit-2511/Air-Quality-Analysis-Dashboard/blob/eaec30423dff9d77ef463d0a6e62122cd410cc63/Images/Screenshot%20(85).png)

### 📊 ML Regression Plot (Linear Regressiom)
![Regression](https://github.com/sanchit-2511/Air-Quality-Analysis-Dashboard/blob/eaec30423dff9d77ef463d0a6e62122cd410cc63/Images/Screenshot%20(86).png)

---

## 🔍 Key Insights

- Certain regions consistently show higher pollution levels, indicating localized environmental concerns.
- Pollution levels fluctuate over time, with noticeable spikes during specific periods.
- Urban areas tend to show higher pollutant concentration compared to surrounding regions.
- Temporal patterns suggest possible links to traffic density or environmental conditions.

---

## 💡 Recommendations

- 🌿 Authorities should focus on high-pollution zones for targeted interventions.
- 🚗 Implement stricter emission controls in urban hotspots.
- ⏰ Monitor pollution spikes and take preventive measures during high-risk periods.
- 📊 Use forecasting models for proactive environmental planning.

---

## 🤖 Machine Learning Model

- Model Used: Linear Regression
- Purpose: Short-term prediction of pollutant levels
- Evaluation Metric: RMSE (Root Mean Squared Error)

> Note: This model is a basic implementation for demonstration purposes.

---

## 🛠️ Tools & Technologies Used

- Python
- Streamlit (Web App)
- Pandas & NumPy (Data Processing)
- Plotly (Visualization)
- Scikit-learn (Machine Learning)

---

## 📂 Project Structure

Air-Quality-Analysis-Dashboard/

│

├── data/

│ └── [air_quality_india.csv](https://github.com/sanchit-2511/Air-Quality-Analysis-Dashboard/blob/eaec30423dff9d77ef463d0a6e62122cd410cc63/Data/air_quality_india.csv)

│ └── [sample pollutant.csv](https://github.com/sanchit-2511/Air-Quality-Analysis-Dashboard/blob/eaec30423dff9d77ef463d0a6e62122cd410cc63/Data/sample_pollutant.csv)

│

├── app/

│ └── [app.py](https://github.com/sanchit-2511/Air-Quality-Analysis-Dashboard/blob/eaec30423dff9d77ef463d0a6e62122cd410cc63/App/app4.py)

│

├── images/

│ ├── [Trend](https://github.com/sanchit-2511/Air-Quality-Analysis-Dashboard/blob/eaec30423dff9d77ef463d0a6e62122cd410cc63/Images/Screenshot%20(83).png)

│ ├── [Map](https://github.com/sanchit-2511/Air-Quality-Analysis-Dashboard/blob/eaec30423dff9d77ef463d0a6e62122cd410cc63/Images/Screenshot%20(84).png)

│ └── [Forecast](https://github.com/sanchit-2511/Air-Quality-Analysis-Dashboard/blob/eaec30423dff9d77ef463d0a6e62122cd410cc63/Images/Screenshot%20(85).png)

│ └── [Regression](https://github.com/sanchit-2511/Air-Quality-Analysis-Dashboard/blob/eaec30423dff9d77ef463d0a6e62122cd410cc63/Images/Screenshot%20(86).png)

│

├── [requirements.txt](https://github.com/sanchit-2511/Air-Quality-Analysis-Dashboard/blob/eaec30423dff9d77ef463d0a6e62122cd410cc63/requirements.txt)

└── README.md


---

## 🚀 How to Run the Project

1. Clone the repository:

git clone https://github.com/sanchit-2511/Air-Quality-Analysis-Dashboard.git


2. Navigate to the project folder:

cd Air-Quality-Analysis-Dashboard


3. Install dependencies:

pip install -r requirements.txt


4. Run the Streamlit app:

streamlit run App/app4.py


---

## 🚀 Conclusion

This project demonstrates how data analytics, visualization, and basic machine learning can be combined to understand and predict environmental patterns, enabling better decision-making.

---

## 🙌 Author

**Sanchit G. Barne**

---
