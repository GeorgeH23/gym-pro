document.addEventListener('DOMContentLoaded', function () {
    // Trigger the modal when the page loads
    var errorModal = new bootstrap.Modal(document.getElementById('errorModal'));
    errorModal.show();

    // Fade out alerts with colors
    fadeOutAlert();

    function fadeOutAlert() {
        const alerts = document.querySelectorAll('.alert');

        alerts.forEach((alert) => {
            const alertColor = getComputedStyle(alert).getPropertyValue('background-color');
            const messageTag = alert.dataset.messageTag;

            setTimeout(() => {
                alert.style.transition = 'opacity 1s';
                alert.style.opacity = '0';
                alert.style.backgroundColor = alertColor;

                setTimeout(() => {
                    alert.remove();
                    // Close the modal when all alerts are removed
                    if (document.querySelectorAll('.alert').length === 0) {
                        errorModal.hide();
                    }
                }, 800); // Remove the alert after fade out
            }, 1300); // Delay for 3 seconds before starting to fade out
        });
    }
});