from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load model and tokenizer
model_name = "google/flan-t5-base"
tokenizer = T5Tokenizer.from_pretrained(model_name, legacy=False)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Define the prompt
prompt = "Answer this: What is a fruit?"

# Tokenize and generate output
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(inputs.input_ids, max_length=50000)

# Decode and print the answer
answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Answer:", answer)