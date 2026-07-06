# Define required keys for the response
REQUIRED_KEYS = {
    "is_critical_emergency",
    "detected_symptoms",
    "clinical_reasoning_summary",
    "routing_destination"
}

# Define function to validate the response
def validate_response(data):

    for key in REQUIRED_KEYS:
        if key not in data:
            print(f"Missing required field: {key}")
            return False
    return True