def get_letter_grade(score):
    """Return the letter grade for a given numeric score."""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Faculty rating functions

def get_options_ratio(option, total):
    """Return the ratio of option to total."""
    if total == 0:
        return 0
    return option / total


def get_faculty_rating(ratio):
    """Return the faculty rating based on the ratio."""
    if not (0 <= ratio < 1):
        return "Invalid Ratio"
    if 0.9 <= ratio < 1:
        return "Excellent"
    elif ratio > 0.8:
        return "Very Good"
    elif ratio > 0.7:
        return "Good"
    elif ratio > 0.6:
        return "Needs Improvement"
    elif 0 <= ratio <= 0.59:
        return "Unacceptable"


