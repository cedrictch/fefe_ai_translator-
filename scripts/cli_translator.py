import sys
import os

# Ensure parent directory is in the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.translate import translate

def main():
    print("Fe'efe'e AI Translator (CLI Mode)")
    print("Type 'exit' to quit.\n")
    while True:
        text = input("Enter a sentence to translate: ").strip()
        if text.lower() == "exit":
            print("Goodbye!")
            break

        if not text:
            print("Please enter some text.\n")
            continue
        try:
            result = translate(text)
            print(f"→ {result}\n")
        except Exception as e:
            print(f"Error during translation: {e}\n")
if __name__ == "__main__":
    main()
