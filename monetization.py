# monetization.py

# Simple premium system (can upgrade later to real payments)

USER_STATUS = {
    "is_premium": False
}


def is_premium_user():
    return USER_STATUS["is_premium"]


def upgrade_to_premium():
    USER_STATUS["is_premium"] = True