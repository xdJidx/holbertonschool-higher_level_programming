// Add a click event handler to the DIV#add_item element
// Ajouter un gestionnaire d'événements clic à l'élément DIV#add_item
$('#add_item').click(function() {
    // Créer un nouvel élément <li> avec le texte "Élément"
    let nouvelElement = $('<li>Item</li>');
    // Ajouter le nouvel élément <li> à UL.my_list
    $('ul.my_list').append(nouvelElement);
});
