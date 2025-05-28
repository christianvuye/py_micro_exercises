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

## Section 2: Test case strategy

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

## Section 3: Performance analysis

**Time complexity:**
- For each input item, my function performs these operations:
  1. Clean the email (lowercase and strip whitespaces)
  2. Check if it matches the pattern
  3. If it does, add to the result

- There's a linear relationship between input size and processing time:
  - As input size goes up, processing time goes up linearly.
  - Time complexity grows proportionally with the input size [O(n)] 

- As each input email must be examined at least once to determine whether it is valid, there is no algorithm that can be faster than [O(n)]. 

- The function does cleaning and validating in a single pass, which by definiting is faster than doing it over multiple passes. 

- The computational bottleneck is the regular expression matching operation:
  - The fullmatch() function must evaluate a complex pattern against each email string;
  - Regex engines are CPU-intensive as they need to compare multiple character comparisons and backtracking.

- If I needed to process 1 million items, the limiting factor would be the cumulative time spent on Regex pattern matching.

**Space complexity:**
- As the input size grows, memory usage scales linearly:
  - If all inputs are valid, the output will be the same size as the input. (worst case)
  - If none of the inputs are valid, the output will be empty. (best case)

- Any function that produces a list of valid emails must use memory to store those results; 
  - the maximum amount of memory used for the output is at least the amount of memory used to store the input; 
  - there is algorithm that could use less memory. 

- The function does cleaning and validating in a single pass and therefore does not use any additional memory for storing any other intermediate data like rejected emails.

- My function uses additional memory for:
  - strip() and lower() create new temporary string objects (as strings are immutable)
  - the Regex engines creates internal data structures for pattern matching

- The largest memory impact comes from the output list that grows as valid emails are found:
  - If all input emails are valid, the function doubles memory usage. 

**Scalability considerations:**
- This solution would work well for datasets up to approximately 100,000 to 1 million emails on typical modern hardware (8-16GB RAM). This estimate assumes average email length of 30 characters and accounts for Python's memory overhead.

- If I needed to optimize for larger datasets (e.g. a million email addresses), I would consider the following factors:
  - given O(n) time complexity, the time to process a larger dataset of a million email addresses would be a million times the amount of time it takes to process a single email address
  - how much time is available to process the dataset? 
  - given linear relationship between input size and processing time, can we process the dataset within the available time?
  - given O(n) space complexity, the amount of memory required to store a million email addresses would be a million times the amount of memory it takes to store a single email address
  - how much memory is available to store both the input and output dataset?
  - given the linear relationshop between input and output size and memory required, can we store the dataset in memory? 

- To optimize space and time complexity for a larger dataset, the following items are worth investigating:
  - What about duplicate emails? Do duplicate emails need to be processed? If a duplicate email exist, we would still need the time to process it by checking whether it already exists in the stored result, but it would save memory as that duplicate would not need to be stored again. Trade-off between memory usage and processing time would depend on how much duplicates are present. 
  - Would there be a way to reduce the size of the dataset prior to begining the processing? E.g. obvious canditates like strings without "@", strings shorter than minimum possible email length. 
  - Would there be an algorithm that is more efficient for processing the dataset than the current O(n) algorithm?
    - parallel processing for very large datasets
    - streaming processing

## Section 4: Alternative approaches

**Modular design alternative:**
- Instead of one function, I could split this function into two seperate functions:
  - The first function would clean and standardize the raw data by removing outer whitespaces and making all the strings lowercase.
  - The second function would check if the data matches the email address pattern from the regex. 

- The benefits of a modular approach would be that it would allow the functions to be used elsewhere if raw data for another usecase needed cleaning in a similar way or if email address strings needed to be checked.
  - For example, if email addresses only need to be validated, without cleaning, one of the two modular function could be used. 
  - Or, if emails needed to be cleaned and validated with different rules than in the current implementation. 

- The drawbacks compared to my current approach would be the additional time and space complexity if the modular functions would be used together for the purpose of this particular use case - cleaning and validating email addresses. 

**Different contexts:**

- In a web application context, where a user registration API needs to validate emails in real-time with a ~50ms response time:
  - The current approach is sufficiently fast for individual requests.  
  - For multiple cients or high traffic scenarios:
    - The regex pattern in the current code gets compiled every time the function runs, which is ineffective under high loads.
    - Pre-compiling the regex pattern as a module-level constant would avoid this:
      ```
      EMAIL_PATTERN = re.compile(r"^[\w.+-]+@[\w.-]+\.[A-Za-z]{2,6}$")
      EMAIL_PATTERN.fullmatch(email_cleaned)
      ```

- For a data pipeline processing millions of records, such as a nightly batch job processing 10 million customer records from a data warehouse: 
  - I would keep the current approach, given sufficient memory on the machine doing the processing, as a nightly batch indictates sufficient, uninterrupted processing time. 
  - However, additional optimizations could be made by:
    - streaming processing (process emails one at a time without loading them all into memory)
    - parallel processing using multiprocessing to utilize multiple CPU cores

- If this needed to integrate with a database system:
  - Input: Read emails directly from database tables using SQL queries
  - Output: Update records with validation status or write to separate validation results table
  - Approach: Process in batches (e.g., 10,000 records at a time) to balance memory usage and database connection efficiency

