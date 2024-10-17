# main.py
# Anthony Caggiano & Alex
# caggiaaj@mail.uc.edu & 

from readingLevelPackage.readingLevel import Reading_Level
from utilitiesPackage.utilities import *
from utilitiesPackage.CSV_Utilities import *
from PDFPackage.PDFUtilities import *
from collections import *
import matplotlib.pyplot as plt


def plot_word_frequency(word_count):
    # Get the top 10 most common words
    most_common_words = word_count.most_common(10)
    words, counts = zip(*most_common_words)

    # Set the style
    plt.style.use('ggplot')

    fig, ax = plt.subplots()
    
    # Create bar chart with custom colors
    colors = plt.cm.Paired(range(len(words)))  # Custom color map
    bars = ax.bar(words, counts, color=colors, edgecolor='black')

    # Add a grid
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

    # Add labels and title
    ax.set_xlabel('Words', fontsize=12, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
    ax.set_title('Top 10 Most Prevalent Words', fontsize=15, fontweight='bold')

    # Add data labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, fontweight='bold', color='darkblue')

    # Add a legend
    ax.legend(['Word Frequencies'], loc='upper right', fontsize=10)

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

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
