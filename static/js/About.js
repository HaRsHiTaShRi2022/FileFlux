document.addEventListener('DOMContentLoaded', function() {
    const uploadBtn = document.getElementById('uploadBtn');
    const uploadDropdown = document.getElementById('uploadDropdown');
    const selectBtn = document.getElementById('selectBtn');
    const toolDropdown = document.getElementById('toolDropdown');
    const toolItems = document.querySelectorAll('.tool-item');

    if (uploadBtn && selectBtn) {
        uploadBtn.addEventListener('click', function() {
            if (uploadDropdown) {
                uploadDropdown.classList.toggle('show');
                uploadBtn.classList.toggle('active');
            }
            
            if (toolDropdown && toolDropdown.classList.contains('show')) {
                toolDropdown.classList.remove('show');
                selectBtn.classList.remove('active');
            }
        });

        selectBtn.addEventListener('click', function() {
            if (toolDropdown) {
                toolDropdown.classList.toggle('show');
                selectBtn.classList.toggle('active');
            }
            
            if (uploadDropdown && uploadDropdown.classList.contains('show')) {
                uploadDropdown.classList.remove('show');
                uploadBtn.classList.remove('active');
            }
        });
    }

    // Tool items selection
    if (toolItems) {
        toolItems.forEach(item => {
            item.addEventListener('click', function() {
                if (selectBtn) {
                    selectBtn.textContent = this.textContent;
                    
                    // Create dropdown arrow
                    const arrow = document.createElement('svg');
                    arrow.className = 'dropdown-arrow';
                    arrow.setAttribute('width', '12');
                    arrow.setAttribute('height', '12');
                    arrow.setAttribute('viewBox', '0 0 12 12');
                    arrow.setAttribute('fill', 'none');
                    arrow.innerHTML = '<path d="M2 4L6 8L10 4" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>';
                    
                    selectBtn.appendChild(arrow);
                    
                    if (toolDropdown) {
                        toolDropdown.classList.remove('show');
                    }
                    
                    if (selectBtn) {
                        selectBtn.classList.remove('active');
                    }
                }
            });
        });
    }

    // Close dropdowns when clicking outside
    document.addEventListener('click', function(event) {
        // Upload dropdown
        if (uploadBtn && uploadDropdown && 
            !uploadBtn.contains(event.target) && 
            !uploadDropdown.contains(event.target)) {
            uploadDropdown.classList.remove('show');
            uploadBtn.classList.remove('active');
        }

        // Tool dropdown
        if (selectBtn && toolDropdown && 
            !selectBtn.contains(event.target) && 
            !toolDropdown.contains(event.target)) {
            toolDropdown.classList.remove('show');
            selectBtn.classList.remove('active');
        }
    });
});
document.addEventListener("DOMContentLoaded", function () {
    const featuresBtn = document.getElementById("featuresBtn");
    const featuresDropdown = document.getElementById("featuresDropdown");

    featuresBtn.addEventListener("click", function () {
        featuresDropdown.classList.toggle("show");
    });

    document.addEventListener("click", function (e) {
        if (!featuresBtn.contains(e.target) && !featuresDropdown.contains(e.target)) {
            featuresDropdown.classList.remove("show");
        }
    });
});