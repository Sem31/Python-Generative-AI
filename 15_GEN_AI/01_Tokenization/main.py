import tiktoken


encoder = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! How are you doing today?"
tokens = encoder.encode(text)
print("Encoded Tokens:", tokens)
# Encoded Tokens: [25216, 3274, 0, 3673, 1308, 382, 398, 3403, 1776, 170676]

decoded = encoder.decode(tokens)
print("Decoded Text:", decoded)
# Decoded Text: Hey There! How are you doing today?


# Steps:
#     Step 1: Tokenization -> The process of converting text into smaller units called tokens, which can be words, subwords, or characters, making it easier for models to process and understand the text.
#     Step 2: Vector Embeddings -> Transforming tokens into numerical vectors that capture semantic meaning, allowing the model to work with the text in a mathematical space.
#     Step 3: Positional Encoding ->  Adding information to token embeddings to indicate the position of each token in the sequence, helping the model understand the order of words.
#     Step 4: Self Attention Mechanism -> A method that allows the model to focus on different parts of the input sequence when generating each part of the output, improving context understanding.
