
# The Gym Tracker App

A simple Flask-based web application to track your gym progress. The app helps you organize your workouts by weeks, muscle groups, and exercises, storing details such as sets, reps, weights, and notes.

---

## Table of Contents

- [Overview](#overview)
- [Data Structure](#data-structure)
- [Handling the Data](#handling-the-data)
- [Updating, Adding, and Removing Data](#updating-adding-and-removing-data)
- [Application Functionality](#application-functionality)
  - [Weeks Page](#weeks-page)
  - [Muscle Group Page](#muscle-group-page)
  - [Exercise Page](#exercise-page)
  - [Details Page](#details-page)
- [Developer Logs](#developer-logs)
- [Future Plans](#future-plans)
- [Installation and Usage](#installation-and-usage)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The Gym Tracker App is designed to help users monitor and log their gym activities. It provides an easy-to-use interface for adding new workout weeks, categorizing workouts by muscle groups, and recording individual exercises with comprehensive details. The app uses a JSON-based datastore to keep your progress saved.

---

## Data Structure

The data is stored as a nested dictionary where each user’s workout history is organized as follows:

- **Weeks**: The top-level dictionary contains keys for each week.
  - **Muscle Groups**: Each week holds multiple muscle groups.
    - **Exercises**: Within every muscle group, you can add exercises.
      - **Exercise Details**: Every exercise stores:
        - **sets**
        - **reps**
        - **weight**
        - **notes**

Example (simplified):
```python
{
  "no_of_weeks": 2,
  "1": {
    "chest": {
      "bench press": {"set": 3, "rep": 10, "weight": 100, "notes": "Felt strong"}
    }
  },
  "2": {
    "back": {
      "deadlift": {"set": 4, "rep": 8, "weight": 150, "notes": ""}
    }
  }
}
```

---

## Handling the Data

The app provides several helper functions for data access and manipulation:

1. **List of Weeks**
   - `get_number_of_weeks()`: Returns the total number of weeks stored.

2. **List of Muscle Groups in a Week**
   - `get_muscle_group_list()`: Returns a sorted list of muscle groups for a given week.
   - *Note:* Sorting may complicate future enhancements. Consider storing muscle groups with a numeric key along with a `name` and a `precedence` value (which could be updated if a user rearranges items) to control the display order.

3. **List of Exercises in a Muscle Group**
   - `get_exercise_list()`: Returns a sorted list of exercises within a specific muscle group.

4. **Exercise Details**
   - The exercise details (sets, reps, weight, and notes) are stored in a dictionary. Direct dictionary access is used for updates instead of separate functions for each detail.

---

## Updating, Adding, and Removing Data

### Updating Exercise Details
Four functions are provided to update an exercise’s:
- Number of **sets**
- **Reps**
- **Weight**
- **Notes**

These functions directly modify the corresponding fields in the exercise’s dictionary.

### Creating New Entries
- **New Exercise**:  
  You can add a new exercise from a list of previously added exercises or define a new one.
  
- **New Muscle Group**:  
  Similar to exercises, new muscle groups can be added with the possibility to use pre-defined groups.
  
- **New Week**:  
  - Option to duplicate data from the previous week.
  - Option to create an empty week.

### Removing Entries
The app supports removal of:
- **Weeks**
- **Muscle Groups**
- **Exercises**

---

## Application Functionality

### Weeks Page
- **Add New Week:**  
  Create a new week to log workouts.
- **Duplicate Previous Week:**  
  Quickly set up a new week by copying the previous week’s data.
- **Sorting:**  
  Future plans include enabling sorting of weeks via drag-and-drop.

### Muscle Group Page
- **Add New Muscle Group:**  
  Introduce a new muscle group for a selected week.
- **Remove Muscle Group:**  
  Easily remove unwanted muscle groups using an adjacent remove button.
- **Edit Muscle Group Name:**  
  (Planned) Ability to change the name of a muscle group.
- **Open Muscle Group:**  
  View all exercises under a specific muscle group.

### Exercise Page
- **Add New Exercise:**  
  Add a new exercise under a chosen muscle group.
- **Delete Exercise:**  
  Remove exercises that are no longer needed.
- **Edit Exercise:**  
  Open an exercise to view or change its details.
- **Edit Exercise Name:**  
  (Planned) Support for renaming an exercise.

### Details Page
- **Edit Details:**  
  Modify the sets, reps, weight, and notes for an exercise.
- **Save Details:**  
  Save updated exercise details.
- **Add/Save Notes:**  
  Store extra notes about the workout or exercise performance.

---

## Developer Logs

> **Regained the Spirits – 19 March 2024**  
> I am Siddhartha Reddy. I embarked on this journey to build a simple gym app for myself. Though app and web development require a lot of learning and time, I decided to start with a basic Flask application to track my workouts. Inspired by O'Reilly's "Head First Python", I began coding functions to store and update user data—even though handling dictionaries within dictionaries turned out to be more complex than I imagined.
>
> **Making New Plans – 08 April 2024**  
> I am considering redesigning the data storage method to reduce redundancy. Instead of duplicating strings for each exercise, a dedicated exercise profile with additional information (description, video links, images, duration, difficulty, etc.) would be more efficient. I plan to discuss this with database experts and explore how to integrate JavaScript for dynamic updates without full-page reloads. Learning JavaScript seems inevitable, and I'm excited to explore progressive web app (PWA) concepts to enhance the user experience.

---

## Future Plans

- **Data Structure Improvements:**  
  Implement a more organized schema for muscle groups and exercise profiles, possibly including a `precedence` key for custom ordering.
- **Frontend Enhancements:**  
  Explore using JavaScript (or frameworks like React) to enable dynamic page updates and a smoother user experience.
- **Progressive Web App (PWA):**  
  Transition to a PWA model for a native-app-like feel.
- **Collaboration:**  
  Plan to collaborate with others (e.g., to integrate a more advanced JavaScript frontend) and to learn more about Git and database design.

---

## Installation and Usage

### Prerequisites

- Python 3.x
- [Flask](https://palletsprojects.com/p/flask/)

### Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/siddhuseelam/GymappPublic.git
   cd GymappPublic
   ```

2. **(Optional) Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install Flask
   ```

4. **Run the Application:**

   ```bash
   python gymapp.py
   ```

5. **Access the App:**

   Open your browser and navigate to [http://localhost:5000](http://localhost:5000).

---

## Contributing

Contributions are welcome! If you have ideas or improvements:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to your branch (`git push origin feature/YourFeature`).
5. Open a pull request.

---

## License

This project is open source. *(Include your chosen license here, e.g., MIT License.)*


