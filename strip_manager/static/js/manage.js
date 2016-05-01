function printSliderValue(source, target) {
    source.setAttribute("title", source.value);

    var container = document.getElementById(target);
    container.innerHTML = source.value;
}

function getComponentFromHex(hex, component) {
    if (component == 'r') return parseInt(hex.substring(1,3), 16);
    else if (component == 'g') return parseInt(hex.substring(3,5), 16);
    else if (component == 'b') return parseInt(hex.substring(5,7), 16);
}

function getColorObject(hex) {
    var red = getComponentFromHex(hex, 'r'),
        green = getComponentFromHex(hex, 'g'),
        blue = getComponentFromHex(hex, 'b'),
        object = {
            "r": red,
            "g": green,
            "b": blue
        };

    return object;
}

document.addEventListener("DOMContentLoaded", function() {
    printSliderValue(document.getElementById("sldrBrightness"), "brightnessVal");

    $(".colorp").minicolors({
        control: $(this).attr('data-control') || 'hue',
        defaultValue: $(this).attr('data-defaultValue') || '',
        format: $(this).attr('data-format') || 'hex',
        keywords: $(this).attr('data-keywords') || '',
        inline: $(this).attr('data-inline') === 'true',
        letterCase: $(this).attr('data-letterCase') || 'lowercase',
        opacity: $(this).attr('data-opacity'),
        position: $(this).attr('data-position') || 'bottom left',
        swatches: $(this).attr('data-swatches') ? $(this).attr('data-swatches').split('|') : [],
        hide: function() {
            console.log(this.value + ", " + this.id);
            if (this.id == "pickerColorStrip") sendCommand(this.id);
        },
        theme: 'bootstrap'
    });

    function sendCommand(caller) {
        switch (caller) {
            case "btnCreateStrip":
                var nmbrIndexLED = document.getElementById("nmbrIndexLED"),
                    nmbrIndexLEDFrom = document.getElementById("nmbrIndexLEDFrom"),
                    count = parseInt(document.getElementById("txtCountLEDs").value),
                    brightness = parseInt(document.getElementById("sldrBrightness").value);

                nmbrIndexLED.setAttribute("max", count - 1);
                nmbrIndexLEDFrom.setAttribute("max", count - 1);

                socket.emit("command", JSON.stringify({
                    "count": count,
                    "brightness": brightness
                }));
                break;
            case "btnTurnOff":
                socket.emit("command", "turnOff");
                break;
            case "btnColorWipe":
                socket.emit("command", "colorWipe");
                break;
            case "btnTheaterChase":
                socket.emit("command", "theaterChase");
                break;
            case "btnRainbow":
                socket.emit("command", "rainbow");
                break;
            case "btnRainbowCycle":
                socket.emit("command", "rainbowCycle");
                break;
            case "btnTheaterChaseRainbow":
                socket.emit("command", "theaterChaseRainbow");
                break;
            case "btnSetLED":
                var hex = document.getElementById("pickerColorLED").value,
                    colorObject = getColorObject(hex),
                    index = parseInt(document.getElementById("nmbrIndexLED").value);

                socket.emit("command", JSON.stringify({
                    "index": index,
                    "color": colorObject
                }));
                break;
            case "btnCreateGradient":
                var startHex = document.getElementById("pickerColorStart").value,
                    endHex = document.getElementById("pickerColorEnd").value,
                    startColorObject = getColorObject(startHex),
                    endColorObject = getColorObject(endHex);

                socket.emit("command", JSON.stringify({
                    "startColor": startColorObject,
                    "endColor": endColorObject
                }));
                break;
            case "pickerColorStrip":
                var hex = document.getElementById("pickerColorStrip").value,
                    colorObject = getColorObject(hex);

                socket.emit("command", JSON.stringify({
                    "color": colorObject
                }));
                break;
        }
    }

    // SocketIO web client
    var socket = io("/strip");

    // Settings - button
    var btnCreateStrip = document.getElementById("btnCreateStrip"),
        btnTurnOff = document.getElementById("btnTurnOff");

    btnCreateStrip.addEventListener("click", function(e) { sendCommand(e.target.id); });
    btnTurnOff.addEventListener("click", function(e) { sendCommand(e.target.id); });

    // Animations - buttons
    var btnColorWipe = document.getElementById("btnColorWipe"),
        btnTheaterChase = document.getElementById("btnTheaterChase"),
        btnRainbow = document.getElementById("btnRainbow"),
        btnRainbowCycle = document.getElementById("btnRainbowCycle"),
        btnTheaterChaseRainbow = document.getElementById("btnTheaterChaseRainbow");

    btnColorWipe.addEventListener("click", function(e) { sendCommand(e.target.id); });
    btnTheaterChase.addEventListener("click", function(e) { sendCommand(e.target.id); });
    btnRainbow.addEventListener("click", function(e) { sendCommand(e.target.id); });
    btnRainbowCycle.addEventListener("click", function(e) { sendCommand(e.target.id); });
    btnTheaterChaseRainbow.addEventListener("click", function(e) { sendCommand(e.target.id); });

    // Modals - buttons
    var btnSetLED = document.getElementById("btnSetLED"),
        btnCreateGradient = document.getElementById("btnCreateGradient");


    btnSetLED.addEventListener("click", function(e) { sendCommand(e.target.id); });
    btnCreateGradient.addEventListener("click", function(e) { sendCommand(e.target.id); });
}, false);
