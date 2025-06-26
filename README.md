# AI File Analyzer

## Introduction

This python based application uses OpenAI API to search for information in files, it uses `gpt-4o` model but you can change it inside the code .

**Requirements:**

- OpenAI Plaftform Account Login or Sign Up from https://auth.openai.com/log-in
- API Key: You can obtain it from https://platform.openai.com/settings/organization/api-keys
- Add Billing information from https://platform.openai.com/settings/organization/billing/payment-methods
- Pricing inforamtion is here https://platform.openai.com/docs/pricing

_It's quite cheap don't worry, only 5$ can last long time!!!!!_

It accept certain file formats as following:

| File Extension |                                Format MIME                                |
| :------------- | :-----------------------------------------------------------------------: |
| .c             |                                 text/x-c                                  |
| .cpp           |                                text/x-c++                                 |
| .cs            |                               text/x-csharp                               |
| .css           |                                 text/css                                  |
| .doc           |                            application/msword                             |
| .docx          |  application/vnd.openxmlformats-officedocument.wordprocessingml.document  |
| .go            |                               text/x-golang                               |
| .html          |                                 text/html                                 |
| .java          |                                text/x-java                                |
| .js            |                              text/javascript                              |
| .json          |                             application/json                              |
| .md            |                               text/markdown                               |
| .pdf           |                              application/pdf                              |
| .php           |                                text/x-php                                 |
| .pptx          | application/vnd.openxmlformats-officedocument.presentationml.presentation |
| .py            |                               text/x-python                               |
| .py            |                           text/x-script.python                            |
| .rb            |                                text/x-ruby                                |
| .sh            |                             application/x-sh                              |
| .tex           |                                text/x-tex                                 |
| .ts            |                          application/typescript                           |
| .txt           |                                text/plain`                                |

## Installation

**1- Create virtual enviroment**

`python3 -m venv venv`

`source venv/bin/activate`

**2- Install requirements**

`pip install -r requirements.txt`

**3- run program**

`python analyze.py`

**4- Add API Key to your OS environment**

- **For macos users**

`export OPENAI_API_KEY="xxx"`

- **For Windows users**

Export an environment variable in PowerShell

`setx OPENAI_API_KEY "your_api_key_here"`

## Code Operation

- The code will ask for a path where the files you want to analyze reside
- Then you will choose the format of the file extension. You can choose one or more separated with commas
- The application will search for all files in the folder with the specific extension
- Next, you will choose one of two analysis method
  - **Method 1**: Upload multiple files and analyze data in all files at once with single prompt
  - **Method 2**: Analyze each file separately with the same prompt.
