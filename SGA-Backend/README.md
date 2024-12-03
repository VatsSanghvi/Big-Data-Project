# Smart Grocery Assistant App

A powerful application that helps you compare grocery prices across different stores, manage shopping lists, and stay within your budget.

## Features

- 🔍 Search products across multiple stores
- 💰 Price comparison
- 📋 Create shopping lists
- 💳 Budget management
- 🏪 Store-specific flyers and deals
- 📱 User-friendly interface

## Installation Guide

#### MacOS Installation

1. **Install Python**
   - Download Python from [python.org](https://www.python.org/downloads/)
   - Click on the downloaded file (it should be named like "python-3.12.x-macos.pkg")
   - When finished, open Terminal (press Cmd + Space, type "Terminal" and press Enter)
   - Type `python3 --version` to verify the installation

2. **Install Git**
   - Download and install Git from [git-scm.com](https://git-scm.com/download/mac)
   - Open Terminal (press Cmd + Space, type "Terminal" and press Enter)
   - Verify installation by typing: `git --version`

3. **Clone the GitHub Repository**
   - Open Terminal
   - Type the following commands:
     ```bash
     cd Desktop
     git clone https://github.com/VatsSanghvi/Big-Data-Project-Group-3.git
     cd Big-Data-Project-Group-3
     ```
   - If asked about credentials, enter your GitHub username and password

#### Windows Installation

1. **Install Git**
   - Download Git from [git-scm.com](https://git-scm.com/download/win)
   - Run the installer (GitSetup.exe)
   - When finished, open Command Prompt (press Windows key, type "cmd" and press Enter)
   - Verify installation by typing: `git --version`

2. **Clone the GitHub Repository**
   - Open Command Prompt
   - Type the following commands:
     ```bash
     cd %USERPROFILE%\Desktop
     git clone https://github.com/VatsSanghvi/Big-Data-Project-Group-3.git
     cd Big-Data-Project-Group-3
     ```
   - If asked about credentials, enter your GitHub username and password

3. **Setup the Application**
   - In Terminal, copy and paste each of these commands one at a time:
     ```
     python3 -m venv venv
     source venv/bin/activate
     pip install -r requirements.txt
     ```
     
4. **Start the Application**
   - In Terminal, type:
     ```
     uvicorn app.main:app --reload
     ```
   - Open your web browser and go to: http://localhost:8000 this will also be the base Postman url

#### Database Configuration

The application requires a SQL Server database. Create a database and update the `.env` file with your credentials:

```env.template
   HOST=localhost
   PORT=1433
   DATABASE=SGA-2
   USERNAME=admin
   PASSWORD=admin
```

NOTE: The `.env.template` file should be renamed to `.env` before running the application.
