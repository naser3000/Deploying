$(document).ready(function (e) {
    $("#register").click(function (e) {

var student_number = $("#student_number").val();
var password = $("#password").val();
var first_name = $("#first_name").val();
var last_name = $("#last_name").val();
var email = $("#email").val();

var form = new FormData();
form.append("student_number", student_number);
form.append("password", password);
form.append("first_name", first_name);
form.append("last_name", last_name);
form.append("email", email);

var settings = {
  "async": true,
  "crossDomain": true,
  "url": "https://illlum2022.herokuapp.com/auth/register",
  //"url": "https://ce419.herokuapp.com/auth/register",
  //"url": "http://127.0.0.1:8000/auth/register",
  "method": "POST",
  "headers": {
    //"cache-control": "no-cache",
    //"postman-token": "36a2dc6a-8b26-8357-6b27-49bbbb72fe83"
  },
  "processData": false,
  "contentType": false,
  "mimeType": "multipart/form-data",
  "data": form
}

$.ajax(settings).done(function (response) {
    var json_response = JSON.parse(response);
  //console.log(json_response);

if(json_response.status == 0){
    window.open("login.html","_self");
} else if(json_response.status == -1) {

    var message = json_response.message;
    var error = document.querySelector('.error');
    
    if(message == "user already exists") {
        error.innerHTML = '.نام کاربری وجود دارد';
    } else if(message == "invalid student number") {
        error.innerHTML = '.نام کاربری نامعتبر است';
    } else if(message == "too short password") {
        error.innerHTML = '.رمز وارد شده کوتاه است';
    } else if(message == "first name needed") {
        error.innerHTML = '.لطفاً نام خود را وارد کنید';
    } else if(message == "last name needed") {
        error.innerHTML = '.لطفاً نام خانوادگی خود را وارد کنید';
    } else if(message == "email needed") {
        error.innerHTML = '.لطفاً ایمیل خود را وارد کنید';
    }
}

    });
});
});
