from normalize_phone_number import normalize_phone_numbers

def test_sample_data():
    """
    Integration test using the complete sample dataset. 
    This verifies that the function correctly handles the mixed input
    provided in the original requirements.
    """

    phone_list = [
    "(555) 123-4567",
    "555-123-4567", 
    "555.123.4567",
    "+1 555 123 4567",
    "5551234567",
    "555-123-45", # Too short
    "555-123-456789", # Too long  
    "abc-def-ghij", # Invalid characters
    " (555) 123-4567 ", # Extra whitespace
    "+1-555-123-4567",
    "not-a-phone-number"
    ]

    result = normalize_phone_numbers(phone_list)

    assert "5551234567" in result

    assert "555-123-45" not in result
    assert "555-123-456789" not in result
    assert "abc-def-ghij" not in result
    assert "not-a-phone-number" not in result

    assert len(result) == 7, f"Expected 7 valid phone numbers, got {len(result)}"

    print("✓ Sample data integration test passed!")

if __name__ == "__main__":
    test_sample_data()