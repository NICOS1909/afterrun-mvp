"""Data models for AfterRun MVP."""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List


@dataclass
class ActivityData:
    """Model for parsed activity data from GPX/TCX files."""
    filename: str
    total_distance: float  # in kilometers
    duration: float  # in seconds
    avg_pace: float  # in minutes per kilometer
    elevation_gain: Optional[float] = None  # in meters
    max_heart_rate: Optional[int] = None
    avg_heart_rate: Optional[int] = None
    timestamp: Optional[datetime] = None
    
    def get_duration_formatted(self) -> str:
        """Return duration in HH:MM:SS format."""
        hours = int(self.duration // 3600)
        minutes = int((self.duration % 3600) // 60)
        seconds = int(self.duration % 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    def get_pace_formatted(self) -> str:
        """Return pace in MM:SS format."""
        minutes = int(self.avg_pace)
        seconds = int((self.avg_pace - minutes) * 60)
        return f"{minutes:02d}:{seconds:02d}"


@dataclass
class SelfAssessment:
    """Model for user self-assessment."""
    feeling: str  # How did you feel? (1-5 scale or descriptive)
    difficulty: str  # How hard was the run?
    notes: str  # Any additional notes


@dataclass
class Feedback:
    """Model for AI-generated feedback."""
    summary: str
    context: str
    data_vs_feeling: str
    reflection_options: List[str]
    
    def to_dict(self) -> dict:
        """Convert feedback to dictionary."""
        return {
            'summary': self.summary,
            'context': self.context,
            'data_vs_feeling': self.data_vs_feeling,
            'reflection_options': self.reflection_options
        }
