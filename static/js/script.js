document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.region-button');
    const overlay = document.getElementById('full-screen-overlay');
    const fullScreenImageContainer = document.getElementById('full-screen-image-container');
    const body = document.body;

    buttons.forEach(button => {
        button.addEventListener('click', function () {
            const regionImages = button.getAttribute('data-region-images').split(',');

            // Show full-screen overlay with the clicked images
            overlay.style.display = 'block';
            body.style.overflow = 'hidden'; // Disallow scrolling

            // Clear previous images
            fullScreenImageContainer.innerHTML = '';

            // Add each image to the overlay
            regionImages.forEach(image => {
                const imgElement = document.createElement('img');
                imgElement.src = image;
                fullScreenImageContainer.appendChild(imgElement);
            });
        });
    });

    if (overlay) {
        overlay.addEventListener('click', function () {
            // Hide full-screen overlay when clicked
            overlay.style.display = 'none';
            body.style.overflow = 'auto'; // Allow scrolling
        });
    }
});
