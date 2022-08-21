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

    // for all post ajax calls
    setCSRFToken();

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

/*    $( function() {
        $( ".dragthis" ).draggable();
    } );*/

    $(function(){  // on page load
        // Create the tree inside the div element.
        $(".tree").fancytree({
            icon: false,
        });
        // Note: Loading and initialization may be asynchronous, so the nodes may not be accessible yet.
    }); // end of onload

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


    // add context menu to these selectors
 /*   $.contextMenu({
        selector: '.context-menu-tools',
        callback: function(key, options) {
            var m = "clicked: " + key;
            window.console && console.log(m) || alert(m);
        },
        items: {
            "create":  {name: "Create", icon: ""},
            "display": {name: "Display", icon: ""},
            "sep1": "---------",
            "quit": {name: "Quit", icon: function(){
                return 'context-menu-icon context-menu-icon-quit';
            }}
        }
    });
    $('.context-menu-tools').on('click', function(e){
        console.log('clicked', this);
        e.preventDefault();
        var selectedValue = $('#modelchoice').find(":selected").text();   // $('#ddid :selected').text()
        var label = $(this.options[this.selectedIndex]).closest('optgroup').prop('label');
        console.log(label);

        $.ajax({
            url : "/",
            type : "GET",
            data : {"modelchoice": selectedValue, 'grplabel': label},
            dataType : "json",
            success : function(data) {
                console.log(data);
            },
            complete:function(){},
            error:function (xhr, textStatus, thrownError){}
        });
    })
*/

    // on change event on sidebar selections
    $("#modelchoice").on("change", function(e){
        e.preventDefault();
        var selectedValue = $('#modelchoice').find(":selected").text();   // $('#ddid :selected').text()
        var label = $(this.options[this.selectedIndex]).closest('optgroup').prop('label');
        console.log(label);

        $.ajax({
            url : "/",
            type : "GET",
            data : {"modelchoice": selectedValue, 'grplabel': label},
            dataType : "json",
            success : function(data) {
                console.log(data);
            },
            complete:function(){},
            error:function (xhr, textStatus, thrownError){}
        });
    });


    $("#predchoice").on("change", function(e){
        e.preventDefault();
        var selectedValue = $('#predchoice').find(":selected").text();   // $('#ddid :selected').text()
        $.ajax({
            url : "/",
            type : "GET",
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
        $.ajax({
            url : "/",
            type : "GET",
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
