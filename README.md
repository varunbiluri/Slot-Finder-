# Slot-Finder

This project was developed during a hackathon at RGMCET by BYTS INDIA(*BYTS HACKLEAGUE 1.0*) within a 24-hour timeframe.

## Project Description

The Slot-Finder project is aimed at automating the process of monitoring and managing parking spaces. It utilizes computer vision techniques to detect the occupancy status of parking slots and provides real-time information about available and used slots. The project includes a user-friendly dashboard for monitoring and an interactive tool for customizing the parking slot layout. The project aims to provide the following functionality:

### Slot Detector
The slot detector component utilizes computer vision techniques to identify available parking slots in a given video feed. It processes the video frames, applies image processing algorithms, and detects the occupancy status of parking slots. It provides accurate and real-time information on available and occupied slots.

### Slot Finder
The slot finder component offers a user-friendly interface for defining and managing parking slots. It allows users to mark parking slots in a given image or video frame manually. Users can add new slots, remove existing slots, and update slot positions as needed. The slot finder facilitates the customization and adaptation of the system to different parking lot layouts.

### Web-based Dashboard
The web-based dashboard provides a convenient and interactive way to visualize the parking slot status. It displays real-time information on available slots, used slots, and total slots. Users can access the dashboard through a web browser and monitor the parking situation remotely. The dashboard also includes login and registration functionality for user authentication and access control.

## Features

- Real-time monitoring of parking space occupancy status
- Display of available slots, used slots, and total slots on the dashboard
- Automated slot detection using computer vision techniques
- Customizable parking slot layout through an interactive GUI
- Efficient utilization of parking space and improved user experience

## Code Files

- `dashboard.html`: HTML template for the project's dashboard user interface
- `main.py`: Flask application for processing parking space data and rendering the dashboard template
- `slot_detector.py`: Implementation of the slot detection algorithm using computer vision techniques
- `slot_finder.py`: Interactive tool for manually defining the parking slot layout

## Team Members

1. Varun Reddy B - Team Leader
2. Sai Kumar G
3. Panvi Krishan J
4. Azeez Basha S
5. Radha Krishan M
6. Viswa Teja Reddy M
7. Kiran Kumar Reddy

## Usage

1. Run the Flask application: `python main.py`
2. Access the dashboard by opening `http://localhost:5000` in your web browser
3. Follow the on-screen instructions to customize the parking slot layout using the slot finder tool
4. Run the main.py file to start the Flask server.
5. Access the web-based dashboard by visiting `http://localhost:5000` in your web browser.
6. Follow the instructions provided in the dashboard to add parking slots and monitor the status.

Please refer to the individual code files for more specific details on each component and their functionalities.


## Project Dependencies  and Installation

1. Clone the repository: `git clone https://github.com/varunbiluri/Slot-Finder-.git`
2. Install the required dependencies: `pip install -r requirements.txt`


To run the Slot-Finder project, ensure that you have the following dependencies installed:

- Flask==1.1.4
- opencv-python==4.5.3.56
- numpy==1.21.0
- csv
- pickle
- itertools
- count

## Demo

https://github.com/varunbiluri/Slot-Finder-/assets/84211999/7c08726e-5c06-4977-ab74-1a31b228217a

## Contributing

  Contributions to the Slot-Finder project are welcome! Here are some ways you can contribute:

- Report any issues or bugs you encounter
- Suggest new features or improvements
- Fork the repository and submit a pull request


## Acknowledgements

We would like to express our gratitude to RGMCET and BYTS INDIA for organizing the hackathon and providing the opportunity to work on this project.

## Contact

For any inquiries or feedback, please contact
  mail to: varunreddy.billuri@gmail.com  (or) 
  mail to: skg.13.edu@gmail.com.

Enjoy using Slot-Finder!
