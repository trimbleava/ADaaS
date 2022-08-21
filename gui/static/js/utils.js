// register a global variable
function init_global(win) {
  // Good: if you must have globals,
  // make sure you separate definition from instantiation
  alert("win.foo = 'bar'");
}

function setCSRFToken() {
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
}


function makeAjaxCall(url, methodtype, data, callback){
    console.log("makeAjaxCall is working.................");

    $.ajax({
        url:      url,
        type:     methodtype,
        //dataType: datatype, // modelarea returns {'aoi-choice': ['Lower Kissimmee']} not a json!
        data:     data,      // The data to send (will be converted to a query string)
        success:  callback,  // handle a successful response
        error : function(xhr,errmsg,err) {
            $('#message_id').html('<div class="alert alert-error alert-dismissible" role="alert">' +
                    '<button type="button" class="close" data-dismiss="alert" aria-label="Close">' +
                        '<span aria-hidden="true">&times</span>' +
                    '</button> We have encountered an error: ' + errmsg + '</div>'); // add the error to the dom
            //console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

function showLoader(){
    var img =  '<img src="' + "{% static 'img/extension16.png' %}" + '>'
    $("#loading").fadeIn(500,0);
    $("#loading").html(img);
}


function hideLoader(){
    $("#loading").fadeOut('slow');
}
