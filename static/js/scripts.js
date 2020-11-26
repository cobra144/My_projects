


window.onscroll = function() {myFunction()};
var header = document.getElementById("nav2");


var sticky = header.offsetTop;

function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("fixed");
  } else {
    header.classList.remove("fixed");
  }
}
