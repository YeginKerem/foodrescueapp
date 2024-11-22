document.addEventListener('DOMContentLoaded', function() {
    const donateForm = document.getElementById('donateForm');
    const donationsList = document.getElementById('donationsList');

    donateForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const item = document.getElementById('item').value;
        const quantity = document.getElementById('quantity').value;
        const expiryDate = document.getElementById('expiryDate').value;

        // Simulate a server request to save the donation
        const donation = {
            item: item,
            quantity: quantity,
            expiryDate: expiryDate
        };

        // Add the donation to the list
        addDonationToList(donation);

        // Clear the form
        donateForm.reset();
    });

    function addDonationToList(donation) {
        const li = document.createElement('li');
        li.textContent = `${donation.item} - Quantity: ${donation.quantity}, Expiry Date: ${donation.expiryDate}`;
        donationsList.appendChild(li);
    }
});
