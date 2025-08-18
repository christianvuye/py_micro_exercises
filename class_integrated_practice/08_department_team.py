"""
Build an organizational management system that handles company departments and their specialized teams.

Concepts practiced:
- Multi-level inheritance (Department → Team → SpecializedTeam)
- Method inheritance across levels (base methods available to all descendants)
- Inheritance chain method resolution (how Python finds methods up the hierarchy)

Business Requirements:
- Track basic department information and headcount
- Support team structures within departments
- Handle specialized teams with additional capabilities
- Calculate budgets and resource allocation across hierarchy levels
- Monitor organizational metrics and reporting structures

Your stakeholder says: "We have departments like Engineering, Marketing. Within each
department we have teams like Frontend Team, Backend Team. Some teams are special -
like our DevOps team that handles both development and operations. Each level needs
different information but should share common organizational functions."

# Test your class:
dept = Department("Engineering", budget=500000)
team = Team("Frontend Team", budget=100000, department=dept, team_size=8)
devops = DevOpsTeam("DevOps Team", budget=150000, department=dept, team_size=5, on_call_rotation=True)

dept.add_employee("John Doe")
team.add_employee("Jane Smith")
team.assign_project("User Dashboard")
devops.add_employee("Bob Wilson")
devops.assign_project("CI/CD Pipeline")
devops.set_on_call_schedule(["Bob Wilson", "Alice Chen"])

print(dept.get_summary())                    # Expected: basic department info
print(team.get_summary())                    # Expected: team info with projects
print(devops.get_summary())                  # Expected: DevOps info with on-call data
print(devops.get_total_responsibilities())   # Expected: count of projects + on-call duties
"""


class BusinessUnit:
    """
    Represents a business unit within an organization, managing its name, budget, and employees.

    The BusinessUnit class provides functionality to initialize a business unit with a name and budget,
    add employees, update the budget, and retrieve a summary of the business unit's details.
    It includes validation for input data to ensure integrity.

    Attributes:
        businessUnit_name (str): The name of the business unit.
        budget (int): The current budget allocated to the business unit.
        employees (list): A list of employee names associated with the business unit.

    Methods:
        add_employee(employee_name: str): Adds an employee to the business unit.
        add_budget(budget: int): Adds to the business unit's budget.
        get_summary() -> str: Returns a formatted summary of the business unit.
        _validate_businessUnit_name(businessUnit_name: str): Validates the business unit name.
        _validate_employee_name(employee_name: str): Validates the employee name.
        _validate_budget(budget: int): Validates the budget value.
    """

    def __init__(self, businessUnit_name: str, budget: int) -> None:
        """
        Initializes a new instance of the BusinessUnit class with the specified business unit name and budget.

        Args:
            businessUnit_name (str): The name of the business unit.
            budget (int): The budget allocated to the business unit.

        Raises:
            ValueError: If businessUnit_name or budget are invalid.
        """
        self.businessUnit_name = self._validate_businessUnit_name(businessUnit_name)
        self.budget = self._validate_budget(budget)
        self.employees = []

    def __str__(self) -> str:
        """
        Return a string representation of the object, including its class name and business unit name.
        """
        return f"{self.__class__.__name__}(name={self.businessUnit_name})"

    def add_employee(self, employee_name: str) -> str:
        """
        Adds a new employee to the business unit's employee list after validating the employee name.

        Args:
            employee_name (str): The name of the employee to add.

        Returns:
            str: A confirmation message indicating the employee was successfully added,
             along with the updated list of employees and the business unit name.
        """
        employee_name = self._validate_employee_name(employee_name)
        self.employees.append(employee_name)
        return (
            f"{employee_name} successfully added to the list of employees: "
            f"{', '.join(self.employees) if self.employees else 'None'} "
            f"for business unit: {self.businessUnit_name}"
        )

    def add_budget(self, budget: int) -> str:
        """
        Adds the specified budget amount to the business unit's current budget after validation.

        Args:
            budget (int): The amount to be added to the business unit budget.

        Returns:
            str: A message indicating the amount added and the updated business unit budget.
        """
        budget = self._validate_budget(budget)
        self.budget += budget
        return f"{budget} was added to the business unit budget. Current business unit budget is now: {self.budget}"

    def get_summary(self) -> str:
        """
        Returns a formatted summary of the business unit, including its name, budget,
        and list of employees.

        Returns:
            str: A multi-line string summarizing the business unit's details.
        """
        return (
            f"Business Unit Summary:\n"
            f"Name: {self.businessUnit_name}\n"
            f"Budget: {self.budget}\n"
            f"Employees: {', '.join(self.employees) if self.employees else 'None'}"
        )

    def _validate_businessUnit_name(self, businessUnit_name: str) -> str:
        """
        Validates that the provided business unit name is a non-empty string.

        Args:
            businessUnit_name (str): The name of the business unit to validate.

        Returns:
            str: The validated business unit name.

        Raises:
            TypeError: If businessUnit_name is not a string.
            ValueError: If businessUnit_name is an empty string.
        """
        if not isinstance(businessUnit_name, str):
            raise TypeError(
                f"{businessUnit_name} should be a str, got {type(businessUnit_name).__name__}"
            )
        if not businessUnit_name:
            raise ValueError(f"{businessUnit_name} is an empty string")
        return businessUnit_name

    @staticmethod
    def _validate_employee_name(employee_name: str) -> str:
        """
        Validates that the provided employee name is a non-empty string.

        Args:
            employee_name (str): The name of the employee to validate.

        Returns:
            str: The validated employee name.

        Raises:
            TypeError: If employee_name is not a string.
            ValueError: If employee_name is an empty string.
        """
        if not isinstance(employee_name, str):
            raise TypeError(
                f"{employee_name} should be a str, got {type(employee_name).__name__}"
            )
        if not employee_name:
            raise ValueError(f"{employee_name} is an empty string")
        return employee_name

    @staticmethod
    def _validate_budget(budget: int) -> int:
        """
        Validates that the provided budget is a non-negative integer.

        Args:
            budget (int): The budget value to validate.

        Returns:
            int: The validated budget value.

        Raises:
            TypeError: If the budget is not an integer.
            ValueError: If the budget is negative.
        """
        if type(budget) is not int:
            raise TypeError(
                f"Budget: {budget} should be an int, got {type(budget).__name__}"
            )
        if budget < 0:
            raise ValueError(f" Budget: {budget} cannot be negative.")
        return budget


