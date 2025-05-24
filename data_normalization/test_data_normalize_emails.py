from normalize_emails import normalize_emails

def test_sample_data():
    """
    Integration test using the complete sample dataset. 
    This verifies that the function correctly handles the mixed input
    provided in the original requirements.
    """

    email_list = [
        " Alice@GMAIL.com ",
        "BOB+work@Yahoo.Com   ",
        "  charlie@outlook.com",
        "diana@COMPANY.co.uk ",
        "invalid-email",
        "  eve@domain.",
        "frank@valid-domain.org",
        "SARAH@university.EDU",
        "not-an-email-at-all",
        " mike@subdomain.company.com "
    ]

    result = normalize_emails(email_list)

    assert "alice@gmail.com" in result
    assert "bob+work@yahoo.com" in result  
    assert "charlie@outlook.com" in result
    assert "diana@company.co.uk" in result
    assert "frank@valid-domain.org" in result
    assert "sarah@university.edu" in result
    assert "mike@subdomain.company.com" in result

    assert "invalid-email" not in result
    assert "not-an-email-at-all" not in result

    assert len(result) == 7, f"Expected 7 valid emails, got {len(result)}"

    print("✓ Exercise sample data integration test passed!")

def test_boundary_conditions():
    """
    Test edge cases like empty lists and minimal valid inputs.
    """

    #Test empty list - should return an empty list
    result = normalize_emails([])
    expected = []
    assert result == expected, f"Empty list test failed: expected {expected}, got {result}"

    print("✓ All boundary condition tests passed!")

    #Test single valid email
    result = normalize_emails(["test@domain.com"])
    expected = ["test@domain.com"]
    assert result == expected, f"Single email test failed: expected {expected}, got {result}"

    #Test minimal valid email (shortest possible valid format)
    result = normalize_emails(["a@b.co"])
    expected = ["a@b.co"]
    assert result == expected, f"Minimal email test failed: expected {expected}, got {result}"

def test_malformed_inputs():
    """
    Test inputs that should be rejected as invalid.
    These tests ensure the validation logic correctly identifies
    and filters out emails that don't meet structural requirements.
    """

    # Test emails missing @ symbol
    result = normalize_emails(["testdomain.com", "another.email.com"])
    expected = []  # Both should be rejected
    assert result == expected, f"Missing @ test failed: expected {expected}, got {result}"

    # Test emails missing domain part
    result = normalize_emails(["user@", "admin@", "test@"])
    expected = []  # All should be rejected
    assert result == expected, f"Missing domain test failed: expected {expected}, got {result}"

    # Test emails missing local part (username)
    result = normalize_emails(["@domain.com", "@gmail.com", "@company.org"])
    expected = []  # All should be rejected
    assert result == expected, f"Missing local part test failed: expected {expected}, got {result}"

    # Test emails with multiple @ symbols
    result = normalize_emails(["user@@domain.com", "test@multi@domain.com", "a@b@c.com"])
    expected = []  # All should be rejected
    assert result == expected, f"Multiple @ test failed: expected {expected}, got {result}"

    # Test emails with invalid domain extensions
    result = normalize_emails(["user@domain", "test@site.", "admin@company."])
    expected = []  # All should be rejected
    assert result == expected, f"Invalid domain extension test failed: expected {expected}, got {result}"

    # Test emails with spaces in the middle
    result = normalize_emails(["user name@domain.com", "test@do main.com", "admin@company .org"])
    expected = []  # All should be rejected
    assert result == expected, f"Spaces in email test failed: expected {expected}, got {result}"

    # Test completely invalid formats
    result = normalize_emails(["just-text", "123456", "@@@@", "....", ""])
    expected = []  # All should be rejected
    assert result == expected, f"Invalid formats test failed: expected {expected}, got {result}"

    print("✓ All malformed input tests passed!")

def test_normalization_cases():
    """
    Test inputs that need cleaning but should be kept.
    These tests verify that the cleaning logic correctly standardizes
    formatting variations while preserving valid email addresses.
    """

    # Various whitespace patterns that should be cleaned
    result = normalize_emails([" user@domain.com ", "  another@site.org  ", "\tuser@company.com\t"])
    expected = ["user@domain.com", "another@site.org", "user@company.com"]
    assert result == expected, f"Whitespace cleaning test failed: expected {expected}, got {result}"
    
    # Mixed case variations that should be standardized
    result = normalize_emails(["USER@DOMAIN.COM", "MixedCase@Site.ORG", "lowercase@site.com"])
    expected = ["user@domain.com", "mixedcase@site.org", "lowercase@site.com"]
    assert result == expected, f"Case normalization test failed: expected {expected}, got {result}"
    
    # Combined whitespace and case issues
    result = normalize_emails([" USER@DOMAIN.COM ", "  MixedCase@Site.ORG  "])
    expected = ["user@domain.com", "mixedcase@site.org"]
    assert result == expected, f"Combined normalization test failed: expected {expected}, got {result}"

    print("✓ All normalization tests passed!")

def test_edge_cases_and_stress():
    """
    Test unusual but potentially valid inputs and boundary conditions.
    These tests help discover behaviors that might not be immediately
    obvious and verify that the function handles complex scenarios correctly.
    """
    
    # Emails with special characters allowed by the regex pattern
    result = normalize_emails(["user.name@domain.com", "user+tag@site.org", "user-identifier@company.co.uk"])
    expected = ["user.name@domain.com", "user+tag@site.org", "user-identifier@company.co.uk"]
    assert result == expected, f"Special characters test failed: expected {expected}, got {result}"
    
    # Mixed valid and invalid emails in the same input list
    result = normalize_emails([" valid@domain.com ", "invalid-email", " another@site.org ", "also-invalid", "third@company.co.uk"])
    expected = ["valid@domain.com", "another@site.org", "third@company.co.uk"]
    assert result == expected, f"Mixed valid/invalid test failed: expected {expected}, got {result}"
    
    # Test the boundaries of the top-level domain length restriction
    result = normalize_emails(["test@domain.co", "test@domain.info", "test@domain.museum"])  # 2, 4, and 6 characters
    expected = ["test@domain.co", "test@domain.info", "test@domain.museum"]
    assert result == expected, f"TLD length boundary test failed: expected {expected}, got {result}"
    
    print("✓ All edge case tests passed!")

def run_all_tests():
    """
    Execute all test functions and provide comprehensive feedback.
    This function coordinates the entire test suite and provides
    clear reporting about which tests pass or fail.
    """
    print("Running comprehensive email normalization tests...\n")
    
    try:
        test_boundary_conditions()
        test_malformed_inputs()
        test_normalization_cases()
        test_edge_cases_and_stress()
        test_sample_data()
        print("\n🎉 All tests passed! The email normalization function is robust and reliable.")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        print("This indicates a specific behavior that needs attention in the implementation.")
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        print("This suggests a fundamental issue that should be investigated.")

# Execute the test suite when this file is run directly
if __name__ == "__main__":
    run_all_tests()