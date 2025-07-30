"""
Build a fitness tracking application that monitors individual workouts and provides global statistics.

Concepts practiced:
- Class vs instance variables (individual vs global data)
- Aggregation methods (calculating totals, averages from collections)
- Class methods for global statistics across all users

Business Requirements:
- Track individual user workout sessions and progress DONE
- Support different exercise types and intensities  NOT DONE -> clarify what different types and intensitites business stakeholder wants
- Provide personal statistics for each user DONE
- Generate community-wide fitness insights NOT DONE
- Handle various measurement units and data validation NOT DONE -> clarify what different units business stakeholder wants

Your stakeholder says: "We're building a fitness app. Users log workouts - steps, 
calories, exercise minutes. We need personal stats for each user, but also want to 
see community totals across all our users for marketing purposes."

# Test your class:
user1 = FitnessTracker("Alice")
user1.log_workout(steps=8000, calories=300, minutes=45)  
user1.log_workout(steps=12000, calories=450, minutes=60)

user2 = FitnessTracker("Bob")
user2.log_workout(steps=5000, calories=200, minutes=30)

print(user1.get_total_steps())           # Expected: 20000
print(user1.get_average_calories())      # Expected: 375.0
print(FitnessTracker.get_global_stats()) # Expected: community-wide data
print(str(user1))                        # Expected: user summary
"""

class FitnessTracker:
    global_total_users: int = 0
    global_total_steps: int = 0
    global_total_calories: int = 0
    global_total_minutes: int = 0
    global_total_workouts: int = 0

    def __init__(self, name: str) -> None:
        """
        Initializes a new FitnessTracker instance with the specified name and sets all tracking attributes to zero.

        Args:
            name (str): The name to assign to the user of the fitness tracker.

        Raises:
            TypeError: If the provided name is not a string.
        """
        if not isinstance(name, str):
            raise TypeError(f"{name} is not a string!")
        
        self.name = name
        self.total_steps = 0
        self.total_calories = 0
        self.total_minutes = 0
        self.total_workouts = 0
        FitnessTracker.global_total_users += 1
    
    def __str__(self) -> str:
        """
        Returns a human-readable description of the Fitness Tracker instance.

        Returns:
            str: A summary of the user's fitness statistics.
        """
        return (f"User: {self.name}\n"
                f"Total Workouts: {self.total_workouts}\n"
                f"Total Steps: {self.total_steps}\n"
                f"Total Calories: {self.total_calories}\n"
                f"Total Minutes: {self.total_minutes}\n"
                f"Average Steps per Workout: {self.get_average_steps():.1f}\n"
                f"Average Calories per Workout: {self.get_average_calories():.1f}\n"
                f"Average Minutes per Workout: {self.get_average_minutes():.1f}")
    
    def log_workout(self, steps: int, calories: int, minutes: int) -> None:
        """
        Logs a workout session by updating the user's and class's total steps, calories, minutes, and workout count.

        Args:
            steps (int): The number of steps taken during the workout.
            calories (int): The number of calories burned during the workout.
            minutes (int): The duration of the workout in minutes.

        Raises:
            TypeError: If any of the arguments (steps, calories, minutes) are not integers.
        """
        if not isinstance(steps, int):
            raise TypeError(f"{steps} is not an integer")
        if not isinstance(calories, int):
            raise TypeError(f"{calories} is not an integer")
        if not isinstance(minutes, int):
            raise TypeError(f"{minutes} is not an integer")

        self.total_steps += steps
        self.total_calories += calories
        self.total_minutes += minutes
        self.total_workouts += 1

        FitnessTracker.global_total_steps += steps
        FitnessTracker.global_total_calories += calories
        FitnessTracker.global_total_minutes += minutes
        FitnessTracker.global_total_workouts += 1
    
    def get_total_steps(self) -> int:
        """
        Gets the total number of steps logged by the user.

        Returns:
            int: The total number of steps recorded for this user.
        """
        return self.total_steps
    
    def get_total_calories(self) -> int:
        """
        Gets the total number of calories burned by the user.

        Returns:
            int: The total number of calories recorded for this user.
        """
        return self.total_calories
    
    def get_total_minutes(self) -> int:
        """
        Gets the total number of workout minutes logged by the user.

        Returns:
            int: The total number of minutes recorded for this user.
        """
        return self.total_minutes
    
    def get_total_workouts(self) -> int:
        """
        Gets the total number of workouts logged by the user.

        Returns:
            int: The total number of workouts recorded for this user.
        """
        return self.total_workouts
    
    def get_average_steps(self) -> float:
        """
        Calculates the average number of steps per workout for the user.

        Returns:
            float: The average steps per workout. Returns 0 if no workouts have been logged.
        """
        if self.total_workouts == 0:
            return 0
        
        return self.total_steps / self.total_workouts
    
    def get_average_calories(self) -> float:
        """
        Calculates the average number of calories burned per workout for the user.

        Returns:
            float: The average calories burned per workout. Returns 0 if no workouts have been logged.
        """
        if self.total_workouts == 0:
            return 0
        
        return self.total_calories / self.total_workouts
    
    def get_average_minutes(self) -> float:
        """
        Calculates the average number of minutes per workout for the user.

        Returns:
            float: The average minutes per workout. Returns 0 if no workouts have been logged.
        """
        if self.total_workouts == 0:
            return 0
        
        return self.total_minutes / self.total_workouts
    
    @classmethod
    def get_global_stats(cls) -> str:
        """
        Gets a formatted string of the community-wide fitness statistics.

        Returns:
            str: A summary of total users, workouts, steps, calories, minutes, and averages per workout for all users.
        """
        if cls.global_total_workouts == 0:
            avg_steps = avg_calories = avg_minutes = 0.0
        else:
            avg_steps = cls.global_total_steps / cls.global_total_workouts
            avg_calories = cls.global_total_calories / cls.global_total_workouts
            avg_minutes = cls.global_total_minutes / cls.global_total_workouts

        return (
            f"Community Fitness Stats:\n"
            f"Total Users: {cls.global_total_users}\n"
            f"Total Workouts: {cls.global_total_workouts}\n"
            f"Total Steps: {cls.global_total_steps}\n"
            f"Total Calories: {cls.global_total_calories}\n"
            f"Total Minutes: {cls.global_total_minutes}\n"
            f"Average Steps per Workout: {avg_steps:.1f}\n"
            f"Average Calories per Workout: {avg_calories:.1f}\n"
            f"Average Minutes per Workout: {avg_minutes:.1f}"
        )

