
# indexing[start:stop:step]

name = "Aliyan Sohaib"

first_name = name[:7]
last_name = name[7:14]
step_name = name[::3]
reverse_name = name[::-1]

print(first_name)
print(last_name)
print(step_name)
print(reverse_name)

# slice(start, stop, step)

web1 = "http://google.com"
web2 = "http://facebook.com"

slice = slice(7, -4)
print(web1[slice])
print(web2[slice])