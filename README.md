🚗 Parking Management System

An AI-assisted Parking Management System developed as a group project using Python, Flask, HTML, CSS, and JavaScript.

📌 Project Overview

Parking management can become difficult when parking slot availability, vehicle entry and exit, and fee calculation are handled manually.

Our project provides a simple browser-based solution to manage these processes digitally. The system allows vehicle numbers to be entered manually or scanned using a camera, assigns an available parking slot, tracks parking duration, and calculates the parking fee during exit.

🎯 Project Objectives

The main objectives of our project are:

- Display parking slot availability in real time
- Automatically assign an available parking slot
- Record vehicle entry time
- Track vehicle parking duration
- Manage vehicle entry and exit
- Calculate parking fees automatically
- Provide camera-based vehicle number scanning
- Reduce manual work in parking management

✨ Key Features

🅿️ Parking Slot Management

- The system maintains 10 parking slots.
- Each slot is displayed as either **FREE** or **TAKEN**.
- The system automatically assigns the first available parking slot.
- Slot status is updated after vehicle entry and exit.
- The vehicle number is displayed for occupied slots.

🚘 Vehicle Entry

- Vehicle numbers can be entered manually.
- A camera can be opened to scan the vehicle license plate.
- After obtaining the vehicle number, the system assigns the first available parking slot.
- The vehicle's entry time is recorded automatically.

📷 Camera-Based OCR

The system provides camera-based license plate text scanning using **Tesseract.js OCR**.

The captured camera image is processed to recognize letters and numbers from the vehicle plate.

If the plate cannot be detected automatically, the vehicle number can be entered manually.

🚪 Vehicle Exit

- The vehicle number is used to find the parked vehicle.
- The system calculates the parking duration using the recorded entry time and current exit time.
- The parking fee is calculated automatically.
- After exit, the vehicle is removed from the assigned slot.
- The released slot becomes available again.

💰 Parking Fee Calculation

The parking fee is calculated according to the parking duration and configured hourly rate.

A minimum parking fee is also applied.

📊 Parking Status

The system provides a live overview of:

- Total parking slots
- Free slots
- Occupied slots
- Vehicle numbers assigned to occupied slots
💾 Browser Data Storage

The system uses **Browser Local Storage** to retain parking information.

This allows the parking data to remain available when the page is refreshed.

🛠️ Technologies Used

- **Python**
- **Flask**
- **HTML**
- **CSS**
- **JavaScript**
- **Tesseract.js**
- **Browser Local Storage**

🔄 System Workflow

https://www.linkedin.com/posts/hema-d-g-778297409_parkingmanagementsystem-smartparking-groupproject-ugcPost-7491790699932123136-cwhQ/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAGgotIwBWIbfgGWHjlYMTOKxWY27f3_-5PA

Vehicle Arrives
       ↓
Scan / Enter Vehicle Number
       ↓
Check Available Slots
       ↓
Assign First Available Slot
       ↓
Record Entry Time
       ↓
Vehicle Parks
       ↓
Vehicle Exit
       ↓
Calculate Parking Duration
       ↓
Calculate Parking Fee
       ↓
Release Parking Slot
       ↓
Update Parking Status
