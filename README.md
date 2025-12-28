# 🎬 Telegram Movie Recommender Bot (All-in-One)

A simple Telegram bot that recommends movies by genre.
The bot uses **Selenium** to parse movie data from **IMDb** and is implemented entirely in **one Python file**.

---

## ✨ Project Overview

This project is a Telegram bot that allows users to choose a movie genre using buttons and receive a list of recommended movies.
All logic (bot + parser) is contained in **one file**, making the project easy to understand, run, and showcase.

---

## 🚀 Features

* Telegram bot with reply keyboard
* Movie recommendations by genre
* IMDb web parsing using Selenium
* Environment variables for secure token storage
* All logic in a single Python file

---

## 🧰 Technologies Used

* Python
* Telegram Bot API (pyTelegramBotAPI)
* Selenium WebDriver
* Google Chrome & ChromeDriver
* python-dotenv

---

## 📁 Project Structure

```
project-folder/
│
├── bot.py        # Telegram bot + Selenium parser (all in one file)
├── token.env     # Environment variables (Telegram bot token)
├── image.jpg     # Optional start image
└── README.md     # Documentation
```

---

## ⚙️ Setup Instructions (Step by Step)

### 1️⃣ Clone the Repository

Clone the project from GitHub to your local machine.

---

### 2️⃣ Install Dependencies

Make sure Python is installed, then install the required libraries using `pip`.

Libraries needed:

* pyTelegramBotAPI
* selenium
* python-dotenv

---

### 3️⃣ Create Telegram Bot Token

1. Open Telegram
2. Search for **@BotFather**
3. Create a new bot
4. Copy the generated token

---

### 4️⃣ Configure Environment Variables

Create a file named `token.env` and store your Telegram bot token inside it.
This keeps your token secure and out of the source code.

---

### 5️⃣ WebDriver Setup

* Install **Google Chrome**
* Download **ChromeDriver** matching your Chrome version
* Make sure ChromeDriver is accessible via system PATH

---

### 6️⃣ Run the Bot

Run the single Python file.
Once started, the bot will begin polling and respond to users in Telegram.

---

## 🤖 Bot Interaction

When the user starts the bot:

* A welcome message is displayed
* Genre buttons appear

Available genres:

* 🔍 Detective
* 🔥 Action
* 🧟‍♀️ Horror
* ➕ More (future features)

The bot parses IMDb and sends movie lists based on the selected genre.

---

## 🧠 How It Works

1. User selects a genre in Telegram
2. Bot launches Selenium
3. IMDb page is opened
4. Movie data is collected
5. Results are sent back to the user

---

## ⚠️ Important Notes

* IMDb may limit frequent requests
* Selenium is slower compared to APIs
* For learning and demo purposes, this approach is acceptable

---

## 🔮 Possible Improvements

* Headless browser optimization
* Replace Selenium with an API-based solution
* Add inline buttons
* Add pagination
* Save results in a database

---

## 👤 Author

**Ani Ginovyan**
Junior Python Developer
Interested in Machine Learning & Data Science

