/******************************** add comment by text and id **********************************************/
$(document).ready(function (e) {
    //console.log(document.querySelector('#confirm'));

  $("#confirm").click(function (e) {
        
            //console.log("**************"+weblog_id);


    var weblog_id = $("#weblog_id").val();
    //console.log("**************");
    //console.log(weblog_id);
    var form = new FormData();
    form.append("weblog_id", weblog_id);        
    var settings = {
      "async": true,
      "crossDomain": true,
      //"url": "http://127.0.0.1:8000/blog/posts",
      "url" : "https://illlum2022.herokuapp.com/blog/posts",
      "method": "POST",
      "headers": {
        //"cache-control": "no-cache",
        //"postman-token": "ecfcb298-3911-4da9-e7c6-9859476ca3b0"
      },
      "processData": false,
      "contentType": false,
      "mimeType": "multipart/form-data",
      "data": form
    }
    localStorage.setItem('weblog_id', weblog_id);

    window.open("otherweblog.html","_blank");
    });
});

/********************************************************************************************************/