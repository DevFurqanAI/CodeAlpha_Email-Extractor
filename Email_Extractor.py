import os
import re

class EmailExtractor:
    def __init__(self, input_file, output_file):
        # Store input and output file paths
        self.input_file = input_file
        self.output_file = output_file

    def read_file(self):
        """
        Reads the content of the input text file.
        Ensures that the file exists before attempting to open it.
        """
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"❌ Input file not found: {self.input_file}")

        with open(self.input_file, "r", encoding="utf-8") as file:
            return file.read()

    def extract_emails(self, text):
        """
        Extracts all email addresses from the provided text.
        Uses a regular expression pattern to match email formats.
        """
        pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        return re.findall(pattern, text)

    def save_emails(self, emails):
        """
        Saves the extracted email addresses to the output file.
        Each email is written on a new line for readability.
        """
        with open(self.output_file, "w", encoding="utf-8") as file:
            for email in emails:
                file.write(email + "\n")

        print(f"✅ Extracted {len(emails)} emails and saved to: {self.output_file}")

    def run(self):
        """
        Coordinates the overall workflow:
        1. Reads the input file.
        2. Extracts emails using regex.
        3. Saves the extracted emails to the output file.
        """
        print("📄 Reading file...")
        text = self.read_file()

        print("🔍 Extracting emails...")
        emails = self.extract_emails(text)

        print("💾 Saving results...")
        self.save_emails(emails)

        print("🎉 Task Completed!")


# Executes the program when run directly from the script
if __name__ == "__main__":
    extractor = EmailExtractor("files.txt", "emails_output.txt")
    extractor.run()
