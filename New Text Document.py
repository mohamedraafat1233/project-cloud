import re
from collections import Counter

file_path = ("C://Users//Mega Store//Desktop//project//paragraphs.txt", "r")
def read_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

def remove_stopwords(text, stopwords):
    words = text.split()
    cleaned_words = [word for word in words if word.lower() not in stopwords]
    return ' '.join(cleaned_words)

def count_word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = Counter(words)
    return word_count

def main():
    # Read the contents of the file
    file_path = "C://Users//Mega Store//Desktop//project//paragraphs.txt"
    text = read_file(file_path)

 # Define stop words
    stopwords = set([
        "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", 
        "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", 
        "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was",
        "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and",
        "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between",
        "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off",
        "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both",
        "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too",
        "very", "s", "t", "can", "will", "just", "don", "should", "now"
    ])
     # Remove stop words
    cleaned_text = remove_stopwords(text, stopwords)
    
    # Count word frequency
    word_frequency = count_word_frequency(cleaned_text)
    
     # Display word frequency count
    for word, count in word_frequency.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
     


