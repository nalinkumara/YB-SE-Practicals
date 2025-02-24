document.getElementById('alertBtn').addEventListener('click', function() {
    alert('Hello from JavaScript!');
});
document.getElementById('nextPage').addEventListener('click', function() {
    window.location.href = "/nextPage";
});
// document.getElementById('backBtn').addEventListener('click', function() {
//     window.history.back();
// });
document.getElementById('loadImage').addEventListener('click', function() {
    let img = document.createElement("img");
    img.src = "/static/panda.jpg"
    img.alt = "Dynamic Image"; 
    img.width = 300; // Set width
    img.height = 200; // Set height

    document.body.appendChild(img);
});
document.getElementById("localImage").addEventListener("change", function(event) {
    const file = event.target.files[0]; // Get the selected file

    if (file) {
        const reader = new FileReader(); // Create a FileReader object

        reader.onload = function(e) {
            const image = document.getElementById("imageDisplay");
            image.src = e.target.result; // Set the image source
            image.style.display = "block"; // Make the image visible
        };

        reader.readAsDataURL(file); // Convert file to a base64 URL
    }
});




