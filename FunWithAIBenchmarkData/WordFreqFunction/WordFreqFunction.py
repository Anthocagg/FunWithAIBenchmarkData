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


#WordFreqfunction.py



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
    ax.set_title('Most Prevalent Words in the Management Test', fontsize=15, fontweight='bold')

    # Add data labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, fontweight='bold', color='darkblue')

    # Add a legend with a transparent background and black outline
    legend = ax.legend(['Word Frequencies'], loc='upper right', fontsize=10)
    legend.get_frame().set_facecolor('none')  # Set background color to transparent
    legend.get_frame().set_edgecolor('black')  # Set the border color to black

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
