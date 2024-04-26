'use strict';

const myArray = ['First item', 'Second item', 'Third item'];

const parentElement = document.getElementById("target");

for (let i = 0; i < myArray.length; i++) {
    const newLi = document.createElement('li');
    newLi.textContent = myArray[i];

    if (i === 1) {
        newLi.classList.add('my-item');
    }

    parentElement.appendChild(newLi);

}