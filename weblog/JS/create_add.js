function create_add() {
    
    var weblog_id = localStorage.getItem('weblog_id');
    var title = 'پست جدیدی بسازید!';
    var summery = 'برای ساخت پست جدید بر روی "اضافه کردن پست جدید" کلیک کنید.';
    var user = 'طراحی وب';
    
    var post = document.createElement('div');
    post.className = 'post';
    
    var photo_text = document.createElement('div');
    photo_text.className = 'post_text';
    
    var photo = document.createElement('div');
    photo.className = 'photo';
    
    var text = document.createElement('div');
    text.className = 'text';

    var a = document.createElement('a');
    a.setAttribute('href','newweblog.html');
    a.setAttribute('target', '_blank');
    
    var p = document.createElement('p');
    var h3 = document.createElement('h3');
    var h5 = document.createElement('h5');
    var input = document.createElement('input');
    input.className = 'botton1';
    input.setAttribute('value','اضافه کردن پست جدید');
    input.setAttribute('type','button');
    input.setAttribute('id','weblog_id');
    
    var image = document.createElement('img');
    var avatar = document.createElement('img');
    var contain = document.querySelector('.contain');

    contain.appendChild(post);
    post.appendChild(photo_text);
    post.appendChild(a);
    photo_text.appendChild(photo);
    photo_text.appendChild(text);
    a.appendChild(input);
    photo.appendChild(h3);
    photo.appendChild(image);
    text.appendChild(avatar);
    text.appendChild(p);
    text.appendChild(h5);
    
    h3.innerHTML = title;
    p.innerHTML = summery;
    h5.innerHTML = user;
    //h5.innerHTML += date;
    var button = input;
    var listener = (function () {
        //console.log("++++++++++++++++++++++++++++");
        localStorage.setItem('post_id',button.getAttribute('id'));
        //console.log(button);
    });
    button.addEventListener('click', listener);
}