class Department(BusinessUnit):
    """
    Department represents a specific type of BusinessUnit within the organization.

    Inherits from BusinessUnit and adds department-specific validation and attributes.

    Class Attributes:
        VALID_DEPARTMENTS (list): List of valid department names.

    Instance Attributes:
        businessUnit_name (str): The name of the department (validated against VALID_DEPARTMENTS).
        budget (int): The budget allocated to the department.
        employees (list): List of employee names in the department (inherited).

    Methods:
        __init__(department_name: str, budget: int): Initializes a Department instance.
        add_employee(employee_name: str): Adds an employee to the department.
        add_budget(budget: int): Adds to the department's budget.
        get_summary() -> str: Returns a formatted summary of the department.
        _validate_businessUnit_name(businessUnit_name: str): Validates the department name.
        _validate_department_name(department_name: str): Checks if department name is valid.
    """

    VALID_DEPARTMENTS = [
        "Engineering",
        "Marketing",
        "Sales",
        "HR",
        "Finance",
        "Operations",
    ]

    def __init__(self, department_name: str, budget: int) -> None:
        """
        Initializes a Department instance with the specified department name and budget.

        Args:
            department_name (str): The name of the department (must be in VALID_DEPARTMENTS).
            budget (int): The budget allocated to the department.

        Attributes:
            teams (list): List of Team instances belonging to this department.
            remaining_budget (int): The budget remaining after allocating to teams.
        """
        super().__init__(businessUnit_name=department_name, budget=budget)
        self.teams = []
        self.remaining_budget = budget

    def get_summary(self) -> str:
        """
        Returns a formatted summary of the department, including its name, budget,
        list of employees, associated teams, and all projects assigned to its teams.

        Returns:
            str: A multi-line string summarizing the department's details, teams, and projects.
        """
        projects = self.get_all_projects()
        return (
            f"Department Summary:\n"
            f"Name: {self.businessUnit_name}\n"
            f"Budget: {self.budget}\n"
            f"Employees: {', '.join(self.employees) if self.employees else 'None'}\n"
            f"Teams: {', '.join(str(team) for team in self.teams) if self.teams else 'None'}\n"
            f"Projects: {', '.join(projects) if projects else 'None'}"
        )

    def add_team(self, team: "Team") -> str:
        """
        Adds a Team instance to the department, updating the department's teams list and adjusting the remaining budget.

        Args:
            team (Team): The Team object to add to the department.

        Side Effects:
            Appends the given team to the department's teams list.
            Decreases the department's remaining budget by the team's budget.

        Returns:
            str: Confirmation message indicating the team was added and the updated remaining budget.
        """
        self.teams.append(team)
        self.remaining_budget -= team.budget
        return f"Added {team} to department {self.businessUnit_name}, remaining budget: {self.remaining_budget}"

    def get_all_projects(self) -> list:
        """
        Returns a list of all projects from every team in the department.

        Iterates through each team in the department and aggregates their projects
        into a single list.

        Returns:
            list: A list containing all projects from all teams.
        """
        all_projects = []
        for team in self.teams:
            all_projects.extend(team.projects)
        return all_projects

    def _validate_businessUnit_name(self, businessUnit_name: str) -> str:
        """
        Validates the provided business unit name by first applying the parent class's validation,
        then further validating it as a department name.

        Args:
            businessUnit_name (str): The name of the business unit to validate.

        Returns:
            str: The validated business unit name.
        """
        businessUnit_name = super()._validate_businessUnit_name(businessUnit_name)
        businessUnit_name = self._validate_department_name(businessUnit_name)
        return businessUnit_name

    @staticmethod
    def _validate_department_name(department_name: str) -> str:
        """
        Validates that the provided department name exists within the list of valid departments.

        Args:
            department_name (str): The name of the department to validate.

        Returns:
            str: The validated department name.

        Raises:
            ValueError: If the department name is not in the list of valid departments.
        """
        if department_name not in Department.VALID_DEPARTMENTS:
            raise ValueError(
                f"{department_name} is not in the list of valid departments: {Department.VALID_DEPARTMENTS}"
            )
        return department_name


