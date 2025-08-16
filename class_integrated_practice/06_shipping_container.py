"""
Design a shipping container management system that handles different types of cargo containers.

Concepts practiced:
- Basic inheritance (parent-child class relationships)
- Parent constructor calling (super().__init__() usage)
- Method extension (enhancing parent behavior in child classes)

Business Requirements:
- Track basic container information and cargo capacity
- Support specialized container types with additional features
- Calculate shipping costs based on container specifications
- Monitor container status and location tracking
- Handle loading and capacity management

Your stakeholder says: "We have standard shipping containers, but we also handle
refrigerated containers that need temperature control. Both share basic info like
ID, weight, location, but the refrigerated ones have extra requirements. We need
to calculate shipping costs differently for each type."

# Test your class:
standard = ShippingContainer("CONT001", max_weight=1000, location="Port A")
refrigerated = RefrigeratedContainer("REFR001", max_weight=800, location="Port B", temp_range=(-20, 5))

standard.load_cargo(500)
refrigerated.load_cargo(300)
refrigerated.set_temperature(-15)

print(standard.get_shipping_cost())      # Expected: cost based on standard rates
print(refrigerated.get_shipping_cost())  # Expected: higher cost due to refrigeration
print(standard.get_status())             # Expected: basic container status
print(refrigerated.get_status())         # Expected: status including temperature info
"""

import re


class ShippingContainer:
    """
    Represents a shipping container with a unique identifier, maximum weight capacity,
    current location, and cargo management functionality.

    The ShippingContainer class provides methods to validate container IDs, load cargo,
    calculate available capacity, compute shipping costs, and report container status.
    Container IDs must follow the format of four uppercase letters followed by a number
    between 001 and 999. Cargo can be loaded up to the specified maximum weight, and
    shipping costs are calculated based on the cargo weight in hundredweight (CWT).

    Attributes:
        id_pattern (re.Pattern): Regex pattern for validating container IDs.
        shipping_rate_cwt (int): Shipping rate per hundredweight (CWT).
        max_weight (int): Maximum weight capacity of the container in pounds.

    Raises:
        ValueError: If max_weight is negative, location is empty, or container_id does
            not match the required format.

    Methods:
        get_available_capacity(): Returns remaining weight capacity in the container.
        load_cargo(weight): Loads cargo if there is sufficient capacity.
        get_shipping_cost(): Calculates shipping cost for the container's cargo.
        get_status(): Returns a formatted string of the container's current status.
    """

    id_pattern = re.compile((r"[A-Z]{4}(?:00[1-9]|0[1-9][0-9]|[1-9][0-9]{2})"))
    shipping_rate_cwt = 2

    def __init__(self, container_id: str, max_weight: int, location: str) -> None:
        """
        Initializes a ShippingContainer instance with the specified container ID, maximum weight, and location.

        Args:
            container_id (str): The unique identifier for the shipping container.
            max_weight (int): The maximum weight capacity of the container.
            location (str): The current location of the container.

        Raises:
            TypeError: If container_id is not a string or max_weight is not an integer.
            ValueError: If max_weight is less than 0 or location is an empty string.
        """
        if not isinstance(container_id, str):
            raise TypeError(
                f"Container ID parameter should be a string, got {container_id} of type {type(container_id).__name__}"
            )
        self.container_id = self._validate_id(container_id)

        if not isinstance(max_weight, int):
            raise TypeError(
                f"Max weight parameter should be an int, got {max_weight} of type {type(max_weight).__name__}"
            )
        if max_weight < 0:
            raise ValueError("Max weight cannot be negative")
        # Assume max_weight is cargo-only (container weight already accounted for)
        self.max_weight = max_weight
        self.cargo = 0

        if not location:
            raise ValueError("Location parameter is empty string")
        self.location = location

    def get_available_capacity(self) -> int:
        """
        Returns the remaining weight capacity available in the shipping container.

        Returns:
            int: The difference between the container's maximum weight and the current cargo weight.
        """
        return self.max_weight - self.cargo

    def load_cargo(self, weight: int) -> str:
        """
        Loads cargo onto the container if there is sufficient available capacity.

        Args:
            weight (int): The weight of the cargo to be loaded.

        Returns:
            str: Confirmation message indicating successful loading of cargo.

        Raises:
            ValueError: If the cargo weight exceeds the available capacity of the container.
        """
        if weight > self.get_available_capacity():
            raise ValueError(
                f"Attempted cargo weight to load on container: {weight} is above the available capacity."
            )
        self.cargo += weight
        return f"Cargo succesfully loaded on the container: {weight} added."

    def get_shipping_cost(self) -> float:
        """
        Calculates the shipping cost for the container's cargo.

        Returns:
            float: The total shipping cost, computed as the cargo weight in hundredweight (CWT)
                 multiplied by the shipping rate per CWT.
        """
        cargo_in_cwt = self._weight_to_cwt(self.cargo)
        return cargo_in_cwt * ShippingContainer.shipping_rate_cwt

    def get_status(self) -> str:
        """
        Returns a formatted string representing the current status of the shipping container,
        including its ID, location, maximum weight capacity, cargo loaded, and available capacity.

        Returns:
            str: A multi-line string detailing the container's status.
        """
        return (
            f"Container Status:\n"
            f"  ID: {self.container_id}\n"
            f"  Location: {self.location}\n"
            f"  Max Weight: {self.max_weight} lbs\n"
            f"  Cargo Loaded: {self.cargo} lbs\n"
            f"  Available Capacity: {self.max_weight - self.cargo} lbs"
        )

    @staticmethod
    def _validate_id(container_id: str) -> str:
        """
        Validate a shipping container ID format.

        Validates that the container ID matches the expected pattern of 4 uppercase
        letters followed by a number between 001-999.

        Args:
            container_id (str): The container ID string to validate.

        Returns:
            str: The validated container ID if it matches the required pattern.

        Raises:
            ValueError: If the container ID does not match the expected format
                        of 4 uppercase letters + number 001-999.
        """
        if not ShippingContainer.id_pattern.fullmatch(container_id):
            raise ValueError(
                f"Invalid code {container_id}: expected 4 uppercase letters + number 001-999"
            )
        return container_id

    @staticmethod
    def _weight_to_cwt(weight: int) -> float:
        """
        Converts a weight in pounds to hundredweight (cwt).

        Args:
            weight (int): The weight in pounds.

        Returns:
            float: The equivalent weight in hundredweight (cwt).
        """
        return weight / 100


