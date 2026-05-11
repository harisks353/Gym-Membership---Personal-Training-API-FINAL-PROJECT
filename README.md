# 🏋️ Elite Gym Management API 
**By: Haris Mohammed (Student ID: 70454)**

## What this project does
This is a "Cloud-Ready" system I built for my final project. It is a backend application that helps a gym manage their members. Instead of a human doing the math, this API automatically calculates how much a member needs to pay based on their training sessions and hourly rates.

## Key Features
* **Smart Math (Fee Calculation):** You can send a list of gym sessions, and the API sums everything up to give a final total instantly.
* **Data Rules (Pydantic):** I set up "safety rules" to prevent mistakes. If a session is too short (less than 15 mins), the API rejects it and explains why.
* **Staff Privacy (Security):** I created a secure staff portal. Only people with the right username (`trainer_haris`) and password can see the member registry.
* **Web Documentation:** I didn't just write code; I created a live website on **AWS S3** so that anyone can see how the API works and what data to send to it.

## Live Website Link
The project documentation is hosted here:http://gym-membership-personal-training-api.s3-website.eu-north-1.amazonaws.com