class Team(BusinessUnit):
    """
    Represents a team within a business unit, associated with a specific department.

    A Team has a name, budget, department affiliation, and a defined team size. It can be assigned projects and is subject to validation rules for budget allocation, team size, and project assignment.

    Attributes:
        MINIMUM_TEAM_SIZE (int): The minimum allowed number of team members.
        MAXIMUM_TEAM_SIZE (int): The maximum allowed number of team members.
        projects (list): List of projects assigned to the team.

    Methods:
        __init__(team_name, budget, department, team_size):
            Initializes a Team instance and adds it to the specified department.
        assign_project(project):
            Assigns a validated project to the team.
        _validate_budget_allocation(budget, department):
            Ensures the team's budget does not exceed the department's remaining budget.
        _validate_project(project):
            Validates that the project name is a non-empty string.
        _validate_team_size(team_size):
            Validates that the team size is within allowed limits.
    """

    MINIMUM_TEAM_SIZE = 1
    MAXIMUM_TEAM_SIZE = 20

    def __init__(
        self, team_name: str, budget: int, department: Department, team_size: int
    ):
        """
        Initializes a Team instance with the specified name, budget, department, and team size.

        Args:
            team_name (str): The name of the team.
            budget (int): The budget allocated to the team.
            department (Department): The department to which the team belongs.
            team_size (int): The number of members in the team.

        Side Effects:
            Adds this team to the provided department via department.add_team(self).
        """
        budget = self._validate_budget_allocation(budget, department)
        super().__init__(businessUnit_name=team_name, budget=budget)
        self.department = department
        self.team_size = self._validate_team_size(team_size)
        department.add_team(self)
        self.projects = []

    def assign_project(self, project: str) -> str:
        """
        Assigns a project to the Team after validating the project name.

        Args:
            project (str): The name of the project to assign.

        Returns:
            str: Confirmation message indicating the project has been assigned.

        Raises:
            TypeError: If project is not a string.
            ValueError: If project is an empty string.
        """
        project = self._validate_project(project)
        self.projects.append(project)
        return f"Assigned {project} to {self.businessUnit_name}"

    def _validate_budget_allocation(self, budget: int, department: Department) -> int:
        """
        Validates that the team's budget allocation does not exceed the department's remaining budget.

        Args:
            budget (int): The proposed budget allocation for the team.
            department (Department): The department to which the team belongs.

        Raises:
            ValueError: If the team's budget allocation exceeds the department's remaining budget.

        Returns:
            int: The validated budget allocation for the team.
        """
        budget = self._validate_budget(budget)
        if budget > department.remaining_budget:
            raise ValueError(
                f"Team budget {budget} exceeds remaining department budget {department.remaining_budget}"
            )
        return budget

    def get_summary(self) -> str:
        """
        Returns a formatted summary of the team's details, including the team name,
        department name, budget, team size, list of employees, and projects.

        Returns:
            str: A multi-line string summarizing the team's information.
        """
        return (
            f"Team Summary:\n"
            f"Name: {self.businessUnit_name}\n"
            f"Department: {self.department.businessUnit_name}\n"
            f"Budget: {self.budget}\n"
            f"Team Size: {self.team_size}\n"
            f"Employees: {', '.join(self.employees) if self.employees else 'None'}\n"
            f"Projects: {', '.join(self.projects) if self.projects else 'None'}"
        )

    @staticmethod
    def _validate_project(project: str) -> str:
        """
        Validates that the provided project is a non-empty string.

        Args:
            project (str): The project name to validate.

        Returns:
            str: The validated project name.

        Raises:
            TypeError: If project is not a string.
            ValueError: If project is an empty string.
        """
        if not isinstance(project, str):
            raise TypeError(f"{project} should a string, got {type(project).__name__}")
        if not project:
            raise ValueError(f"{project} is an empty string")
        return project

    @staticmethod
    def _validate_team_size(team_size: int) -> int:
        """
        Validates that the provided team size is an integer within the allowed range.

        Args:
            team_size (int): The size of the team to validate.

        Returns:
            int: The validated team size.

        Raises:
            TypeError: If team_size is not an integer.
            ValueError: If team_size is less than the minimum or greater than the maximum allowed team size.
        """
        if type(team_size) is not int:
            raise TypeError(
                f"{team_size} should be an int, got {type(team_size).__name__}"
            )
        if team_size < Team.MINIMUM_TEAM_SIZE:
            raise ValueError(f"Team size has to be at least {Team.MINIMUM_TEAM_SIZE}")
        if team_size > Team.MAXIMUM_TEAM_SIZE:
            raise ValueError(f"Team size has to be at most {Team.MAXIMUM_TEAM_SIZE}")
        return team_size


