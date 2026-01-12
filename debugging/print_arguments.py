$ cat print_arguments.py
#!/usr/bin/python3
import sys

for i in range(len(sys.argv)):
    print(sys.argv[i])

$ ./print_arguments.py 1 2 3
print_arguments.py
1
2
3