# Phone Number Lookup Application

This repository contains a Flask application that allows users to look up phone numbers and retrieve associated details. It showcases a user-friendly web interface for submitting and viewing phone number data. Below you will find details on the project structure, setup instructions, and usage. 

## Features

- **Interactive Web Forms**: Users can submit phone numbers through a web form to retrieve associated information.


## Project Structure

### Python Scripts

- **`app.py`**: Main Flask application file. Handles URL routing and integrates with other components of the application.
- **`forms.py`**: Defines the WTForms used for input validation and rendering in the HTML forms.

### HTML Templates

- **`base.html`**: Base template providing the HTML structure used by other templates.
- **`lookup.html`**: Template for the phone number lookup form and displaying the lookup results.
- **`patient_info.html`**: Displays detailed information about a phone number, such as name and number.

## Installation

To set up the application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/phone-number-lookup.git
   cd phone-number-lookup
