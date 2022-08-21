function makeAjaxCall(url, methodType, callback){
    $.ajax({
    url : url,
    method : methodType,
    dataType : "json",
    success : callback,
    error : function (reason, xhr){
     console.log("error in processing your request", reason);
    }
    });
    }
// git hub url to get btford details
var URL = "https://api.github.com/users/btford";
makeAjaxCall(URL, "GET", function(respJson){
 document.getElementById("userid").innerHTML = respJson.login;
 document.getElementById("name").innerHTML = respJson.name;
 document.getElementById("company").innerHTML = respJson.company;
 document.getElementById("blog").innerHTML = respJson.blog;
 document.getElementById("location").innerHTML = respJson.location;
});
