// Wait for the document to be ready
$(document).ready(function() {
    // Use jQuery to make an AJAX GET request to the URL
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
        // Extract the translation from the response data
        let translation = data.hello;
        // Display the translation in the DIV#hello element
        $('#hello').text(translation);
    });
});
