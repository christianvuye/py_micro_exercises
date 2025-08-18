"""
Create a restaurant management system that handles different types of dining establishments with specialized features at each level.

Concepts practiced:
- Three-level inheritance chain (progressive specialization)
- Method resolution order (MRO) in complex hierarchies
- Constructor chaining with super() across multiple levels
- Method overriding and extension at each inheritance level
- Progressive feature addition from general to specific

Business Requirements:
- Track basic restaurant operations and customer service
- Support fast food establishments with efficiency metrics
- Handle drive-thru locations with vehicle-specific service features
- Each level should add specialized functionality while maintaining parent capabilities
- Monitor performance metrics specific to each restaurant type

Your stakeholder says: "We're expanding our restaurant chain and need a system that
can handle our regular sit-down restaurants, fast food locations, and drive-thru spots.
Each type builds on the previous - all restaurants serve customers and track sales,
fast food places also track order speed and efficiency, and drive-thru adds vehicle
handling and lane management. We need this to scale as we add more location types."

# Test your classes:
restaurant = Restaurant("Downtown Bistro", max_capacity=50)
fast_food = FastFood("Quick Burger", max_capacity=30, target_service_time=3)
drive_thru = DriveThru("Speedy Drive", max_capacity=20, target_service_time=2, num_lanes=2)

# Test basic restaurant functionality
restaurant.serve_customer()
restaurant.add_sale(25.50)

# Test fast food functionality
fast_food.serve_customer()
fast_food.add_sale(12.99)
fast_food.record_service_time(2.5)

# Test drive-thru functionality
drive_thru.serve_customer()
drive_thru.add_sale(8.75)
drive_thru.record_service_time(1.8)
drive_thru.process_vehicle("car")
drive_thru.process_vehicle("truck")

print(restaurant.get_status())      # Expected: basic restaurant info
print(fast_food.get_status())       # Expected: restaurant info + efficiency metrics
print(drive_thru.get_status())      # Expected: all info + vehicle/lane data
print(drive_thru.get_lane_status()) # Expected: lane utilization info
"""

import re


