"""
Create a Website class that tracks total visits across all instances.

Requirements:
- Class variable total_visits = 0 (shared by all instances)
- Initialize with site_name and individual visit_count (default: 0)
- Create method record_visit() that increments both instance and class counters
- Create method get_site_stats() that returns individual stats
- Create class method get_global_stats() that returns total visits across all sites

Test your class:
site1 = Website("blog.com")
site2 = Website("shop.com")
site1.record_visit()
site1.record_visit()
site2.record_visit()
print(site1.get_site_stats())     # Should show 2 visits
print(Website.get_global_stats()) # Should show 3 total visits
"""

class Website:
    total_visits = 0

    def __init__(self, site_name, visit_count=0):
        self.site_name = site_name
        self.visit_count = visit_count
    
    def record_visit(self):
        Website.total_visits += 1
        self.visit_count += 1
    
    def get_site_stats(self):
        return f"{self.site_name}: {self.visit_count} visits"
    
    @classmethod
    def get_global_stats(cls):
        return f"Total visits across all sites: {cls.total_visits}"

site1 = Website("blog.com")
site2 = Website("shop.com")
site1.record_visit()
site1.record_visit()
site2.record_visit()
print(site1.get_site_stats())     # Should show 2 visits
print(Website.get_global_stats()) # Should show 3 total visits