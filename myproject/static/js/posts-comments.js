// Get the modal
var modal2 = document.getElementById("posts-comments");

// Get the button that opens the modal
var btn2 = document.getElementById("myBtncomment");

// Get the <span> element that closes the modal

// When the user clicks the button, open the modal 
btn2.onclick = function() {
  modal2.style.display = "block";
}

// When the user clicks on <span> (x), close the modal


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal2) {
    modal2.style.display = "none";
  }
}