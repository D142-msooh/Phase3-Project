# Phase3-Project

# Opportunity Recommender System  
*A Python + SQLite CLI app for personalized growth and productivity recommendations*

## Overview

The **Opportunity Recommender System** is a command-line application that helps users discover personalized opportunities based on their **skills**, **goals**, and **available time**. It also includes a **progress logging system**, allowing users to track their daily achievements and monitor their growth over time.


## Features

### 1. Create User Profile
Users can enter:
- Name  
- Age  
- Main goal (money / discipline / skill)  
- Free hours per day  
- List of skills  

This information is saved in the SQLite database.


### 2. Personalized Recommendations
The system analyzes:
- User skills  
- Daily free time  
- Goals  

Then generates relevant opportunities such as:
- Micro-learning tasks  
- Freelance ideas  
- Portfolio projects  
- Writing exercises  
- Discipline-building routines  


### 3. Add Progress Log
Users can record what they achieved today.  
Each log entry is saved with a timestamp.


### 4. View Progress Logs
Displays all logs for the user in a clean, readable format.


## Database Structure (SQLite)

### **users table**
| Column      | Type    | Description |
|-------------|---------|-------------|
| id          | INTEGER | Primary Key |
| name        | TEXT    | User’s name |
| age         | INTEGER | User’s age |
| main_goal   | TEXT    | User’s goal |
| free_hours  | INTEGER | Time available daily |

### **skills table**
| Column  | Type    | Description |
|---------|---------|-------------|
| id      | INTEGER | Primary Key |
| user_id | INTEGER | Foreign key |
| skill   | TEXT    | User skill |

### **logs table**
| Column  | Type    | Description |
|---------|---------|-------------|
| id      | INTEGER | Primary Key |
| user_id | INTEGER | Foreign key |
| entry   | TEXT    | Progress log text |
| date    | TEXT    | Timestamp |


## Recommendation Logic Summary

- If **free_hours < 2** → suggest micro-learning  
- If **free_hours ≥ 2** → suggest project tasks  
- Skills affect suggested opportunities  
- Goals influence direction (money, discipline, skill)  


## How to Run the Project

### 1. Clone the repository

``bash

git clone <your-repo-url>
cd opportunity-recommender

### 2. install dependencies.
pipenv install
pipenv shell

### 3. Run the program
``bash
python3 main.py

### 4. File Structure
css

- opportunity-recommender
    - main.py
    - database.db
    - README.md

## Technologies Used

    **Python 3**

    **SQLite**

    **datetime module**

    **CLI interface**

## Future Improvements

Add multiple user profiles

Export logs to PDF or CSV

Machine learning–based recommendation engine

Full GUI version or web app version

Scheduled reminders or notifications

## Author
Created by **Damaris Kinyanjui.**
Feel free to contribute or extend the project!




