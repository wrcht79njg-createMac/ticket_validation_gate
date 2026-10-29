def validate_ticket(text):
    """
    Validates a support ticket text string against defined business rules.
    
    Returns trimmed text string on success or raises ValueError on validation failure.
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")

    trimmed = text.strip()

    if len(trimmed) == 0:
        raise ValueError("Ticket text cannot be empty or whitespace only.")

    if len(trimmed) > 1000:
        raise ValueError("Ticket text cannot exceed 1000 characters.")

    return trimmed
