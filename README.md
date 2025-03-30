# Fresh Mind

Fresh Mind is a Django-based web application designed to help users track their daily mood, habits, and receive motivational quotes. This app is aimed at promoting mental wellness by allowing users to track their feelings and actions.

## Features
- **Quote of the Day**: Displays a random motivational quote to inspire you.
- **Mood Tracker**: Allows users to record their mood daily.
- **Habit Tracker**: Enables users to track and manage their habits.

## Installation

Follow these steps to run the project locally:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/fresh_mind.git
    ```

2. Navigate to the project directory:
    ```bash
    cd fresh_mind
    ```

3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use venv\Scripts\activate
    ```

4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Apply the database migrations:
    ```bash
    python manage.py migrate
    ```

6. Run the server:
    ```bash
    python manage.py runserver
    ```

7. Open your browser and visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to see the app.

## Technologies Used
- **Django**: Web framework for Python
- **HTML/CSS**: For frontend styling

## Contributing

If you want to contribute to the development of this project, feel free to fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
