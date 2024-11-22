document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('feedback-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Thank you for your feedback!');
                form.reset();
            } else {
                alert('There was an error submitting your feedback.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('There was an error submitting your feedback.');
        });
    });
});
