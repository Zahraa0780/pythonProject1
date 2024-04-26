'use strict';

document.getElementById('searchForm').addEventListener('submit', function(event) {
  event.preventDefault();

  const query = document.getElementById('query').value;

  fetch(`https://api.tvmaze.com/search/shows?q=${query}`)
      .then(response => response.json())
      .then(data => {
        console.log(JSON.stringify(data, null, 2));
  })
      .catch(error => {
        console.error('Error fetching data:', error);
  });
});