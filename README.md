# 📓 My Diary — A Secure Terminal-Based Personal Journal

## About
**My Diary** is a lightweight, command-line interface (CLI) application designed for users who prioritize privacy and simplicity in their journaling routine. Built with a focus on data security, the application ensures that every entry—from daily thoughts to specific timestamps—is obfuscated using a custom XOR cipher. This prevents unauthorized users from reading the raw text files stored locally on your machine, providing a digital "lock and key" for your private data.

## Features
* **🔐 XOR Encryption:** Secures all journal entries and timestamps with a user-defined secret key.
* **📅 Automated Time-stamping:** Automatically logs the exact date and time of entries using the `Asia/Kolkata` timezone.
* **📂 Smart File Management:** Dynamically creates and manages data directories within the user's `Documents` folder.
* **🔍 Granular Retrieval:** Options to read the entire journal history or select specific entries via an indexed timestamp menu.
* **🛡️ Secure Authentication:** Uses hidden password masking for secret key entry to prevent shoulder-surfing.

## Tech Stack
| Technology | Purpose |
| :--- | :--- |
| **Python 3** | Core programming language |
| **Pathlib / OS** | Cross-platform file system and directory management |
| **Datetime / ZoneInfo** | Precise chronological logging and timezone handling |
| **Getpass** | Secure, masked user input for sensitive keys |

## Getting Started

### Prerequisites
* Python 3.9 or higher installed on your system.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/hiteshkumbhar/My_Diary.git
2. Navigate to the project directory:
   ```bash
    cd my-diary
3. Run the script:
   ```bash
   python My_Diary.py   

## What I Learned

Building this project was a deep dive into the practicalities of file I/O operations in Python. I learned how to manage file pointers using .seek() and .readline() to navigate through custom-formatted text files, which was essential for the "Read Specific Content" feature.
   
# Author
Your Name 
* GitHub: @hiteshkumbhar
