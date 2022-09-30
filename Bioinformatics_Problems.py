#Reverse Complement of the DNA string/strand

from audioop import reverse


# class Reverse_complement: #we are just defining the name of the class;
#     # new_string = '' #we are defining the class variables here;
#     def __init__(self, input_1, new_string, reverse_string): #we are initializing the class and passing the object and input string;         
#         self.input_1 = input_1 #we have linked the class variables with self (object of the class);
#         self.new_string = new_string
#         self.reverse_string = reverse_string
#     def complement(self):
#         # new_string = ''
#         for input in self.input_1:
#             if input == 'A':
#                 self.new_string += 'T'
#                 # print(self.new_string)
#             elif input == 'T':
#                 self.new_string += 'A'
#             elif input == 'C':
#                 self.new_string += 'G'
#             elif input == 'G':
#                 self.new_string+='C'
#             else:
#                 pass
#         # print("The complement strand of DNA is:", self.new_string)
#         # return self.new_string

#     def reverse(self):
#         self.reverse_string = self.new_string[::-1]

# #******This is the example of Single Inheritance, using child class we are calling parent class, and using child class object we are calling the function of parent class*******#

# class GC_content(Reverse_complement):
#     def __init__(self, input_1, new_string, reverse_string, count):
#         Reverse_complement.__init__(self, input_1, new_string, reverse_string) #calling the parent class constructors
#         self.count = count
#         # print(self.input_1)
#     def gc_count(self):
#         # i = 0
#         # while i < len(self.input_1):
#         #     if input_1[i] == 'G' or input_1[i] == 'C':
#         #         self.count += 1
#         #     else:
#         #         pass
#         #     i += 1
#         # for i in range(len(self.input_1)):
#         #     if self.input_1[i] == 'G' or self.input_1[i] == 'C':
#         #         self.count += 1
#         #     else:
#         #         pass
#         for input in self.input_1:
#             if input == 'G' or input == 'C':
#                 self.count += 1
#             else:
#                 pass


# input_1 = input("Enter your DNA string here") #we are defining the local variables here, which are linked to the class variables;
# new_string = ''
# reverse_string = '' 
# count = 0
# # rev_com = Reverse_complement(input_1, new_string, reverse_string) #created the object for the class and connected with the corresponding class;
# gc_cont = GC_content(input_1, new_string, reverse_string, count)

# gc_cont.complement() #Calling the function of parent class by connecting with the object of the child class;
# print("The complement of the DNA string is:", gc_cont.new_string)
# gc_cont.reverse()
# print("The reverse complement of the DNA string is:", gc_cont.reverse_string)
# gc_cont.gc_count()
# print("The total GC content of the string is:", gc_cont.count)

# # rev_com.complement() #Calling the function by connecting with the object to see the output of that function;
# # print("The complement of the DNA string is:", rev_com.new_string) #Through the object of the class we are cllaing the variable and printing the stored values in it;
# # rev_com.reverse()
# # print("The reverse complemen of the DNA string is:", rev_com.reverse_string)

# class Counting_mutation:
#     def __init__(self, input_1, input_2, count):
#         self.input_1 = input_1
#         self.input_2 = input_2
#         self.count = count

#     def point_mutations(self): #Function to compare position by position alphabets and count dissimilar locations/mutations of equal length of the string;
#         if len(self.input_1) == len(self.input_2):
#             print("The length of the two strings are equal and can perfom the alignment")
#             for i in range (len(self.input_1)):
#             # for j in range(len(self.input_2)): #We can have nested loop when we would like to compare all the values of input_2 one by one with input_1
#                 if self.input_1[i] != self.input_2[i]:
#                     self.count += 1
#                 else:
#                     pass
#         else:
#             print("The length of the two strings are not equal and can't perfom the alignment")


