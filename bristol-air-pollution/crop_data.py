file_in = 'bristol-air-quality-data.csv'
file_out = 'air-quality-data.updated.csv'    # the file to be written to csv
infile = open(file_in, 'r')                  # opening file
outfile = open(file_out, 'w')
lines = infile.readlines()
print("the file " + file_in + " has " + str(len(lines)) + " lines.")
infile.close()
year = "2010"
for lines in lines:
    if lines > year:
        outfile.write(lines)
outfile = open(file_out, 'r')
lines = outfile.readlines()
print("the file " + file_out + " has " + str(len(lines)) + " lines.")

