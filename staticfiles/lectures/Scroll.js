$( document ).ready(function() {
    // Listener for the hero templates
    function scrollToHeroTemplate() {
        return function (e) 
        {
             $('html,body').animate({
                // scrollTop: $("#herogrid").offset().top
            }, 380);
        }
    }
    function showMeta() {
        return function (e) 
        {   
            //  var email = document.getElementById("bigboy");
            //  var meta = document.getElementById("meta");
            //  if ((meta.className.indexOf("active") !== -1))
            //  {
            //     //  meta.className = "meta";
            //  }
            //  else
            //  {
            //       meta.className = "meta meta__active";
            //       localStorage.setItem("meta", true);
            //  }
        }
    }
    var heroNodes = document.getElementById("herotemplateselector").childNodes;
    var i;
    for (i = 0; i < heroNodes.length; i++)
    {
        heroNodes[i].addEventListener("click", showMeta(), false);
    }
    
    if (localStorage.getItem("meta"))
    {
        var meta = document.getElementById("meta");
        meta.className = "meta meta__active";
    }

});