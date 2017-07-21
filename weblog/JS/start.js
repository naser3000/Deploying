//window.alert(document.getElementsByName('student_number').value);


 function ersal() {
            var name = $('.student_number').val();
            var name = $('.password').val();

            $.ajax({
                type: "Post",
                url: "https://ce419.herokuapp.com/auth/login",
                data: "{'name':'" + name + "'}",
                contentType: "application/json; charset=utf-8",
                success: function (a) {
                    
                    var data = a.d;
                    $('.student_number').val(data);
                },
                error: function() {
                    alert("There is an error");
                }

            });
        }

/*var a = (document.getElementsByTagName("input"))[0];
console.log(a);

var b = new XMLHttpRequest();
//console.log(b);
b.open('POST', 'https://ce419.herokuapp.com/auth/login', true, 'student_number=92109031&password=4310741691');
b.send();
var result = b.responseType;
//treeLabel numberLabel
//objectBox objectBox-string
console.log(result);
console.log('hi');
//result = '' + result ;
result = JSON.parse(result);
console.log(result.status);
console.log(result);
*/
/*function ersal() {
    console.log(a);
    console.log('hihihi');
    var b = new XMLHttpRequest();
    b.open('POST', 'https://ce419.herokuapp.com/auth/login', true, 'student_number=92109031&password=4310741691');
    b.send();
    var result = b.responseText;
    result = JSON.parse(result);
    console.log(result);
    console.log('end');
}*/