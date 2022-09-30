import os, gzip, shutil
import sys
from Bio import SeqIO
import pylab as plt
import numpy as np
# def unzipping_files(input_1): #Function definition;
    #print("the total length of the GC")
    # extension = ".gz"
    # os.chdir(input_1)
    # for item in os.listdir(input_1):
    #     if item.endswith(extension):
    #         gz_name = os.path.abspath(item) # Complete path of the files with zipped format and whole directory path;
    #         #print("The full path of directory files:", gz_name)
    #         file_name = (os.path.basename(gz_name)).rsplit('.',1)[0] # Just the base name of the file without .gz extension;
    #         #print(file_name)
    #         with gzip.open(gz_name,"rb") as f_in, open(file_name, "wb") as f_out:
    #             shutil.copyfileobj(f_in, f_out)
# GC_Content_Percent("/Users/neha/Desktop/Data_Files_Python_Analysis/Zipped_Input_Files/Food-1-R1.fastq")
            #os.remove(gz_name)

def GC_Content_Percent(file_name):
    gc_list = []
    length_list = []
    limit = 0
    for fastq_parser in SeqIO.parse(open(file_name, "rt"), "fastq"):
        limit += 1
        # print(fastq_parser.seq)
        count = 0
        for i in fastq_parser.seq:
            if i == "C" or i == "G":
                count = count + 1
        gc_list.append(count)
            # else:
                # count = count
    # print("The total value of G and Cs':", gc_list)
        
        read_length = len(fastq_parser.seq)
        length_list.append(read_length)

        if limit >= 10:
            break
    
    print("The total value of G and Cs':", gc_list)
    print("The total length':", length_list)


    
    plt.plot(range(0,10), gc_list,)
    plt.ylabel("GC Count")
    plt.xlabel("Length")
    plt.savefig("gc_plot.pdf")
    plt.show()

    # print(length_list)
        
        # if limit >= 10000:
        #     break
        
        
# input_1 =  input("enter your path") 
# unzipping_files(input_1) #Calling the Function;
GC_Content_Percent("/Users/neha/Desktop/Data_Files_Python_Analysis/Zipped_Input_Files/Food-1-R1.fastq")




# /Users/neha/Desktop/Data_Files_Python_Analysis/Zipped_Input_Files