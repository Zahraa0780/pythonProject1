'use strict';

document.getElementById('searchForm').addEventListener('submit', function(event) {
  event.preventDefault();

  const query = document.getElementById('query').value;

  fetch(`https://api.tvmaze.com/search/shows?q=${query}`)
      .then(response => response.json())
      .then(data => {
        displayResults(data); // Print the search results to the HTML
  })
      .catch(error => {
        console.error('Error fetching data:', error);
  });
});

// Print the following information: name(h2), URL(a), Medium Image(<img src="" alt="">), summary (p)
function displayResults(results) {
  const resultsContainer = document.getElementById('searchResults');

  // Clear existing content inside this div to make sure it replaces the previous content
  resultsContainer.innerHTML = "";

  results.forEach(({ show }) => {
    const showDiv = document.createElement('div');

    showDiv.innerHTML = `
      <h2>${show.name}</h2>
      <img src="${show.image?.medium}" alt="${show.name}">
      <a href="${show.url}" target="_blank">${show.name}\n</a>
      <p>${show.summary}</p>
    `;

    resultsContainer.appendChild(showDiv);
  });
}