class Restaurant:
    """
    Represents a restaurant with a name, maximum capacity, customer count, and total sales.

    Provides validation for attributes, customer service, sales recording, and status reporting.

    Attributes:
        RESTAURANT_NAME_PATTERN (re.Pattern): Regular expression for validating restaurant names.
        MIN_CAPACITY (int): Minimum allowed capacity.
        MAX_CAPACITY (int): Maximum allowed capacity.
    """

    RESTAURANT_NAME_PATTERN = re.compile(
        r"^(?=.{3,50}$)[A-Za-z0-9](?:[A-Za-z0-9 '\u2019-]*[A-Za-z0-9])$"
    )

    MIN_CAPACITY = 10
    MAX_CAPACITY = 500

    def __init__(self, name: str, max_capacity: int) -> None:
        """
        Initializes a new instance of the class with the specified name and maximum capacity.

        Args:
            name (str): The name of the restaurant.
            max_capacity (int): The maximum capacity of the restaurant.

        Raises:
            TypeError: If name is not a string or max_capacity is not an integer.
            ValueError: If the name is invalid or max_capacity is out of allowed range.
        """
        self.name = self._validate_name(name)
        self.max_capacity = self._validate_max_capacity(max_capacity)
        self.customer_count = 0
        self.total_sales = 0.0

    def serve_customer(self) -> int:
        """
        Increments the customer count by one and returns the updated count.

        Returns:
            int: The updated number of customers served.

        Raises:
            ValueError: If the restaurant is at full capacity and cannot serve more customers.
        """
        if self.customer_count == self.max_capacity:
            raise ValueError(
                f"The restaurant is at full capacity already: {self.max_capacity}"
            )
        self.customer_count += 1
        return self.customer_count

    def add_sale(self, amount: float) -> None:
        """
        Adds a sale to the total sales after validating the sale amount.

        Parameters:
            amount (float): The amount of the sale to be added.

        Returns:
            None
        """
        amount = self._validate_sale_amount(amount)
        self.total_sales += amount

    def get_total_sales(self) -> float:
        """
        Returns the total sales for the restaurant.

        Returns:
            float: The total sales amount.
        """
        return self.total_sales

    def get_status(self) -> str:
        """
        Returns a formatted string containing the restaurant's name, maximum capacity,
        number of customers served, and total sales.

        Returns:
            str: A summary of the restaurant's current status.
        """
        return (
            f"Restaurant: {self.name}\n"
            f"Max Capacity: {self.max_capacity}\n"
            f"Customers Served: {self.customer_count}\n"
            f"Total Sales: ${self.total_sales:.2f}"
        )

    @staticmethod
    def _validate_sale_amount(amount: float) -> float:
        """
        Validates that the sale amount is a positive float.

        Args:
            amount (float): The sale amount to validate.

        Returns:
            float: The validated sale amount.

        Raises:
            TypeError: If the amount is not a float.
            ValueError: If the amount is not positive.
        """
        if not isinstance(amount, float):
            raise TypeError(f"{amount} should be a float, got {type(amount).__name__}")
        if amount <= 0:
            raise ValueError("Sale amount must be positive")
        return amount

    @staticmethod
    def _validate_name(name: str) -> str:
        """
        Validates that the provided name is a non-empty string matching the restaurant naming pattern.

        Args:
            name (str): The name to validate.

        Returns:
            str: The validated name.

        Raises:
            TypeError: If name is not a string.
            ValueError: If name is an empty string or does not match the naming pattern.
        """
        if not isinstance(name, str):
            raise TypeError(f"{name} has to be str, got {type(name).__name__}")
        if not name:
            raise ValueError(f"{name} cannot be an empty string")
        if not Restaurant.RESTAURANT_NAME_PATTERN.fullmatch(name):
            raise ValueError(f"{name} is not a valid name")
        return name

    @staticmethod
    def _validate_max_capacity(max_capacity: int) -> int:
        """
        Validates that the provided max_capacity is an integer within the allowed range.

        Args:
            max_capacity (int): The maximum capacity to validate.

        Returns:
            int: The validated maximum capacity.

        Raises:
            TypeError: If max_capacity is not an integer.
            ValueError: If max_capacity is less than Restaurant.MIN_CAPACITY or greater than Restaurant.MAX_CAPACITY.
        """
        if type(max_capacity) is not int:
            raise TypeError(
                f"{max_capacity} has to be an int, got {type(max_capacity).__name__}"
            )
        if max_capacity < Restaurant.MIN_CAPACITY:
            raise ValueError(
                f"{max_capacity} is too low. Minimum is {Restaurant.MIN_CAPACITY}"
            )
        if max_capacity > Restaurant.MAX_CAPACITY:
            raise ValueError(
                f"{max_capacity} is too high. Maximum capacity is {Restaurant.MAX_CAPACITY}"
            )
        return max_capacity


