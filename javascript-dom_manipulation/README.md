# JavaScript DOM manipulation

## Tasks

0. Color Me <br>
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

1. Click and turn red<br>
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

2. Add `.red` class<br>
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

3. Toggle classes<br>
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

4. List of elements<br>
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

5. Change the text<br>