class DevOpsTeam(Team):
    """
    DevOpsTeam represents a specialized team within a department focused on DevOps responsibilities.

    Extends Team with on-call rotation management and scheduling.

    Attributes:
        on_call_rotation (bool): If the team has on-call rotation.
        on_call_schedule (list[str]): Team members assigned to on-call.

    Methods:
        set_on_call_schedule(team_members): Add members to on-call schedule.
        get_total_responsibilities(): Count projects + on-call duties.
        get_summary(): DevOps team details including on-call info.
        _validate_team_members(team_members): Validate team member names.
    """

    def __init__(
        self,
        team_name: str,
        budget: int,
        department: Department,
        team_size: int,
        on_call_rotation: bool,
    ):
        """
        Initializes a new DevOpsTeam instance.

        Args:
            team_name (str): The name of the DevOpsTeam.
            budget (int): The team's budget.
            department (Department): The department to which the DevOpsTeam belongs.
            team_size (int): The number of members in the team.
            on_call_rotation (bool): Indicates if the DevOpsTeam participates in an on-call rotation.

        Raises:
            TypeError: If on_call_rotation is not a boolean.
        """
        super().__init__(
            team_name=team_name,
            budget=budget,
            department=department,
            team_size=team_size,
        )
        if type(on_call_rotation) is not bool:
            raise TypeError(
                f"{on_call_rotation} should be bool, got {type(on_call_rotation).__name__}"
            )
        self.on_call_rotation = on_call_rotation
        self.on_call_schedule = []

    def set_on_call_schedule(self, team_members: list[str]) -> str:
        """
        Adds validated team members to the DevOps team's on-call schedule.

        Args:
            team_members (list[str]): List of team member names to add to the on-call schedule.

        Returns:
            str: Confirmation message listing the team members added to the on-call schedule.

        Raises:
            ValueError: If on_call_rotation is False.
            TypeError, ValueError: If team_members is not a valid list of non-empty strings.
        """
        if not self.on_call_rotation:
            raise ValueError(
                f"This team does not have on call rotation, on_call_rotation param set to {self.on_call_rotation}"
            )
        team_members = self._validate_team_members(team_members)
        self.on_call_schedule.extend(team_members)
        return f"{team_members} added to on call schedule!"

    def get_total_responsibilities(self) -> int:
        """
        Calculates the total number of responsibilities by summing the number of projects and on-call schedule entries.

        Returns:
            int: The total count of responsibilities.
        """
        return len(self.projects) + len(self.on_call_schedule)

    def get_summary(self) -> str:
        """
        Returns a formatted summary of the DevOps team's details, including the team name,
        department name, budget, team size, list of employees, projects, on-call rotation status,
        and the current on-call schedule.

        Returns:
            str: A multi-line string summarizing the DevOps team's information, including
            on-call rotation and schedule.
        """
        return (
            f"DevOps Team Summary:\n"
            f"Name: {self.businessUnit_name}\n"
            f"Department: {self.department.businessUnit_name}\n"
            f"Budget: {self.budget}\n"
            f"Team Size: {self.team_size}\n"
            f"Employees: {', '.join(self.employees) if self.employees else 'None'}\n"
            f"Projects: {', '.join(self.projects) if self.projects else 'None'}\n"
            f"On-Call Rotation: {'Yes' if self.on_call_rotation else 'No'}\n"
            f"On-Call Schedule: {', '.join(self.on_call_schedule) if self.on_call_schedule else 'None'}"
        )

    @staticmethod
    def _validate_team_members(team_members: list[str]) -> list[str]:
        """
        Validates that the input is a list of non-empty strings representing team members.

        Args:
            team_members (list[str]): The list of team member names to validate.

        Returns:
            list[str]: The validated list of team member names.

        Raises:
            TypeError: If team_members is not a list, or if any element in the list is not a string.
            ValueError: If any team member name is an empty string.
        """
        if not isinstance(team_members, list):
            raise TypeError(
                f"{team_members} should be a list, got {type(team_members).__name__}"
            )
        for team_member in team_members:
            if not isinstance(team_member, str):
                raise TypeError(
                    f"{team_member} should be a list, got {type(team_member).__name__}"
                )
            if not team_member:
                raise ValueError("Empty string is invalid")
        return team_members


