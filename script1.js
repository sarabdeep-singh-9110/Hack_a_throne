document.getElementById('portfolioForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = new FormData(this);
    const data = {
        age: formData.get('age'),
        income: formData.get('income'),
        investment_amount: formData.get('investment_amount'),
        risk_tolerance: formData.get('risk_tolerance')
    };

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = `Recommended Portfolio: ${data.portfolio_type}`;
    })
    .catch(error => console.error('Error:', error));
});