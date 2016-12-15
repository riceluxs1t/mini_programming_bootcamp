$(window).on('load', function (e) {

    var IS_SAFARI = window && /Version\/[\d\.]+.*Safari/.test(window.navigator.userAgent);
     $(document).on('click','.downloader-button',function(e) {
        //  fetch("http://0.0.0.0:1338/templateGenerate?s=" + localStorage.getItem('structured-elm-todo-state'));
        if (!IS_SAFARI) {
            fetch(document.location.origin + "/templateGenerate?s=" + encodeURIComponent(JSON.stringify(localStorage.getItem('structured-elm-todo-state'))))
            .then(function(response) {
                return response.blob();
            }).then(function(blob) {
                download(blob, "download.zip");
                setTimeout(function() {
                    var popup = document.getElementById("downloaded-popup");
                    popup.className = "downloader-popup downloader-popup__active"
                    ga('send', {
                        hitType: 'event',
                        eventCategory: 'Download',
                        eventAction: 'Click',
                        transport: 'beacon'
                    });
                }, 1000);
            });
        } else {
            setTimeout(function() {
                var popup = document.getElementById("downloaded-popup");
                popup.className = "downloader-popup downloader-popup__active";
                ga('send', {
                    hitType: 'event',
                    eventCategory: 'Download',
                    eventAction: 'Click',
                    transport: 'beacon'
                });
            }, 2000);
        }
     });

     if (IS_SAFARI) {
        $(document).on("mouseenter", ".footertemplateforsafari", function(event){
            // console.log("help");
        var help = document.getElementById("marc-downloader-button");
        help.href = document.location.origin + "/templateGenerate?s=" + encodeURIComponent(JSON.stringify(localStorage.getItem('structured-elm-todo-state'))) + "";
        });
    }
});
