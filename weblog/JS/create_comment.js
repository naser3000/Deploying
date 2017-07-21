function create_comment(text,date) {
 
    var each_comment = document.createElement('div');
    each_comment.className = 'each_comment';
    
    var all_comments = document.querySelector('#all_comments');
    
    all_comments.appendChild(each_comment);
    each_comment.innerHTML = text;
    each_comment.innerHTML += '<br><p style="font-size: 12;">'+ date +'</p>';

}