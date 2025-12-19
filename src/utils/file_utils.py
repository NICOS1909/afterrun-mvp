"""Utility functions for file operations."""
import os
from datetime import datetime
from typing import Optional


def save_uploaded_file(uploaded_file, upload_dir: str = "data/uploads") -> Optional[str]:
    """
    Save an uploaded file to the upload directory.
    
    Args:
        uploaded_file: Streamlit UploadedFile object
        upload_dir: Directory to save uploaded files
        
    Returns:
        Path to the saved file or None if save fails
    """
    try:
        # Create upload directory if it doesn't exist
        os.makedirs(upload_dir, exist_ok=True)
        
        # Generate a unique filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        original_filename = uploaded_file.name
        filename_parts = os.path.splitext(original_filename)
        new_filename = f"{filename_parts[0]}_{timestamp}{filename_parts[1]}"
        
        file_path = os.path.join(upload_dir, new_filename)
        
        # Save the file
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        return file_path
        
    except Exception as e:
        print(f"Error saving file: {e}")
        return None


def cleanup_old_files(upload_dir: str = "data/uploads", days: int = 7) -> None:
    """
    Clean up files older than specified days.
    
    Args:
        upload_dir: Directory containing uploaded files
        days: Number of days to keep files
    """
    try:
        if not os.path.exists(upload_dir):
            return
        
        current_time = datetime.now()
        
        for filename in os.listdir(upload_dir):
            file_path = os.path.join(upload_dir, filename)
            
            if os.path.isfile(file_path):
                file_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                days_old = (current_time - file_modified_time).days
                
                if days_old > days:
                    os.remove(file_path)
                    print(f"Removed old file: {filename}")
                    
    except Exception as e:
        print(f"Error cleaning up old files: {e}")
