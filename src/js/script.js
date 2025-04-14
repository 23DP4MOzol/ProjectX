// Smooth scroll for internal links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    });
});

// Show the login section when clicking the "Login" button
document.getElementById('login-btn').addEventListener('click', function(e) {
    e.preventDefault();
    document.getElementById('login').style.display = 'block';  // Show the login section
    document.getElementById('signup').style.display = 'none'; // Hide the sign-up section
});

// Switch to the sign-up form when clicking "Sign up here" on the login form
document.getElementById('signup-link').addEventListener('click', function(e) {
    e.preventDefault();
    document.getElementById('login').style.display = 'none';  // Hide the login section
    document.getElementById('signup').style.display = 'block'; // Show the sign-up section
});

// Switch back to the login form when clicking "Login here" on the sign-up form
document.getElementById('login-link').addEventListener('click', function(e) {
    e.preventDefault();
    document.getElementById('login').style.display = 'block';  // Show the login section
    document.getElementById('signup').style.display = 'none'; // Hide the sign-up section
});

// Handle Login Form Submission
document.getElementById('login-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    // Simulate login validation
    if (username && password) {
        alert('Login Successful!');
    } else {
        alert('Please fill in both fields!');
    }
});

// Handle Sign-Up Form Submission
document.getElementById('signup-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const newUsername = document.getElementById('new-username').value;
    const newPassword = document.getElementById('new-password').value;
    const email = document.getElementById('email').value;
    
    // Simulate sign-up validation
    if (newUsername && newPassword && email) {
        alert('Sign-Up Successful!');
    } else {
        alert('Please fill in all fields!');
    }
});

