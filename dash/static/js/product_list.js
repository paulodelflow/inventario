document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('inventoryBtn').addEventListener('click', function() {
        document.getElementById('productList').style.display = 'block';
        document.getElementById('addProductFormContainer').style.display = 'none';
    });

    document.getElementById('addProductBtn').addEventListener('click', function() {
        document.getElementById('addProductFormContainer').style.display = 'block';
        document.getElementById('productList').style.display = 'none';
    });

    document.getElementById('createProductBtn').addEventListener('click', function() {
        document.getElementById('addProductFormContainer').style.display = 'block';
    });

    document.getElementById('accountBtn').addEventListener('click', function() {
        document.getElementById('productList').style.display = 'none';
        document.getElementById('addProductFormContainer').style.display = 'none';
    });
});



function searchProduct() {
    let searchTerm = document.getElementById('searchInput').value.toLowerCase();
    let productBars = document.querySelectorAll('.search-results .content-bar');
    let hasResults = false;

    productBars.forEach(function(bar) {
        let productTitle = bar.querySelector('.itemtitle').textContent.toLowerCase();
        if (productTitle.includes(searchTerm)) {
            bar.style.display = 'grid'; 
            hasResults = true;
        } else {
            bar.style.display = 'none'; 
        }
    });

    if (hasResults) {
        document.getElementById('productList').style.display = 'block';
        document.getElementById('addProductForm').style.display = 'none';
    } else {
        document.getElementById('productList').style.display = 'none';
    }
}

function confirmDelete(productId) {
    Swal.fire({
        title: '¿Estás seguro?',
        text: '¿Estás seguro de que deseas eliminar este producto?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Sí, eliminar',
        cancelButtonText: 'No, eliminar'
    }).then((result) => {
        if (result.isConfirmed) {
            document.getElementById('deleteForm' + productId).submit();
        }
    });
}