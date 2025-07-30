"""
Design a movie ticketing system that handles different pricing models and customer types.

Concepts practiced:
- Class variables for shared pricing configuration
- Conditional pricing logic based on multiple factors
- Instance calculations with business rules

Business Requirements:
- Handle different ticket types (adult, child, senior)
- Support time-based pricing (matinee vs evening)
- Apply discounts for special circumstances
- Track theater capacity and ticket sales

Your stakeholder says: "We need a ticket system that charges different prices based on 
age and showtime. Kids and seniors get discounts. Matinee shows are cheaper. 
Also track how many tickets we've sold."

# Test your class:
ticket1 = MovieTicket("Avatar", "adult", "evening")
ticket2 = MovieTicket("Avatar", "child", "matinee")
ticket3 = MovieTicket("Avatar", "senior", "evening")

print(ticket1.get_price())           # Expected: varies based on your pricing
print(ticket2.get_price())           # Expected: lower than adult
print(MovieTicket.get_total_sales()) # Expected: total from all tickets
print(str(ticket1))                  # Expected: meaningful ticket description
"""

from typing import Any, List

class MovieTicket:
    BASE_ADULT_PRICE: int = 12
    BASE_CHILD_PRICE: int = 8
    BASE_SENIOR_PRICE: int = 10
    MATINEE_DISCOUNT: float = 0.8
    THEATER_CAPACITY: int = 1000
    total_tickets_sold: int = 0

    def __init__(self, movie: str, customer_type: str, showtime: str) -> None:
        """
        Initialize a MovieTicket instance, validate inputs, and increment ticket sales.

        Args:
            movie (str): The title of the movie.
            customer_type (str): The type of customer ('adult', 'child', or 'senior').
            showtime (str): The showtime for the movie ('evening' or 'matinee').

        Raises:
            TypeError: If movie or customer_type or showtime are not strings.
            ValueError: If customer_type or showtime are not valid options.
        """
        if isinstance(movie, str):
            self.movie = movie
        else:
            raise TypeError("Movie should be a string!") 
        self.customer_type = self._validate_customer_type(customer_type)
        self.showtime = self._validate_showtime(showtime)

        MovieTicket.total_tickets_sold += 1
    
    def __str__(self) -> str:
        """
        Returns a human-readable description of the ticket.
        """
        return (f"MovieTicket: '{self.movie}' | Customer: {self.customer_type.capitalize()} | "
                f"Showtime: {self.showtime.capitalize()} | Price: ${self.get_price():.2f}")
    
    def get_price(self) -> float:
        """
        Calculates and returns the ticket price based on customer type and showtime.
        
        Returns:
            float: The calculated ticket price after applying any applicable discounts.
        Notes:
            - Adult, child, and senior customers have different base prices.
            - If the showtime is a matinee, a discount is applied to the base price.
        """
        if self.customer_type == "adult":
            base_price = self.BASE_ADULT_PRICE
        elif self.customer_type == "child":
            base_price = self.BASE_CHILD_PRICE
        else:
            base_price = self.BASE_SENIOR_PRICE
        
        if self.showtime == "matinee":
            matinee_adjusted_price = base_price * self.MATINEE_DISCOUNT
            return matinee_adjusted_price
        return base_price

    @classmethod
    def get_remaining_capacity(cls) -> int:
        """
        Calculates and returns the number of remaining seats in the theater.

        Returns:
            int: The number of seats still available for sale, based on the theater's total capacity and the total tickets sold.
        """
        return cls.THEATER_CAPACITY - cls.total_tickets_sold
    
    @classmethod
    def get_total_sales(cls) -> int:
        """
        Returns the total number of tickets sold.

        Returns:
            int: The total number of tickets sold across all instances.
        """
        return cls.total_tickets_sold

    @staticmethod
    def _validate_customer_type(customer_type: Any) -> str:
        """
        Validates that the provided customer_type is a string and matches one of the allowed types: 'adult', 'child', or 'senior'.

        Args:
            customer_type (Any): The customer type to validate.

        Returns:
            str: The validated and normalized (lowercase) customer type.

        Raises:
            TypeError: If customer_type is not a string.
            ValueError: If customer_type is not one of ['adult', 'child', 'senior'].
        """
        customer_types: List[str] = ["adult", "child", "senior"]
        if not isinstance(customer_type, str):
            raise TypeError(f"{customer_type} should be a string")
        if customer_type.lower() not in customer_types:
            raise ValueError(f"{customer_type} should be one of: {customer_types}")
        return customer_type.lower()
    
    @staticmethod
    def _validate_showtime(showtime: Any) -> str:
        """
        Validates that the provided showtime is a string and one of the allowed showtimes.

        Args:
            showtime (Any): The showtime to validate.

        Returns:
            str: The validated showtime in lowercase.

        Raises:
            TypeError: If showtime is not a string.
            ValueError: If showtime is not one of the allowed showtimes ("evening", "matinee").
        """
        showtimes: List[str] = ["evening", "matinee"]
        if not isinstance(showtime, str):
            raise TypeError(f"{showtime} should be a string")
        if showtime.lower() not in showtimes:
            raise ValueError(f"{showtime} should be one of: {showtimes}")
        return showtime.lower()
    

# Test your class:
ticket1 = MovieTicket("Avatar", "adult", "evening")
ticket2 = MovieTicket("Avatar", "child", "matinee")
ticket3 = MovieTicket("Avatar", "senior", "evening")

print(ticket1.get_price())           # Expected: varies based on your pricing
print(ticket2.get_price())           # Expected: lower than adult
print(MovieTicket.get_total_sales()) # Expected: total from all tickets
print(str(ticket1))                  # Expected: meaningful ticket description

"""
=== BUSINESS COMMUNICATION SUMMARY ===

Initial Request: "We need a ticket system that charges different prices based on age and showtime. 
Kids and seniors get discounts. Matinee shows are cheaper. Also track how many tickets we've sold."

Developer Clarifications Asked:
- Should "special circumstances" include additional discount types beyond matinee pricing?
- What should theater capacity be set to?
- Should get_total_sales() return count or revenue?

Stakeholder Responses:  
- Keep discounts simple - matinee pricing covers the special circumstances requirement
- Developer discretion on theater capacity (chose 1000 seats)
- Total sales should return ticket count for operational tracking

Final Technical Decisions:
- Class variables for all pricing configuration (easy to modify)
- Matinee discount as the primary "special circumstance"
- Added theater capacity tracking for future operational needs
- Used appropriate method decorators (@classmethod vs @staticmethod)

Assumptions Documented:
- Integer base prices converted to float for discount calculations
- Theater capacity of 1000 seats (reasonable for mid-size venue)
- Ticket counting rather than revenue tracking for get_total_sales()
"""