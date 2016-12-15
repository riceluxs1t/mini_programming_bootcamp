// This only serves to hide the first click, not saved in local storage.
$( document ).ready(function() {

    function hideHeaderFooter() {
        return function (e) 
        {
            $('.websiteheader').hide();
            $('.websitefooter').hide(); 
        }
    }

    var heroNodes = document.getElementById("herotemplateselector").childNodes;
    var i;
    for (i = 0; i < heroNodes.length; i++)
    {
        heroNodes[i].addEventListener("click", hideHeaderFooter(), false);
    }

});