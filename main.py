import ollama

response = ollama.generate(model='llama3', prompt='Why is the sky blue?')


print(response)