#Create a dictionary of 5 countries with their currency details and display them.

world = {
    "India": {"capital": "Delhi", "currency": "Rupees", "language": "Hindi"},
    "USA": {"capital": "Washington", "currency": "Dollars", "language": "English"},
    "UK": {"capital": "London", "currency": "Pound Sterling", "language": "English"},
    "France": {"capital": "Paris", "currency": "Euro", "language": "French"},
    "Japan": {"capital": "Tokyo", "currency": "Yen", "language": "Japanese"}
}
for country,details in world.items():
    print(f"The capital of {country} is {details['capital']}, the currency is {details['currency']} and primary language spoken here is {details["language"]}")