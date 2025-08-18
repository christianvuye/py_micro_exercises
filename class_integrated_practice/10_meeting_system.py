"""
Create a meeting management system that handles regular meetings and video meetings with specialized online features.

Concepts practiced:
- Simple inheritance with additional attributes (child class extends parent state)
- Parent method reuse (calling parent methods from child methods)
- Method extension (enhancing parent behavior rather than replacing it)
- Constructor parameter passing and additional initialization
- Conditional logic based on inheritance hierarchy

Business Requirements:
- Track basic meeting information and participant management
- Support video meetings with online-specific features and technical requirements
- Handle meeting lifecycle (scheduling, starting, ending)
- Manage participant attendance and meeting capacity
- Provide meeting summaries and status reporting

Your stakeholder says: "We're building a corporate meeting management system.
All meetings need basic info like title, duration, participant limits, and attendance tracking.
But video meetings also need technical specs like platform, meeting links, recording settings,
and bandwidth requirements. Video meetings should do everything regular meetings do,
plus handle the online-specific stuff. We need this for hybrid work scheduling."

# Test your classes:
regular_meeting = Meeting("Team Standup", max_participants=8, duration=30)
video_meeting = VideoMeeting("All Hands", max_participants=50, duration=60,
                           platform="Zoom", meeting_link="https://zoom.us/j/123456")

# Test basic meeting functionality
regular_meeting.add_participant("Alice")
regular_meeting.add_participant("Bob")
regular_meeting.start_meeting()

# Test video meeting functionality
video_meeting.add_participant("Charlie")
video_meeting.add_participant("Diana")
video_meeting.enable_recording()
video_meeting.start_meeting()

# Test error case - should raise RuntimeError for both meeting types
try:
    video_meeting.add_participant("Eve")  # Should raise RuntimeError - meeting already started
except RuntimeError as e:
    print(f"Expected error: {e}")

try:
    regular_meeting.add_participant("Frank")  # Should also raise RuntimeError
except RuntimeError as e:
    print(f"Expected error: {e}")

# Test meeting status and summaries
print(regular_meeting.get_meeting_info())    # Expected: basic meeting details
print(video_meeting.get_meeting_info())      # Expected: basic + video platform info
print(regular_meeting.end_meeting())         # Expected: meeting summary
print(video_meeting.end_meeting())           # Expected: enhanced video meeting summary
"""

import re
from typing import Literal


