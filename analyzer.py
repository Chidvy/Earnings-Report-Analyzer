import anthropic
import sys

def analyze_earnings(text, api_key):
    client = anthropic.Anthropic(api_key=api_key)
    
    prompt = f"""You are a financial analyst. Analyze the following earnings report or press release and return a structured summary with these sections:

1. COMPANY & PERIOD: Company name and reporting period
2. KEY METRICS: Revenue, net income, EPS, and YoY growth where available
3. HIGHLIGHTS: 3 bullet points of major positives
4. RISKS: 2 bullet points of concerns or headwinds
5. SENTIMENT: One word — Positive, Neutral, or Negative

Earnings Report:
{text}"""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return message.content[0].text

def main():
    api_key = input("Enter your Anthropic API key: ")
    print("\nPaste your earnings report text below.")
    print("When done, type END on a new line and press Enter:\n")
    
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    
    report_text = "\n".join(lines)
    
    print("\nAnalyzing...\n")
    result = analyze_earnings(report_text, api_key)
    print("=" * 50)
    print(result)
    print("=" * 50)

if __name__ == "__main__":
    main()