$( document ).ready(function() {
    $(document).on("mouseenter", ".emojihover", function(event){
       $(this.childNodes[0].childNodes[0].childNodes[0]).focus();
    });
    $(document).on("click", ".emojihover", function(event){
       $(this.childNodes[0].childNodes[0].childNodes[0]).focus();
    });
});
