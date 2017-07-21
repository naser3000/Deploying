$(document).ready(function (e) {
    $("#login").click(function (e) {

var student_number = $("#student_number").val();
var password = $("#password").val();

var form = new FormData();
form.append("student_number", student_number);
form.append("password", password);

var settings = {
  "async": true,
  "crossDomain": true,
  "url": "https://illlum2022.herokuapp.com/auth/login",
  //"url": "http://127.0.0.1:8000/auth/login",
  //"url": "https://ce419.herokuapp.com/auth/login",
  "method": "POST",
  "headers": {
    //"cache-control": "no-cache",
    //"postman-token": "f3fc8d69-f58c-7a9c-fc92-cbd4c185ea46"
  },
  "processData": false,
  "contentType": false,
  "mimeType": "multipart/form-data",
  "data": form
}

$.ajax(settings).done(function (response) {
    var json_response = JSON.parse(response);
  //console.log(json_response);

    
    /*$(".send").click(function (e) {
        window.open("file:///C:/Users/Naser/Desktop/web95-92109031-phase2/HTML/weblogs.html","_self");
        //alert('.ثبت نام شما با موفقیت انجام شد');
        //var mess = document.querySelector('.error');
        //mess.innerHTML = '.ثبت نام شما با موفقیت انجام شد';
    });*/
if(json_response.status == 0){
    //alert('!شما با موفقیت وارد شدید');
    localStorage.setItem('x-token',json_response.token);
    //console.log(localStorage.getItem('x-token'));
    window.open("weblogs.html","_self");
} else if(json_response.status == -1) {

    var message = json_response.message;
    var error = document.querySelector('.error');
    
    if(message == "user not found") {
        error.innerHTML = '.نام کاربری اشتباه است';
    } else if(message == "wrong password") {
        error.innerHTML = '.رمز عبور اشتباه است';
    }
}

});
});
});
