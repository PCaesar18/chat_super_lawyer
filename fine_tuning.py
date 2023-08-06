from modal import Image, Stub, gpu, method, web_endpoint




def download_model():
    # Load model directly
    from transformers import AutoTokenizer, AutoModelForCausalLM
    # Download model from HuggingFace
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-13b-hf")
    model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-13b-hf")