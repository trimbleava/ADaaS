function addContextMenu(selector) {
    var el = "." + selector;
    $.contextMenu({
        selector: el,
        callback: function(key, options) {
            var m = "clicked: " + key;
            window.console && console.log(m) || alert(m);
        },
        items: {
            "add":    {name: "Add", icon: "add"},
            "remove": {name: "Remove", icon: "cut"},
            "sep1": "---------",
            "quit": {name: "Quit", icon: function(){
                return 'context-menu-icon context-menu-icon-quit';
            }}
        }
    });
}
