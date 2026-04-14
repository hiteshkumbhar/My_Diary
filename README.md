📓 My Diary — A Secure Terminal-Based Personal Journal

About: 
My Diary is a lightweight, command-line interface (CLI) application designed for users who prioritize privacy and simplicity in their journaling routine. Built with a focus on data security, the application ensures that every entry—from daily thoughts to specific timestamps—is obfuscated. This prevents unauthorized users from reading the raw text files stored locally on your machine, providing a digital "lock and key" for your private data.

Features: 
📅 Automated Time-stamping: Automatically logs the exact date and time of entries using the Asia/Kolkata timezone.

📂 Smart File Management: Dynamically creates and manages data directories within the user's Documents folder.

🔍 Granular Retrieval: Options to read the entire journal history or select specific entries via an indexed timestamp menu.

🛡️ Secure Authentication: Uses hidden password masking for secret key entry to prevent shoulder-surfing.

## Tech Stack
| Technology | Purpose |
| :--- | :--- |
| **Python 3** | Core programming language |
| **Pathlib / OS** | Cross-platform file system and directory management |
| **Datetime / ZoneInfo** | Precise chronological logging and timezone handling |
| **Getpass** | Secure, masked user input for sensitive keys |
