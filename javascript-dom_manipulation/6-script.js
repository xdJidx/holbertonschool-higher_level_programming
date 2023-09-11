// Get a reference to the element with id "character"
const characterElement = document.getElementById("character");

// URL of the API endpoint
const apiUrl = "https://swapi-api.hbtn.io/api/people/5/?format=json";

// Use the Fetch API to make a GET request to the API endpoint
fetch(apiUrl)
  .then((response) => {
    // Check if the response status is OK (status code 200)
    if (response.ok) {
      // Parse the JSON response
      return response.json();
    } else {
      throw new Error("Failed to fetch character data");
    }
  })
  .then((data) => {
    // Extract the character name from the response data
    const characterName = data.name;

    // Display the character name in the "character" element
    characterElement.textContent = characterName;
  })
  .catch((error) => {
    console.error("Error:", error);
  });
