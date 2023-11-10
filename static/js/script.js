document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.region-button');
    const overlay = document.getElementById('overlay');
    const modal = document.querySelector('.region-popup');
    const modalName = document.getElementById('region-modal-name');
    const modalImage = document.getElementById('region-modal-image');
    const modalDescription = document.getElementById('region-modal-description');
    const closeModalButton = document.getElementById('close-modal');

    buttons.forEach(button => {
        button.addEventListener('click', function () {
            const regionName = button.getAttribute('data-region-name');
            const regionImage = button.getAttribute('data-region-image');
            const regionDescription = button.getAttribute('data-region-description');

            modalName.textContent = regionName;
            modalImage.src = regionImage;
            modalDescription.textContent = regionDescription;

            setTimeout(() => {
                overlay.classList.add('modal-open');
                modal.classList.add('modal-open');
            }, 50);
        });
    });

    closeModalButton.addEventListener('click', closeModal);
    overlay.addEventListener('click', closeModal);

    function closeModal() {
        // Hide overlay and modal
        overlay.classList.remove('modal-open');
        modal.classList.remove('modal-open');
    }
});
