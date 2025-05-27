from normalize_product_names import normalize_product_names

def test_sample_data():
    """
    Integration test using the complete sample dataset. 
    This verifies that the function correctly handles the mixed input
    provided in the original requirements.
    """

    product_names = [
        "  Apple Inc.  ",
        "MICROSOFT CORPORATION",
        "Google LLC",
        "amazon.com inc",
        "Tesla, Inc.",
        "Meta Platforms, Inc.",
        "netflix inc.",
        "Adobe Systems Incorporated",
        "salesforce.com, inc.",
        "IBM Corp",
        "oracle corporation",
        "  ", # Empty/whitespace only
        "A", # Too short to be real company
        "NVIDIA Corporation"
    ]

    result = normalize_product_names(product_names)

    assert 'Apple Inc' in result
    assert 'Microsoft Corp' in result
    assert 'Google Llc' in result

    assert "  " not in result
    assert "A" not in result
    assert "amazon.com inc" not in result
    assert "MICROSOFT CORPORATION" not in result

    assert len(result) == 12, f"Expected 12 valid company names, got {len(result)}"

    print("✓ Sample data integration test passed!")

if __name__ == "__main__":
    test_sample_data()