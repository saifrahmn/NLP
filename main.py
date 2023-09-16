# Import library
import spacy

# Load the language model
nlp = spacy.load("en_core_web_sm")

# Process the text
text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously.  uh ahh umm “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")
doc = nlp(text)

# Remove stop words
filtered_tokens = [token.text for token in doc]

# Print the text excluding stop words
print(filtered_tokens)