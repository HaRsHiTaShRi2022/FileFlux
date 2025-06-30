# FileFlux

**Effortless File Conversion, Secure & Free**

[](https://lnkd.in/gtajXda9)
[](https://www.google.com/search?q=LICENSE)
[](https://www.google.com/search?q=https://github.com/HaRsHiTaShRi2022/FileFlux/stargazers)
[](https://www.google.com/search?q=https://github.com/HaRsHiTaShRi2022/FileFlux/network/members)

-----

## 🚀 Introduction

FileFlux is a free and open-source web application designed to simplify your file conversion needs. Built with a focus on user-friendliness and security, FileFlux allows you to effortlessly convert various document and image formats with just a few clicks. Our mission is to provide a reliable, efficient, and accessible tool for everyone.

-----

## ✨ Features

  * **Word to PDF:** Convert `.doc` and `.docx` files to PDF format.
  * **Image to PDF:** Merge multiple images (`.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`) into a single PDF document.
  * **PDF to Word:** Transform your PDF files back into editable Word documents (`.docx`).
  * **Excel to JSON:** Convert tabular data from `.xls` and `.xlsx` files into JSON format.
  * **JSON to Excel:** Convert JSON data into an Excel spreadsheet (`.xlsx`).
  * **PowerPoint to PDF:** Convert `.ppt` and `.pptx` presentations to PDF.
  * **Secure & Private:** All uploaded files are automatically deleted from the server after conversion to ensure your privacy and save space.
  * **User-Friendly Interface:** A clean and intuitive design built with HTML, CSS, and JavaScript for a seamless experience.
  * **Completely Free & Open-Source:** FileFlux is free to use and welcomes community contributions.

-----

## 🛠️ Technologies Used

**Frontend:**

  * **HTML5**
  * **CSS3**
  * **JavaScript**

**Backend:**

  * **Python**
  * **Flask:** A lightweight Python web framework.
  * **Pillow (PIL Fork):** For image processing.
  * **pandas:** For handling Excel and JSON data conversions.
  * **pdf2docx:** For PDF to Word conversions.
  * **LibreOffice:** Utilized via `subprocess` for robust document (Word, PowerPoint) to PDF conversions.

**Deployment:**

  * **Render:** Cloud platform used for hosting the live application.

-----

## ⚙️ Installation and Local Setup

To run FileFlux locally, follow these steps:

### Prerequisites

  * **Python 3.x**
  * **pip** (Python package installer)
  * **LibreOffice:** Essential for document conversions (Word to PDF, PowerPoint to PDF).
      * **On Debian/Ubuntu:**
        ```bash
        sudo apt update
        sudo apt install libreoffice
        ```
      * **On macOS (using Homebrew):**
        ```bash
        brew install --cask libreoffice
        ```
      * **On Windows:** Download and install from the [official LibreOffice website](https://www.google.com/search?q=https://www.libreoffice.org/download/download/). Ensure it's added to your system's PATH, or update the `LIBREOFFICE_PATH` variable in `app.py` to point to your LibreOffice executable.

### Steps

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/HaRsHiTaShRi2022/FileFlux.git
    cd FileFlux
    ```

2.  **Create and activate a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

      * *Note:* If `requirements.txt` is not present, you can create one by running `pip freeze > requirements.txt` after manually installing the dependencies shown in `app.py`: `Flask`, `pandas`, `Pillow`, `pdf2docx`.

4.  **Run the Flask application:**

    ```bash
    python app.py
    ```

5.  **Access the application:**
    Open your web browser and go to `http://127.0.0.1:5000/`.

-----

## 🤝 Contributing

We welcome contributions from the community\! Whether you're a developer, designer, or just an enthusiast, your input is valuable. Here are some ways you can contribute:

  * **Report Bugs:** If you find any issues, please open an issue on our GitHub repository.
  * **Suggest Features:** Have an idea for a new conversion type or an improvement? Let us know\!
  * **Submit Pull Requests:**
    1.  Fork the repository.
    2.  Create a new branch (`git checkout -b feature/YourFeature`).
    3.  Make your changes.
    4.  Commit your changes (`git commit -m 'Add Your Feature'`).
    5.  Push to the branch (`git push origin feature/YourFeature`).
    6.  Open a Pull Request.

-----

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.

-----

## 👨‍💻 Meet the Team

FileFlux was developed by a team of enthusiastic engineering students:

  * **Harshit Ashri** – Backend Development & Deployment
  * **Mukund Joshi** – Frontend Development
  * **Anwesh Ajitabh Dash** – UI/UX & Design
  * **PRATEEK HOTA** – UI/UX & Design

This project was an incredible learning experience for us, especially in full-stack development and overcoming deployment challenges on Render. We're committed to continuously improving FileFlux.

-----

## 🚀 What's Next?

We aim to expand FileFlux by adding more file formats, optimizing conversion speed, and further enhancing the user experience. Join us in making FileFlux the go-to platform for all your file conversion needs\!

-----
