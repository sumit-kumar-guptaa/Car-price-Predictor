document.querySelector(".prediction-form").addEventListener("submit", function(event) {
    event.preventDefault();

    const carModel = document.getElementById("carModel").value;
    const carYear = document.getElementById("carYear").value;
    const carMileage = document.getElementById("carMileage").value;
    const carCondition = document.getElementById("carCondition").value;

    if (carModel && carYear && carMileage && carCondition) {
        // Simple prediction logic (this would be replaced with a real API call or logic)
        let basePrice = 20000;  // base price of the car in USD
        const age = new Date().getFullYear() - carYear;
        const mileageFactor = carMileage / 100000;
        const conditionFactor = carCondition === 'new' ? 1 : 0.7;

        let predictedPrice = basePrice - (age * 1000) - (mileageFactor * 5000);
        predictedPrice *= conditionFactor;

        // Show the result section
        document.getElementById("predictedPrice").textContent = `$${predictedPrice.toFixed(2)}`;
        document.getElementById("result-section").style.display = 'block';
    }
});
