import pandas as pd

# Load dataset
df = pd.read_csv("cars.csv")

# Clean and convert values if needed
df.dropna(inplace=True)

# Recommender function (using Present_Price and Fuel_Type)
def recommend_cars(min_price, max_price, fuel_type=None):
    filtered = df[(df['Present_Price'] >= min_price) & (df['Present_Price'] <= max_price)]

    if fuel_type:
        filtered = filtered[filtered['Fuel_Type'].str.lower() == fuel_type.lower()]

    return filtered.sort_values(by='Present_Price')

# Test
results = recommend_cars(3, 7, fuel_type="Petrol")

# Display
print("\nRecommended Cars:\n")
print(results[["Car_Name", "Present_Price", "Fuel_Type", "Year", "Kms_Driven", "Transmission"]].reset_index(drop=True))