# Test your class:
dept = Department("Engineering", budget=500000)
team = Team("Frontend Team", budget=100000, department=dept, team_size=8)
devops = DevOpsTeam(
    "DevOps Team", budget=150000, department=dept, team_size=5, on_call_rotation=True
)

dept.add_employee("John Doe")
team.add_employee("Jane Smith")
team.assign_project("User Dashboard")
devops.add_employee("Bob Wilson")
devops.assign_project("CI/CD Pipeline")
devops.set_on_call_schedule(["Bob Wilson", "Alice Chen"])

print(dept.get_summary())  # Expected: basic department info
print(team.get_summary())  # Expected: team info with projects
print(devops.get_summary())  # Expected: DevOps info with on-call data
print(
    devops.get_total_responsibilities()
)  # Expected: count of projects + on-call duties

"""
=== BUSINESS COMMUNICATION SUMMARY ===

Initial Request: "We have departments like Engineering, Marketing. Within each department we have teams like Frontend Team, Backend Team. Some teams are special - like our DevOps team that handles both development and operations. Each level needs different information but should share common organizational functions."

Developer Clarifications Asked:
- Should teams inherit from departments or have a different relationship structure?
- How should budget allocation work between departments and teams?
- Should team creation require an existing department object for data integrity?
- What validation is needed for department names vs. generic business unit names?
- How should specialized teams like DevOps extend regular team functionality?
- Should budget validation happen before or after parent constructor calls?

Stakeholder Responses:
- Teams belong to departments but aren't a type of department (composition over inheritance)
- Teams get budget FROM departments - must not exceed remaining department budget
- Yes, require actual department objects for team creation to ensure data integrity
- Departments should validate against approved list (Engineering, Marketing, Sales, HR, Finance, Operations)
- DevOps teams need on-call rotation features and enhanced responsibility tracking
- Validate budget allocation before any object creation to prevent invalid states

Final Technical Decisions:
- Inheritance structure: BusinessUnit (base) → Department/Team (peers) → DevOpsTeam (specialized)
- Budget system: Department tracks remaining_budget, decremented when teams added
- Object relationships: Team constructor takes Department object, auto-registers with department
- Validation inheritance: Child classes override validation methods using super() + specific rules
- Multi-level inheritance: DevOpsTeam extends Team with on-call scheduling and responsibility counting
- Method resolution: get_summary() enhanced at each inheritance level with specialized information
- Constructor patterns: Each level calls super().__init__() then adds its own initialization

Assumptions Documented:
- Department validation enforces business-approved department list for organizational consistency
- Team-department relationships use dependency injection pattern for data integrity
- Budget allocation is atomic operation - validation and registration happen together
- Specialized teams (DevOps) extend base team functionality rather than replacing it
- On-call schedules stored as instance attributes specific to DevOpsTeam instances
- String representations use business unit names for clear logging and user feedback
- Auto-registration pattern ensures teams cannot exist without valid department association
- Method inheritance allows specialized summaries while preserving core business unit information

Technical Enhancement Made:
- Initial budget validation design had logical flaw (validating before department assignment)
- Enhanced to proper dependency injection where department object passed to enable validation
- Evolved from static validation methods to instance methods for inheritance-friendly validation
- Refined constructor order to validate dependencies before calling parent constructors
"""
