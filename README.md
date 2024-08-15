
## Overview

The Bengaluru Metro System project provides a GUI interface for calculating metro travel details between stations in Bengaluru(Green and Purple line). The application is built using Python Tkinter and includes functionalities such as route distance, estimated travel time, fare calculation, and QR code generation.

## Features

- **Station Selection:** Users can select their source and destination stations from a list of Bengaluru metro stations.
- **Route Details:** Displays travel distance, time, and fare between selected stations.
- **QR Code Generation:** Generates a QR code with travel details that can be saved or shared.
- **GUI Interface:** User-friendly interface built with Tkinter.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone git@github.com:jmlakshmisagar/Bengaluru-Metro-System.git
   cd jmlakshmisagar/Bengaluru-Metro-System
   ```

2. **Install Required Packages:**

   Ensure you have Python installed, then install the necessary packages using pip:

   ```bash
   pip install pillow qrcode
   ```

## Usage

1. **Run the Application:**

   Execute the main script to launch the application:

   ```bash
   python main.py
   ```

2. **Interface Overview:**

   - **Main Window:** Displays the Bengaluru Metro logo and provides options for selecting stations.
   - **Select Stations:** Use the dropdown menus to select your source and destination stations.
   - **Generate Button:** Click to calculate travel details and generate a QR code.
   - **Reset Button:** Resets the selection and information displayed.
## Sample Output

 <p align="center">
  <img src="https://github.com/user-attachments/assets/4bf189a6-1384-4ba0-85a5-f6fb12d1bba7" alt="main" width="400px">
</p>  
<p align="center">
  Before Data Entry: Displays the main screen of the application before any data is entered.
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/90141aa9-0d24-480c-ae0e-49af54bc3747" alt="error" width="400px">
</p>
<p align="center">
  Error Image: Shows an error message when invalid data is entered or if there are issues with the station information.
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/4acb78eb-057e-4036-bb0a-16376a1007c3" alt="output" width="400px">
</p>
<p align="center">
  Output Image: Displays the result after processing the data, including travel details and the generated QR code.
</p>


