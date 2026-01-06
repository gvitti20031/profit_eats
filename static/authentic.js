const REQUIRED_FIELDS = ['p', 'd', 't', 'm']

function validateForm() {
    let isValid = true;

    REQUIRED_FIELDS.forEach(id => {
        const input = document.getElementById(id);
        // Ensure you have an error span with ID 'error-p', 'error-d', etc., in your HTML
        const errorSpan = document.getElementById(`error-${id}`);
        const value = input.value.trim();
        const numberValue = parseFloat(value);
        let errorMessage = "Please enter a number larger than 0.";

        // --- Validation Checks ---

        // Check 1: Minlength of 1 (Not Empty)
        if (value.length === 0) {
            errorMessage = "This field cannot be empty.";
            errorSpan.textContent = errorMessage;
            errorSpan.style.display = 'block';
            isValid = false;
            return; // Move to next field
        }

        // Check 2: Numeric Check (should be caught by validateFloat, but double check)
        if (isNaN(numberValue)) {
            errorMessage = "Please enter a valid number.";
            errorSpan.textContent = errorMessage;
            errorSpan.style.display = 'block';
            isValid = false;
            return;
        }

        // Check 3: Positive Value Check (> 0)
        if (numberValue <= 0) {
            errorSpan.textContent = errorMessage; // Use default "larger than 0" message
            errorSpan.style.display = 'block';
            isValid = false;
            return;
        }

        // If all checks pass for this field, hide the error
        errorSpan.style.display = 'none';
    });

    return isValid;
}