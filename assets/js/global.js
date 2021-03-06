document.addEventListener("DOMContentLoaded", function(event) {

  // Mobile menu toggle
  document.querySelector('.toggle').addEventListener('click', function(event){
    document.querySelector('.toggle').classList.toggle('is-active');
    document.querySelector('nav').classList.toggle('expanded');
  });

  // Archive accordions
  var leaves = document.querySelectorAll('.accordion-title');
  for(var i = 0; i < leaves.length; i++){
    leaves[i].addEventListener('click', function(event){
      this.classList.toggle('accordion-title-display');
      this.nextElementSibling.classList.toggle('accordion-leaf-display');
    })
  }
});
