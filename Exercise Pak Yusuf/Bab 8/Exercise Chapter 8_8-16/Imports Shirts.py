# 1. import module_name
import shirts
print("1. import shirts")
shirts.make_shirt("L", "Belajar Python")

# 2. from module_name import function_name
from shirts import make_shirt
print("\n2. from shirts import make_shirt")
make_shirt("M", "Hello, World!")

# 3. from module_name import function_name as fn
from shirts import make_shirt as fn
print("\n3. from shirts import make_shirt as fn")
fn("S", "Python itu seru")

# 4. import module_name as mn
import shirts as mn
print("\n4. import shirts as mn")
mn.make_shirt("XL", "Coding malam hari")

# 5. from module_name import *
from shirts import *
print("\n5. from shirts import *")
make_shirt("L", "Semua fungsi ikut terimpor")