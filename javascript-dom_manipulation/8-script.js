function fetchHello() {
    // Select the HTML element with the id "hello"
    const helloElement = document.getElementById('hello');

    const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

    // Use the Fetch API to retrieve the translation
    fetch(apiUrl)
      .then((response) => response.json())
      .then((data) => {
        // Extract and display the translation
        const helloTranslation = data.hello;
        helloElement.textContent = helloTranslation;
      })
      .catch((error) => {
        console.error('Fetch error:', error);
      });
  }

  // Call the function when the document is ready
  document.addEventListener('DOMContentLoaded', fetchHello);
