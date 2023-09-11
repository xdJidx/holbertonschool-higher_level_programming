document.addEventListener('DOMContentLoaded', function () {
  // Le code à l'intérieur de cette fonction sera exécuté après que le DOM soit prêt
  // Get a reference to the HTML <div> element with id "hello"
  const helloElement = document.querySelector('header');

  // URL of the API endpoint
  const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Use the Fetch API to make a GET request to the API endpoint
  fetch(apiUrl)
    .then((response) => {
      // Check if the response status is OK (status code 200)
      if (response.ok) {
        // Parse the JSON response
        return response.json();
      } else {
        throw new Error('Failed to fetch translation data');
      }
    })
    .then((data) => {
      // Display the translation in the "hello" element
      helloElement.textContent = data.hello;
    })
    .catch((error) => {
      console.error('Error:', error);
      helloElement.textContent = 'Error: Failed to fetch translation data';
    });
});
