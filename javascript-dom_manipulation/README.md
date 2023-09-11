# JavaScript DOM manipulation

## Tasks

### 0. Color Me <br>
Pour définir une couleur sur un header, définissez la variable dans le fichier .js :
```
// Select the header element using document.querySelector
const header = document.querySelector('header');
```
Ensuite attribuez lui le style voulu :
```
// Update the text color to red (#FF0000)
header.style.color = '#FF0000';
```
Votre text header est maintenant rouge.

### 1. Click and turn red<br>
Ajoutons un evenement 'click' pour changer la couleur du header en rouge avec red_header :
```
// Select the header element using document.querySelector
const header = document.querySelector('header');
const redHeader = document.querySelector('#red_header');
```
Pour définir un evenement, on utilise :
```
redHeader.addEventListener('click', () => {
  // Update the text color to red (#FF0000)
  header.style.color = '#FF0000';
});
```
Le text du header devient rouge en appuyant sur header_red.

### 2. Add `.red` class<br>
Cette fois ci la couleur sera définie dans une classe 'red'.
```
// Get the element with id "red_header"
const redHeader = document.getElementById('red_header');
const header = document.querySelector('header');
```
On ajoute la classe 'red' dans header quand on interagi avec red_header :
```
// Add a click event listener to the "red_header" element
redHeader.addEventListener('click', () => {
  // Add the class "red" to the header element
  header.classList.add('red');
});
```

### 3. Toggle classes<br>
Cette fois-ci, le header possède une couleur et celle-ci change à chaque fois que nous cliquons sur 'toggle_header'.
```
// Get the elements by their respective IDs
const toggleHeader = document.getElementById('toggle_header');
const header = document.querySelector('header');
```
Il suffit d'une simple condition if et else if pour passer d'une couleur à l'autre, on ajoute l'une des classes et on enleve l'autre :
```
// Add a click event listener to the "toggle_header" element
toggleHeader.addEventListener('click', function () {
  // Toggle between the "red" and "green" classes on the header element
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else if (header.classList.contains('green')) {
    header.classList.remove('green');
    header.classList.add('red');
  }
});
```

### 4. List of elements<br>
On crée une liste li qui ajoute 'Item' à chaque fois dans l'élément ul d'une classe my_list.
```
// Get the element with id 'add_item'
const addItem = document.getElementById('add_item');
// Get the <ul> element with class 'my_list'
const myList = document.querySelector('.my_list');
```
On crée une fonction qui utilise l'évenement 'click' pour ajouter un nouveau Item dans l'élément ul.
```
// Add a click event listener to the 'add_item' element
addItem.addEventListener('click', function () {
  // Create a new <li> element
  const newItem = document.createElement('li');

  // Set the text content of the new <li> element
  newItem.textContent = 'Item';

  // Append the new <li> element to the <ul> element
  myList.appendChild(newItem);
});

```

### 5. Change the text<br>
Changer un text en appuyant sur un text, le concept reste le même. Déclaré les variables :
```
const header = document.querySelector('header');
const updateHeader = document.getElementById('update_header');
```
Changer l'élément avec l'option .textContent :
```
updateHeader.addEventListener('click', function () {
  header.textContent = 'New Header!!!';
});
```

### 6. Star wars character<br>
Nous utilisons la fonction fetch() pour récupérer des données vient un url :
```
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
```
Etape 1 : Définir les variables ainsi que l'url
Etape 2 : Utiliser fetch() dans un premier temps pour vérifier que la réponse est bien reçu puis récupérer la donnée dans un format .json.

### 7. Star Wars movies
On retourne la liste des films d'une url donnée.
Toujours dans fetch :
```
.then((data) => {
    // Extract movie titles from the data
    const movies = data.results;

    // Iterate through the movies and add them to the list
    movies.forEach((movie) => {
      const title = movie.title;
      const listItem = document.createElement("li");
      listItem.textContent = title;
      movieList.appendChild(listItem);
    });
})
```
Le retour est dynamique et ajoutera d'autre titres qui viendraient s'ajouter dans cette base de donnée.

### 8. Say Hello!
Le but est de récupérer le string d'une url pour l'ajouter au text.
La difficulté ici était d'ajouter un écouteur d'événements DOMContentLoaded pour vous assurer que le code JavaScript ne s'exécute que lorsque le DOM est prêt.
```
document.addEventListener('DOMContentLoaded', function() {
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
```
Avec ce code, le text : 'Say Hello' récupère le text dans 'hello' et le remplace.
