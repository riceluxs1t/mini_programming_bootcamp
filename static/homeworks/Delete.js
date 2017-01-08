$( document ).ready(function() {


    $(document).on("click", ".meta-buttons-delete", function(event){
        var deleteR = document.getElementById("delete-modal-id");
        deleteR.className = "delete delete__active"
    //    $(this.childNodes[0].childNodes[0].childNodes[0]).focus();
    });

    $(document).on("click", ".delete-local-storage-button", function(event){
        var deleteR = document.getElementById("delete-modal-id");
        if (deleteR.className == "delete delete__active")
        {
            localStorage.clear();
            deleteR.className = "delete";
            location.reload();

        }
    });

    $(document).on("click", ".keep-local-storage-button", function(event){
        var deleteR = document.getElementById("delete-modal-id");
        if (deleteR.className == "delete delete__active")
        {
            deleteR.className = "delete";
        }
    });
    // $(document).on("click", ".emojihover", function(event){
    //    $(this.childNodes[0].childNodes[0].childNodes[0]).focus();
    // });

    $(document).click(function (e) {
        // var popup = document.getElementById("downloaded-popup");
        var container = $(".delete-confirm");
        if (!container.is(e.target) // if the target of the click isn't the container...
            && container.has(e.target).length === 0) // ... nor a descendant of the container
        {
            var deleteme = $("#delete-button");
            if (!deleteme.is(e.target) // if the target of the click isn't the container...
                && deleteme.has(e.target).length === 0) // ... nor a descendant of the container
            {
                var deleteR = document.getElementById("delete-modal-id");
                deleteR.className = "delete"
            }
        }
    });
});
