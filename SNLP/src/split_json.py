import sys
import os



folder_loc = sys.argv[1]
filename =sys.argv[2]
count = 0
current_piece = 1
output_name_template='output_%s.json'

fileobj = open(os.path.join(folder_loc, filename));
current_out_path = os.path.join(folder_loc, output_name_template  % current_piece)

current_out_writer = open(current_out_path,"w+");

for line in fileobj:  
    for i in range(len(line)):
 		if (line[i] == '{'):
 			count = count + 1
 		if (count == current_piece * 10000):
 			current_piece = current_piece + 1
 			current_out_path = os.path.join(folder_loc, output_name_template  % current_piece)
 		current_out_writer = open(current_out_path,"a");
 		current_out_writer.write(line[i])


