file_fullpath = r"C:\Users\Izaq Baraka\Desktop\Python Ventures\supplementary_knowledge\TextDocument.txt"

# this block of code writes specified data into the file
with open(file_fullpath, 'a') as f: #   if 'w' was used instead, we would end up overwritting instead of adding at the end
    f.write("I'm added to the stars\n")
    f.write("Ready to go far\n")
    f.write("I'm star-walking!!\n")

with open(file_fullpath, 'r') as f:
    print(f.read())