class FastFood(Restaurant):
    """
    Represents a fast food restaurant with service time tracking and performance metrics.

    Attributes:
        TARGET_SERVICE_TIME_MIN (float): Minimum allowed service time in minutes.
        TARGET_SERVICE_TIME_MAX (float): Maximum allowed service time in minutes.
        PERFORMANCE_TARGET_SERVICE_TIME (float): Service time threshold for performance evaluation.

    Methods:
        record_service_time(service_time): Records a service time and checks if it meets the target.
        get_average_service_time(): Returns the average of recorded service times.
        get_service_target_met_percentage(): Returns the percentage of service times meeting the performance target.
        get_status(): Returns a summary of the restaurant's status and performance metrics.
    """

    TARGET_SERVICE_TIME_MIN = 0.5
    TARGET_SERVICE_TIME_MAX = 15.0
    PERFORMANCE_TARGET_SERVICE_TIME = 4.0

    def __init__(
        self, name: str, max_capacity: int, target_service_time: int | float
    ) -> None:
        """
        Initialize a new instance of the class.

        Args:
            name (str): The name of the restaurant.
            max_capacity (int): The maximum number of guests the restaurant can accommodate.
            target_service_time (int | float): The target time (in minutes) to serve a guest.

        Raises:
            TypeError: If target_service_time is not an int or float.
            ValueError: If target_service_time is not a positive number.
        """
        super().__init__(name=name, max_capacity=max_capacity)
        self.target_service_time = self._validate_service_time(target_service_time)
        self.service_times = []

    def record_service_time(self, service_time: int | float) -> float:
        """
        Records a service time for the restaurant and checks if it meets the target service time.

        Args:
            service_time (int | float): The time taken to serve a customer.

        Returns:
            bool: True if the recorded service time is less than or equal to the target service time, False otherwise.
        """
        service_time = self._validate_service_time(service_time)
        self.service_times.append(service_time)
        return service_time <= self.target_service_time

    def get_average_service_time(self) -> float:
        """
        Calculates and returns the average service time.

        Returns:
            float: The average of all recorded service times.

        Raises:
            ValueError: If there are no service times recorded.
        """
        if len(self.service_times) == 0:
            raise ValueError(
                f"No service times have been recorded {self.service_times}"
            )
        return sum(self.service_times) / len(self.service_times)

    def get_service_target_met_percentage(self) -> float:
        """
        Calculates the percentage of recorded service times that meet or are below the performance target.

        Returns:
            float: The fraction of service times that are less than or equal to the PERFORMANCE_TARGET_SERVICE_TIME.

        Raises:
            ValueError: If no service times have been recorded.
        """
        if len(self.service_times) == 0:
            raise ValueError(
                f"No service times have been recorded {self.service_times}"
            )
        count = 0
        for service_time in self.service_times:
            if service_time <= FastFood.PERFORMANCE_TARGET_SERVICE_TIME:
                count += 1
        return count / len(self.service_times)

    def get_status(self) -> str:
        """
        Returns a formatted string containing the fast food restaurant's name, maximum capacity,
        number of customers served, total sales, target service time, and performance statistics.

        Returns:
            str: A summary of the fast food restaurant's current status and performance metrics.
        """
        avg_service_time = (
            self.get_average_service_time() if self.service_times else "N/A"
        )
        service_target_pct = (
            self.get_service_target_met_percentage() if self.service_times else "N/A"
        )
        min_service_time = min(self.service_times) if self.service_times else "N/A"
        max_service_time = max(self.service_times) if self.service_times else "N/A"
        return (
            f"FastFood Restaurant: {self.name}\n"
            f"Max Capacity: {self.max_capacity}\n"
            f"Customers Served: {self.customer_count}\n"
            f"Total Sales: ${self.total_sales:.2f}\n"
            f"Target Service Time: {self.target_service_time} min\n"
            f"Average Service Time: {avg_service_time if avg_service_time == 'N/A' else f'{avg_service_time:.2f}'} min\n"
            f"Service Target Met %: {service_target_pct if service_target_pct == 'N/A' else f'{service_target_pct * 100:.1f}'}%\n"
            f"Min Service Time: {min_service_time if min_service_time == 'N/A' else f'{min_service_time:.2f}'} min\n"
            f"Max Service Time: {max_service_time if max_service_time == 'N/A' else f'{max_service_time:.2f}'} min"
        )

    @staticmethod
    def _validate_service_time(service_time: int | float) -> float:
        """
        Validates and rounds the service time for a fast food restaurant.

        Args:
            service_time (int | float): The desired service time to validate.

        Returns:
            float: The validated and rounded service time.

        Raises:
            TypeError: If service_time is not an int or float.
            ValueError: If service_time is outside the allowed minimum and maximum bounds
                defined by FastFood.TARGET_SERVICE_TIME_MIN and FastFood.TARGET_SERVICE_TIME_MAX.
        """
        if not isinstance(service_time, float) and type(service_time) is not int:
            raise TypeError(
                f"{service_time} should be a float or int, got {type(service_time).__name__}"
            )
        target_service_time = round(float(service_time), 1)
        if target_service_time < FastFood.TARGET_SERVICE_TIME_MIN:
            raise ValueError(
                f"{service_time} is too low, minimum is {FastFood.TARGET_SERVICE_TIME_MIN}"
            )
        if target_service_time > FastFood.TARGET_SERVICE_TIME_MAX:
            raise ValueError(
                f"{service_time} is too high, maximum is {FastFood.TARGET_SERVICE_TIME_MAX}"
            )
        return service_time


