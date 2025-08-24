# Python Practice Microprojects

A collection of Python microprojects and exercises for practicing small problems, coding katas, and fundamental concepts. This repository serves as a hands-on learning environment for various Python programming patterns and techniques, with a focus on Object-Oriented Programming, Data Normalization, and Functional Programming.

## Repository Structure

The repository is organized into four main learning areas:

### 1. Object-Oriented Programming (`class_fundamentals/`)
This section contains dozens of standalone scripts demonstrating core OOP concepts, organized into a logical progression:
- **`1_core_concepts/`**: The building blocks of classes: `__init__`, instance variables, and methods.
- **`2_class_variables_and_methods/`**: Attributes and methods that belong to the class itself.
- **`3_static_methods/`**: Utility functions related to a class but independent of its state.
- **`4_inheritance/`**: Extending parent class functionality in child classes.
- **`5_class_interaction_and_composition/`**: How instances of different classes interact or are composed of other objects.
- **`6_advanced_class_design/`**: Advanced patterns like method chaining, complex initialization, and wrapper classes.
- **`7_encapsulation/`**: Best practices for data hiding using private attributes and properties.

### 2. Integrated Practice (`class_integrated_practice/`)
The integrated practice exercises in `class_integrated_practice` are designed to help you practice combining multiple Object-Oriented Programming (OOP) concepts in Python. Unlike the focused, single-concept scripts in `class_fundamentals`, these exercises are larger and more realistic. They require you to:

- Integrate several OOP principles (like inheritance, class/instance/static methods, encapsulation, and composition) in one solution.
- Design and implement small systems (e.g., a weather station, movie ticketing system) that reflect real-world business problems.
- Handle vague or incomplete requirements, simulating real-world software development where you must clarify, design, and justify your choices.
- Practice code organization, validation, and maintainability—skills needed for long-term, production-quality code.

### 3. Data & Functional Programming (`data_normalization/`)
This area focuses on data processing and functional programming techniques.
- **Data Normalization**: Real-world functions for cleaning and standardizing data, such as emails, phone numbers, and product names.
- **Functional Programming Concepts (`fp_concepts/`)**: Over 100 small exercises covering `lambda`, `map`, `filter`, `reduce`, and list comprehensions.
- **FP in Data Engineering (`fp_in_de/`)**: Practical applications of functional patterns in data engineering scenarios.


### 4. Data Structures and Algorithms (`dsa/`)
This section is dedicated to practicing common data structures and algorithms problems, similar to what one might encounter in a technical interview.
- **`lists, dicts, sets/`**: Contains problems that can be solved using lists, dictionaries, and sets.
- **`heuristics/`**: Contains reference guides for time and space complexity analysis.

### Running Individual Exercises
Each exercise file is a standalone script that can be run directly to see the concept in action:
```bash
# Example from OOP section
python class_fundamentals/1_core_concepts/class_car.py

# Example from FP section
python data_normalization/fp_concepts/lambda/lambda_square.py
```

## Philosophy

These microprojects follow the coding kata philosophy—small, focused exercises that can be completed quickly but provide deep learning through repetition and variation. Each exercise is designed to:
- Focus on a single concept or pattern
- Provide immediate feedback through execution
- Build muscle memory for common programming tasks
- Prepare for real-world application scenarios

Perfect for daily practice, interview preparation, or exploring new Python concepts.
