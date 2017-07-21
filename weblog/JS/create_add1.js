
function create_add() {
//var contain = document.querySelector('.contain');
//contain.innerHTML += 'سلامممممم';
var title = 'پست جدیدی بسازید!';
var summery = 'در این قسمت می توانید برای پست خود یک خلاصه قرار دهید!';
var user = 'طراحی وب';
//var date = '1394/04/27';

    var post = document.createElement('div');
    post.className = 'post';
    
    var photo_text = document.createElement('div');
    photo_text.className = 'post_text';
    
    var photo = document.createElement('div');
    photo.className = 'photo';
    
    var text = document.createElement('div');
    text.className = 'text';

    var a = document.createElement('a');
    a.setAttribute('href','weblog.html');
    a.setAttribute('target', '_blank');
    
    var title_input = document.createElement('input');
    title_input.className = 'photo_input';
    title_input.setAttribute('placeholder',title);
    
    var edit = document.createElement('button');
    edit.setAttribute('id','change');
    edit.setAttribute('value','ویرایش');
    
    var summery_input = document.createElement('textarea');
    summery_input.className = 'text_input';
    summery_input.setAttribute('placeholder',summery);
    
    var h5 = document.createElement('h5');
    var input = document.createElement('input');
    input.className = 'botton1';
    input.setAttribute('value','نوشتن متن پست ...');
    input.setAttribute('type','button');
    
    var image = document.createElement('img');
    var avatar = document.createElement('img');
    var contain = document.querySelector('.contain');

    contain.appendChild(post);
    post.appendChild(photo_text);
    post.appendChild(a);
    photo_text.appendChild(photo);
    photo_text.appendChild(text);
    a.appendChild(input);
    photo.appendChild(title_input);
    photo.appendChild(image);
    title_input.appendChild(edit);
    text.appendChild(summery_input);
    summery_input.appendChild(edit);
    text.appendChild(avatar);
    text.appendChild(h5);
    //a.innerHTML = '        <input class="botton1" type="button" value="نوشتن متن پست ...">';

    //h3.innerHTML = title;
    //p.innerHTML = summery;
    h5.innerHTML = user;
    //h5.innerHTML += date;
    
    /*post = document.querySelector('.post');
    post.innerHTML += '<a href="weblog.html" target="_blank"><input class="botton1" type="button" value="نوشتن متن پست ..."></a>';*/
}