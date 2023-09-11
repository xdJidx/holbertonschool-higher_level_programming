// Get the elements by their respective IDs
const toggleHeader = document.getElementById('toggle_header');
const header = document.querySelector('header');

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
