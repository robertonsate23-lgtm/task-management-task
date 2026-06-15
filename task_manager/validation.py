from datetime import datetime

def validate_task_title(title):
    """Validates that the title is a non-empty string and within a reasonable length."""
    if not isinstance(title, str) or not title.strip():
        return False
    if len(title) > 50:
        return False
    return True

def validate_task_description(description):
    """Validates that the description is a valid string."""
    if not isinstance(description, str) or not description.strip():
        return False
    return True

def validate_due_date(due_date):
    """Validates that the date is in YYYY-MM-DD format and is a valid calendar date."""
    try:
        # Strictly checks format and actual calendar placement
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False