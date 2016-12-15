$(window).on('load', function (e) {

    $(document).click(function (e) {
        // var popup = document.getElementById("downloaded-popup");
        var container = $(".downloader-popup-block");
        if (!container.is(e.target) // if the target of the click isn't the container...
            && container.has(e.target).length === 0) // ... nor a descendant of the container
        {
            var downloader = $("#marc-downloader-button");
            if (!downloader.is(e.target) // if the target of the click isn't the container...
                && downloader.has(e.target).length === 0) // ... nor a descendant of the container
            {
                var popup = document.getElementById("downloaded-popup");
                popup.className = "downloader-popup"
            }
        }
    });


    // This is a listener for escape key
    document.onkeydown = function (evt) {
        evt = evt || window.event;
        var isEscape = false;
        var isTab = false;
        if ("key" in evt) {
            isEscape = evt.key == "Escape";
            isTab = evt.key == "Tab";
        } else {
            isEscape = evt.keyCode == 27;
            isTab = evt.keyCode == 9;
        }
        if (isEscape) {
            var popup = document.getElementById("downloaded-popup");
            popup.className = "downloader-popup"
        }
    };
});