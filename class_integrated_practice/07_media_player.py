"""
Create a multimedia playback system that handles different types of media files with specialized playback features.

Concepts practiced:
- Parent constructor calling with super().__init__()
- Specialized instance methods (child-specific functionality)
- Method inheritance and extension (shared behavior from parent)

Business Requirements:
- Handle basic media playback operations for all file types
- Support specialized players for different media formats
- Track playback state and media file information
- Provide format-specific features and controls
- Monitor playback statistics and format-specific settings

Your stakeholder says: "We're building a media player app. All players need basic
controls like play, pause, stop and track the same file info. But video players
need subtitle support and quality settings, while audio players need equalizer
and playlist features. Each player type has additional settings to initialize."

# Test your class:
basic_player = MediaPlayer("song.mp3", duration=180)
video_player = VideoPlayer("movie.mp4", duration=7200)
audio_player = AudioPlayer("podcast.wav", duration=3600)

basic_player.play()
video_player.play()
video_player.set_quality("1080p")
video_player.toggle_subtitles()
audio_player.set_equalizer("rock")
audio_player.add_to_playlist("My Favorites")

print(basic_player.get_playback_info())    # Expected: basic playback status
print(video_player.get_playback_info())    # Expected: status + quality + subtitles
print(audio_player.get_playback_info())    # Expected: status + equalizer info
print(audio_player.get_playlist_count())   # Expected: number of playlists
"""

import re


class MediaPlayer:
    """
    MediaPlayer manages playback for audio and video files.

    Validates file names/extensions, enforces duration limits, and tracks playback status.

    Supported formats: mp3, mp4, mkv, webm, mov, avi, aac, m4a, wav, flac, opus, ogg.

    Methods:
        __init__, play, pause, stop, get_playback_info, _validate_file, _validate_duration
    """

    FILE_PATTERN = re.compile(
        r'^(?=.{1,255}$)(?!(?:CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(?:\..*)?$)(?![ .])(?!.*[ .]$)[^<>:"/\\|?*\x00-\x1F]+\.[A-Za-z0-9]{1,63}$'
    )

    FILE_FORMATS = [
        "mp3",
        "mp4",
        "mkv",
        "webm",
        "mov",
        "avi",
        "aac",
        "m4a",
        "wav",
        "flac",
        "opus",
        "ogg",
    ]

    MIN_DURATION = 1  # 1 second
    MAX_DURATION = 36000  # 10 hours

    PLAYBACK_STATUS = ("Not Started", "Playing", "Paused", "Stopped")

    def __init__(self, file: str, duration: int) -> None:
        """
        Initializes a media player instance with the specified file and duration.

        Args:
            file (str): The path to the media file.
            duration (int): The duration of the media file in seconds.

        Raises:
            TypeError: If file is not a string or duration is not an int.
            ValueError: If the file path does not match the required pattern,
                if the file extension is not supported,
                if duration is less than the minimum allowed,
                or if duration exceeds the maximum allowed.
        """
        self.file = self._validate_file(file)
        self.duration = self._validate_duration(duration)
        self.status = "Not Started"

    def play(self) -> None:
        """
        Starts media playback by setting the player's status to 'Playing'.

        Returns:
            None
        """
        self.status = "Playing"

    def pause(self) -> None:
        """
        Pauses the media player by setting its status to 'Paused'.

        Returns:
            None
        """
        self.status = "Paused"

    def stop(self) -> None:
        """
        Stops media playback and updates the player status to 'Stopped'.

        Returns:
            None
        """
        self.status = "Stopped"

    def get_playback_info(self) -> str:
        """
        Returns a string containing playback information for the media file.
        The returned string includes the file name, duration in seconds, and current playback status.

        Returns:
            str: A formatted string with file name, duration, and status.
        """
        return f"File: {self.file}, Duration: {self.duration}s, Status: {self.status}"

    @staticmethod
    def _validate_file(file: str) -> str:
        """
        Validates the provided file name and extension.

        Checks if the input is a string, matches the expected filename pattern,
        and has a valid file extension as defined in MediaPlayer.FILE_FORMATS.

        Args:
            file (str): The file name to validate.

        Returns:
            str: The validated file name in lowercase.

        Raises:
            TypeError: If file is not a string.
            ValueError: If file does not match the filename pattern or has an invalid extension.
        """
        if not isinstance(file, str):
            raise TypeError(f"{file} should be a str, got {type(file).__name__}")
        if not MediaPlayer.FILE_PATTERN.fullmatch(file):
            raise ValueError(f"{file} is not a valid filename")

        _, file_extension = file.rsplit(".", 1)
        if file_extension.lower() not in MediaPlayer.FILE_FORMATS:
            raise ValueError(f"{file_extension} is not a valid file extension.")
        return file.lower()

    @staticmethod
    def _validate_duration(duration: int) -> int:
        """
        Validates that the given duration is an integer within the allowed range.

        Args:
            duration (int): The duration to validate.

        Returns:
            int: The validated duration.

        Raises:
            TypeError: If duration is not an integer.
            ValueError: If duration is less than MIN_DURATION or greater than MAX_DURATION.
        """
        if type(duration) is not int:
            raise TypeError(
                f"{duration} should be an int, got {type(duration).__name__}"
            )
        if duration < MediaPlayer.MIN_DURATION:
            raise ValueError(
                f"{duration} should be at least {MediaPlayer.MIN_DURATION} second(s)"
            )
        if duration > MediaPlayer.MAX_DURATION:
            raise ValueError(
                f"{duration} can't be more than {MediaPlayer.MAX_DURATION} seconds"
            )
        return duration


