# Name: Anthony Caggiano & Alex Carnes
# email:  caggiaaj@mail.uc.edu / carnesas@mail.uc.edu
# Assignment Number: Assignment 07  
# Due Date:   10/24/24
# Course #/Section:   IS4010 001
# Semester/Year:   24F
# Brief Description of the assignment:  This assignment is focused on taking a provided python solution
# and using any resource we can find to visualize the data in an interesting fashion.
# Brief Description of what this module does: Creates a function that visualizes our data into a bar chart
# that counts the most prevalent words in the question list.
# Citations: Microsoft Copilot 
# https://stackoverflow.com/questions/45142897/how-to-edit-tables-in-python
# https://matplotlib.org/stable/api/pyplot_summary.html
# https://www.geeksforgeeks.org/how-to-create-a-table-with-matplotlib/
# https://jakevdp.github.io/PythonDataScienceHandbook/04.06-customizing-legends.html
# Anything else that's relevant:

# main.py


from readingLevelPackage.readingLevel import Reading_Level
from utilitiesPackage.utilities import *
from utilitiesPackage.CSV_Utilities import *
from PDFPackage.PDFUtilities import *
from collections import *
import matplotlib.pyplot as plt
from WordFreqFunction.WordFreqFunction import *


if __name__ == "__main__":
    CSV_Processor = MMLU_CSV_Processor("dataPackage/MMLU/data/", ["management_test.csv"])
    questions = CSV_Processor.read_data()
    print(len(questions), "questions read")
 
    myPDF = PDFUtilities()
    myPDF.create_question_PDF("Management Test", "MMLU", questions)
   
    print("The first question:")
    print(questions[0])
    
    text = convert_dictionaries_to_string(questions, ["prompt", "possible answers"])
    #print("\ntext from dictionaries:", text[0:500])

    #0. Append all the prompts into a big string - See utilities.convert_dictionaries_to_string()
    
    #1. Perform reading level analysis on the big string and print the results to the console.
    Reading_Level.compute_readability_indices("MMLU", text)
    
    #2. Process the big string to find the longest word
    longest_word = max(text.split(), key=len)
    print(f"The longest word in the text is: {longest_word}")

    #3. Process the big string to find the most prevalent word
    words = text.split()
    word_count = Counter(words)
    
    # Ensure there are words to count
    if word_count:
        most_common_word = word_count.most_common(1)[0]
        print(f"The most prevalent word in the text is: '{most_common_word[0]}' with {most_common_word[1]} occurrences.")
    else:
        print("No words found in the text.")
    
    #4. Perform data visualization
    plot_word_frequency(word_count)

    #5. Use the VS debugger: set a breakpoint somewhere to pause the project when a prompt containing the word "PEST" is read from the original CSV file
    
    #6a. Write all the questions and possible answers (without the correct answer) to a text file. Use a CSV format and create a unique identifier field for each question.
    #6b. Write the question identifier (see 6a, above) and the correct answer to another text file. Use a CSV format.
    questions_written = write_questions_to_text_files("MMLU", questions)
    print(questions_written, "questions written to the file.")




