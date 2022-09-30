class Reverse_complement: #we are just defining the name of the class;
#     # new_string = '' #we are defining the class variables here;
    def __init__(self, input_1, new_string, reverse_string): #we are initializing the class and passing the object and input string;         
        self.input_1 = input_1 #we have linked the class variables with self (object of the class);
        self.new_string = new_string
        self.reverse_string = reverse_string
    def complement(self):
        # new_string = ''
        for input in self.input_1:
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

class Counting_mutation(Reverse_complement,GC_content):
    def __init__(self, input_1, input_2, count1, new_string, reverse_string, count):
        Reverse_complement.__init__(self, input_1, new_string, reverse_string)
        GC_content.__init__(self, reverse_string, count)
        # self.input_1 = input_1
        self.input_2 = input_2
        self.count1 = count1
 
    def point_mutations(self): #Function to compare position by position alphabets and count dissimilar locations/mutations of equal length of the string;
        if len(self.reverse_string) == len(self.input_2):
            print("The length of the two strings are equal and can perfom the alignment")
            for i in range (len(self.reverse_string)):
            # for j in range(len(self.input_2)): #We can have nested loop when we would like to compare all the values of input_2 one by one with input_1
                if self.reverse_string[i] != self.input_2[i]:
                    self.count1 += 1
                else:
                    pass
        else:
            print("The length of the two strings are not equal and can't perfom the alignment")

input_1 = input("Enter your first DNA string here,")
input_2 = input("Enter your second DNA string here,")
count1 = 0
new_string = ''
reverse_string = ''
count = 0 

cm = Counting_mutation(input_1, input_2, count1, new_string, reverse_string, count)
cm.complement()
print("The complement format of the DNA string is:", cm.new_string)
cm.reverse()
print("The reverse format of the DNA string is:", cm.reverse_string)
cm.gc_count()
print("The GC content of the DNA string is:", cm.count)
cm.point_mutations()
print("The total number of point mutations among the DNA strings are:", cm.count1)