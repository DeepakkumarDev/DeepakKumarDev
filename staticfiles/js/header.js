document.addEventListener("DOMContentLoaded", function() {
    // Pagination functionality
    const arrowLeft = document.querySelector(".arrow-left");
    const arrowRight = document.querySelector(".arrow-right");
    const progressForeground = document.querySelector(".progress-sub-foreground");
    const slideNumbers = document.querySelector("#slide-numbers");
  
    let currentPage = 1;
    const totalPages = 5; // Replace with actual total number of pages
  
    // Function to update pagination
    function updatePagination() {
      progressForeground.style.width = `${(currentPage / totalPages) * 100}%`;
      slideNumbers.innerHTML = currentPage;
    }
  
    // Event listeners for pagination arrows
    arrowLeft.addEventListener("click", function() {
      if (currentPage > 1) {
        currentPage--;
        updatePagination();
      }
    });
  
    arrowRight.addEventListener("click", function() {
      if (currentPage < totalPages) {
        currentPage++;
        updatePagination();
      }
    });
  
    // Example button click event
    const discoverButtons = document.querySelectorAll(".discover");
    discoverButtons.forEach(button => {
      button.addEventListener("click", function() {
        console.log("Discover button clicked");
        // Add functionality for discovery button click
      });
    });
  
    // Example bookmark button click event
    const bookmarkButtons = document.querySelectorAll(".bookmark");
    bookmarkButtons.forEach(button => {
      button.addEventListener("click", function() {
        console.log("Bookmark button clicked");
        // Add functionality for bookmark button click
      });
    });
  
    // Example navigation click event
    const navLinks = document.querySelectorAll("nav div:not(.svg-container)");
    navLinks.forEach(link => {
      link.addEventListener("click", function() {
        console.log(`Navigated to ${link.textContent}`);
        // Add functionality for navigation link click
        // Example: Highlighting active link
        navLinks.forEach(navLink => {
          navLink.classList.remove("active");
        });
        link.classList.add("active");
      });
    });
  });
  