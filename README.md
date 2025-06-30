# 🌊 FileFlux

<div align="center">

**Effortless File Conversion • Secure • Free • Open Source**

[![Apache License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://choosealicense.com/licenses/apache-2.0/)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-red.svg)](https://flask.palletsprojects.com/)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)

*Transform your files with ease — No registration required, completely free forever*

[🚀 Live Demo](https://fileflux.onrender.com) • [📖 Documentation](#-features) • [🤝 Contributing](#-contributing) • [🐛 Report Issues](https://github.com/HaRsHiTaShRi2022/FileFlux/issues)

</div>

---

## 🎯 What is FileFlux?

FileFlux is a **powerful**, **secure**, and **completely free** web application that simplifies file conversion. Whether you're a student, professional, or anyone who works with documents, FileFlux handles your conversion needs without compromising your privacy.

> **🔒 Privacy First**: Your files are automatically deleted after conversion — we never store your data.

---

## ✨ Features

<table>
<tr>
<td align="center">
<img src="https://img.icons8.com/color/64/000000/microsoft-word-2019.png" width="48">
<br><strong>Word ↔ PDF</strong>
<br>Convert .doc/.docx to PDF<br>and PDF back to .docx
</td>
<td align="center">
<img src="https://img.icons8.com/color/64/000000/image.png" width="48">
<br><strong>Images → PDF</strong>
<br>Merge multiple images<br>into a single PDF
</td>
<td align="center">
<img src="https://img.icons8.com/color/64/000000/microsoft-excel-2019.png" width="48">
<br><strong>Excel ↔ JSON</strong>
<br>Convert spreadsheets to JSON<br>and vice versa
</td>
</tr>
<tr>
<td align="center">
<img src="https://img.icons8.com/color/64/000000/microsoft-powerpoint-2019.png" width="48">
<br><strong>PowerPoint → PDF</strong>
<br>Convert .ppt/.pptx<br>presentations to PDF
</td>
<td align="center">
<img src="https://img.icons8.com/color/64/000000/security-checked.png" width="48">
<br><strong>Secure & Private</strong>
<br>Files auto-deleted<br>after conversion
</td>
<td align="center">
<img src="https://img.icons8.com/color/64/000000/open-source.png" width="48">
<br><strong>Open Source</strong>
<br>Free forever<br>& community-driven
</td>
</tr>
</table>

### 📋 Supported Formats

| **Input Format** | **Output Format** | **Status** |
|------------------|-------------------|------------|
| `.doc`, `.docx` | `.pdf` | ✅ Ready |
| `.pdf` | `.docx` | ✅ Ready |
| `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp` | `.pdf` | ✅ Ready |
| `.xls`, `.xlsx` | `.json` | ✅ Ready |
| `.json` | `.xlsx` | ✅ Ready |
| `.ppt`, `.pptx` | `.pdf` | ✅ Ready |

---

## 🛠️ Tech Stack

<div align="center">

### Frontend
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

### Backend
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

### Libraries & Tools
![Pillow](https://img.shields.io/badge/Pillow-Image%20Processing-blue?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green?style=for-the-badge)
![LibreOffice](https://img.shields.io/badge/LibreOffice-Document%20Conversion-orange?style=for-the-badge)

### Deployment
![Render](https://img.shields.io/badge/Render-Cloud%20Platform-purple?style=for-the-badge)

</div>

---

## 🚀 Quick Start

### 📋 Prerequisites

Before you begin, ensure you have:
- **Python 3.x** installed
- **LibreOffice** for document conversions

<details>
<summary><strong>📦 Installing LibreOffice</strong></summary>

#### On Ubuntu/Debian:
```bash
sudo apt update && sudo apt install libreoffice
```

#### On macOS:
```bash
brew install --cask libreoffice
```

#### On Windows:
Download from [LibreOffice official website](https://www.libreoffice.org/download/download/) and ensure it's added to your system PATH.

</details>

### 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/HaRsHiTaShRi2022/FileFlux.git
   cd FileFlux
   ```

2. **Set up virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   
   # Activate virtual environment
   # On Windows:
   .\venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   <details>
   <summary>If requirements.txt is missing, install manually:</summary>
   
   ```bash
   pip install Flask pandas Pillow pdf2docx
   ```
   </details>

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access FileFlux**
   
   Open your browser and navigate to: `http://127.0.0.1:5000/`

---

## 🤝 Contributing

We ❤️ contributions! FileFlux is built by the community, for the community.

### 🌟 Ways to Contribute

- 🐛 **Report Bugs** — Found an issue? [Let us know!](https://github.com/HaRsHiTaShRi2022/FileFlux/issues)
- 💡 **Suggest Features** — Have ideas? [Share them with us!](https://github.com/HaRsHiTaShRi2022/FileFlux/discussions)
- 🔧 **Submit Code** — Ready to contribute? Follow our guide below!

### 📝 Development Workflow

1. **Fork** the repository
2. **Create** a feature branch
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make** your changes
4. **Commit** with clear messages
   ```bash
   git commit -m "Add amazing feature"
   ```
5. **Push** to your branch
   ```bash
   git push origin feature/amazing-feature
   ```
6. **Open** a Pull Request

<details>
<summary><strong>🎯 Contribution Guidelines</strong></summary>

- Follow Python PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed
- Keep commits focused and atomic
- Write clear commit messages

</details>

---

## 👥 Meet Our Team

<div align="center">

FileFlux is crafted with ❤️ by passionate engineering students:

| **Role** | **Team Member** | **Contribution** |
|----------|----------------|------------------|
| 🔧 **Backend & Deployment** | **Harshit Ashri** | Core backend development, server deployment |
| 🎨 **Frontend Development** | **Mukund Joshi** | User interface, client-side functionality |
| 🎯 **UI/UX Design** | **Anwesh Ajitabh Dash** | User experience design, interface design |
| 🎨 **UI/UX Design** | **Prateek Hota** | Visual design, user interface elements |

*This project has been an incredible journey of learning full-stack development, tackling deployment challenges, and building something meaningful together.*

</div>

---

## 📄 License

This project is licensed under the **Apache License 2.0** — see the [LICENSE](LICENSE) file for details.

```
Apache License 2.0 - Feel free to use, modify, and distribute!
```

---

## 🎯 Roadmap

### 🔮 What's Coming Next?

- [ ] 📊 **More Formats**: CSV, TXT, RTF conversions
- [ ] ⚡ **Speed Optimization**: Faster conversion algorithms
- [ ] 🌐 **API Access**: RESTful API for developers
- [ ] 📱 **Mobile App**: Native mobile applications
- [ ] 🔄 **Batch Processing**: Convert multiple files simultaneously
- [ ] 🌍 **Internationalization**: Multi-language support

---

## 🙏 Acknowledgments

- **LibreOffice** for providing excellent document conversion capabilities
- **Flask** community for the robust web framework
- **Render** for reliable cloud hosting
- **Contributors** who help make FileFlux better every day

---

<div align="center">

### 🌟 Star us on GitHub!

If FileFlux helped you, please consider giving us a ⭐ on GitHub. It helps others discover our project!

**[⭐ Star FileFlux](https://github.com/HaRsHiTaShRi2022/FileFlux)** • **[🐦 Follow Updates](https://twitter.com/)** • **[💬 Join Community](https://discord.gg/)**

---

*Made with ❤️ by the FileFlux Team*

</div>
