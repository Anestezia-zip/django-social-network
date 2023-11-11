document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.region-button');
    const overlay = document.getElementById('full-screen-overlay');
    const fullScreenImage = document.getElementById('full-screen-image');

    buttons.forEach(button => {
        button.addEventListener('click', function () {
            const regionImage = button.getAttribute('data-region-image');
            
            // Show full-screen overlay with the clicked image
            overlay.style.display = 'block';
            fullScreenImage.src = regionImage;
        });
    });

    overlay.addEventListener('click', function () {
        // Hide full-screen overlay when clicked
        overlay.style.display = 'none';
    });
});
