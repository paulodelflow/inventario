function confirmDelete(productId) {
    if (confirm('¿Estás seguro de que deseas eliminar este producto?')) {
        document.getElementById('deleteForm' + productId).submit();
    }
}
function searchProduct() {
    var searchTerm = document.getElementById('searchInput').value.toLowerCase();
    var productBars = document.querySelectorAll('.search-results .content-bar');

    productBars.forEach(function(bar) {
        var productTitle = bar.querySelector('.itemtitle').textContent.toLowerCase();
        if (productTitle.includes(searchTerm)) {
            bar.style.display = 'block'; // Muestra la barra si coincide con el término de búsqueda
        } else {
            bar.style.display = 'none'; // Oculta la barra si no coincide con el término de búsqueda
        }
    });
}
