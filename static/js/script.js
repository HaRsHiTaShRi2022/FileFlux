document.addEventListener("DOMContentLoaded", function () {
    const uploadBtn = document.getElementById("uploadBtn");
    const selectBtn = document.getElementById("selectBtn");
    const toolDropdown = document.getElementById("toolDropdown");
    const convertBtn = document.querySelector(".convert-btn");
    let selectedTool = "";
    let selectedFiles = [];

    // Upload button click event
    uploadBtn.addEventListener("click", function () {
        if (!selectedTool) {
            alert("Please select a conversion tool first.");
            return;
        }

        const input = document.createElement("input");
        input.type = "file";
        input.accept = "*/*"; // Allow all file types
        input.multiple = true; // Allow multiple file selection
        input.click();

        input.addEventListener("change", function () {
            if (input.files.length > 0) {
                selectedFiles = Array.from(input.files);
                uploadBtn.innerHTML = `${selectedFiles.length} file(s) selected`;
            }
        });
    });

    // Tool selection dropdown
    selectBtn.addEventListener("click", function () {
        toolDropdown.classList.toggle("show");
    });

    // Handle tool selection
    toolDropdown.addEventListener("click", function (e) {
        if (e.target.classList.contains("tool-item")) {
            selectedTool = e.target.innerText.toLowerCase().replace(/ /g, "-");
            selectBtn.innerText = e.target.innerText;
            toolDropdown.classList.remove("show");
            uploadBtn.innerHTML = "UPLOAD FILES"; // Reset upload button text
            selectedFiles = [];
        }
    });

    // Convert button click event
    convertBtn.addEventListener("click", function () {
        if (selectedFiles.length === 0) {
            alert("Please upload at least one file.");
            return;
        }
        if (!selectedTool) {
            alert("Please select a conversion tool.");
            return;
        }

        convertBtn.innerHTML = "CONVERTING...";
        convertBtn.disabled = true;

        let formData = new FormData();
        selectedFiles.forEach(file => {
            formData.append("file", file);
        });

        fetch(`/${selectedTool}`, {
            method: "POST",
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                return response.text().then(text => { throw new Error(text || "Error during conversion"); });
            }
            return response.blob();
        })
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.href = url;
            a.download = "converted_files";
            document.body.appendChild(a);
            a.click();
            a.remove();

            alert("Conversion completed successfully!");
            resetConvertButton();
        })
        .catch(error => {
            alert("Error during conversion: " + error.message);
            resetConvertButton();
        });
    });

    function resetConvertButton() {
        convertBtn.innerHTML = "CONVERT";
        convertBtn.disabled = false;
    }

    document.addEventListener("click", function (e) {
        if (!selectBtn.contains(e.target) && !toolDropdown.contains(e.target)) {
            toolDropdown.classList.remove("show");
        }
    });
});