class Meeting:
    """
    A class for managing meeting sessions with participant validation and status tracking.

    Class Attributes:
        Validation regexes and limits for names, participants, and duration.
    """

    MEETING_NAME_RE = re.compile(
        r"^(?=.{5,100}$)[A-Za-z0-9](?:[A-Za-z0-9 :()-]*[A-Za-z0-9])$"
    )
    PARTICIPANT_NAME_RE = re.compile(
        r"^(?=.{2,50}$)[A-Za-z](?:[A-Za-z '\u2019-]*[A-Za-z])$"
    )
    MEETING_MIN_PARTICIPANTS = 2
    MEETING_MAX_PARTICIPANTS = 1000
    MEETING_MIN_DURATION = 5
    MEETING_MAX_DURATION = 480

    def __init__(self, name: str, max_participants: int, duration: int) -> None:
        """
        Initializes a new Meeting instance.

        Args:
            name (str): The name of the meeting.
            max_participants (int): The maximum number of participants allowed.
            duration (int): The duration of the meeting in minutes.

        Attributes:
            name (str): The validated name of the meeting.
            max_participants (int): The validated maximum number of participants.
            duration (int): The validated duration of the meeting in minutes.
            participants (set[str]): A set containing the names of participants.
            status (Literal["Scheduled", "In Progress", "Ended"]): The current status of the meeting.
        """
        self.name: str = self._validate_meeting_name(name)
        self.max_participants: int = self._validate_participant_count(max_participants)
        self.duration: int = self._validate_meeting_duration(duration)
        self.participants: set[str] = set()
        self.status: Literal["Scheduled", "In Progress", "Ended"] = "Scheduled"

    def can_start_or_join(self) -> bool:
        """
        Determines whether the meeting can be started or joined based on its current status.

        Returns:
            bool: True if the meeting status is "Scheduled", allowing it to be started or joined; False otherwise.
        """
        return self.status == "Scheduled"

    def can_end(self) -> bool:
        """
        Determines whether the meeting can be ended based on its current status.

        Returns:
            bool: True if the meeting status is "In Progress", allowing it to be ended; False otherwise.
        """
        return self.status == "In Progress"

    def add_participant(self, participant_name: str) -> str:
        """
        Adds a participant to the meeting after validating constraints and the participant's name.

        Args:
            participant_name (str): The name of the participant to be added.

        Performs the following checks in order:
            1. Meeting status: Ensures the meeting is joinable (not 'In Progress' or 'Ended').
            2. Capacity: Checks if the meeting has reached maximum participant capacity.
            3. Duplicate: Verifies the participant is not already present.
            4. Adds the participant to the set.

        Raises:
            RuntimeError: If the meeting is not joinable due to its status or if it's full.
            ValueError: If the participant is already present.

        Returns:
            str: Confirmation message indicating successful addition of the participant.
        """
        if not self.can_start_or_join():
            raise RuntimeError(f"Meeting is {self.status} and cannot be joined")
        if len(self.participants) >= self.max_participants:
            raise RuntimeError(
                f"Meeting is full ({len(self.participants)}/{self.max_participants})."
            )
        participant_name = self._validate_participant_name(participant_name)
        if participant_name in self.participants:
            raise ValueError(f"{participant_name} is already present in the meeting")
        self.participants.add(participant_name)
        return (
            f"{participant_name} has been successfully added to the meeting "
            f"along with {len(self.participants) - 1} other(s)"
        )

    def start_meeting(self) -> str:
        """
        Starts the meeting if it has not already started or ended.

        Raises:
            RuntimeError: If the meeting is already in progress or has ended.

        Returns:
            str: A message indicating that the meeting has started.
        """
        if not self.can_start_or_join():
            raise RuntimeError(f"Meeting is {self.status} and cannot be started")
        self.status = "In Progress"
        return f"Meeting {self.name} has started and is {self.status}"

    def end_meeting(self) -> str:
        """
        Ends the meeting if it is currently in progress.

        Raises:
            RuntimeError: If the meeting is not in progress (either scheduled or already ended).

        Returns:
            str: A message summarizing the meeting that has ended.
        """
        if not self.can_end():
            raise RuntimeError(f"Meeting is {self.status} and cannot be ended")
        self.status = "Ended"
        return f"Meeting {self.name} has ended with {len(self.participants)} participant(s)"

    def get_meeting_info(self) -> str:
        """
        Returns a formatted string containing all relevant meeting information.

        Includes:
            - Meeting name
            - Status
            - Duration
            - Maximum participants
            - Current participant count
            - Participant names (comma-separated)

        Returns:
            str: Nicely formatted meeting details.
        """
        info = [
            f"Meeting Name: {self.name}",
            f"Status: {self.status}",
            f"Duration: {self.duration} minutes",
            f"Max Participants: {self.max_participants}",
            f"Current Participants: {len(self.participants)}",
            f"Participant List: {', '.join(sorted(self.participants)) if self.participants else 'None'}",
        ]
        return "\n".join(info)

    @staticmethod
    def _validate_participant_name(participant_name: str) -> str:
        """
        Validates and formats a participant's name.

        This method ensures the provided participant name is a non-empty string, strips leading/trailing whitespace,
        capitalizes it, and checks if it matches the required format using a regular expression.

        Args:
            participant_name (str): The name of the participant to validate.

        Returns:
            str: The validated and formatted participant name.

        Raises:
            TypeError: If participant_name is not a string.
            ValueError: If participant_name is empty or does not meet the name requirements.
        """
        if not isinstance(participant_name, str):
            raise TypeError(
                f"{participant_name} should be a string, got {type(participant_name).__name__}"
            )
        participant_name = participant_name.strip().title()
        if not participant_name:
            raise ValueError(f"{participant_name} cannot be empty.")
        if not Meeting.PARTICIPANT_NAME_RE.fullmatch(participant_name):
            raise ValueError(f"{participant_name} does not meet the name requirements")
        return participant_name

    @staticmethod
    def _validate_meeting_name(name: str) -> str:
        """
        Validates and formats a meeting name.

        This method checks if the provided meeting name is a string, strips leading/trailing whitespace,
        converts it to title case, and ensures it matches the required meeting name format using a regular expression.

        Args:
            name (str): The meeting name to validate.

        Returns:
            str: The validated and formatted meeting name.

        Raises:
            TypeError: If the name is not a string.
            ValueError: If the name does not meet the meeting name requirements.
        """
        if not isinstance(name, str):
            raise TypeError(f"{name} should be str, got {type(name).__name__}")
        name = name.strip().title()
        if not name:
            raise ValueError(f"{name} cannot be empty.")
        if not Meeting.MEETING_NAME_RE.fullmatch(name):
            raise ValueError(f"{name} does not meet the meeting name requirements")
        return name

    @staticmethod
    def _validate_participant_count(participant_count: int) -> int:
        """
        Checks if the given participant count is an integer and within the allowed range.

        Args:
            participant_count (int): The number of participants to validate.

        Raises:
            TypeError: If participant_count is not an integer.
            ValueError: If participant_count is less than MEETING_MIN_PARTICIPANTS or greater than MEETING_MAX_PARTICIPANTS.

        Returns:
            int: The validated participant count.
        """
        if type(participant_count) is not int:
            raise TypeError(
                f"{participant_count} should be an integer, got {type(participant_count).__name__}"
            )
        if participant_count < Meeting.MEETING_MIN_PARTICIPANTS:
            raise ValueError(
                f"{participant_count} is too low, the minimum is {Meeting.MEETING_MIN_PARTICIPANTS}"
            )
        if participant_count > Meeting.MEETING_MAX_PARTICIPANTS:
            raise ValueError(
                f"{participant_count} is too high, the maximum is {Meeting.MEETING_MAX_PARTICIPANTS}"
            )
        return participant_count

    @staticmethod
    def _validate_meeting_duration(duration: int) -> int:
        """
        Validates that the meeting duration is an integer within the allowed range.

        Args:
            duration (int): Meeting duration in minutes.

        Returns:
            int: Validated duration.

        Raises:
            TypeError: If `duration` is not of type `int`.
            ValueError: If `duration` is less than `Meeting.MEETING_MIN_DURATION` or greater than `Meeting.MEETING_MAX_DURATION`.
        """
        if type(duration) is not int:
            raise TypeError(
                f"{duration} should be an integer, got {type(duration).__name__}"
            )
        if duration < Meeting.MEETING_MIN_DURATION:
            raise ValueError(
                f"{duration} is too short, the minimum duration is {Meeting.MEETING_MIN_DURATION} minutes"
            )
        if duration > Meeting.MEETING_MAX_DURATION:
            raise ValueError(
                f"{duration} is too long, the maximum duration is {Meeting.MEETING_MAX_DURATION} minutes"
            )
        return duration