class DriveThru(FastFood):
    """
    DriveThru class represents a drive-thru facility for a fast food restaurant, managing multiple lanes and vehicle assignments.

    Attributes:
        MIN_NUM_LANES (int): Minimum number of drive-thru lanes allowed.
        MAX_NUM_LANES (int): Maximum number of drive-thru lanes allowed.
        VEHICLE_TYPES_ALLOWED (tuple): Vehicle types permitted in the drive-thru.
        VEHICLE_TYPES_NOT_ALLOWED (tuple): Vehicle types not permitted in the drive-thru.

    Methods:
        process_vehicle: Assigns a vehicle to a lane.
        get_lane_status: Summarizes vehicle counts per lane.
        _validate_num_lanes: Validates lane count.
        _validate_vehicle_type: Validates vehicle type.
    """

    MIN_NUM_LANES = 1
    MAX_NUM_LANES = 4
    VEHICLE_TYPES_ALLOWED = ("car", "suv", "truck", "van", "motorcycle")
    VEHICLE_TYPES_NOT_ALLOWED = ("large truck", "bus", "rv", "bicycle", "pedestrian")

    def __init__(
        self,
        name: str,
        max_capacity: int,
        target_service_time: int | float,
        num_lanes: int,
    ) -> None:
        "docstring"
        super().__init__(
            name=name,
            max_capacity=max_capacity,
            target_service_time=target_service_time,
        )
        self.num_lanes = self._validate_num_lanes(num_lanes)
        self.vehicle_count = 0
        self.next_lane = 1
        self.lane_vehicle_counts = [0] * self.num_lanes

    def process_vehicle(self, vehicle_type: str) -> int:
        """
        Assigns an incoming vehicle to a drive-thru lane and updates vehicle counts.
            int: The lane number assigned to the vehicle (1-based index).

        Details:
            - Validates the vehicle type.
            - Increments the total vehicle count.
            - Assigns the vehicle to the next available lane in a cyclic manner.
            - Updates the count of vehicles for the assigned lane.
            - Resets lane assignment to the first lane after reaching the maximum number of lanes.
        """
        vehicle_type = self._validate_vehicle_type(vehicle_type)
        self.vehicle_count += 1
        assigned_lane = self.next_lane
        self.next_lane += 1
        if self.next_lane > self.num_lanes:
            self.next_lane = 0
        self.lane_vehicle_counts[assigned_lane - 1] += 1
        return assigned_lane

    def get_lane_status(self) -> str:
        """
        Returns a summary of the current status of all lanes, including the number of vehicles in each lane,
        and identifies the busiest and slowest lanes.

        Returns:
            str: A formatted string listing the vehicle count for each lane, and indicating which lane is busiest and which is slowest.
        """
        lane_info = [
            f"Lane {i + 1}: {count} vehicles"
            for i, count in enumerate(self.lane_vehicle_counts)
        ]
        busiest_idx = max(
            range(len(self.lane_vehicle_counts)),
            key=lambda i: self.lane_vehicle_counts[i],
        )
        slowest_idx = min(
            range(len(self.lane_vehicle_counts)),
            key=lambda i: self.lane_vehicle_counts[i],
        )
        return (
            f"{', '.join(lane_info)}. "
            f"Busiest: Lane {busiest_idx + 1}, "
            f"Slowest: Lane {slowest_idx + 1}"
        )

    @staticmethod
    def _validate_num_lanes(num_lanes: int) -> int:
        """
        Validates the number of lanes for a drive-thru.

        Args:
            num_lanes (int): The number of lanes to validate.

        Returns:
            int: The validated number of lanes.

        Raises:
            TypeError: If `num_lanes` is not an integer.
            ValueError: If `num_lanes` is less than `DriveThru.MIN_NUM_LANES` or greater than `DriveThru.MAX_NUM_LANES`.
        """
        if type(num_lanes) is not int:
            raise TypeError(
                f"{num_lanes} has to be an int, got {type(num_lanes).__name__}"
            )
        if num_lanes < DriveThru.MIN_NUM_LANES:
            raise ValueError(f"{num_lanes} has to be minimum {DriveThru.MIN_NUM_LANES}")
        if num_lanes > DriveThru.MAX_NUM_LANES:
            raise ValueError(f"{num_lanes} can be maximum {DriveThru.MAX_NUM_LANES}")
        return num_lanes

    @staticmethod
    def _validate_vehicle_type(vehicle_type: str) -> str:
        """
        Validates the provided vehicle type string.

        Checks that the input is a non-empty string, strips and lowercases it,
        and ensures it is an allowed vehicle type for the drive-thru.

        Args:
            vehicle_type (str): The type of vehicle to validate.

        Returns:
            str: The validated and normalized vehicle type.

        Raises:
            TypeError: If vehicle_type is not a string.
            ValueError: If vehicle_type is empty, not allowed, or not recognized.
        """
        if not isinstance(vehicle_type, str):
            raise TypeError(
                f"{vehicle_type} should be a string, got {type(vehicle_type).__name__}"
            )
        if not vehicle_type:
            raise ValueError(f"{vehicle_type} cannot be an empty string")
        vehicle_type = vehicle_type.strip().lower()
        if vehicle_type in DriveThru.VEHICLE_TYPES_NOT_ALLOWED:
            raise ValueError(f"{vehicle_type} is not allowed")
        if vehicle_type not in DriveThru.VEHICLE_TYPES_ALLOWED:
            raise ValueError(f"{vehicle_type} is not a recognized vehicle type")
        return vehicle_type


