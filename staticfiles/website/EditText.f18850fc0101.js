$(window).on('load', function (e) {
    function insertTextAtCursor(text) {
        var sel, range, html;
        if (window.getSelection) {
            sel = window.getSelection();
            if (sel.getRangeAt && sel.rangeCount) {
            range = sel.getRangeAt(0);
            range.deleteContents();
            range.insertNode(document.createTextNode(text));
            }
        } else if (document.selection && document.selection.createRange) {
            document.selection.createRange().text = text;
        }
    }

    $(document).on('paste','.editable[contenteditable]',function(e) {
        e.preventDefault();
        if ((e.originalEvent || e).clipboardData && (e.originalEvent || e).clipboardData.getData) {
            var text = (e.originalEvent || e).clipboardData.getData("text/plain");
            document.execCommand("insertHTML", false, text);
        } else if (window.clipboardData && window.clipboardData.getData) {
            var text = window.clipboardData.getData("Text");
            insertTextAtCursor(text);
        }
    });
});

