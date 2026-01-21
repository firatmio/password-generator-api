from fastapi import FastAPI
import uvicorn
import random
import string

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/password")
def create_password(
    length: int, 
    lower: bool = False, 
    upper: bool = False, 
    digits: bool = False, 
    special: bool = False
):
    if length <= 0:
        return {"error": "Length must be a positive integer."}
    
    char_sets = {
        'lower': string.ascii_lowercase,
        'upper': string.ascii_uppercase,
        'digits': string.digits,
        'special': string.punctuation
    }
    
    selected_chars = ""
    if lower:
        selected_chars += char_sets['lower']
    if upper:
        selected_chars += char_sets['upper']
    if digits:
        selected_chars += char_sets['digits']
    if special:
        selected_chars += char_sets['special']
        
    if not selected_chars:
        return {"error": "At least one character set (lower, upper, digits, special) must be selected."}
        
    password = ''.join(random.choice(selected_chars) for _ in range(length))
    return {"password": password}

"""

example usage:
http://localhost:8000/password?length=12&lower=true&upper=true&digits=true&special=false

"""

def main():
    uvicorn.run(f"main:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    main()