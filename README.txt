===== OEC 2024 =====

=== Authors ===
- Matteo Golin
- Grant Achuzia
- Hetarthi Soni
- Hamnah Qureshi

=== About the Competition ===
The task is to develop an adaptive learning system to accommodate individual student learning disabilities.

=== Super Readers===
Super Readers is a child friendly educational website that helps dyslexic students in grades 4 improve their reading
skills. The website is meant to cater to students with a visual learning style.

We used semantic HTML tags so that users with screen readers will have an easier time interpreting the content on the
page.

=== Technologies Used ===
- HTML/CSS
- JavaScript
- Python 3.11+
    - Flask
- tsParticles: [https://confetti.js.org/more.html]

=== Setup Instructions ===

These instructions assume that the user already has Python installed on their machine.

1. Install the required dependencies for this project by running `pip install -r requirements.txt`.
   You may choose to install these in a virtual environment.

2. Run the main.py entry point using `py main.py` on Windows systems or `python3 main.py` on Linux.

3. Once the main.py file has been executed, the website will be hosted on your machine locally. Flask will display the
   URL where the website is hosted in a message that says: "Running on http://<your ip>".
   If you open this URL in your browser, you will be able to navigate the site.

=== Project Components ===

`requirements.txt` file: Describes the Python dependencies for this project.

`main.py` file: The main entry point that hosts the website and handles web traffic requests.

`templates` directory: Contains the HTML pages that make up the website and which are rendered by Flask.

`app/` directory: Contains the Python source code files for implementing word bank and reading logic. These files
contain a database of available stories and words for the learning activities.

`static` directory: Contains the CSS files that style the website's HTMl web pages.

`static/assets` directory: Contains the images and story files that are displayed on the website as part of the learning
activities.

