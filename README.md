# Chess.com Username Autocomplete

This project provides an autocomplete feature for Chess.com usernames.

## Setup

1. Ensure you have Python 3.12 installed.

2. Clone the repository:
   ```
   git clone https://github.com/turbotobbe/chesscom-username-autocomplete.git
   cd chesscom-username-autocomplete
   ```

3. Create and activate a virtual environment:
   ```
   python3.12 -m venv venv
   source venv/bin/activate  # On Unix or MacOS
   venv\Scripts\activate  # On Windows
   ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Project

To run the main application:

```
python src/main.py
```

## Running Tests

To run the test suite:

```
python -m unittest discover tests
```

## Development

1. Make sure your virtual environment is activated.

2. Install the project in editable mode:
   ```
   pip install -e .
   ```

3. Add any new dependencies to `requirements.txt`.

4. Write your code in the `src` directory.

5. Add tests in the `tests` directory.

## Project Structure

```
chesscom-username-autocomplete/
│
├── src/
│   ├── __init__.py
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   └── test_main.py
│
├── venv/
├── requirements.txt
├── setup.py
└── README.md
```

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.