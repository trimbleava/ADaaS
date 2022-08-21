function getLocalStorage(selectorID){
    $('#' + selectorID + ' :input').each(function(){
        var key = $(this).attr('id');
        if(localStorage.getItem(key)) {
            var value = localStorage.getItem(key);
            $(this).val(value);

        }
    });

}

function setLocalStorage(selectorID){
    $('#' + selectorID + ' :input').each(function(){
        var id = $(this).attr('id');
        var value = $(this).val();
        localStorage.setItem(id, value);
    });
}


function getMapCache(){
    if(localStorage.getItem("aoi-choice")) {
        var name = localStorage.getItem("aoi-choice");
        var data = localStorage.getItem("aoi-data");
        return([name, data]);
    }
}


function setMapCache(selectedItem, data) {
    localStorage.setItem("aoi-choice", selectedItem);
    localStorage.setItem("aoi-data", data);
}