import re

# Regex patterns for extraction

EMAIL_REGEX = re.compile(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b')
URL_REGEX = re.compile(r'\bhttps?:\/\/[^\s<>"]+\b')
PHONE_REGEX = re.compile(r'\b(?:\(?\d{3}\)?[\s.-]?)\d{3}[\s.-]?\d{4}\b')
CARD_REGEX = re.compile(r'\b(?:\d{4}[-\s]?){3}\d{4}\b')

def is_safe(value: str) -> bool:

    #Basic defensive check to ignore potentially malicious input
    
    blacklist = ["<", ">", "script", "javascript:"]
    value = value.lower()
    return not any(bad in value for bad in blacklist)

def mask_card(card: str) -> str:
    
    #Masks credit card numbers to avoid exposing sensitive data so that Only the last 4 digits are shown.
    
    digits = re.sub(r'\D', '', card)
    return f"**** **** **** {digits[-4:]}"

def extract_data(text: str) -> dict:
    
    #Extracts structured data from raw text using regex, while ignoring unsafe input.
    
    data = {
        "emails": [],
        "urls": [],
        "phones": [],
        "credit_cards": []
    }

    for email in EMAIL_REGEX.findall(text):
        if is_safe(email):
            data["emails"].append(email)

    for url in URL_REGEX.findall(text):
        if is_safe(url):
            data["urls"].append(url)

    for phone in PHONE_REGEX.findall(text):
        if is_safe(phone):
            data["phones"].append(phone)

    for card in CARD_REGEX.findall(text):
        if is_safe(card):
            data["credit_cards"].append(mask_card(card))

    return data

def main():
    # Read sample input from text file
    with open("sample_input.txt", "r") as file:
        raw_text = file.read()

    extracted = extract_data(raw_text)

    # Output results in a readable way
    print("Extracted Data:\n")
    for key, values in extracted.items():
        print(f"{key.capitalize()}:")
        for value in values:
            print(f"  - {value}")
        print()

if __name__ == "__main__":
    main()