class VideoPlayer(MediaPlayer):
    """
    VideoPlayer extends MediaPlayer to support video-specific features such as adjustable quality settings and subtitle toggling.

    Attributes:
        VIDEO_QUALITY_PRESETS (tuple): Available video quality presets.
        subtitles_enabled (bool): Indicates if subtitles are enabled.
        quality (str): Current video quality preset.
    """

    VIDEO_QUALITY_PRESETS = ("480p", "720p", "1080p", "4K")

    def __init__(self, file: str, duration: int) -> None:
        super().__init__(file, duration)
        self.subtitles_enabled = False
        self.quality = "720p"

    def set_quality(self, quality: str) -> None:
        """
        Sets the video quality for the player.

        Parameters:
            quality (str): The desired video quality preset. Must be one of the values defined in VIDEO_QUALITY_PRESETS.

        Raises:
            TypeError: If the provided quality is not a string.
            ValueError: If the provided quality is not a valid preset.
        """
        if not isinstance(quality, str):
            raise TypeError(f"{quality} should be a str, got {type(quality).__name__}")
        if quality not in VideoPlayer.VIDEO_QUALITY_PRESETS:
            raise ValueError(f"{quality} should be {VideoPlayer.VIDEO_QUALITY_PRESETS}")
        self.quality = quality

    def toggle_subtitles(self):
        """
        Toggles the state of subtitles in the media player.

        If subtitles are currently enabled, this method will disable them.
        If subtitles are currently disabled, this method will enable them.
        """
        self.subtitles_enabled = not self.subtitles_enabled

    def get_playback_info(self) -> str:
        """
        Returns a formatted string with playback information for the media file.

        str: Playback information including file name, duration, status, quality, and subtitles.
        """
        return (
            f"File: {self.file}, Duration: {self.duration}s, Status: {self.status}, "
            f"Quality: {self.quality}, Subtitles: {'On' if self.subtitles_enabled else 'Off'}"
        )


