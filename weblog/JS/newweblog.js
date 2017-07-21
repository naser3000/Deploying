$(document).ready(function (e) {
    $(".confirm").click(function (e) {

        var title = $("#title").val();
        var summery = $("#summery").val();
        var text = $("#text").val();
        var weblog_id = localStorage.getItem('weblog_id');
        var token = localStorage.getItem("x-token");
        //console.log(url);
/************************ confirm post and get post id ***********************************************/
        var form = new FormData();
        form.append("title", title);
        form.append("summary", summery);
        form.append("text", text);
        form.append("weblog_id", weblog_id);
        
        var settings = {
          "async": true,
          "crossDomain": true,
          //"url": "http://127.0.0.1:8000/blog/post",
          "url" : "https://illlum2022.herokuapp.com/blog/post",
          "method": "POST",
          "headers": {
            "x-token": token
            //"cache-control": "no-cache",
            //"postman-token": "e841286f-c56f-eb22-cc86-2e27a01de62e"
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
                if (json_response.message == "can't be empty") {
        
                  error.innerHTML += '<p style="color: deeppink;">فیلدها نباید خالی باشند.</p>';
        
                } else if (json_response.message == "u can't") {
        
                  error.innerHTML += '<p style="color: deeppink;">این وبلاگ شما نیست!</p>';
        
                }
                
                
            } else if(json_response.status == 0){
                var post_id = json_response.post_id;
                localStorage.setItem('post_id',post_id);
                window.open("weblogs.html","_self");
            }
        
          });
    });
});