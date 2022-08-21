// <input type="submit" name="submit" id="submit" value="Submit">
// document.getElementById("submit").addEventListener('click', function(event){
    // NOTE: You are clicking a submit button.  After this function runs,
    // then the form will be submitted.  If you want to *stop* that, you can
    // use the following:
    // event.preventDefault();

    // In here `this` will be the element that was clicked, the submit button
//     this.value = document.getElementById('otherelement').value;
// });
// <script type="text/javascript">
//     var a = "{{someDjangoVariable|safe}}";
// </script>

$(document).ready(function () {

    // Initialize tooltip component
    $('[data-toggle="tooltip"]').mouseenter(function(){
        var that = $(this)
        that.tooltip('show');
        setTimeout(function(){
            that.tooltip('hide');
        }, 2000);
    });

    $('[data-toggle="tooltip"]').mouseleave(function(){
        $(this).tooltip('hide');
    });
    // Initialize popover component
    $(function () {
      $('[data-toggle="popover"]').popover()
    });


    // To style all selects
    $('.selectpicker').selectpicker({
        size: 4
    });

    $("#sidebar").mCustomScrollbar({
        theme: "minimal"
    });

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $(this).toggleClass('active');
    });

    // for all post ajax calls
    setCSRFToken();

    // on change event on sidebar selections
    $("#modelchoice").on("change", function(e){
        e.preventDefault();
        var selectedValue = $('#modelchoice').find(":selected").text();   // $('#ddid :selected').text()
        var label = $(this.options[this.selectedIndex]).closest('optgroup').prop('label');
        console.log(selectedValue + " - " + label);

        $.ajax({
            url : '/',
            type : "GET",
            cache: false,
            data : {"modelchoice": selectedValue, 'grplabel': label},
            dataType : "json",
            success : function(data) {
                console.log("data: " + data);
            },
            complete:function(){},
            error:function (xhr, textStatus, thrownError){}
        });
    });

    // cach must be false because user keep changing and when cached
    // the cached value prevents sending the ajax to view where is needed.
    $("#predchoice").on("change", function(e){
        e.preventDefault();
        var selectedValue = $('#predchoice').find(":selected").text();   // $('#ddid :selected').text()
        console.log(selectedValue);
        $.ajax({
            url : "/",
            type : "GET",
            cache: false,
            data : {"predchoice": selectedValue},
            dataType : "json",
            success : function(data) {
                console.log(data);
            },
            complete:function(){},
            error:function (xhr, textStatus, thrownError){}
        });
    });

    $("#eventchoice").on("change", function(e){
        e.preventDefault();
        var selectedValue = $('#eventchoice').find(":selected").text();   // $('#ddid :selected').text()
        var label = $(this.options[this.selectedIndex]).closest('optgroup').prop('label');
        console.log(selectedValue + " - " + label);

        $.ajax({
            url : "/",
            type : "GET",
            cache: false,
            data : {"eventchoice": selectedValue, 'grplabel': label},
            dataType : "json",
            success : function(data) {
                console.log(data);
            },
            complete:function(){},
            error:function (xhr, textStatus, thrownError){}
        });
    });

});
