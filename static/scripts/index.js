//=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=
//
//          BY BUT0N
//
//=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=
$(function() {
    $(".key-submit").each(function(i,e) {
        $(e).prev().bind('keypress',function(event) {
            if (event.keyCode == '13') {
                $(e).click();
            }
        });
        $(e).click(function() {
            if ($(e).prev().val())
                window.open("/search/"+$(e).prev().val());
        });
    });
});
