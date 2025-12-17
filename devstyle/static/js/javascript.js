document.addEventListener("DOMContentLoaded", () => {
    // 1. Animación de entrada escalonada (Staggered Fade-in) al cargar la página
    // Usamos IntersectionObserver para disparar la animación cuando los elementos entran en pantalla
    const cards = document.querySelectorAll('.product-card');
            
    const observerOptions = {
        root: null, // viewport
        threshold: 0.1, // disparar cuando el 10% del elemento es visible
        rootMargin: "0px 0px -50px 0px" // margen inferior para que la animación empiece un poco antes
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                // Añadimos un pequeño retraso basado en el índice para el efecto escalonado
                setTimeout(() => {
                    entry.target.classList.add('is-visible');
                }, index * 150); // 150ms de diferencia entre cada tarjeta
                observer.unobserve(entry.target); // Dejar de observar una vez animado
            }
        });
    }, observerOptions);

    cards.forEach(card => {
        observer.observe(card);
    });

    // 2. Animación e interactividad del botón "Agregar"
    const addButtons = document.querySelectorAll('.add-to-cart-btn');

    addButtons.forEach(button => {
        button.addEventListener('click', function() {
            const originalText = this.innerText;
                    
            // Añadir clase para la animación de pulso
            this.classList.add('btn-clicked', 'bg-green-600', 'hover:bg-green-700');
            this.classList.remove('bg-tech-blue', 'hover:bg-blue-700');
            // Cambiar texto temporalmente para feedback visual
            this.innerHTML = `
                        <span class="flex items-center justify-center gap-1">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2.5" stroke="currentColor" class="w-4 h-4">
                              <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                            </svg>
                            Agregado
                        </span>
                    `;

            // Resetear el botón después de 2 segundos
            setTimeout(() => {
                this.classList.remove('btn-clicked', 'bg-green-600', 'hover:bg-green-700');
                this.classList.add('bg-tech-blue', 'hover:bg-blue-700');
                this.innerText = originalText;
            }, 2000);
        });
    });

    // 3. Busqueda de productos
    const searchInput = document.getElementById('search-input');
    const productCards = document.querySelectorAll('.product-card');
    const totalProducts = document.getElementById('total-products');
    const resultsCount = document.getElementById('results-count');
    resultsCount.style.display = 'none';
    
    if(searchInput){
        searchInput.addEventListener('input', function(e) {
            totalProducts.style.display = 'none';
            resultsCount.style.display = 'block';
            const searchTerm = e.target.value.toLowerCase();
            let visibleCount = 0;
            productCards.forEach(card => {
                const productName = card.querySelector('.product-name').textContent.toLowerCase();
                if (productName.includes(searchTerm)) {
                    card.style.display = 'block';
                    visibleCount++;
                } else {
                    card.style.display = 'none';
                }
            });
            resultsCount.textContent = `Mostrando ${visibleCount} producto${visibleCount !== 1? 's': ''}`;
        });
    }
});
