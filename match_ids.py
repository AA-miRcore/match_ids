import sys
import argparse
import cStringIO
from cStringIO import StringIO

##### parse arguments
parser = argparse.ArgumentParser(description="Matches the TCGA ids listed in file A with those in file B and outputs the results to a file.");
parser.add_argument('file_A', metavar="file_A", help="The name of the file containing the subset of TCGA ids to match with file B.");
parser.add_argument('file_B', metavar="file_B", help="The name of the larger file containing the TCGA ids and ascociated file names (tab seperated).");
parser.add_argument('output_file', metavar="output_file", help="The name of the file to output the results. If the file exists, it will be OVERWRITTEN.");

_args = parser.parse_args();
globals()['args'] = _args;

##### VARS
subset_file = open(args.file_A)
with open(args.file_B) as main_file:
    main_lines = main_file.readlines()
output_file = open(args.output_file, "w+")
#A pointer for the current line of file_B (main_file)
pointer = 0

##### FUNCTIONS
#Points the reader of file B to the current TCGA id
def point_to_id(tcga_id):
    global pointer
    row = main_lines[pointer]
    while(row.split('\t')[0] != tcga_id):
        pointer += 1
        row = main_lines[pointer]

#Reads all the rows in file B with the specified TCGA id and appends them to the output file. Also returns the output so it can be reused
def read_and_append_rows(tcga_id):
    global pointer
    output = StringIO();
    row = main_lines[pointer]
    while(row.split('\t')[0] == tcga_id):
        output.write(row)
        pointer += 1
        #End reached, stop and write final output
        if(pointer >= len(main_lines)):
            break
        row = main_lines[pointer]
    #Write and return output
    output_value = output.getvalue()
    output_file.write(output_value)
    return output_value

##### MAIN
#Loop to the next unqiue TCGA id
last_line = None;
last_output = None;
for line in subset_file:
    line = line.strip()
    if(line != last_line):
        #If a new TCGA id, move the pointer in file B
        point_to_id(line)
        #Find matches, append to the output file, and store matches locally
        last_output = read_and_append_rows(line)
    else:
        #If duplicate line, repeat the last output
        output_file.write(last_output)
    last_line = line