class AudioPlayer(MediaPlayer):
    "docstring"

    EQ_PRESETS = (
        "Flat",
        "Bass Boost",
        "Treble Boost",
        "Vocal",
        "Rock",
        "Pop",
        "Classical",
        "Jazz",
        "Dance",
        "Acoustic",
        "Hip-Hop",
        "Electronic",
    )

    def __init__(self, file: str, duration: int) -> None:
        """
        Initializes a media player instance with the specified file and duration.

        Args:
            file (str): The path or name of the media file to be played.
            duration (int): The duration of the media file in seconds.

        Attributes:
            equalizer (str): The current equalizer setting. Defaults to "Flat".
            playlists (list): A list to store playlists associated with the media player.
        """
        super().__init__(file, duration)
        self.equalizer = "Flat"
        self.playlists = []

    def set_equalizer(self, equalizer: str) -> None:
        """
        Sets the equalizer preset for the audio player.

        Parameters:
            equalizer (str): The name of the equalizer preset to set.

        Raises:
            TypeError: If the provided equalizer is not a string.
            ValueError: If the provided equalizer preset is not available in EQ_PRESETS.

        """
        if not isinstance(equalizer, str):
            raise TypeError(
                f"{equalizer} should be a str, got {type(equalizer).__name__}"
            )
        if equalizer.title() not in AudioPlayer.EQ_PRESETS:
            raise ValueError(f"{equalizer} not in {AudioPlayer.EQ_PRESETS}")
        self.equalizer = equalizer

    def add_to_playlist(self, playlist: str) -> None:
        """
        Adds the specified playlist to the list of playlists.

        Args:
            playlist (str): The name of the playlist to add.

        Raises:
            TypeError: If `playlist` is not a string.
            ValueError: If `playlist` is an empty string.
            ValueError: If the playlist already exists in the list.

        """
        if not isinstance(playlist, str):
            raise TypeError(
                f"{playlist} should be a str, got {type(playlist).__name__}"
            )
        if not playlist:
            raise ValueError(f"{playlist} cannot be an empty string")
        if playlist in self.playlists:
            raise ValueError(f"{self.file} is already stored in {playlist}")
        self.playlists.append(playlist)

    def get_playlist_count(self) -> int:
        """
        Returns the number of playlists currently managed by the audio player.

        Returns:
            int: The total count of playlists.
        """
        return len(self.playlists)

    def get_playback_info(self) -> str:
        """
        Returns a formatted string with playback information for the audio file.

        The returned string includes file name, duration, playback status, equalizer setting, and playlist count.

        Returns:
            str: Playback information including file name, duration, status, equalizer, and playlists.
        """
        return (
            f"File: {self.file}, Duration: {self.duration}s, Status: {self.status}, "
            f"Equalizer: {self.equalizer}, Playlists: {len(self.playlists)}"
        )


# Test your class:
basic_player = MediaPlayer("song.mp3", duration=180)
video_player = VideoPlayer("movie.mp4", duration=7200)
audio_player = AudioPlayer("podcast.wav", duration=3600)

basic_player.play()
video_player.play()
video_player.set_quality("1080p")
video_player.toggle_subtitles()
audio_player.set_equalizer("rock")
audio_player.add_to_playlist("My Favorites")

print(basic_player.get_playback_info())  # Expected: basic playback status
print(video_player.get_playback_info())  # Expected: status + quality + subtitles
print(audio_player.get_playback_info())  # Expected: status + equalizer info
print(audio_player.get_playlist_count())  # Expected: number of playlists

"""
=== BUSINESS COMMUNICATION SUMMARY ===

Initial Request: "We're building a media player app. All players need basic controls like play, pause, stop 
and track the same file info. But video players need subtitle support and quality settings, while audio 
players need equalizer and playlist features. Each player type has additional settings to initialize."

Developer Clarifications Asked:
- Which file formats should be supported?
- Should there be duration limits for media files?
- What video quality options should be available?
- Which equalizer presets are needed?
- Are there formatting requirements for playlist names?

Stakeholder Responses:
- Support common formats (MP3, WAV, MP4, AVI) but don't be too restrictive
- Reasonable duration limits (not negative, not excessively long like 1000+ hours)
- Standard quality options (480p, 720p, 1080p, 4K for premium)
- Typical equalizer presets (Rock, Pop, Jazz, Classical, Bass Boost)
- Keep playlist names simple - just ensure they're not empty

Final Technical Decisions:
- Comprehensive file format support (12 formats) with regex validation
- Duration limits: 1 second minimum, 10 hours maximum
- Four video quality presets with validation
- Twelve equalizer presets covering all major audio styles
- Inheritance pattern: Child classes extend parent constructor and methods
- Method overriding: get_playback_info() enhanced by child classes with specialized data
- State management: Child classes initialize and manage their own specialized attributes

Assumptions Documented:
- File validation includes comprehensive filename pattern checking
- Case-insensitive equalizer preset matching for user convenience
- Playlist management allows multiple playlists per audio player
- Video players default to 720p quality and subtitles disabled
- Audio players default to "Flat" equalizer and empty playlist collection
- Status tracking uses simple string states for basic playback control
"""