# Test your classes:
restaurant = Restaurant("Downtown Bistro", max_capacity=50)
fast_food = FastFood("Quick Burger", max_capacity=30, target_service_time=3)
drive_thru = DriveThru(
    "Speedy Drive", max_capacity=20, target_service_time=2, num_lanes=2
)

# Test basic restaurant functionality
restaurant.serve_customer()
restaurant.add_sale(25.50)

# Test fast food functionality
fast_food.serve_customer()
fast_food.add_sale(12.99)
fast_food.record_service_time(2.5)

# Test drive-thru functionality
drive_thru.serve_customer()
drive_thru.add_sale(8.75)
drive_thru.record_service_time(1.8)
drive_thru.process_vehicle("car")
drive_thru.process_vehicle("truck")

print(restaurant.get_status())  # Expected: basic restaurant info
print(fast_food.get_status())  # Expected: restaurant info + efficiency metrics
print(drive_thru.get_status())  # Expected: all info + vehicle/lane data
print(drive_thru.get_lane_status())  # Expected: lane utilization info

"""
=== BUSINESS COMMUNICATION SUMMARY ===

Initial Request: "We're expanding our restaurant chain and need a system that can handle our regular sit-down restaurants, fast food locations, and drive-thru spots. Each type builds on the previous - all restaurants serve customers and track sales, fast food places also track order speed and efficiency, and drive-thru adds vehicle handling and lane management."

Developer Clarifications Asked:
- Should this be inheritance vs composition?
- What are capacity limits for restaurants?
- What validation is needed for restaurant names?
- What should serve_customer() and add_sale() methods do?
- Should methods return useful information?
- What are service time limits and vehicle type restrictions?
- How should lane assignment and tracking work?

Stakeholder Responses:
- Inheritance chain represents business reality (FastFood IS-A Restaurant, DriveThru IS-A FastFood)
- Capacity: 10-500 customers based on operational constraints
- Restaurant names: 3-50 characters, professional standards
- Methods should track running totals and provide immediate feedback
- Service times: 0.5-15 minutes with location-specific targets
- Vehicle types: standard vehicles only (no large trucks, buses, etc.)
- Round-robin lane assignment for even distribution

Final Technical Decisions:
- Three-level inheritance with super() constructor chaining
- Progressive method overriding (get_status enhanced at each level)
- Comprehensive input validation with business-appropriate error messages
- Simple but effective analytics (averages, percentages, min/max tracking)
- Round-robin vehicle distribution across lanes with utilization tracking

Assumptions Documented:
- Customers are served and leave quickly (no complex occupancy tracking)
- Service times stored as simple list for analytics calculations
- Lane assignment uses 1-based numbering for business clarity
- Vehicle count tracks total processed (no artificial maximum)
- Performance metrics calculated against class-level constants
"""
