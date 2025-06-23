"""
Create a class called `Timer` with instance variable `seconds`. Add methods `add_time` 
that adds seconds and `display` that shows time in MM:SS format.

Your task: Define Timer class with time formatting
Test it with:
timer = Timer(125)
print(timer.display())  # Should print "02:05"
timer.add_time(35)
print(timer.display())  # Should print "02:40"
"""

class Timer:
    def __init__(self, seconds):
        self.seconds = seconds
    
    def add_time(self, seconds_to_add):
        self.seconds += seconds_to_add
    
    def display(self):
        mm, ss = divmod(self.seconds, 60)
        return f"{mm:02d}:{ss:02d}"
    
timer = Timer(125)
print(timer.display())  # Should print "02:05"
timer.add_time(35)
print(timer.display())  # Should print "02:40"