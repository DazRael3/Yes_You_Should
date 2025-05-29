import openai

openai.api_key = "your_openai_api_key_here"  # Or use an environment variable

def generate_description(title, features):
    prompt = f"Write an engaging product description for a product titled '{title}' with these features: {features}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].message["content"].strip()

def mock_ebay_price_comparison(title):
    # Simulated eBay price data (real API can be plugged in here)
    return f"eBay Price Range: $1.50 - $2.30 (Simulated)"
