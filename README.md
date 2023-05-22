# Slot-Finder-
This project is done in hackathon under 24hrs in RGMCET 
This project involves developing a parking slot detection and management system. The system includes several code files:

1. `dashboard.html`: This file is an HTML template for the project's dashboard. It includes various CSS and JavaScript dependencies for styling and functionality. The dashboard displays information about available slots, used slots, and total slots.

2. `main.py`: This file contains the main Flask application. It reads data from a CSV file (`freespace.csv`) and calculates the number of available and used slots. It renders the `dashboard.html` template with the calculated data.

3. `slot_detector.py`: This file implements the slot detection algorithm. It loads a pre-trained model (`parking_area`) that contains the coordinates of parking slots. It processes a video feed or image, detects occupied slots, and calculates the number of available slots. The count is then saved to the `freespace.csv` file.

4. `slot_finder.py`: This file allows the user to manually define the parking slots by selecting areas on an image. It provides an interactive GUI where the user can add or remove parking slots. The selected slots' coordinates are saved in the `parking_area` file.

The system utilizes computer vision techniques to detect parking slot occupancy and manage slot availability. The dashboard provides a real-time view of slot information, and the slot detection algorithm updates the available slot count. The slot finder tool allows the user to customize the parking slot layout.

The project aims to automate parking slot management and provide an efficient way to monitor slot occupancy. By combining computer vision and web technologies, it offers a user-friendly interface for parking management.
