import os
import threading
import pandas as pd
from PIL import Image
from flask import Flask, request, send_file, jsonify, render_template, after_this_request
from pdf2docx import Converter
import subprocess
import zipfile
import json
import time

app = Flask(__name__, static_folder="static", template_folder="templates")
UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def delete_files(*file_paths):
    def delete():
        for file in file_paths:
            retry_count = 0
            max_retries = 3
            while retry_count < max_retries:
                try:
                    if os.path.exists(file):
                        os.remove(file)
                        print(f"Successfully deleted: {file}")
                        break
                    else:
                        print(f"File not found for deletion: {file}")
                        break
                except (PermissionError, OSError) as e:
                    print(f"Error deleting {file} (attempt {retry_count + 1}): {e}")
                    retry_count += 1
                    time.sleep(1)
            if retry_count == max_retries:
                print(f"Failed to delete {file} after {max_retries} attempts")
    cleanup_thread = threading.Thread(target=delete)
    cleanup_thread.start()
    return cleanup_thread

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Deves')
def Deves():
    return render_template('Deves.html')

@app.route('/About')
def About():
    return render_template('About.html')


@app.route('/word-to-pdf', methods=['POST'])
def word_to_pdf():
    try:
        if 'file' not in request.files:
            return "No file uploaded", 400
        files = request.files.getlist('file')
        if not files or files[0].filename == '':
            return "No selected files", 400

        pdf_paths = []
        word_paths = []

        for word_file in files:
            filename, ext = os.path.splitext(word_file.filename)
            if ext.lower() not in ['.doc', '.docx']:
                return f"Invalid file format for {word_file.filename}. Please upload only Word documents", 400

            word_path = os.path.join(UPLOAD_FOLDER, word_file.filename)
            output_path = os.path.join(UPLOAD_FOLDER, f"{filename}.pdf")
            word_file.save(word_path)

            # Use LibreOffice for conversion instead of docx2pdf
            subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", UPLOAD_FOLDER, word_path], check=True)

            pdf_paths.append(output_path)
            word_paths.append(word_path)

        if len(pdf_paths) == 1:
            @after_this_request
            def remove_file(response):
                delete_files(word_paths[0], pdf_paths[0])
                return response
            return send_file(pdf_paths[0], as_attachment=True, download_name=f"{filename}.pdf")

        zip_path = os.path.join(UPLOAD_FOLDER, "converted_documents.zip")
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for pdf_path in pdf_paths:
                zipf.write(pdf_path, os.path.basename(pdf_path))

        @after_this_request
        def remove_files(response):
            delete_files(*word_paths, *pdf_paths, zip_path)
            return response
        return send_file(zip_path, as_attachment=True, download_name="converted_documents.zip")

    except Exception as e:
        return f"Error converting Word to PDF: {str(e)}", 500


@app.route('/image-to-pdf', methods=['POST'])
def image_to_pdf():
    try:
        if 'file' not in request.files:
            return "No file uploaded", 400
        files = request.files.getlist('file')
        if not files or files[0].filename == '':
            return "No selected files", 400
        images = []
        for image_file in files:
            filename, ext = os.path.splitext(image_file.filename)
            if ext.lower() not in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
                return f"Invalid file format for {image_file.filename}. Please upload only image files", 400
            image = Image.open(image_file)
            if image.mode == 'RGBA':
                image = image.convert('RGB')
            images.append(image)
        if not images:
            return "No valid images found", 400
        output_path = os.path.join(UPLOAD_FOLDER, "merged_images.pdf")
        images[0].save(output_path, save_all=True, append_images=images[1:])

        @after_this_request
        def remove_file(response):
            delete_files(output_path)
            return response
        return send_file(output_path, as_attachment=True, download_name="merged_images.pdf")
    except Exception as e:
        return f"Error merging images into PDF: {str(e)}", 500


