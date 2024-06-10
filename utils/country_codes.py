import requests

def clean_country_codes_data(data):
    cleaned_data = []
    for country, code in data.items():
        if not code.strip():
            continue
        codes = code.replace("+", "").split(" and ")
        for individual_code in codes:
            cleaned_data.append({"country": country, "code": individual_code})
    return cleaned_data

def get_country_calling_codes():
    url = "http://country.io/phone.json"
    result = {}
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            cleaned_data = clean_country_codes_data(data)
            result = cleaned_data
        else:
            result["error"] = f"Error fetching country calling codes: {response.status_code}"
    except Exception as e:
        result["error"] = f"An error occurred while fetching country calling codes: {e}"
    return result
