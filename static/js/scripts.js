

document.addEventListener("DOMContentLoaded", function() {
    const password1 = document.getElementById("id_password1");
    const password2 = document.getElementById("id_password2");

    password2.addEventListener('input', function() {
        if (password1.value !== password2.value) {
            password2.setCustomValidity("Passwords do not match");
        } else {
            password2.setCustomValidity("");
        }
    });
});


// # loader



document.addEventListener("DOMContentLoaded", function () {
    // Handle form submit event
    var loader = document.getElementById("loader");
    // Display loader on page load
    loader.style.display = "flex";
    // Hide loader once the page is fully loaded
   

    // Hide the loader once the page is fully loaded (after submission or any page reload)
    window.onload = function () {
        loader.style.display = "none";
    };
});

