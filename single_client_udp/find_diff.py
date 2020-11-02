import os
import subprocess

source_files = "diff_buffer"
main_file = "server_storage/40074-0.txt"
dest_dir = "difference_files"


for file in os.listdir(source_files):
    dest_file = "{}/difference-{}.txt".format(dest_dir,file)
    # print(file)
    # print(main_file)
    # print(dest_file)
    bashCmd = ["diff", "{}/{}".format("diff_buffer",file), main_file]
    process = subprocess.Popen(bashCmd, stdout=open(dest_file,"w"))

# bashCmd = ["ls", "."]
# process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)