// function for the comment button to hide or show comments
function commentReplyToggle(parent_id) {
    const row = document.getElementById(parent_id);

    if (row.classList.contains('d-none')) {
        row.classList.remove('d-none');
    } else {
        row.classList.add('d-none');
    }
}

var popup1 = document.getElementById("popup-1")
var openPopup1 = document.getElementById("open-popup-1")
var closePopup1 = document.getElementById('close-popup-1')

openPopup1.addEventListener('click', () => {
	popup1.style.display = "block";
})

closePopup1.addEventListener('click', () => {
	popup1.style.display = "none";
})

var popup2 = document.getElementById("popup-2")
var openPopup2 = document.getElementById("open-popup-2")
var closePopup2 = document.getElementById('close-popup-2')

openPopup2.addEventListener('click', () => {
	popup2.style.display = "block";
})

closePopup2.addEventListener('click', () => {
	popup2.style.display = "none";
})