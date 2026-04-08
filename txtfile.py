import os.path
import sys

fname = input("Enter the filename to sort: ")


if not os.path.isfile(fname):
    print("File", fname, "doesn't exist")
    sys.exit(0)

infile = open(fname, "r")
lines = infile.readlines()
infile.close()


linelist = []
for line in lines:
    linelist.append(line.strip())

linelist.sort()


outfile_name = "sorted.txt"
with open(outfile_name, "w") as outfile:
    for item in linelist:
        outfile.write(item + "\n")


if os.path.isfile(outfile_name):
    print("Success! Created sorted.txt")
else:
    print("Not able to create sorted.txt")
    sys.exit(0)

for line in linelist:
    outfile.write(line + "\n")

outfile.seek(0, 0)
fstr = outfile.read()

print("sorted.txt contains", len(linelist), "Lines")
# Optional: print(fstr.count('\n')) 

outfile.close()