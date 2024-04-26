
'use strict';

document.getElementById('searchForm').addEventListener('submit', function(event) {
  event.preventDefault();

  const query = document.getElementById('query').value;

  fetch(`https://api.tvmaze.com/search/shows?q=${query}`)
      .then(response => response.json())
      .then(data => {
        console.log(data); // Print the search results to the console
  })
      .catch(error => {
        console.error('Error fetching data:', error);
  });
});
