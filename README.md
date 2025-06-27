# AI File Analyzer

## Introduction

This python based application uses OpenAI API to search for information in files, it uses `gpt-4o` model but you can change it inside the code .

This application will accept multiple subsequent prompts and will retain the conversion history.

**Requirements:**

- OpenAI Plaftform Account Login or Sign Up from https://auth.openai.com/log-in
- API Key: You can obtain it from https://platform.openai.com/settings/organization/api-keys
- Add Billing information from https://platform.openai.com/settings/organization/billing/payment-methods
- Pricing inforamtion is here https://platform.openai.com/docs/pricing

_It's quite cheap don't worry, only 5$ can last long time!!!!!_

It accept certain file formats as following:

| File Extension |                                Format MIME                                |
| :------------: | :-----------------------------------------------------------------------: |
|       .c       |                                 text/x-c                                  |
|      .cpp      |                                text/x-c++                                 |
|      .cs       |                               text/x-csharp                               |
|      .css      |                                 text/css                                  |
|      .doc      |                            application/msword                             |
|     .docx      |  application/vnd.openxmlformats-officedocument.wordprocessingml.document  |
|      .go       |                               text/x-golang                               |
|     .html      |                                 text/html                                 |
|     .java      |                                text/x-java                                |
|      .js       |                              text/javascript                              |
|     .json      |                             application/json                              |
|      .md       |                               text/markdown                               |
|      .pdf      |                              application/pdf                              |
|      .php      |                                text/x-php                                 |
|     .pptx      | application/vnd.openxmlformats-officedocument.presentationml.presentation |
|      .py       |                               text/x-python                               |
|      .py       |                           text/x-script.python                            |
|      .rb       |                                text/x-ruby                                |
|      .sh       |                             application/x-sh                              |
|      .tex      |                                text/x-tex                                 |
|      .ts       |                          application/typescript                           |
|      .txt      |                                text/plain`                                |

## Installation

**1- Add API Key to your OS environment**

- **For macos users**

`export OPENAI_API_KEY="your_api_key_here"`

- **For Windows users**

Export an environment variable in PowerShell

`setx OPENAI_API_KEY "your_api_key_here"`

**2- Create virtual enviroment**

`python3 -m venv venv`

`source venv/bin/activate`

**3- Install requirements**

`pip install -r requirements.txt`

**4- run program**

`python analyze.py`

## Code Operation

- The code will ask for a path where the files you want to analyze reside
- Then you will choose the format of the file extension. You can choose one or more separated with commas
- The application will search for all files in the folder with the specific extension
- Next, you will choose one of two analysis method
  - **Method 1**: Upload multiple files and analyze data in all files at once with single prompt
  - **Method 2**: Analyze each file separately with the same prompt.

## Testing Code the methods

I have included folder `team` which contains two files `team1.txt` and `team2.txt`. Each file contain list of names and we will use both methods to show to analyze these two files in different ways.

**Method1**

```
==> Enter your choice (1 or 2): 1
===================================================
 ~~~~ Enter your prompt [type 'exit' to quit]: list the team memebr names?
Here are the team members listed in the files:

**Team 1:**
1. Anna Müller – Team Lead, Software Engineering
2. Luis Fernández – Backend Developer
3. Clara Dupont – UX Designer
4. James O’Connor – Cloud Infrastructure Engineer
5. Peter Novak – QA Engineer
6. Sofia Rossi – Mobile Developer
7. Eva Petrova – Data Analyst
8. Lena Schmidt – Scrum Master
9. Marko Jovanovic – DevOps Engineer
10. Aylin Demir – Frontend Developer

