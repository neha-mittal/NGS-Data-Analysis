class Reverse_complement: #we are just defining the name of the class;
#     # new_string = '' #we are defining the class variables here;
    def __init__(self, input_1, reverse_string): #we are initializing the class and passing the object and input string;         
        self.input_1 = input_1 #we have linked the class variables with self (object of the class);
        self.new_string = ''
        self.reverse_string = reverse_string
    def complement(self):
        for input in self.input_1:
            # print(self.input_1)
            if input == 'A':
                self.new_string += 'T'
                # print(self.new_string)
            elif input == 'T':
                self.new_string += 'A'
            elif input == 'C':
                self.new_string += 'G'
            elif input == 'G':
                self.new_string+='C'
            else:
                pass
        # print("The complement strand of DNA is:", self.new_string)
        # return self.new_string

    def reverse(self):
        self.reverse_string = self.new_string[::-1]

class GC_content():
    def __init__(self, reverse_string, count):
    #     Reverse_complement.__init__(self, input_1, new_string, reverse_string) #calling the parent class constructors
        self.count = count
        self.reverse_string = reverse_string
    #     # print(self.input_1)
    def gc_count(self):
        # i = 0
        # while i < len(self.input_1):
        #     if input_1[i] == 'G' or input_1[i] == 'C':
        #         self.count += 1
        #     else:
        #         pass
        #     i += 1
        # for i in range(len(self.input_1)):
        #     if self.input_1[i] == 'G' or self.input_1[i] == 'C':
        #         self.count += 1
        #     else:
        #         pass
        for reverse in self.reverse_string:
            if reverse == 'G' or reverse == 'C':
                self.count += 1
            else:
                pass

class Counting_mutation(Reverse_complement):
    def __init__(self, input_1, input_2, count1, reverse_string):
        Reverse_complement.__init__(self, input_1, reverse_string)
        # GC_content.__init__(self, reverse_string, count)
        # self.input_1 = input_1
        self.input_2 = input_2
        self.count1 = count1
        # print(self.count1)
 
    def point_mutations(self): #Function to compare position by position alphabets and count dissimilar locations/mutations of equal length of the string;
        if len(self.reverse_string) == len(self.input_2):
            print("The length of the two strings are equal and can perfom the alignment")
            for i in range (len(self.reverse_string)):
            # for j in range(len(self.input_2)): #We can have nested loop when we would like to compare all the values of input_2 one by one with input_1
                # print(self.reverse_string[i])
                if self.reverse_string[i] != self.input_2[i]:
                    # print(self.input_2[i])
                    self.count1 += 1
                    # print(self.count1)
                else:
                    pass
        else:
            print("The length of the two strings are not equal and can't perfom the alignment")

class Transcribe_and_Translation(Counting_mutation):
    def __init__(self, input_1, input_2, count1, reverse_string, transcribe_string):
        Counting_mutation.__init__(self, input_1, input_2, count1, reverse_string)
        # self.input_3 = input_3
        # print(self.input_3)
        self.transcribe_string = transcribe_string
        # self.translation_dict = translation_dict
    
    def transcription(self):
        i = 0
        while i < len(self.reverse_string):
            # print(self.input_3)
            if self.reverse_string[i] == "T":
                # print(self.input_3)
                self.transcribe_string = self.reverse_string.replace("T", "U")
                # print(self.transcribe_string)
            else:
                pass
            i += 1
    
    def translation(self):
        translation_output = ''
        self.translation_output = translation_output
        translation_dict = {'F':['UUU','UUC'], 'L': ['UUA','UUG','CUU','CUC','CUA','CUG'], 'I':['AUU','AUC','AUA'], 'M':['AUG'],
        'V':['GUU','GUC','GUA','GUG'], 'S':['UCU','UCA','UCG','UCC'], 'P':['CCU','CCC','CCA','CCG'], 'T':['ACU','ACC','ACA','ACG'],
        'A':['GCU','GCC','GCA','GCG'], 'Y':['UAU','UAC'], 'H':['CAU','CAC'], 'Q':['CAA','CAG'], 'N':['AAU','AAC'], 'K':['AAA','AAG'],
        'D':['GAU','GAC'], 'E':['GAA','GAG'], 'C':['UGU','UGC'], 'W':['UGG'], 'R':['CGU','CGC','CGA','CGG','AGA','AGG'], 'S':['AGU','AGC'],
        'G':['GGU','GGC','GGA','GGG'], 'STOP':['UAA','UAG','UGA']}
        i=0
        if len(self.transcribe_string) % 3 == 0:
            print("The string length is multiple of three and can perform the genetic code identification function")
            while i < len(self.transcribe_string):
                for key, value in translation_dict.items():
                    for j in value:
            # print(self.transcribe_string[i:i+3])
                        if self.transcribe_string[i:i+3] == j:
                            self.translation_output += key                       
                        else:
                            pass
                i+=3
        else:
            print("The string length is not multiple of three and can not perform the genetic code identification function")
        # print("The key corresponding to the defined genetic code is:", self.translation_output)
        # for i in range(len(self.transcribe_string),3):
        #     for key, value in self.translation_dict.items():
        #         for j in value:
        #             # print(self.transcribe_string[i:i+3])
        #             if self.transcribe_string[i:i+3] == j:
        #                 # print("The key corresponding to the defined genetic code is:", key)
        #             else:
        #                 pass

input_1 = input("Enter your first DNA string here,")
input_2 = input("Enter your second DNA string here,")
count1 = 0
reverse_string = ''
count = 0
# translation_dict = {}
# input_3 = input("Enter your DNA string for transcription and translation here")
transcribe_string = ''
t2 = Transcribe_and_Translation(input_1, input_2, count1, reverse_string, transcribe_string)
t2.complement()
t2.reverse()
t2.point_mutations()
print("The total number of point mutations among the input strings are:", t2.count1)
t2.transcription()
print("The transcribed RNA:", t2.transcribe_string)
t2.translation()
print("The key corresponding to the defined genetic code is:", t2.translation_output)
 