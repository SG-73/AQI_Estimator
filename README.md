# Machine Learning-Based Air Quality Prediction System

### Overview
Built a **Machine Learning model** that predicts the **Air Quality Index (AQI)** of different cities based on pollutant concentration levels.
The model helps in monitoring air quality and assists in raising environmental awareness.
A simple and interactive **Streamlit web app** allows users to input pollutant levels and get instant AQI predictions.

### Problem Statement
Air pollution poses a severe threat to health and the environment.
Accurate AQI prediction enables better understanding of air quality conditions and supports proactive measures.
This project uses historical pollutant data and machine learning to estimate real-time AQI and categorize air quality levels.

### Tools & Technologies
- **Language:** Python
- **Frameworks & Libraries:** Streamlit, NumPy, Pickle
- **Model Used:** XGBoost Regressor
- **Deployment:** Streamlit Cloud

### Approach
1. **Data Preprocessing:** Cleaned and structured pollutant data including PM2.5, PM10, NO₂, SO₂, CO, and others.
2. **Feature Encoding:** Converted city names into one-hot encoded vectors to make them machine-readable.
3. **Model Training:** Trained an XGBoost Regressor on the processed dataset to predict AQI values.
4. **Classification:** Mapped predicted AQI values into six standard categories — GOOD, SATISFACTORY, MODERATE, POOR, VERY POOR, and SEVERE.
5. **Deployment:** Deployed the trained model using Streamlit for real-time user interaction.

### Results
- Delivers accurate AQI predictions for 25+ major Indian cities.
- Classifies air quality into standardized AQI categories.
- User-friendly web interface for quick predictions and analysis.
- Lightweight and deployable on any platform supporting Streamlit.

### How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/SG-73/AQI_Estimator.git
   cd AQI_Estimator
   ```

2. Install dependencies:

   pip install -r requirements.txt

3. Run the app:

   streamlit run AQI_Estimator.py

4. Access the app locally at http://localhost:8501
