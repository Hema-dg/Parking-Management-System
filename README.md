# Parking-Management-System

# 🚗 Parking Management System

An AI-assisted Parking Management System developed as a group project using Python, Flask, HTML, CSS and JavaScript.

## 📌 Project Overview

Parking management can become difficult when slot availability, vehicle entry and exit, and fee calculation are handled manually.

Our project provides a simple digital solution to manage these processes through a browser-based interface.

The system can:

- Display available and occupied parking slots
- Automatically assign an available parking slot
- Record vehicle entry time
- Track parking duration
- Calculate parking fees
- Manage vehicle entry and exit
- Detect license plates using OCR

## ✨ Key Features

### 🅿️ Parking Slot Management

- 10 parking slots are maintained by the system.
- Slots are displayed as FREE or TAKEN.
- The system automatically assigns an available slot.
- Slot status is updated after vehicle entry and exit.

### 🚘 Vehicle Entry

- Vehicle numbers can be entered manually.
- Camera-based license plate scanning is available.
- An available parking slot is automatically assigned to the vehicle.

### 📷 License Plate Detection

The system uses the device camera and Tesseract.js OCR to detect license plate text.

If automatic detection is unsuccessful, the vehicle number can be entered manually.

### 🚪 Vehicle Exit

- Vehicle number is used to identify the parked vehicle.
- Parking duration is calculated using the entry and exit times.
- The parking slot becomes available after the vehicle exits.

### 💰 Fee Calculation

Parking charges are calculated according to the parking duration and configured hourly rate.

A minimum parking fee is also applied.

### 📊 Parking Status

The system displays:

- Total parking slots
- Free slots
- Occupied slots
- Vehicle numbers assigned to occupied slots

### 💾 Data Storage

Browser Local Storage is used to retain parking information.

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Tesseract.js
- Browser Local Storage

## 🔄 System Workflow

```text
Vehicle Arrives
       ↓
Scan / Enter Vehicle Number
       ↓
Check Available Slots
       ↓
Assign Parking Slot
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
Update Slot Availability
