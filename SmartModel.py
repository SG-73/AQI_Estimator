# 🌆 Air Quality Index (AQI) Prediction Script
# Uses a trained regression model (pickled) to estimate AQI category

import numpy as np
import pickle

def predict(df):
    """
    Predicts the Air Quality Index (AQI) category for a given city based on pollutant levels.

    Parameters:
        df (pandas.DataFrame): A single-row DataFrame containing pollutant values and city name.

    Returns:
        str: The AQI category (GOOD / SATISFACTORY / MODERATE / POOR / VERY POOR / SEVERE)
    """

    # Define the list of pollutant columns used as input features
    cols = ['PM25', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene']

    # Ensure all pollutant values are converted to float type
    for col in cols:
        df[col] = df[col].astype(float)

    # List of all supported city names used during model training
    # Each city will be one-hot encoded as part of the input feature vector
    cities = [
        'Ahmedabad', 'Aizawl', 'Amaravati', 'Amritsar', 'Bengaluru', 'Bhopal', 'Brajrajnagar', 'Chandigarh', 'Chennai',
        'Coimbatore', 'Delhi', 'Ernakulam', 'Gurugram', 'Guwahati', 'Hyderabad', 'Jaipur', 'Jorapokhar', 'Kochi',
        'Kolkata', 'Lucknow', 'Mumbai', 'Patna', 'Shillong', 'Talcher', 'Thiruvananthapuram', 'Visakhapatnam'
    ]

    # Create a dictionary mapping each city to a unique column index in the feature array
    # Offset starts from 12 since first 12 indices are reserved for pollutant features
    city_map = {city: index + 12 for index, city in enumerate(cities)}

    # Identify the one-hot encoding index corresponding to the selected city
    city_index = city_map[df['city'].iloc[0]]

    # Initialize feature vector (total 38 features: 12 pollutants + 26 city indicators)
    x = np.zeros(38)

    # Insert pollutant values into the first 12 positions of the array
    x[:len(cols)] = [df[col].iloc[0] for col in cols]

    # Set the corresponding city index to 1 (one-hot encoding)
    x[city_index] = 1

    # Load the pre-trained AQI prediction model from pickle file
    model = pickle.load(open('aqi_daily_model.pickle', 'rb'))

    # Make AQI prediction using the trained model
    aqi = model.predict(x.reshape(1, -1))
    print('Aqi value is:', aqi[0])

    # Convert numerical AQI value into qualitative category
    if aqi <= 50:
        return 'GOOD'
    elif aqi <= 100:
        return 'SATISFACTORY'
    elif aqi <= 200:
        return 'MODERATE'
    elif aqi <= 300:
        return 'POOR'
    elif aqi <= 400:
        return 'VERY POOR'
    else:
        return 'SEVERE'