class RefrigeratedContainer(ShippingContainer):
    """
    A specialized ShippingContainer that supports temperature control for refrigerated cargo.

    Attributes:
        REFRIGERATED_TEMP_MIN (int): Minimum allowable temperature for the container (-30°C).
        REFRIGERATED_TEMP_MAX (int): Maximum allowable temperature for the container (50°C).
        shipping_rate_cwt (int): Shipping rate per hundredweight (CWT) for refrigerated cargo.

        max_weight (int): Maximum weight capacity of the container in pounds.

        ValueError: If temp_range does not contain exactly two elements or is outside allowed limits.

    Methods:
        set_temperature(temperature: int) -> str:
            Sets the container's temperature after validation.

        get_shipping_cost() -> float:
            Calculates the shipping cost based on cargo weight and shipping rate.

        get_status() -> str:
            Returns a formatted string representing the container's current status.

        _validate_temperature(temperature: int) -> int:
            Validates that the temperature is an integer within the allowed range.

        _validate_temp_range(temp_range: tuple[int, int]) -> tuple[int, int]:
            Validates that the temperature range is within the allowed refrigerated container limits.
    """

    REFRIGERATED_TEMP_MIN = -30
    REFRIGERATED_TEMP_MAX = 50
    shipping_rate_cwt = 3

    def __init__(
        self,
        container_id: str,
        max_weight: int,
        location: str,
        temp_range: tuple[int, int],
    ) -> None:
        """
        Initializes a shipping container with temperature control.

        Args:
            container_id (str): Unique identifier for the container.
            max_weight (int): Maximum weight capacity of the container.
            location (str): Current location of the container.
            temp_range (tuple[int, int]): Acceptable temperature range (min, max) for the container.

        Raises:
            TypeError: If temp_range is not a tuple or its elements are not integers.
            ValueError: If temp_range does not contain exactly two elements.
        """
        super().__init__(container_id, max_weight, location)

        if not isinstance(temp_range, tuple):
            raise TypeError(
                f"{temp_range} should be a tuple, got {type(temp_range).__name__}"
            )
        if len(temp_range) != 2:
            raise ValueError(f"{temp_range} must contain exactly two integers")
        if type(temp_range[0]) is not int:
            raise TypeError(
                f"{temp_range[0]} must be int, got {type(temp_range[0]).__name__}"
            )
        if type(temp_range[1]) is not int:
            raise TypeError(
                f"{temp_range[1]} must be int, got {type(temp_range[1]).__name__}"
            )
        self.temp_range = self._validate_temp_range(temp_range)

        self.temperature = 0

    def set_temperature(self, temperature: int) -> str:
        """
        Sets the temperature of the container after validating the input.

        Args:
            temperature (int): The desired temperature to set for the container.

        Returns:
            str: Confirmation message indicating the temperature has been set.

        Raises:
            ValueError: If the provided temperature is not within the valid range.
        """
        temperature = self._validate_temperature(temperature)

        self.temperature = temperature
        return f"Temperature on the container succesfully set to: {temperature}."

    def get_shipping_cost(self) -> float:
        """
        Calculates the shipping cost for the container's cargo.

        Returns:
            float: The total shipping cost, computed as the cargo weight in hundredweight (CWT)
                 multiplied by the shipping rate per CWT.
        """
        cargo_in_cwt = self._weight_to_cwt(self.cargo)
        return cargo_in_cwt * RefrigeratedContainer.shipping_rate_cwt

    def get_status(self) -> str:
        """
        Returns a formatted string representing the current status of the shipping container,
        including its ID, location, maximum weight capacity, cargo loaded, available capacity,
        temperature range and current temperature.

        Returns:
            str: A multi-line string detailing the container's status.
        """
        return (
            f"Container Status:\n"
            f"  ID: {self.container_id}\n"
            f"  Location: {self.location}\n"
            f"  Max Weight: {self.max_weight} lbs\n"
            f"  Cargo Loaded: {self.cargo} lbs\n"
            f"  Available Capacity: {self.max_weight - self.cargo} lbs\n"
            f"  Temperature Range: {self.temp_range} \n"
            f"  Current Temperature: {self.temperature}"
        )

    def _validate_temperature(self, temperature: int) -> int:
        """
        Validates that the given temperature is an integer and within the container's configured temperature range.

        Args:
            temperature (int): The temperature value to validate.

        Returns:
            int: The validated temperature value.

        Raises:
            TypeError: If the temperature is not an integer.
            ValueError: If the temperature is outside the container's allowed range.
        """
        if type(temperature) is not int:
            raise TypeError(
                f"{temperature} should be an int, got {type(temperature).__name__}"
            )
        low, high = self.temp_range

        if not (low <= temperature <= high):
            raise ValueError(
                f"Temperature: {temperature} has to be between {low} and {high}"
            )
        return temperature

    @staticmethod
    def _validate_temp_range(temp_range: tuple[int, int]) -> tuple[int, int]:
        """
        Validates that the provided temperature range is within the allowed refrigerated container limits.

        Args:
            temp_range (tuple[int, int]): A tuple containing the minimum and maximum temperatures.

        Raises:
            ValueError: If the minimum temperature is greater than the maximum temperature.
            ValueError: If the minimum temperature is outside the allowed range.
            ValueError: If the maximum temperature is outside the allowed range.

        Returns:
            tuple[int, int]: The validated temperature range.
        """
        min_temp, max_temp = temp_range
        LO = RefrigeratedContainer.REFRIGERATED_TEMP_MIN
        HI = RefrigeratedContainer.REFRIGERATED_TEMP_MAX

        if min_temp > max_temp:
            raise ValueError(
                f"Min temp: {min_temp} cannot be larger than Max temp: {max_temp}"
            )
        if not (LO <= min_temp <= HI):
            raise ValueError(f"Min temp: {min_temp} has to be between {LO} and {HI}")
        if not (LO <= max_temp <= HI):
            raise ValueError(f"Max temp: {max_temp} has to be between {LO} and {HI}")

        return temp_range


