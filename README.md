# Python Practice Microprojects

A collection of Python microprojects and exercises for practicing small problems, coding katas, and fundamental concepts. This repository serves as a hands-on learning environment for various Python programming patterns and techniques.

## Repository Structure

### Current Topics

#### Data Normalization (`data_normalization/`)
Real-world data processing functions with comprehensive test suites:
- **Email normalization**: Clean and validate email addresses from multiple sources
- **Phone number normalization**: Standardize phone number formats
- **Product name normalization**: Clean product names from different vendors

#### Functional Programming Concepts (`data_normalization/fp_concepts/`)
Educational exercises organized by technique:
- **Lambda functions**: 35+ exercises on anonymous functions
- **List comprehensions**: 25+ exercises on Pythonic collection processing
- **Map operations**: 30+ exercises on applying transformations
- **Filter operations**: 15+ exercises on data filtering
- **Reduce operations**: 10+ exercises on aggregation patterns
- **Combined patterns**: Lambda + list comprehension combinations

#### Functional Programming in Data Engineering (`data_normalization/fp_in_de/`)
Advanced exercises with real-world data engineering scenarios:
- **Map transformations**: API response processing, data conversion, ETL operations
- **Filter operations**: Data quality checks, validation, record filtering

## Future Expansion

This repository will grow to include exercises on:
- **Python Backend Development**: API design, database operations, web frameworks
- **Python Data Engineering**: ETL pipelines, data processing, analytics
- **Python AI/ML**: Machine learning workflows, data science patterns
- **Additional Python concepts**: As learning progresses

## Getting Started

### Running Tests
```bash
python test_data_normalize_emails.py
python test_data_normalize_phone_numbers.py
python test_data_normalize_product_names.py
```

### Running Individual Exercises
```bash
python data_normalization/fp_concepts/lambda/lambda_square.py
python data_normalization/fp_concepts/map/map_squared.py
```

Each exercise file contains a focused implementation of a single concept, making it easy to practice and understand specific patterns.

## Philosophy

These microprojects follow the coding kata philosophy - small, focused exercises that can be completed quickly but provide deep learning through repetition and variation. Each exercise is designed to:

- Focus on a single concept or pattern
- Provide immediate feedback through execution
- Build muscle memory for common programming tasks
- Prepare for real-world application scenarios

Perfect for daily practice, interview preparation, or exploring new Python concepts.