# ideas.py

from data import business_data


business_ideas = {
    "food": [
        "Street food stand",
        "Mobile catering service",
        "Fast food takeaway",
        "Coffee shop",
        "Home-based baking business"
    ],

    "tech": [
        "Mobile app development",
        "AI business solutions",
        "Website design agency",
        "Tech support services",
        "Online SaaS startup"
    ],

    "transport": [
        "Delivery service",
        "Courier business",
        "Taxi service",
        "Logistics company",
        "Moving services"
    ],

    "retail": [
        "Clothing store",
        "Online shop",
        "Sneaker reselling",
        "Local market stall",
        "Beauty products store"
    ],

    "services": [
        "Cleaning services",
        "Hair salon",
        "Plumbing business",
        "Electrical services",
        "Car wash business"
    ]
}


def generate_ideas(business_type):
    if business_type not in business_ideas:
        return []

    return business_ideas[business_type]