class VideoMeeting(Meeting):
    "docstring"

    ALLOWED_PLATFORMS = ("Zoom", "Teams", "WebEx", "Google Meet", "GoToMeeting")
    VIDEO_MEETING_URL_RE = re.compile(
        r"^(?=.{10,500}$)"
        r"https://"
        r"(?:"
        r"(?:[a-z0-9-]+\.)*zoom\.us"
        r"|teams\.microsoft\.com"
        r"|(?:[a-z0-9-]+\.)*webex\.com"
        r"|meet\.google\.com"
        r"|(?:meet\.goto\.com|(?:[a-z0-9-]+\.)?gotomeeting\.com)"
        r")"
        r"(?::\d{2,5})?"
        r"(?:[/?#][^\s]*)?$",
        re.IGNORECASE,
    )

    def __init__(
        self,
        name: str,
        max_participants: int,
        duration: int,
        platform: str,
        meeting_link: str,
    ) -> None:
        """
        Initialize a Video meeting instance with the specified parameters.

        Args:
            name (str): The name of the meeting.
            max_participants (int): The maximum number of participants allowed.
            duration (int): The duration of the meeting in minutes.
            platform (str): The platform on which the meeting will be held (e.g., Zoom, Teams).
            meeting_link (str): The URL link to join the meeting.

        Attributes:
            platform (str): The validated platform name.
            meeting_link (str): The validated meeting link.
            recording_enabled (bool): Indicates if recording is enabled for the meeting (default is False).
        """
        super().__init__(
            name=name, max_participants=max_participants, duration=duration
        )
        self.platform: str = self._validate_platform(platform)
        self.meeting_link: str = self._validate_meeting_link(meeting_link)
        self.recording_enabled: bool = False

    def enable_recording(self) -> bool:
        """
        Enables the recording feature for the meeting.

        Returns:
            bool: True if recording was successfully enabled.
        """
        self.recording_enabled = True
        return True

    def get_meeting_info(self) -> str:
        """
        Returns a formatted string containing all relevant video meeting information.

        Includes:
            - Meeting name
            - Status
            - Duration
            - Maximum participants
            - Current participant count
            - Participant names (comma-separated)
            - Platform
            - Meeting link
            - Recording enabled status

        Returns:
            str: Nicely formatted video meeting details.
        """
        info = [
            f"Meeting Name: {self.name}",
            f"Status: {self.status}",
            f"Duration: {self.duration} minutes",
            f"Max Participants: {self.max_participants}",
            f"Current Participants: {len(self.participants)}",
            f"Participant List: {', '.join(sorted(self.participants)) if self.participants else 'None'}",
            f"Platform: {self.platform}",
            f"Meeting Link: {self.meeting_link}",
            f"Recording Enabled: {'Yes' if self.recording_enabled else 'No'}",
        ]
        return "\n".join(info)

    @staticmethod
    def _validate_platform(platform: str) -> str:
        """
        Validate and format the meeting platform name.

        Args:
            platform (str): The name of the video meeting platform to validate.

        Returns:
            str: The validated and formatted platform name (stripped and title-cased).

        Raises:
            TypeError: If the platform is not a string.
            ValueError: If the platform is an empty string or not in the list of allowed platforms.
        """
        if not isinstance(platform, str):
            raise TypeError(
                f"{platform} should be string, got {type(platform).__name__}"
            )
        platform = platform.strip().title()
        if not platform:
            raise ValueError(f"{platform} cannot be an empty string")
        if platform not in VideoMeeting.ALLOWED_PLATFORMS:
            raise ValueError(
                f"{platform} is not in the list of allowed platforms: {VideoMeeting.ALLOWED_PLATFORMS}"
            )
        return platform

    @staticmethod
    def _validate_meeting_link(meeting_link: str) -> str:
        """
        Validates a meeting link string to ensure it is non-empty, of type `str`, and matches the required video meeting URL format.

        Args:
            meeting_link (str): The meeting link to validate.

        Returns:
            str: The validated and stripped meeting link.

        Raises:
            TypeError: If `meeting_link` is not a string.
            ValueError: If `meeting_link` is empty or does not match the required format.
        """
        if not isinstance(meeting_link, str):
            raise TypeError(
                f"{meeting_link} should be string, got {type(meeting_link).__name__}"
            )
        meeting_link = meeting_link.strip()
        if not meeting_link:
            raise ValueError("Meeting link cannot be an empty string")
        if not VideoMeeting.VIDEO_MEETING_URL_RE.fullmatch(meeting_link):
            raise ValueError(
                "Meeting link does not match the required format for allowed platforms"
            )
        return meeting_link


