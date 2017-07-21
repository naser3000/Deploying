//function add_comment(){

$(document).ready(function (e) {
    $("#confirm").click(function (e) {
        
//console.log(document.querySelector('#confirm'));
        
        var text = $(".comment_text").val();
        var user = localStorage.getItem('user');
        var id = localStorage.getItem('id');

        var token = localStorage.getItem("x-token");
        //console.log("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@");
        //console.log("token");
        //console.log(url);
/************************ confirm comment and get comment datetime ***************************************/
var form = new FormData();
form.append("post_id", id);
form.append("text", text);

var settings = {
  "async": true,
  "crossDomain": true,
  //"url": "https://ce419.herokuapp.com/blog/comment",
  "url": "https://illlum2022.herokuapp.com/blog/comment",
  "method": "POST",
  "headers": {
    "x-token": token
    //"cache-control": "no-cache",
    //"postman-token": "538704d7-af03-aa66-48b0-1737f5ed3001"
  },
  "processData": false,
  "contentType": false,
  "mimeType": "multipart/form-data",
  "data": form
}

$.ajax(settings).done(function (response) {
    var json_response = JSON.parse(response);
  //console.log(json_response);
    if(json_response.status == -1){
        var error = document.querySelector('.text');
        error.innerHTML += '<p style="color: deeppink;">قسمت نظر دهی نباید خالی باشند.</p>';
        
    } else if(json_response.status == 0){
        
        /*var text = json_response.comment.text;
        var date = json_response.comment.datetime;
        date = changedatetime(date);
        
        var comment_div = document.createElement('div');
        comment_div.className = 'comment_div';
        //post.setAttribute('id',id);    
        var comment = document.querySelector('.comment');
        var copy = comment.innerHTML;
        comment.innerHTML = '';
        comment.appendChild(comment_div);
        comment_div.innerHTML = text;
        comment_div.innerHTML += '<br><p style="font-size: 12;">'+date+'</p>';
        comment.innerHTML += copy;*/
        //window.open("file:///C:/Users/Naser/Desktop/web95-92109031-phase2/HTML/weblog.html","_self");
    }

});
    });
});
//}