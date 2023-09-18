const loginbutton = document.getElementById('signin')
const modal2 = document.getElementById('modal2')
const main = document.getElementById('main');

loginbutton.addEventListener('click',() =>{
    modal2.style.display = 'block';
    main.style.filter="brightness(30%)";
});





function closeModal() {
    var modal = document.getElementById('modal');
    modal.style.display = 'none';
    main.style.filter="brightness(100%)";
}


function closeModal2() {
    var modal = document.getElementById('modal2');
    modal.style.display = 'none';
    main.style.filter="brightness(100%)";
}

// Signup Modal
const signup = document.getElementById('signup')
const modal = document.getElementById('modal')

signup.addEventListener('click',() =>{
    modal.style.display = 'block';
    main.style.filter="brightness(30%)";
});

