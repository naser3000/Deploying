var id = localStorage.getItem('post_id');
//var token = localStorage.getItem('x-token');
//console.log(id);
/*********************************** Get text by id ********************************************************/
//var url = "https://ce419.herokuapp.com/blog/post?id="+id;
//var url = "http://127.0.0.1:8000/blog/posts?id="+id;
var url = "https://illlum2022.herokuapp.com/blog/posts?id="+id;
var settings = {
  "async": true,
  "crossDomain": true,
  "url": url,
  "method": "GET",
  "headers": {
    //"x-token": token
    //"cache-control": "no-cache",
    //"postman-token": "c7b85a00-5687-f55a-bec3-9e44a53bed0d"
  }
}
            //console.log(i);

$.ajax(settings).done(function (response) {
    var json_response = response.post;
    var title = json_response[0].title;
    var text = json_response[0].text;
    var date = json_response[0].datetime;
    date = changedatetime(date);
    var user = '';
    
   create_more(title,text,user,date);
});
/********************************** Get comments by id ****************************************************/

var settings = {
  "async": true,
  "crossDomain": true,
  //"url": "https://ce419.herokuapp.com/blog/comments?post_id="+id,
  //"url": "http://127.0.0.1:8000/blog/comments?post_id="+id,
  "url": "https://illlum2022.herokuapp.com/blog/comments?post_id="+id,
  "method": "GET",
  "headers": {
    //"x-token": token
    //"cache-control": "no-cache",
    //"postman-token": "f5cd6b5d-4e00-f510-a8e1-d37d96edebdc"
  }
}

$.ajax(settings).done(function (response) {
  //console.log(id);
    var comments = response.comments;
    //console.log(comments);
    var l = comments.length;
    for(var i in comments){
        var j = l-i-1 ;
        var text = comments[j].text;
        var date = comments[j].datetime;
        date = changedatetime(date);
        //console.log(text);
        //console.log(j);
        create_comment(text,date);
    }
});

//add_comment();