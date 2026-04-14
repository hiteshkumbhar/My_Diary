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


# 📓 My Diary — A Secure Terminal-Based Personal Journal

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-XOR_Encryption-blue?style=for-the-badge)

## About
**My Diary** is a lightweight, command-line interface (CLI) application designed for users who prioritize privacy and simplicity in their journaling routine. Built with a focus on data security, the application ensures that every entry—from daily thoughts to specific timestamps—is obfuscated using a custom XOR cipher. This prevents unauthorized users from reading the raw text files stored locally on your machine, providing a digital "lock and key" for your private reflections.

Engineered with robustness in mind, the project features a reliable file-handling system that manages data persistence within a dedicated directory in the user's home folder. By combining Python's `pathlib` for cross-platform compatibility and `zoneinfo` for accurate regional time-stamping, My Diary offers a seamless experience for documenting personal growth while maintaining a strictly local and private footprint.

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
   git clone [https://github.com/yourusername/my-diary.git](https://github.com/yourusername/my-diary.git)
