
'use strict';

const items = ['First item', 'Second item', 'Third item'];

const target = document.getElementById("target");

let finalAnswer = "";

for (let i = 0; i < items.length; i++) {
    finalAnswer += "<li>" + items[i] + "</li>";
}

target.innerHTML = finalAnswer;
