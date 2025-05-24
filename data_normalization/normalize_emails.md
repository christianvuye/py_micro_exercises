# Code Review and analysis

## Section 1: Solution explanation
**Problem statement:**
- For a fictional customer data integration project, email addresses have been collected from multiple sources (forms, CSVs, API).
- A function is required to normalize the emails, so they can be used consistently accross different parts of the application. 
- The function must not only clean the data but also filter out invalid entries.

**Core approach & code walkthrough:**
- My solution uses the following approach:
  - The function takes in a list of strings containing raw string items, and returns a list with cleaned string items.
  - Each string in the original list with raw string data gets looped over:
    - Each string item in the original list is stripped of outer whitespaces and made lowercase for consistency and easier evaluation.
    - In order to ensure that all the provided email addresses are valid, the raw string items need to match a regex pattern. 
      - The regex enforces the following structure:
        - The part before "@" can be one or more word character(s) (letter, digit, underscore), as well as a ".", "+" and/or "-". This should cover most if not all email address formats.
        - The first part after "@" but before the "." can be one or more word character(s), a "." or "-". This allows for domain names such as "@company.department" or "@company-department". 
        - Finally, the part after the "." must be two or more letters (eiher lower or uppercase) to match common formats like ".es" or ".com". Technically, uppercase is not required as the strings are made lowercase prior to being checked against the pattern. Furthermore, the "two or more letters" allows for an infinite amount of letters after the ".", which is unnecessary and would allow non-existing endings such as ".blablablablablablablabla...", which could potentially allow for "fake" email string data. 
        - Therefore, it is reasonable to restrict the range to "{2,6}" characters as this would cover all real top-level domains while preventing obviously invalid ones. There is little upside to being permissive and a lot of upside in being strict with this validation.
    - Once the data has consistent formatting, it gets compared to the regex pattern to match.
    - If the string item matches the regex pattern, it gets added to the new list. 
  - After the function has looped through the original list with raw strings, it finally returns the new list with the cleaned strings which are valid email addresses.

**Design decisions:**
- I chose a single-pass algorithm using one iterator to clean and validate each email string in one iteration. A two-pass approach where cleaning and validating were done seperately would require for a second intermediate list/array to be stored in memory, which would double the amount of memory required. This could potentially become problematic with large datasets. A single-pass approach is more efficient and does not make the code less clear. 
- I evaluated two approaches and chose the single-function design because it best aligned with the specific requirements, 
- though I also considered a modular approach that would offer greater reusability by splitting the single function into two seperate functions:
  - The first function would clean and standardize the raw data by removing outer whitespaces and making all the strings lowercase.
  - This would allow the function to be used elsewhere if raw data for another usecase needed cleaning in a similar way. For example, product names from different vendors with different formatting. 
  - The second function would check if the data matches the email address pattern from the regex. 
  - Again, this function could be used elsewhere if email address strings needed to be checked. Any situation in which cleanly formatted data containing email addresses are provided as input list could use this function. 
  - Eventually, I decided against splitting the function into two functions as the RFC required a single function.
- For this implementation, I focused on the core validation pattern specified in the requirements. 
- I recognize that production email validation involves additional edge cases like international domains and escaped characters, which could be addressed in future iterations if business requirements expand. 

## Section 2: Test case trategy

**Categories to consider:**
- For boundary conditions, I need to test the following funtion inputs:
  - empty list
  - single valid email
  - shortest possible valid email
- For malformed inputs that should be rejected, I should test the following function inputs:
  - emails missing @ symbol
  - emails missing domain part
  - emails missing local part (username)
  - emails with multiple @ symbols
  - emails with invalid domain extensions
  - emails with spaces in the middle
  - completely invalid formats
- For valid inputs that need normalization, I should test the following inputs:
  - Various whitespace patterns that should be cleaned
  - Mixed case variations that should be standardized
  - Combined whitespace and case issues
- For edge cases that might reveal bugs, I should test:
  - Emails with special characters allowed by the regex pattern
  - Mixed valid and invalid emails in the same input list
  - Test the boundaries of the top-level domain length restriction
- Integration test that verifies that the function correctly handles the mixed input provided in the original requirements.

**Test data design:**
- The test cases should include examples that are both expected and perhaps less expected input values. Both of these types of values need to be verified. Finally, the integration test should be the most challenging test case as it contains the most "realistic" list input. 

## Section 3: Performance Analysis

**Space Complexity:**
- "My function uses additional memory for..."
- "As the input size grows, memory usage scales..."
- "The largest memory impact comes from..."

**Time Complexity:**
- "For each input item, my function performs these operations..."
- "The computational bottleneck would be..."
- "If I needed to process 1 million items, the limiting factor would be..."

**Scalability Considerations:**
- "This solution would work well for datasets up to..."
- "If I needed to optimize for larger datasets, I would consider..."

## Section 4: Alternative Approaches

**Modular Design Alternative:**
- "Instead of one function, I could split this into..."
- "The benefits of a modular approach would be..."
- "The drawbacks compared to my current approach would be..."

**Different Contexts:**
- "In a web application context, I might modify this by..."
- "For a data pipeline processing millions of records, I would..."
- "If this needed to integrate with [specific system], I would consider..."

## Section 5: Applied Learning (Additional Scenarios)

**Scenario Application:**
- "Applying the same pattern to [new scenario], I would need to modify..."
- "The key differences in requirements would be..."
- "My validation logic would change to..."

## Section 6: Key Learning Items (Flashcard Material)

**Technical Concepts:**
- "The most important programming concept I reinforced was..."
- "A pattern I should remember for future problems is..."
- "The key insight about [specific topic] was..."

**Professional Skills:**
- "In terms of software engineering practices, I learned..."
- "For code organization, the important principle was..."
- "For problem-solving approach, I should remember..."