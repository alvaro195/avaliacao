const stars = document.querySelectorAll(".star");
const ratingInput = document.getElementById("rating");

let rating = 0;

stars.forEach((star, index) => {

  star.addEventListener("click", () => {

    rating = index + 1;

    ratingInput.value = rating;

    stars.forEach((s) => {
      s.classList.remove("active");
    });

    for (let i = 0; i <= index; i++) {
      stars[i].classList.add("active");
    }

  });

});