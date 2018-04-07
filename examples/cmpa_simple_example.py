
from cmpa import compare, Compare

# Just compare directory with itself.
compare(['.', '.'])
print()

# Use the class for finer grain observability
c = Compare(['.', '.'], silent=True)
print(c.get_total_files())
print(c.get_file_counts())
print(c.compare_ok_count)
