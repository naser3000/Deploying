function create_more(title,text,user,date) {

    var h3 = document.querySelector('h3');
    var p = document.querySelector('p');
    var h5 = document.querySelector('h5');

    
    h3.innerHTML = title;
    p.innerHTML = text;
    h5.innerHTML = user;
    h5.innerHTML += date;

}