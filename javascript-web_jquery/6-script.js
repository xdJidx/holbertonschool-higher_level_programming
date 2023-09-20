// Wait for the document to be fully loaded before executing the script
$(document).ready(function () {
  // Select the DIV#update_header element and attach a click event handler
  $('#update_header').click(function () {
    // Update the text of the <header> element to "New Header!!!"
    $('header').text('New Header!!!');
  });
});