# Test your class:
standard = ShippingContainer("CONT001", max_weight=1000, location="Port A")
refrigerated = RefrigeratedContainer(
    "REFR001", max_weight=800, location="Port B", temp_range=(-20, 5)
)

standard.load_cargo(500)
refrigerated.load_cargo(300)
refrigerated.set_temperature(-15)

print(standard.get_shipping_cost())  # Expected: cost based on standard rates
print(refrigerated.get_shipping_cost())  # Expected: higher cost due to refrigeration
print(standard.get_status())  # Expected: basic container status
print(refrigerated.get_status())  # Expected: status including temperature info

"""
=== BUSINESS COMMUNICATION SUMMARY ===

Initial Request: "We have standard shipping containers, but we also handle refrigerated containers 
that need temperature control. Both share basic info like ID, weight, location, but the refrigerated 
ones have extra requirements. We need to calculate shipping costs differently for each type."

Developer Clarifications Asked:
- Do container IDs follow a particular format for standardization?
- Is there a minimum weight requirement for shipping containers?
- Are there predetermined valid locations, or should location validation be flexible?
- How exactly should shipping costs be calculated? Which rates apply?
- Does only weight (and refrigeration) affect shipping costs, or are there other factors?
- What specific information should be included in container status monitoring?
- Should location tracking be integrated into status reporting or handled separately?
- What are reasonable temperature ranges for refrigerated container equipment?
- Should temperature validation enforce global equipment limits or container-specific ranges?

Stakeholder Responses:
- Container IDs should follow some standard format with letters and numbers for uniqueness
- No specific minimum weight requirements - just ensure they're not negative
- Keep location validation flexible - we ship everywhere and constantly add new locations
- Shipping costs based on weight: $2 per 100 lbs (CWT) for standard, $3 per 100 lbs for refrigerated
- For now, focus on weight-based pricing (distance calculations are complex for later)
- Status should show location, cargo weight, capacity, and any operational issues
- Include location in status - operators need all info in one view
- Temperature equipment typically operates from -30°F to 50°F for business operations
- Each container should enforce its own operational temperature range within global limits

Final Technical Decisions:
- Container ID format: 4 uppercase letters + 001-999 (e.g., CONT001, REFR001)
- Weight validation: non-negative integers, no minimum weight restriction
- Location validation: non-empty strings for maximum operational flexibility
- Inheritance pattern: RefrigeratedContainer extends ShippingContainer using super().__init__()
- Method overriding: get_shipping_cost() for different rates, get_status() for enhanced info
- Temperature system: Global equipment limits (-30°C to 50°C) with container-specific ranges
- Validation approach: Container-specific temperature validation rather than global limits
- Cost calculation: Simple weight-based pricing in hundredweight (CWT) units

Assumptions Documented:
- max_weight represents cargo capacity only (container tare weight already accounted for)
- Each refrigerated container defines its own operational temperature range within equipment limits
- Container-specific temperature validation prevents impossible settings for individual units
- Location tracking integrated into status reporting for operational efficiency
- Shipping cost calculation simplified to weight-only (distance-based pricing deferred)
- Regular expressions used for container ID validation to ensure format consistency
- Temperature ranges must be logically valid (minimum ≤ maximum) and within equipment limits

Technical Enhancement Made:
- Initial implementation used global temperature limits for validation
- Enhanced to container-specific range validation for more realistic business logic
- Each container now enforces its own operational capabilities rather than generic limits
- Prevents setting temperatures outside individual container's actual range specifications

Business Value Delivered:
- Flexible container management system supporting multiple container types
- Proper inheritance structure allows easy addition of new specialized container types
- Comprehensive validation ensures data integrity and operational safety
- Cost calculation system ready for different pricing models
- Professional error handling provides clear feedback for operational staff
- Temperature control system prevents equipment damage and cargo spoilage
- Status reporting provides complete operational visibility in single interface
"""
