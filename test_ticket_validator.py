from ticket_validator import validate_ticket
import pytest

def test_trims_spaces():
    results = validate_ticket(" Cannot log in ")
    assert results == "Cannot log in"

def test_rejects_blank_text():
    with pytest.raises(ValueError):
        validate_ticket("  ")

def test_length_after_trimming():
    text = "a" * 1000
    assert validate_ticket("  " + text + "  ") == text

def test_accepts_one_character():
    assert validate_ticket("a") == "a"

# test_accepts_1000_character()




# test_rejects_1001_character()


  


# test_rejects_number()












