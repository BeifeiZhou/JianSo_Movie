//=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=
//
//          BY BUT0N
//
//=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=
$(function() {
    $(".label-title").each(function(i,e) {
        $(e).click(function() {
            // $(".item").removeClass("item-active");
            $(".item-active").find(".dash-label").click()
            $(e).parent().parent().addClass("item-active");
            $(e).text($(e).parent().parent().attr("_src"));
        })
    });
    $('.dash-label').each(function(i,e) {
        $(e).click(function() {
            $(e).parent().parent().removeClass("item-active");
            $(e).parent().next().next().find(".label-title").text($(e).text())
        });
    });
    $('.dash-icon').each(function(i,e) {
        $(e).click(function() {
            window.open($(e).parent().parent().attr("_src"))
        });
    });
});
