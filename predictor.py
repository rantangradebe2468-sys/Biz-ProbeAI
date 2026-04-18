# predictor.py

from data import business_data
from ideas import generate_ideas
from location_data import location_data


def detect_business_type(user_input):
    """
    Detect business type based on keywords
    """
    user_input = user_input.lower()

    best_match = None
    best_score = 0

    for b_type, info in business_data.items():
        for keyword in info["keywords"]:
            if keyword in user_input:
                score = len(keyword)

                if score > best_score:
                    best_score = score
                    best_match = b_type

    return best_match


def detect_location(user_input):
    """
    Detect real location from user input
    """
    user_input = user_input.lower()

    for location in location_data.keys():
        if location in user_input:
            return location

    return "cape town"  # default location


def calculate_score(business_type, location_type):
    """
    Calculate opportunity score using base + location data
    """

    # base data from CSV
    base = business_data[business_type]

    # safety check
    if location_type not in location_data:
        location_type = "cape town"

    loc = location_data[location_type][business_type]

    # combine values
    demand = (base["demand"] + loc["demand"]) / 2
    competition = (base["competition"] + loc["competition"]) / 2

    # scoring formula
    score = (demand * 0.65) + ((1 - competition) * 0.35)

    return round(score * 100, 2)


def predict_opportunity(user_input):
    """
    Main AI function used by your app
    """

    business_type = detect_business_type(user_input)
    location_type = detect_location(user_input)

    # if business type not found
    if business_type is None:
        return {
            "score": 0,
            "level": "UNKNOWN BUSINESS TYPE ❓",
            "type": None,
            "ideas": [],
            "location": location_type
        }

    try:
        score = calculate_score(business_type, location_type)
        ideas = generate_ideas(business_type)

        # determine level
        if score >= 75:
            level = "HIGH OPPORTUNITY 🔥"
        elif score >= 50:
            level = "MEDIUM OPPORTUNITY ⚠️"
        else:
            level = "LOW OPPORTUNITY ❌"

        return {
            "score": score,
            "level": level,
            "type": business_type,
            "ideas": ideas,
            "location": location_type
        }

    except Exception as e:
        return {
            "score": 0,
            "level": f"ERROR: {str(e)}",
            "type": None,
            "ideas": [],
            "location": location_type
        }