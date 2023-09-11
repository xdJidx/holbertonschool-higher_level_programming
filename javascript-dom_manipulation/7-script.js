// Get a reference to the HTML <ul> element with id "list_movies"
const movieList = document.getElementById('list_movies');

// URL of the API endpoint
const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Use the Fetch API to make a GET request to the API endpoint
fetch(apiUrl)
  .then((response) => {
    // Check if the response status is OK (status code 200)
    if (response.ok) {
      // Parse the JSON response
      return response.json();
    } else {
      throw new Error('Failed to fetch movie data');
    }
  })
  .then((data) => {
    // Extract movie titles from the data
    const movies = data.results;

    // Iterate through the movies and add them to the list
    movies.forEach((movie) => {
      const title = movie.title;
      const listItem = document.createElement('li');
      listItem.textContent = title;
      movieList.appendChild(listItem);
    });
  })
  .catch((error) => {
    console.error('Error:', error);
    movieList.textContent = 'Error: Failed to fetch movie data';
  });
