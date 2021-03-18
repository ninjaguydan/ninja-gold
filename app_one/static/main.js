var gold = $('gold').attr('gold');
var count = $('gold').attr('count');
var buttons = document.querySelectorAll('#location');

if (gold > 100) { //Player loses when Gold exceeds 100
    alert("You lose :(");
    buttons.forEach(function(button) {
        button.style.display = "none";
    });
};
if (count == 10 && gold < 100) { //Player loses when turn count reaches 10 and Gold is under 100
    alert("You lose :(");
    buttons.forEach(function(button) {
        button.style.display = "none";
    })
};
if (gold == 100) { //Player wins when Gold is equal to 100
    alert("Wow! Incredible!!");
    buttons.forEach(function(button) {
        button.style.display = "none";
    })
};