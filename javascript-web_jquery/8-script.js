// Use jQuery to make an AJAX GET request to the URL
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
    // Extract the movie titles from the response data
    let movies = data.results;
    let ul = $('#list_movies');

    // Iterate through the movies and append their titles to the UL
    $.each(movies, function(index, movie) {
        let li = $('<li>').text(movie.title);
        ul.append(li);
    });
});
