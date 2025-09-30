📂 Project Structure
.
├── support_bot_agent.py    # Main bot script
├── support_bot_log.txt     # Log file (ignored by git)
├── requirements.txt        # Dependencies
├── README.md               # Project guide
└── notebooks/              # (Optional) Jupyter notebooks for experiments

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/khandusurwase/Faqbot.git
cd Faqbot

2️⃣ Create a Virtual Environment (recommended)
python -m venv venv
source venv/bin/activate     # On Linux/Mac
venv\Scripts\activate        # On Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Running the Bot

Run the Python script:

python support_bot_agent.py


Example log (support_bot_log.txt):

[2025-09-30 12:30:05] INFO: Bot started
[2025-09-30 12:30:06] INFO: Document uploaded: customer_policy.pdf
[2025-09-30 12:30:12] ACTION: Extracting text from PDF
[2025-09-30 12:30:18] DECISION: Using QA module for user query
[2025-09-30 12:30:19] ACTION: Sending query to LLM -> "What is the refund policy?"
[2025-09-30 12:30:23] RESPONSE: "Refunds are processed within 7 business days."

🛠 Dependencies

Python 3.8+

openai (for LLM calls)

PyPDF2 or pdfplumber (for PDF extraction)

logging (for log management)

Install them via:

pip install -r requirements.txt

📝 Notes

By default, the bot writes logs to support_bot_log.txt.

The log file is ignored in .gitignore (to avoid large commits).

You can provide a sample PDF in the repo (like sample_faq.pdf) for testing.

📌 Future Improvements

Add a FastAPI/Flask web interface.

Enable chatbot integration (Telegram, Slack, etc.).

Support multiple document types (Word, Excel).
