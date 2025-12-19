"""Service for parsing GPX and TCX activity files."""
import gpxpy
from tcxparser import TCXParser
from datetime import datetime
from typing import Optional
import os

from src.models.activity import ActivityData


class FileParserService:
    """Service to parse GPX and TCX files and extract activity data."""
    
    @staticmethod
    def parse_gpx(file_path: str) -> Optional[ActivityData]:
        """
        Parse a GPX file and extract activity data.
        
        Args:
            file_path: Path to the GPX file
            
        Returns:
            ActivityData object or None if parsing fails
        """
        try:
            with open(file_path, 'r') as gpx_file:
                gpx = gpxpy.parse(gpx_file)
                
            # Extract data from GPX
            total_distance = 0.0
            duration = 0.0
            elevation_gain = 0.0
            timestamps = []
            heart_rates = []
            
            for track in gpx.tracks:
                for segment in track.segments:
                    # Get segment data
                    segment_data = segment.get_moving_data()
                    if segment_data:
                        total_distance += segment_data.moving_distance
                        duration += segment_data.moving_time
                    
                    # Get elevation data
                    uphill, downhill = segment.get_uphill_downhill()
                    elevation_gain += uphill
                    
                    # Get heart rate data if available
                    for point in segment.points:
                        if point.time:
                            timestamps.append(point.time)
                        
                        # Check for heart rate extension
                        if hasattr(point, 'extensions') and point.extensions:
                            for ext in point.extensions:
                                hr = ext.find('.//{http://www.garmin.com/xmlschemas/TrackPointExtension/v1}hr')
                                if hr is not None and hr.text:
                                    heart_rates.append(int(hr.text))
            
            # Convert distance to kilometers
            distance_km = total_distance / 1000.0
            
            # Calculate average pace (min/km)
            avg_pace = (duration / 60.0) / distance_km if distance_km > 0 else 0
            
            # Calculate heart rate stats
            max_hr = max(heart_rates) if heart_rates else None
            avg_hr = int(sum(heart_rates) / len(heart_rates)) if heart_rates else None
            
            # Get timestamp
            timestamp = timestamps[0] if timestamps else None
            
            filename = os.path.basename(file_path)
            
            return ActivityData(
                filename=filename,
                total_distance=round(distance_km, 2),
                duration=duration,
                avg_pace=round(avg_pace, 2),
                elevation_gain=round(elevation_gain, 2) if elevation_gain > 0 else None,
                max_heart_rate=max_hr,
                avg_heart_rate=avg_hr,
                timestamp=timestamp
            )
            
        except Exception as e:
            print(f"Error parsing GPX file: {e}")
            return None
    
    @staticmethod
    def parse_tcx(file_path: str) -> Optional[ActivityData]:
        """
        Parse a TCX file and extract activity data.
        
        Args:
            file_path: Path to the TCX file
            
        Returns:
            ActivityData object or None if parsing fails
        """
        try:
            tcx = TCXParser(file_path)
            
            # Extract data from TCX
            distance_km = tcx.distance / 1000.0 if tcx.distance else 0.0
            duration = tcx.duration if tcx.duration else 0.0
            
            # Calculate average pace (min/km)
            avg_pace = (duration / 60.0) / distance_km if distance_km > 0 else 0
            
            # Get heart rate data
            max_hr = int(tcx.hr_max) if tcx.hr_max else None
            avg_hr = int(tcx.hr_avg) if tcx.hr_avg else None
            
            # Get elevation gain
            elevation_gain = tcx.ascent if tcx.ascent else None
            
            # Get timestamp
            timestamp = tcx.started_at if hasattr(tcx, 'started_at') else None
            
            filename = os.path.basename(file_path)
            
            return ActivityData(
                filename=filename,
                total_distance=round(distance_km, 2),
                duration=duration,
                avg_pace=round(avg_pace, 2),
                elevation_gain=round(elevation_gain, 2) if elevation_gain else None,
                max_heart_rate=max_hr,
                avg_heart_rate=avg_hr,
                timestamp=timestamp
            )
            
        except Exception as e:
            print(f"Error parsing TCX file: {e}")
            return None
    
    @staticmethod
    def parse_activity_file(file_path: str) -> Optional[ActivityData]:
        """
        Parse an activity file (GPX or TCX) based on file extension.
        
        Args:
            file_path: Path to the activity file
            
        Returns:
            ActivityData object or None if parsing fails
        """
        file_extension = os.path.splitext(file_path)[1].lower()
        
        if file_extension == '.gpx':
            return FileParserService.parse_gpx(file_path)
        elif file_extension == '.tcx':
            return FileParserService.parse_tcx(file_path)
        else:
            print(f"Unsupported file format: {file_extension}")
            return None