# Test your class:
user1 = FitnessTracker("Alice")
user1.log_workout(steps=8000, calories=300, minutes=45)  
user1.log_workout(steps=12000, calories=450, minutes=60)

user2 = FitnessTracker("Bob")
user2.log_workout(steps=5000, calories=200, minutes=30)

print(user1.get_total_steps())           # Expected: 20000
print(user1.get_average_calories())      # Expected: 375.0
print(FitnessTracker.get_global_stats()) # Expected: community-wide data
print(str(user1))                        # Expected: user summary

"""
=== BUSINESS COMMUNICATION SUMMARY ===

Initial Request: "We're building a fitness app. Users log workouts - steps, calories, exercise minutes. 
We need personal stats for each user, but also want to see community totals across all our users for marketing purposes."

Developer Clarifications Asked:
- Should we support different exercise types and intensities in this version?
- What measurement units should be supported beyond the basic metrics?
- What specific community insights are most valuable for marketing?

Stakeholder Responses:
- Focus on the core MVP features first - steps, calories, minutes tracking
- Standard units are sufficient for Phase 1 (steps as count, calories as kcal, minutes as duration)
- Marketing needs total users, total workouts, and community averages for promotional materials

Final Technical Decisions:
- Clear separation of personal vs global statistics with `global_` prefix naming
- Comprehensive validation for all workout inputs (type checking)
- Both individual and community aggregation methods for complete data analysis
- Rich string formatting for user-friendly data presentation

Assumptions Documented:
- Integer inputs for workout metrics (steps, calories, minutes)
- Community averages calculated per workout (not per user)
- Zero-division handling for users with no workouts
- Class-level tracking persists across all instances
"""