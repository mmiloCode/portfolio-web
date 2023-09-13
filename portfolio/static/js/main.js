console.log("works")

let nav = document.getElementById('nav')

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        nav.classList.add('nav--active')
    } else if (window.scrollY <= 50) {
        nav.classList.remove('nav--active')
    }
})

let navBar = document.getElementById('navbar')
let navToggler = document.getElementById('toggler')

navToggler.addEventListener('click', () => {
    navBar.classList.toggle('nav__navbar--active')
})



navLinks = document.querySelectorAll('.nav__link')

navLinks.forEach(link => link.addEventListener("click", () => {
    navBar.classList.remove('nav__navbar--active')
}))


document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});


