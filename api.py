# api.py

from predictor import predict_opportunity
from ranker import get_top_businesses
from monetization import is_premium_user


def get_prediction(user_input):

    if not user_input.strip():
        return {
            "score": 0,
            "level": "ENTER A BUSINESS IDEA ⚠️",
            "type": None,
            "ideas": [],
            "location": None
        }

    try:
        return predict_opportunity(user_input)
    except Exception as e:
        return {
            "score": 0,
            "level": f"ERROR: {str(e)}",
            "type": None,
            "ideas": [],
            "location": None
        }


def get_top_opportunities(location):

    # 🔒 LOCK FEATURE IF NOT PREMIUM
    if not is_premium_user():
        return "LOCKED"

    try:
        return get_top_businesses(location)
    except Exception:
        return []