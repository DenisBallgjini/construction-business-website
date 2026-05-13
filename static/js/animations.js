const revealElements = document.querySelectorAll(
    ".reveal"
);

function revealOnScroll() {

    const windowHeight = window.innerHeight;

    revealElements.forEach((element) => {

        const elementTop =
        element.getBoundingClientRect().top;

        if (elementTop < windowHeight - 100) {

            element.classList.add("active");
        }
    });
}

window.addEventListener("scroll", revealOnScroll);

revealOnScroll();