

a = None
b = 4
if not a or not b:
    print("not None ist wahr")

if 0.0 or None or [] or {} or 1:
    print("Unwahre Werte")



a = "San Francisco"
if "San" in a:
    print("San ist in San Francisco zu finden")

if "XXX" not in a:
    print("XXX aber nicht!")