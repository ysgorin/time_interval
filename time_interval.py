# time_interval.py

# Create a class representing a time interval
class TimeInterval:
    # the __init__ method should accept
    # hours, minutes, and seconds parameters
    def __init__(self, hours, minutes, seconds):
        # Validate input types
        if not all(isinstance(i, int) for i in (hours, minutes, seconds)):
            raise TypeError('Hours, minutes, and seconds must be integers.')

        # Validate input values
        if hours < 0 or minutes < 0 or seconds < 0:
            raise ValueError('Hours, minutes, and seconds must be positive integers.')
        
        # Normalize the time values
        self.total_seconds = (hours * 3600) + (minutes * 60) + seconds
        self.hours = self.total_seconds // 3600

        if self.hours > 99:
            raise ValueError('Hours cannot exceed 99.')

        self.minutes = (self.total_seconds % 3600) // 60
        self.seconds = self.total_seconds % 60

    def __str__(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'
    
    def __add__(self, other):
        result_total_seconds = self.total_seconds + other.total_seconds
        result_hours = result_total_seconds // 3600
        result_minutes = (result_total_seconds % 3600) // 60
        result_seconds = result_total_seconds % 60
        return f'{result_hours:02d}:{result_minutes:02d}:{result_seconds:02d}'

    def __mul__(self, other):
        result_total_seconds = self.total_seconds * other
        result_hours = result_total_seconds // 3600
        result_minutes = (result_total_seconds % 3600) // 60
        result_seconds = result_total_seconds % 60
        return f'{result_hours:02d}:{result_minutes:02d}:{result_seconds:02d}'

tt1 = TimeInterval(5, 66, 80)
print(tt1)