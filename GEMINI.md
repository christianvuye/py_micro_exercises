# Gemini Project Context: Python Practice Microprojects

This file provides context for the Gemini AI assistant to effectively assist with this project.

## Project Overview

This repository is a collection of Python micro-projects designed for practice and learning. It covers fundamental and advanced concepts in Python, including Object-Oriented Programming, data normalization techniques, and functional programming paradigms.

## Tech Stack

- **Language:** Python
- **Testing Framework:** pytest

## Coding Conventions

- Follow the existing coding style and patterns within the file being edited.
- Adhere to PEP 8 standards for new Python code.

## Build and Test Commands

- The project uses `pytest` for testing.
- Tests are located in the `data_normalization/` directory.
- To run all tests, execute the following command from the project root:
  ```bash
  python -m pytest
  ```

## Directory Structure

- **`class_fundamentals/`**: Contains standalone scripts demonstrating core Object-Oriented Programming (OOP) concepts, organized into subdirectories by concept:
    - **`1_core_concepts/`**: Files demonstrating the fundamental building blocks of classes: `__init__`, instance variables, and basic instance methods.
    - **`2_class_variables_and_methods/`**: Focuses on attributes and methods that belong to the class itself, not just an instance.
    - **`3_static_methods/`**: Focuses on the `@staticmethod` decorator, for utility functions that are related to a class but do not depend on class or instance state.
    - **`4_inheritance/`**: Demonstrates how a child class can inherit and extend the functionality of a parent class.
    - **`5_class_interaction_and_composition/`**: Examples where instances of different classes interact with each other or where one class is "composed" of other objects.
    - **`6_advanced_class_design/`**: Contains more advanced class design patterns, further categorized:
        - **`6a_method_chaining/`**: Classes with methods that `return self` to allow for calling multiple methods in a single, fluid line.
        - **`6b_initialization_and_validation/`**: Classes that perform significant logic, validation, or have flexible arguments within their `__init__` method.
        - **`6c_wrappers_and_data_management/`**: Classes designed to manage resources, wrap external services, or format/parse complex data.
- **`data_normalization/`**: Includes scripts for cleaning and standardizing common data formats (e.g., emails, phone numbers). This directory also contains the project's tests.
- **`fp_concepts/`**: A collection of small, focused examples illustrating functional programming concepts in Python, such as `map`, `filter`, `reduce`, and `lambda` functions.
- **`fp_in_de/`**: Contains scripts that show the practical application of functional programming concepts in the context of data engineering tasks.

## Key Files

- **`data_normalization/normalize_emails.py`**: An example of a data normalization script.
- **`data_normalization/test_data_normalize_emails.py`**: An example of a test file.
- **`class_fundamentals/5_class_interaction_and_composition/class_member_book_clean.py`**: A good example of a more complex class interaction.

## User Preferences

The user has established a custom command, `sync`, which encapsulates the entire Git workflow for committing and pushing changes. When invoked, it performs the following actions:

1.  **Detects Changes:** It begins by running `git status` to find any new, modified, or deleted files in the repository.
2.  **Stages All Files:** It stages all detected changes using `git add .`.
3.  **Generates a Commit Message:** It reads the content of the staged files and intelligently creates a descriptive commit message that summarizes the changes.
4.  **Requires User Approval:** It presents the generated commit message to the user for approval, ensuring the user has the final say before any changes are committed.
5.  **Commits, Pushes, and Cleans Up:** Once the user approves the message, it automatically commits the changes, pushes them to the `origin master` branch, and removes any temporary files used during the process.

Essentially, it's a single command to automate the entire sequence of staging, committing, and pushing code, complete with an AI-generated commit message.