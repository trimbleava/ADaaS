function initInputLocalStorage(){
    Object.keys(xmlinput_elements_dict).forEach(function(key) {
        if (localStorage.getItem(key) == null) {
            try {
                localStorage.setItem(key, xmlinput_elements_dict[key]);
            } catch(dom_error) {
                localStorage.setItem(key, "");
            }
        }
    });
}


function saveInputLocalStorage() {
    xmlinput_dict = {}
    $('#input-form :input').each(function(){
        var id = $(this).attr('id');
        var value = $(this).val();
        localStorage.setItem(id, value);
        if (id == "id_mesh_geom_file") {
            localStorage.setItem("id_mesh_file_name", value);
            $('#input-form #id_mesh_file_name').val(value);
        } else if (id == "id_shead_file") {
            localStorage.setItem("id_shead_file_name", value);
            $('#input-form #id_shead_file_name').val(value);
        } else if (id == "id_network_geom_file") {
            localStorage.setItem("id_network_file_name", value);
            $('#input-form #id_network_file_name').val(value);
        } else if (id == "id_canal_init_file") {
            localStorage.setItem("id_canal_file_name", value);
            $('#input-form #id_canal_file_name').val(value);
        } else if (id == "id_arcs_file") {
            localStorage.setItem("id_arcs_file_name", value);
            $('#input-form #id_arcs_file_name').val(value);
        }
    });
    localStorage.setItem("xmlinput_data", xmlinput_dict);
}


function loadInputLocalStorage(){
    $('#input-form :input').each(function(){
        try {
            var key = $(this).attr('id');
            if(localStorage.getItem(key)) {
            var value = localStorage.getItem(key);
            $(this).val(value);
        }
        } catch(dom_error) {
            //This occurs for 'files' input
            //alert("Attempted to set file chosen value.\nThis is a major security violation.");
        }
    });
}
