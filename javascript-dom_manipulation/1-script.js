// Select the header element using document.querySelector
const header = document.querySelector('header');
const redHeader = document.querySelector('#red_header');

redHeader.addEventListener('click', () => {
  // Update the text color to red (#FF0000)
  header.style.color = '#FF0000';
});