**Team 2:**
1. Julia Schneider – Product Manager
2. Miguel Santos – Frontend Developer
3. Antoine Morel – Marketing Analyst
4. Sean Murphy – Cybersecurity Engineer
5. Jan Kowalski – QA Engineer
6. Alessia Bianchi – Solutions Architect
7. Maria Ivanova – Data Scientist
8. Daniel Hoffmann – Business Analyst
9. Nikola Petrović – Site Reliability Engineer (SRE)
10. Elif Yılmaz – AI/ML Engineer
===================================================
 ~~~~ Enter your prompt [type 'exit' to quit]: list memebers per country?
Here are the team members listed by country:

**Germany:**
- Anna Müller – Team Lead, Software Engineering
- Lena Schmidt – Scrum Master
- Julia Schneider – Product Manager
- Daniel Hoffmann – Business Analyst

**Spain:**
- Luis Fernández – Backend Developer
- Miguel Santos – Frontend Developer

**France:**
- Clara Dupont – UX Designer
- Antoine Morel – Marketing Analyst

**Ireland:**
- James O’Connor – Cloud Infrastructure Engineer
- Sean Murphy – Cybersecurity Engineer

**Czechia:**
- Peter Novak – QA Engineer

**Italy:**
- Sofia Rossi – Mobile Developer
- Alessia Bianchi – Solutions Architect

**Bulgaria:**
- Eva Petrova – Data Analyst
- Maria Ivanova – Data Scientist

**Serbia:**
- Marko Jovanovic – DevOps Engineer
- Nikola Petrović – Site Reliability Engineer (SRE)

**Türkiye:**
- Aylin Demir – Frontend Developer
- Elif Yılmaz – AI/ML Engineer

**Poland:**
- Jan Kowalski – QA Engineer
===================================================
```

**Method2**

```
Please choose a method:
==> Enter your choice (1 or 2): 2
===================================================
 ~~~~ Enter your prompt [type 'exit' to quit]: what are the names?
===> Processing team1.txt
The names mentioned in the document are:

1. Anna Müller
2. Luis Fernández
3. Clara Dupont
4. James O’Connor
5. Peter Novak
6. Sofia Rossi
7. Eva Petrova
8. Lena Schmidt
9. Marko Jovanovic
10. Aylin Demir.
===> Processing team2.txt
Here are the names from the document:

1. Julia Schneider
2. Miguel Santos
3. Antoine Morel
4. Sean Murphy
5. Jan Kowalski
6. Alessia Bianchi
7. Maria Ivanova
8. Daniel Hoffmann
9. Nikola Petrović
10. Elif Yılmaz.
===================================================
 ~~~~ Enter your prompt [type 'exit' to quit]: list the team members per coutnry?
===> Processing team1.txt
Here are the team members listed by country:

- **Germany**
  - Anna Müller – Team Lead, Software Engineering
  - Lena Schmidt – Scrum Master

- **Spain**
  - Luis Fernández – Backend Developer

- **France**
  - Clara Dupont – UX Designer

- **Ireland**
  - James O’Connor – Cloud Infrastructure Engineer

- **Czechia**
  - Peter Novak – QA Engineer

- **Italy**
  - Sofia Rossi – Mobile Developer

- **Bulgaria**
  - Eva Petrova – Data Analyst

- **Serbia**
  - Marko Jovanovic – DevOps Engineer

- **Türkiye**
  - Aylin Demir – Frontend Developer.
===> Processing team2.txt
Here are the team members listed by country:

- **Germany**
  - Julia Schneider – Product Manager
  - Daniel Hoffmann – Business Analyst

- **Spain**
  - Miguel Santos – Frontend Developer

- **France**
  - Antoine Morel – Marketing Analyst

- **Ireland**
  - Sean Murphy – Cybersecurity Engineer

- **Poland**
  - Jan Kowalski – QA Engineer

- **Italy**
  - Alessia Bianchi – Solutions Architect

- **Bulgaria**
  - Maria Ivanova – Data Scientist

- **Serbia**
  - Nikola Petrović – Site Reliability Engineer (SRE)

- **Türkiye**
  - Elif Yılmaz – AI/ML Engineer.
===================================================
```