- A microservice that other teams' applications need to call for email validation:
  - API design: RESTful endpoint like POST /validate-emails accepting JSON arrays
  - Response format: Return detailed results including validation status, cleaned email, and error reasons
  - Additional features: Bulk validation endpoints, detailed error messages ("missing @ symbol", "inval-id domain"), API versioning for different validation rules, authentication and rate limiting

## Section 5: Applied learning (Additional scenarios)

**Scenario application:**
- [Normalize phone numbers](data_normalization/normalize_phone_number.py)
- [Normalize product names](data_normalization/normalize_product_names.py)

## Section 6: Key Learning Items (Flashcard material)

**Algorithms and Data Structures, key terms:**
  - Time Complexity:
    - how much computational steps (time or operations) are required, and how do these steps change at larger scale (more input data)

  - Space Complexity: 
  - how much working memory is required for the function, and how does this working memory change with larger scale
  - includes both input storage and any additional working memory (temporary variables, output storage, etc)

  - O(n): 
    - "O" stands for "order of", "n" is the input size (e.g. number of elements in an array)
    - O(n) means "on the order of n", which means that for a given input n, the time complexity grows linearly  with n: double the input, double the time it takes

  Algorithmic patterns:
  - filtering and transformationg pattern (filter, transform and validate)
  - Map reduce and filter operations in Python (see functional approaches)
  - The same algorithmic pattern applies across domains - filter/transform works for emails, phone numbers, product names, and hundreds of other problems

  - Functional approaches:
    -  Lambda functions are anonymous functions - functions without a name.
    -  Syntax: *lambda arguments : expression* where:
      - *lambda* is the keyword to define the function.
      - *arguments* is a comma-separated list of input parameters (like in a regular function).
      - *expression* is a single expression that is evaluated and returned.
      ```
      s1 = 'GeeksforGeeks'
      s2 = lambda func: func.upper()
      print(s2(s1))

      # Output: GEEKSFORGEEKS
      ```
    - To apply data transformations, a lambda can be combined with a list comprehension:
      ```
      li = [lambda arg=x: arg * 10 for x in range(1, 5)]
      for i in li:
          print(i())
      # Output: 10 20 30 40
      ```
    
    - The *map(function, iterable)* function is used to apply a given function to every item of an iterable (list, tuple) and returns a map object, which is an iterator:
      ```
      s = ['1', '2', '3', '4']
      res = map(int, s)
      print(list(res))
      # Output: [1, 2, 3, 4]
      ```
      - Syntax: *map(function, iterable)* where:
        - *function* is the function we want to apply to every element in the iterable.
        - *iterable* is the iterable whose elements we want to process.
      - Returns: a *map object*.

    - The *reduce(function, iterable[, initializer])* function is used to apply a particular function passed in its argument to all of the iterable elements passed along. 
      ```
      from functools import reduce
      
      def add(x, y):
          return x + y

      a = [1, 2, 3, 4, 5]
      res = reduce(add, a)

      print(res)  # Output: 15
      ```
      - Syntax: *reduce(function, iterable[, initializer])* where:
        - *function* is the function that takes two arguments and performs an operation on them.
        - *iterable* is the iterable whose elements are processed by the function
        - *initializer (optional)* is an optional argument for the starting value for the operation.
    
    - The *filter(function, sequence)* function is used to filter the given sequence in its argument based on the function given in its argument that tests whether each element in the sequence is true or not.
      ```
      # Function to check if a number is even
      def even(n):
          return n % 2 == 0

      a = [1, 2, 3, 4, 5, 6]
      b = filter(even, a)

      # Convert filter object to a list
      print(list(b))
      # [2, 4, 6]
      ```
      - Syntax: *filter(function, sequence)* where:
        - *function* is the function that defines the condition to filter the elements. This function should return True for items you want to keep and False for those you want to exclude.
        - *iterable* is the iterable you want to filter (e.g., list, tuple, set).

**Performance analysis:**
- The single-pass algorithm had a lower space complexity in this case, but it is not always the case.
- Avoid computing and storing data multiple times if you can compute and store it once and then re-use it:
  - Pre-computing and compiling a Regex pattern is usually more efficient than compiling it every time its used.
- Performance and scalability is context dependent, what is an appropriate strategy in one situation might not be appropriate in another situation.

**Testing strategy**
- Systematic test categorization: Boundary conditions, malformed inputs, valid inputs needing normalization, edge cases
- Integration vs unit testing: Different purposes and when to use each
- Test data design: Mix of expected and unexpected inputs
- Professional test organization: Clear naming, descriptive assertions, comprehensive coverage

**Code organization**
- Code organization and quality is highly context dependent, deciding how to design your code optimally depends on the context it operates in. 
- A modular approach might be suitable in one situation, but not in another situation.
- Seperation of concerns: keep different responsibilites (cleaning vs validation) seperated
- single responsibility principle: each function should have one job

**Professional communication**
- Avoid communicating that you "only did what the requirements said", instead always consider different approaches and communicate those different approaches, their trade offs and why you chose a particular approach over another. 
- Structure technical presentations: Problem statement → approach → design decisions → tradeoffs → results
- Justify decisions with data: Using complexity analysis and concrete examples to support architectural choices

**Software Engineering mindset and professional development:**
- Thinking about edge cases and error conditions - considering what can go wrong and designing for it
- Systematic analysis approach: 
  - Breaking complex problems into manageable components (requirements → implementation → testing → performance → alternatives)
- Multiple solution thinking: Always consider 2-3 different approaches before choosing one

**Learning strategy:**
- Learning CS concepts through real code - understanding theory through practical application rather than abstract study