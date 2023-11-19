
const venue = document.getElementById('venue');
const hall_people_capacity = document.getElementById('hall_people_capacity');
const building_standard = document.getElementById('building_standard');
const broadband_speed = document.getElementById('broadband_speed');
const international_airport_proximity = document.getElementById('international_airport_proximity');
const minimum_lease_period = document.getElementById('minimum_lease_period');
const day_price = document.getElementById('day_price');

const international_conference_button = document.getElementById('international_conference_button');
const domestic_conference_button = document.getElementById('domestic_conference_button');
const reset_validation_button = document.getElementById('reset_validation_button');


// Show input error message
function showError(input, message) {
  const recordDataControl = input.parentElement;
  recordDataControl.className = 'record_data error';
  const small = recordDataControl.querySelector('small');
  small.innerText = message;
}

// Show success outline
function showSuccess(input, message) {
  const recordDataControl = input.parentElement;
  recordDataControl.className = 'record_data success';
  const small = recordDataControl.querySelector('small');
  small.innerText = message;
}

// Reset status
function resetStatus(input) {
  const recordDataControl = input.parentElement;
  recordDataControl.className = 'record_data';
  const small = recordDataControl.querySelector('small');
  small.innerText = "";
}

// Get fieldname
function getFieldName(input) {
  return input.id.charAt(0).toUpperCase() + input.id.slice(1);
}

// Check input length
function checkLength(input, min, max) {
  if (input.textContent.length < min) {
    showError(
      input,
      `${getFieldName(input)} must be at least ${min} characters`
    );
  } else if (input.textContent.length > max) {
    showError(
      input,
      `${getFieldName(input)} must be less than ${max} characters`
    );
  } else {
    showSuccess(input, `${getFieldName(input)} has correct data`);
  }
}

// Check input length
function checkValue(input, min, max) {
  if (parseInt(input.textContent) < min) {
    showError(
      input,
      `Value should be at least ${min}`
    );
  } else if (parseInt(input.textContent) > max) {
    showError(
      input,
      `Value should be less than ${max}`
    );
  } else {
    showSuccess(input, `Value is correct`);
  }
}


// Check input length
function checkValueByComparison(input, compared_value) {
  if (input.textContent != compared_value) {
    showError(
      input,
      `Desired value is ${compared_value}`
    );
  } else {
    showSuccess(input, `Value is correct`);
  }
}

// Event listeners
international_conference_button.addEventListener('click', function() {
  checkValue(hall_people_capacity, 3000, 30000000);
  checkValueByComparison(building_standard, "Prestigious")
  checkValue(broadband_speed, 300, 30000);
  checkValue(international_airport_proximity, 0, 50);
  checkValue(minimum_lease_period, 0, 7);
  checkValue(day_price, 0, 50000);
});

domestic_conference_button.addEventListener('click', function() {
  checkValue(hall_people_capacity, 2, 30000000);
  checkValueByComparison(building_standard, "Inexpensive")
  checkValue(broadband_speed, 150, 30000);
  checkValue(international_airport_proximity, 0, 150);
  checkValue(minimum_lease_period, 0, 3);
  checkValue(day_price, 0, 5000);
});

reset_validation_button.addEventListener('click', function() {
  resetStatus(hall_people_capacity);
  resetStatus(building_standard);
  resetStatus(broadband_speed);
  resetStatus(international_airport_proximity);
  resetStatus(minimum_lease_period);
  resetStatus(day_price);
});














































































































