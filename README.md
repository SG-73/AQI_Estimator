# 🌆 Air Quality Index (AQI) Estimator

### Overview
This project uses **Machine Learning** to predict the **Air Quality Index (AQI)** of cities based on the concentration of air pollutants such as PM2.5, PM10, NO₂, SO₂, CO, and O₃.
It provides a simple, web-based interface built using **Streamlit** for real-time AQI estimation and visualization.

### Problem Statement
Air pollution poses serious risks to human health and the environment.
This model predicts the AQI category (Good, Moderate, Unhealthy, etc.) using historical air pollutant data, helping users and authorities make informed decisions.

### Tools & Technologies
- **Languages:** Python
- **Libraries:** pandas, numpy, scikit-learn, streamlit, pickle
- **Model Used:** XGBoost Regressor
- **Environment:** Jupyter Notebook / Streamlit

### Approach
1. **Data Preprocessing:** Handle missing values and outliers in pollutant readings.
2. **Feature Engineering:** Selected key pollutant features affecting AQI.
3. **Model Training:** Trained and tuned a XGBoost Regressor for AQI prediction.
4. **Evaluation:** Compared predictions against real AQI values using regression metrics.
5. **Deployment:** Deployed via **Streamlit** for user-friendly interaction.

### Results
- Achieved high accuracy in AQI estimation with consistent model performance.
- Provided interactive visualization for AQI prediction across multiple cities.

### How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/SG-73/AQI_Estimator.git
   cd AQI_Estimator

2. Install dependencies:

   pip install -r requirements.txt

3. Run the app:

   streamlit run AQI_Prediction.py

4. Access the app locally at http://localhost:8501
