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
