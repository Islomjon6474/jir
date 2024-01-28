import Levenshtein as lev
import jiwer

def word_similarity_check(text, bad_words_arr, threshold=0.5):
    # Preprocess the text and bad words for comparison
    transform = jiwer.Compose([
        jiwer.ToLowerCase(),
        jiwer.RemoveMultipleSpaces(),
        jiwer.Strip(),
        jiwer.RemovePunctuation()
    ])

    text = transform(text)
    bad_words_arr = [transform(word) for word in bad_words_arr]

    # Split the text into words
    words = text.split()

    # Initialize an array to hold the found bad words
    found_bad_words = []

    # Check each word in the text
    for word in words:
        for bad_word in bad_words_arr:
            # Calculate the ratio of similarity using Levenshtein distance
            similarity = lev.ratio(bad_word, word)

            # If similarity is above the threshold, we consider it a match
            if similarity >= threshold:
                return True

    # Remove duplicates from the list
    found_bad_words = list(set(found_bad_words))

    # Return the list of found bad words
    return found_bad_words

