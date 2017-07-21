var token = localStorage.getItem('x-token');

var settings = {
  "async": true,
  "crossDomain": true,
  //"url": "https://ce419.herokuapp.com/blog/posts",
  //"url": "http://127.0.0.1:8000/blog/default/posts",
  "url": "https://illlum2022.herokuapp.com/blog/default/posts",
  "method": "GET",
  "headers": {
    "x-token": token
    //"cache-control": "no-cache",
    //"postman-token": "5f92b5b8-aa9e-1b93-a49c-3cb061049590"
  }
}

$.ajax(settings).done(function (response) {

    var weblog_id = response.weblog_id;
    var json_response = response.posts;
    //console.log(response);

    for (var i in json_response) {

        var id = json_response[i].id;
        var title = json_response[i].title;
        var summery = json_response[i].summary;
        var date = json_response[i].datetime;
        date = changedatetime(date);
        var user = '';
        create_post(id,title,summery,user,date);
    }
    localStorage.setItem('weblog_id', weblog_id);
    create_add(); 
    //show_weblog();
});
/********************************************************************************************************/

