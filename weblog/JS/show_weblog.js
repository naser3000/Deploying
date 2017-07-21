function show_weblog() {

    var title = 'بازدید از سایر وبلاگ ها!';
    var summery = 'برای دیدن وبلاگ سایر کاربران شماره وبلاگ را وارد نمایید.';
    
    var post = document.createElement('div');
    post.className = 'post';
    post.setAttribute('style', 'height : 200px');
    
    var photo_text = document.createElement('div');
    photo_text.className = 'post_textt';
    
    var photo = document.createElement('div');
    photo.className = 'photo';
    
    var text = document.createElement('div');
    text.className = 'text';

    //var a = document.createElement('a');
    //a.setAttribute('href','otherweblog.html');
    //a.setAttribute('target', '_blank');
    
    var p = document.createElement('p');
    var h3 = document.createElement('h3');
    var form = document.createElement('form');
    form.setAttribute('action','#');
    var weblog_id = document.createElement('input');
    weblog_id.setAttribute('id','weblog_id');
    weblog_id.setAttribute('type','text');
    //weblog_id.setAttribute('name','quantity');
    //weblog_id.setAttribute('min','1');
    //weblog_id.setAttribute('max','1000');
    weblog_id.setAttribute('style','background-color: antiquewhite; width: 300px; height: 50px; border: solid; border-radius: 10px;');
    var input = document.createElement('input');
    input.className = 'botton1';
    input.setAttribute('id',"show");
    input.setAttribute('value','مشاهده وبلاگ');
    input.setAttribute('type','button');
    //input.setAttribute('style','margin-top: 20px;');
    var contain = document.querySelector('.contain');

    contain.appendChild(post);
    post.appendChild(photo_text);
    post.appendChild(form);
    //form.appendChild(a);
    photo_text.appendChild(photo);
    photo_text.appendChild(text);
    photo.appendChild(h3);
    text.appendChild(p);
    post.appendChild(weblog_id);
    post.appendChild(input);
    
    h3.innerHTML = title;
    p.innerHTML = summery;
}