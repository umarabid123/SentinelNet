from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("facebook/llama-3b")
tokenizer = AutoTokenizer.from_pretrained("facebook/llama-3b")
