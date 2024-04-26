
'use strict';
const names = ['John', 'Paul', 'Jones'];

const element = document.getElementById('target');

for (let i = 0; i < names.length; i++) {
    element.innerHTML += `<li>${names[i]}</li>`;
}
