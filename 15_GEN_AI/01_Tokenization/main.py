import tiktoken


encoder = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! How are you doing today?"
tokens = encoder.encode(text)
print("Encoded Tokens:", tokens)
# Encoded Tokens: [25216, 3274, 0, 3673, 1308, 382, 398, 3403, 1776, 170676]

decoded = encoder.decode(tokens)
print("Decoded Text:", decoded)
# Decoded Text: Hey There! How are you doing today?
