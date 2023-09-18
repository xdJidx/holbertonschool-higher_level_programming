// Use jQuery to make an AJAX GET request to the URL
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function(data) {
    // Extract the character's name from the response data
    let characterName = data.name;
    // Display the character's name in the DIV#character element
    $('#character').text(characterName);
});
