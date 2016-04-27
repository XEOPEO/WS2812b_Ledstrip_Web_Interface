window.addEventListener('DOMContentLoaded',
    function ()
    {
        // Process needed code here
        // Ask for number of LEDs
        var count = getLEDCount();
        // -> Generate grid from the amount of LEDs
        createGrid(count);
        // -> Retreive LED information if any
        getLEDInformation(count);
        
        // Add eventhandler when clicking on an object
        // -> Show a color picker
        // -> Color chosen = click the color area to save it
    },
    false
);

function getLEDCount() {
    return count;
}

function createGrid(count) {
    // Create as much as elements as the count of LEDs
    for(var i = 0; i < count; i++) {
        // Create elements
        // Fill element with LED info if any
        // element.value = setLEDInformation(i);
        // Add to container
    }
}

function getLEDInformation(index) {
    // Get LED data for the corresponding HTML element
    return data;
}

window.addEventListener('DOMContentLoaded',
    function ()
    {
        // Process needed code here
        // Ask for number of LEDs
        var count = getLEDCount();
        // -> Generate grid from the amount of LEDs
        createGrid(count);
        // -> Retreive LED information if any
        getLEDInformation(count);
        
        // Add eventhandler when clicking on an object
        // -> Show a color picker
        // -> Color chosen = click the color area to save it
    },
    false
);

function getLEDCount() {
    return count;
}

function createGrid(count) {
    // Create as much as elements as the count of LEDs
    for(var i = 0; i < count; i++) {
        // Create elements
        // Fill element with LED info if any
        // element.value = setLEDInformation(i);
        // Add to container
    }
}

function getLEDInformation(index) {
    // Get LED data for the corresponding HTML element
    return data
}