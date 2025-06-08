# type: ignore
"""
File Size Conversion: Convert file sizes from bytes to megabytes (divide by 1,048,576 and round to 2 decimals)
"""

file_sizes_bytes = [5242880, 1048576, 15728640, 3145728]

file_sizes_megabytes = map(lambda x: round(x/1048576,2), file_sizes_bytes)

print(list(file_sizes_megabytes))