# input_1 = input("Enter your first DNA string here,")
# input_2 = input("Enter your second DNA string here,")
# count = 0
# mutation = Counting_mutation(input_1, input_2, count)
# mutation.point_mutations() #calling the function of the class using the object of the class;
# print("The total number of point mutations among the string are:", mutation.count) # calling the variable of the function from the class whose results I would like to see using the object of the class;


# class Transcribe_and_Translation:
#     def __init__(self, input_3, transcribe_string, translation_dict):
#         self.input_3 = input_3
#         # print(self.input_3)
#         self.transcribe_string = transcribe_string
#         self.translation_dict = translation_dict
    
#     def Transcription(self):
#         i = 0
#         while i < len(self.input_3):
#             # print(self.input_3)
#             if self.input_3[i] == "T":
#                 # print(self.input_3)
#                 self.transcribe_string = self.input_3.replace("T", "U")
#             else:
#                 pass
#             i += 1
    
#     def Translation(self):
#         translation_output = ''
#         self.translation_output = translation_output
#         self.translation_dict = {'F':['UUU','UUC'], 'L': ['UUA','UUG','CUU','CUC','CUA','CUG'], 'I':['AUU','AUC','AUA'], 'M':['AUG'],
#         'V':['GUU','GUC','GUA','GUG'], 'S':['UCU','UCA','UCG','UCC'], 'P':['CCU','CCC','CCA','CCG'], 'T':['ACU','ACC','ACA','ACG'],
#         'A':['GCU','GCC','GCA','GCG'], 'Y':['UAU','UAC'], 'H':['CAU','CAC'], 'Q':['CAA','CAG'], 'N':['AAU','AAC'], 'K':['AAA','AAG'],
#         'D':['GAU','GAC'], 'E':['GAA','GAG'], 'C':['UGU','UGC'], 'W':['UGG'], 'R':['CGU','CGC','CGA','CGG','AGA','AGG'], 'S':['AGU','AGC'],
#         'G':['GGU','GGC','GGA','GGG'], 'STOP':['UAA','UAG','UGA']}
#         i=0
#         if len(self.transcribe_string) % 3 == 0:
#             print("The string length is multiple of three and can perform the genetic code identification function")
#             while i < len(self.transcribe_string):
#                 for key, value in self.translation_dict.items():
#                     for j in value:
#             # print(self.transcribe_string[i:i+3])
#                         if self.transcribe_string[i:i+3] == j:
#                             self.translation_output += key                       
#                         else:
#                             pass
#                 i+=3
#         else:
#             print("The string length is not multiple of three and can not perform the genetic code identification function")
#         # print("The key corresponding to the defined genetic code is:", self.translation_output)
#         # for i in range(len(self.transcribe_string),3):
#         #     for key, value in self.translation_dict.items():
#         #         for j in value:
#         #             # print(self.transcribe_string[i:i+3])
#         #             if self.transcribe_string[i:i+3] == j:
#         #                 # print("The key corresponding to the defined genetic code is:", key)
#         #             else:
#         #                 pass

# input_3 = input("Enter your DNA string for transcription and translation here")
# transcribe_string = ''
# translation_dict = {}
# t2 = Transcribe_and_Translation(input_3, transcribe_string, translation_dict)
# t2.Transcription()
# print("The transcribed RNA:", t2.transcribe_string)
# t2.Translation()
# print("The key corresponding to the defined genetic code is:", t2.translation_output)

class Find_motif:
    def __init__(self, str1, motif1, list1):
        self.str1 = str1
        self.motif1 = motif1
        self.list1 = list1

    def motif_identity(self):
        i = 0
        while i < len(self.str1):
            # for j in range(len(self.motif1)):
                if self.str1[i:i+len(self.motif1)] == self.motif1:
                    self.list1.append(i+1)
                else:
                    pass
                # print("The string contains the motif alphabet or value")
                i += 1

str1 = input("Enter your main string here")
motif1 = input("Enter your substring/motif here")
list1 = []
fm1 = Find_motif(str1, motif1, list1)
fm1.motif_identity()
print("The positions of the substring are:", fm1.list1)








































