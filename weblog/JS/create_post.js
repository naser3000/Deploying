function create_post(id,title,summery,user,date) {
    var post = document.createElement('div');
    post.className = 'post';
    post.setAttribute('id',id);
    
    var photo_text = document.createElement('div');
    photo_text.className = 'post_text';
    
    var photo = document.createElement('div');
    photo.className = 'photo';
    
    var text = document.createElement('div');
    text.className = 'text';

    var a = document.createElement('a');
    a.setAttribute('href','weblog.html');
    a.setAttribute('target', '_blank');
    
    var p = document.createElement('p');
    var h3 = document.createElement('h3');
    var h5 = document.createElement('h5');
    var input = document.createElement('input');
    input.className = 'botton1 btn';
    input.setAttribute('value','ادامه مطلب ...');
    input.setAttribute('type','button');
    input.setAttribute('id',id);
    
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
    h5.innerHTML += date;

    //console.log(id);
    var buttons = document.querySelectorAll('.btn');
    for (var j=0; j<buttons.length; j++) {
        var listener = (function (n) {
        
            return function (ev) {
                //console.log(buttons[n]);
                //console.log(n);
                //console.log("++++++++++++++++++++++++++++");
                localStorage.setItem('post_id',buttons[n].getAttribute('id'));
                //console.log(id);
            };
        })(j);
        buttons[j].addEventListener('click', listener);
    }

}