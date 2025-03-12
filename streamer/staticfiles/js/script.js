document.addEventListener('DOMContentLoaded', function() {
    // Header scroll effect
    const header = document.querySelector('header');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // Mobile menu toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mainNav = document.querySelector('.main-nav');
    
    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', function() {
            this.classList.toggle('active');
            
            if (mainNav.style.display === 'flex') {
                mainNav.style.display = 'none';
            } else {
                mainNav.style.display = 'flex';
                mainNav.style.flexDirection = 'column';
                mainNav.style.position = 'absolute';
                mainNav.style.top = '60px';
                mainNav.style.left = '0';
                mainNav.style.width = '100%';
                mainNav.style.backgroundColor = 'var(--background-dark)';
                mainNav.style.padding = '20px';
                mainNav.style.zIndex = '1000';
            }
        });
    }

    // Carousel functionality
    const carousels = document.querySelectorAll('.carousel');
    
    carousels.forEach(carousel => {
        const prevBtn = carousel.parentElement.querySelector('.prev-btn');
        const nextBtn = carousel.parentElement.querySelector('.next-btn');
        const itemWidth = carousel.querySelector('.carousel-item').offsetWidth + 16; // width + gap
        
        if (prevBtn) {
            prevBtn.addEventListener('click', () => {
                carousel.scrollBy({
                    left: -itemWidth * 2,
                    behavior: 'smooth'
                });
            });
        }
        
        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                carousel.scrollBy({
                    left: itemWidth * 2,
                    behavior: 'smooth'
                });
            });
        }
    });

    // Video card hover effect
    const videoCards = document.querySelectorAll('.video-card');
    
    videoCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            // You could add a play icon or preview animation here
            card.querySelector('.thumbnail').style.opacity = '0.7';
        });
        
        card.addEventListener('mouseleave', () => {
            card.querySelector('.thumbnail').style.opacity = '1';
        });
    });

    // Search functionality
    const searchBox = document.querySelector('.search-box input');
    const searchBtn = document.querySelector('.search-btn');
    
    if (searchBtn && searchBox) {
        searchBtn.addEventListener('click', () => {
            performSearch();
        });
        
        searchBox.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                performSearch();
            }
        });
        
        function performSearch() {
            const searchTerm = searchBox.value.trim();
            if (searchTerm) {
                // In a real application, this would navigate to search results
                alert(`Searching for: ${searchTerm}`);
                // You could redirect to a search page like:
                // window.location.href = `/search?q=${encodeURIComponent(searchTerm)}`;
            }
        }
    }

    // Add to My List functionality
    const myListBtn = document.querySelector('.btn-secondary');
    
    if (myListBtn) {
        myListBtn.addEventListener('click', () => {
            // Toggle the "added to list" state
            myListBtn.classList.toggle('added');
            
            if (myListBtn.classList.contains('added')) {
                myListBtn.innerHTML = `
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M9 11l3 3L22 4"></path>
                        <path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"></path>
                    </svg>
                    Added to List
                `;
                // In a real app, you would save this to the user's list in a database
            } else {
                myListBtn.innerHTML = `
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10"></circle>
                        <line x1="12" y1="8" x2="12" y2="16"></line>
                        <line x1="8" y1="12" x2="16" y2="12"></line>
                    </svg>
                    My List
                `;
            }
        });
    }

    // Simulate loading content (for demonstration purposes)
    setTimeout(() => {
        document.querySelectorAll('.carousel-item img, .video-card img, .category-card img').forEach(img => {
            // In a real application, this would be replaced with actual content loading logic
            img.style.opacity = '1';
        });
    }, 1000);
});