@app.route('/pdf-to-word', methods=['POST'])
def pdf_to_word():
    try:
        if 'file' not in request.files:
            return "No file uploaded", 400
        files = request.files.getlist('file')
        if not files or files[0].filename == '':
            return "No selected files", 400
        pdf_paths = []
        word_paths = []
        for pdf_file in files:
            filename, ext = os.path.splitext(pdf_file.filename)
            if ext.lower() != '.pdf':
                return f"Invalid file format for {pdf_file.filename}. Please upload only PDF files", 400
            pdf_path = os.path.join(UPLOAD_FOLDER, pdf_file.filename)
            output_path = os.path.join(UPLOAD_FOLDER, f"{filename}.docx")
            pdf_file.save(pdf_path)
            cv = Converter(pdf_path)
            cv.convert(output_path)
            cv.close()
            pdf_paths.append(pdf_path)
            word_paths.append(output_path)
        if len(word_paths) == 1:
            @after_this_request
            def remove_file(response):
                delete_files(pdf_paths[0], word_paths[0])
                return response
            return send_file(word_paths[0], as_attachment=True,
                             download_name=f"{os.path.splitext(files[0].filename)[0]}.docx")

        zip_path = os.path.join(UPLOAD_FOLDER, "converted_pdfs.zip")
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for word_path in word_paths:
                zipf.write(word_path, os.path.basename(word_path))

        @after_this_request
        def remove_files(response):
            all_files = pdf_paths + word_paths + [zip_path]
            delete_files(*all_files)
            return response
        return send_file(zip_path, as_attachment=True, download_name="converted_pdfs.zip")
    except Exception as e:
        return f"Error converting PDF to Word: {str(e)}", 500


@app.route('/excel-to-json', methods=['POST'])
def excel_to_json():
    try:
        if 'file' not in request.files:
            return "No file uploaded", 400
        files = request.files.getlist('file')
        if not files or files[0].filename == '':
            return "No selected files", 400
        results = []
        for excel_file in files:
            filename, ext = os.path.splitext(excel_file.filename)
            if ext.lower() not in ['.xls', '.xlsx']:
                return f"Invalid file format for {excel_file.filename}. Please upload only Excel files", 400
            df = pd.read_excel(excel_file)
            json_data = df.to_json(orient='records')
            results.append({
                "filename": excel_file.filename,
                "data": json.loads(json_data)
            })
        if len(results) == 1:
            return jsonify(results[0]["data"])
        return jsonify(results)
    except Exception as e:
        return f"Error converting Excel to JSON: {str(e)}", 500


@app.route('/json-to-excel', methods=['POST'])
def json_to_excel():
    try:
        if request.is_json:
            json_data = request.json
        elif request.form.get('json_data'):
            json_data = json.loads(request.form.get('json_data'))
        else:
            try:
                json_data = json.loads(request.data.decode('utf-8'))
            except:
                return "No valid JSON data provided. Please ensure your request contains JSON data.", 400
        if not json_data:
            return "No JSON data provided", 400
        output_path = os.path.join(UPLOAD_FOLDER, 'converted.xlsx')
        df = pd.DataFrame(json_data)
        df.to_excel(output_path, index=False)

        @after_this_request
        def remove_file(response):
            delete_files(output_path)
            return response
        return send_file(output_path, as_attachment=True, download_name="converted.xlsx")
    except Exception as e:
        return f"Error converting JSON to Excel: {str(e)}", 500


@app.route('/ppt-to-pdf', methods=['POST'])
def ppt_to_pdf():
    try:
        if 'file' not in request.files:
            return "No file uploaded", 400
        files = request.files.getlist('file')
        if not files or files[0].filename == '':
            return "No selected files", 400

        ppt_paths = []
        pdf_paths = []

        for ppt_file in files:
            filename, ext = os.path.splitext(ppt_file.filename)
            if ext.lower() not in ['.ppt', '.pptx']:
                return f"Invalid file format for {ppt_file.filename}. Please upload only PowerPoint files", 400

            ppt_path = os.path.join(UPLOAD_FOLDER, ppt_file.filename)
            output_path = os.path.join(UPLOAD_FOLDER, f"{filename}.pdf")
            ppt_file.save(ppt_path)
            subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", UPLOAD_FOLDER, ppt_path], check=True)

            ppt_paths.append(ppt_path)
            pdf_paths.append(output_path)

        if len(pdf_paths) == 1:
            @after_this_request
            def remove_file(response):
                delete_files(ppt_paths[0], pdf_paths[0])
                return response
            return send_file(pdf_paths[0], as_attachment=True, download_name=f"{filename}.pdf")

        zip_path = os.path.join(UPLOAD_FOLDER, "converted_presentations.zip")
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for pdf_path in pdf_paths:
                zipf.write(pdf_path, os.path.basename(pdf_path))

        @after_this_request
        def remove_files(response):
            delete_files(*ppt_paths, *pdf_paths, zip_path)
            return response
        return send_file(zip_path, as_attachment=True, download_name="converted_presentations.zip")

    except Exception as e:
        return f"Error converting PPT to PDF: {str(e)}", 500

@app.errorhandler(404)
def not_found(error):
    return "Page not found", 404

@app.errorhandler(500)
def server_error(error):
    return "Server error: " + str(error), 500

if __name__ == '__main__':
    app.run(debug=True)
