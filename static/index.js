$(document).ready(function() {
    const all = $(".configbutton");

    function change_config(config) {
        console.log("cc" + config);
        $.ajax({
            type: "POST",
            url: "/setconfig",
            data: JSON.stringify(config),
            contentType: "application/json; charset=utf-8"
        })
    }

    for(var i = 0; i < all.length; i++){
        let btnid = all[i].id;
        all[i].addEventListener('click', function() {
            change_config(btnid);
        }, false);
    }
});
