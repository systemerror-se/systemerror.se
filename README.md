# My Python Project

This project is a simple Flask web application that serves a "Hello World" webpage. It is designed to be statically hosted on GitHub Pages using GitHub Actions with Jekyll.

## Project Structure

```
systemeror.se
├── src
│   ├── app.py
│   └── templates
│       └── index.html
├── .github
│   └── workflows
│       └── github-pages.yml
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/systemerror-se/systemerror.se.git
   ```

2. **Install dependencies:**
   Make sure you have Python and pip installed. Then run:
   ```
   python -m venv .venv
   .venv\Scripts\pip.exe install -r .\requirements.txt
   ```

3. **Run the Flask application:**
   You can start the Flask server by running:
   ```
   .venv\Scripts\python.exe src\app.py
   ```
   The application will be available at `http://127.0.0.1:5000`.

## Usage

Once the server is running, navigate to `http://127.0.0.1:5000` in your web browser to see the "Hello World" message.

## Deployment

This project is set up to be deployed to GitHub Pages using GitHub Actions. The workflow file is located at `.github/workflows/github-pages.yml`. Make sure to configure the workflow according to your repository settings.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.