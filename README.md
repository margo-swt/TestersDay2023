# TestersDay2023
Beginners Guide to Android App Automation Using Python

# Mobile App Automation Workshop README

## Introduction

Welcome to the Mobile App Automation Workshop Repository conducted on Tester's Day 2023. In this workshop, we focused on automating mobile app testing using Python, Android Studio, the Pixel emulator, Python 3.9.13, and the pytest framework. This README provides an overview of the workshop and instructions for setting up the automation environment.

## Workshop Overview

In this workshop, we covered the following key topics:

1. Setting up the Mobile App Automation Environment.
2. Introduction to Android Studio and the Pixel emulator.
3. Writing mobile app automation scripts in Python.
4. Test automation best practices.
5. Running automated tests using pytest.

## Prerequisites

Before you get started, ensure that you have the following prerequisites in place:

- **Android Studio**: Make sure you have Android Studio installed on your machine. You can download it from [here](https://developer.android.com/studio).

- **Pixel Emulator**: We will use the Pixel emulator as our test device. You can create a Pixel emulator using Android Studio's AVD Manager.

- **Python 3.9.13**: Python is the scripting language we'll use for automation. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/release/python-3913/).

- **pytest**: We will use pytest as our testing framework. Install pytest using pip:

  ```bash
  pip install pytest
  ```

## Getting Started

1. **Clone the Repository**: Start by cloning this repository to your local machine:

   ```bash
   git clone <repository_url>
   ```

2. **Set Up Your Environment**: Open Android Studio and create a Pixel emulator using the AVD Manager. Ensure that your Android emulator is running and accessible.

3. **Install Dependencies**: Navigate to the project directory and install the required Python dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. **Writing Tests**: Write your mobile app automation test scripts using Python. You can find sample test scripts in the "tests" directory of this repository.

5. **Running Tests**: Execute your tests using pytest:

   ```bash
   pytest -v
   ```

   This command will discover and run all the test cases in the project.

## Additional Resources

- [Android Studio Documentation](https://developer.android.com/studio/intro)
- [Python Official Documentation](https://docs.python.org/3/)
- [pytest Documentation](https://docs.pytest.org/en/latest/)


Happy testing! 📱🤖🧪
