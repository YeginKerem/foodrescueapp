document.addEventListener('DOMContentLoaded', function() {
    
    const donateForm = document.getElementById('donateForm');
    const donationsList = document.getElementById('donationsList');
    
    donateForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const item = document.getElementById('item').value;
        const quantity = document.getElementById('quantity').value;
        const expiryDate = document.getElementById('expiryDate').value;

       
        const donation = {
            item: item,
            quantity: quantity,
            expiryDate: expiryDate
        };

        
        addDonationToList(donation);

  
        donateForm.reset();
    });

    function addDonationToList(donation) {
        const li = document.createElement('li');
        li.textContent = `${donation.item} - Quantity: ${donation.quantity}, Expiry Date: ${donation.expiryDate}`;
        donationsList.appendChild(li);
    }
});
