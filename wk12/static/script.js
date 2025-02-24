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




