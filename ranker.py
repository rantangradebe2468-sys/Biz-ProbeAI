# ranker.py

from data import business_data
from location_data import location_data
from ideas import generate_ideas


def calculate_score(business_type, location_type):
    base = business_data[business_type]

    if location_type not in location_data:
        location_type = "cape town"

    loc = location_data[location_type][business_type]

    demand = (base["demand"] + loc["demand"]) / 2
    competition = (base["competition"] + loc["competition"]) / 2

    score = (demand * 0.65) + ((1 - competition) * 0.35)

    return round(score * 100, 2)


def get_top_businesses(location_type="cape town"):
    results = []

    for b_type in business_data.keys():
        score = calculate_score(b_type, location_type)
        ideas = generate_ideas(b_type)

        results.append({
            "type": b_type,
            "score": score,
            "ideas": ideas[:2]
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:5]