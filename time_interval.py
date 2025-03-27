# time_interval.py

# Create a class representing a time interval
class TimeInterval:
    # the constructor initializes the TimeInterval object with hours, minutes, and seconds
    def __init__(self, hours, minutes, seconds):
        # Validate that all inputs are integers
        if not all(isinstance(i, int) for i in (hours, minutes, seconds)):
            raise TypeError('Hours, minutes, and seconds must be integers.')

        # Validate that all inputs are non-negative
        if hours < 0 or minutes < 0 or seconds < 0:
            raise ValueError('Hours, minutes, and seconds must be positive integers.')
        
        # Convert the inputs into total seconds for easier calculations
        self.total_seconds = (hours * 3600) + (minutes * 60) + seconds
        
    # Helper method to normalize total seconds
    def _normalize_time(self, total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return hours, minutes, seconds

    #  Helper method to format total seconds as HH:MM:SS
    def _format_time(self, total_seconds):
        hours, minutes, seconds = self._normalize_time(total_seconds)
        return f'{hours}:{minutes:02d}:{seconds:02d}'

    # String representation of the TimeInterval object
    def __str__(self):
        return self._format_time(self.total_seconds)
    
    # Magic method for addition (+)
    def __add__(self, other):
        # Adding an integer means to add seconds
        if isinstance(other, int):
            return self._format_time(self.total_seconds + other)
        elif isinstance(other, TimeInterval):
            return self._format_time(self.total_seconds + other.total_seconds)
        else:
            raise ValueError(f'{type(other)} is not valid for TimeInterval addition.')

    # Magic method for subtraction (-)     
    def __sub__(self, other):
        # Subtracting an integer means to subtract seconds
        if isinstance(other, int):
            return self._format_time(self.total_seconds - other)
        elif isinstance(other, TimeInterval):
            return self._format_time(self.total_seconds - other.total_seconds)
        else:
            raise ValueError(f'{type(other)} is not valid for TimeInterval subtraction.')
    
    # Magic method for multiplication (*)
    def __mul__(self, other):
        return self._format_time(self.total_seconds * other)