import sys
import os
import subprocess

output_file_path = "wc_log.txt"

source_files = "diff_buffer"
main_file = "server_storage/40074-0.txt"


#main file
bashCmd = ["wc", main_file]
process = subprocess.Popen(bashCmd, stdout=open(output_file_path,"a"))

#generated files
for file in os.listdir(source_files):
    # print(file)
    # print(main_file)
    # print(dest_file)
    file_path = "{}/{}".format("diff_buffer",file)
    bashCmd = ["wc", file_path]
    process = subprocess.Popen(bashCmd, stdout=open(output_file_path,"a"))

# bashCmd = ["ls", "."]
# process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)