# Test your classes:
regular_meeting = Meeting("Team Standup", max_participants=8, duration=30)
video_meeting = VideoMeeting(
    "All Hands",
    max_participants=50,
    duration=60,
    platform="Zoom",
    meeting_link="https://zoom.us/j/123456",
)

# Test basic meeting functionality
regular_meeting.add_participant("Alice")
regular_meeting.add_participant("Bob")
regular_meeting.start_meeting()

# Test video meeting functionality
video_meeting.add_participant("Charlie")
video_meeting.add_participant("Diana")
video_meeting.enable_recording()
video_meeting.start_meeting()

# Test error case - should raise RuntimeError for both meeting types
try:
    video_meeting.add_participant(
        "Eve"
    )  # Should raise RuntimeError - meeting already started
except RuntimeError as e:
    print(f"Expected error: {e}")

try:
    regular_meeting.add_participant("Frank")  # Should also raise RuntimeError
except RuntimeError as e:
    print(f"Expected error: {e}")

# Test meeting status and summaries
print(regular_meeting.get_meeting_info())  # Expected: basic meeting details
print(video_meeting.get_meeting_info())  # Expected: basic + video platform info
print(regular_meeting.end_meeting())  # Expected: meeting summary
print(video_meeting.end_meeting())  # Expected: enhanced video meeting summary

"""
=== BUSINESS COMMUNICATION SUMMARY ===

Initial Request: "We're building a corporate meeting management system. All meetings need basic info like title, duration, participant limits, and attendance tracking. But video meetings also need technical specs like platform, meeting links, recording settings, and bandwidth requirements. Video meetings should do everything regular meetings do, plus handle the online-specific stuff."

Developer Clarifications Asked:
- What validation is needed for meeting names, participant counts, and duration limits?
- Should participant names be stored in a list as instance attributes?
- What meeting states should be tracked and what should the initial state be?
- Should late joining be allowed for video meetings vs regular meetings?
- Should enable_recording() return anything useful?
- Should recording_enabled be initialized in the constructor?

Stakeholder Responses:
- Meeting names: 5-100 characters, professional format with letters, numbers, spaces, colons, hyphens, parentheses
- Participant limits: 2-1000 participants, duration 5-480 minutes
- Store participants in list/set for attendance tracking and capacity management
- All meetings start in "Scheduled" state, transition through "In Progress" to "Ended"
- Consistent rule: no late joining for either meeting type once started (Option B - lock attendance)
- enable_recording() should return boolean confirmation
- Yes, initialize recording_enabled=False in VideoMeeting constructor for complete object initialization

Final Technical Decisions:
- Two-level inheritance: Meeting → VideoMeeting with clean specialization
- State machine pattern with helper methods (can_start_or_join, can_end)
- Method extension: get_meeting_info() enhanced in child class rather than replaced
- Comprehensive validation with regex patterns for names and URLs
- Smart exception hierarchy: RuntimeError for state issues, ValueError for data validation
- Set data structure for participants to prevent duplicates automatically

Assumptions Documented:
- Meeting lifecycle follows corporate standards (scheduled → in progress → ended)
- Platform validation includes major enterprise video platforms
- URL validation ensures proper HTTPS format with platform-specific domains
- Participant management consistent across meeting types for predictable behavior
- Recording feature exclusive to video meetings, defaults to disabled
- Meeting status transitions are unidirectional (no going backwards)
"""
