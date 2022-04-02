import os,glob

os.chdir("/Users/varunpintu/Downloads")

for file in glob.glob("*.pdf"):
    print(file)