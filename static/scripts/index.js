//=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=
//
//          BY BUT0N
//
//=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=
var aim = [],
    link = [,,,,,,"http://github.com/but0n", "http://instagram.com/but0n"],
    x = window.innerWidth,
    y = window.innerHeight;
$(function() {
    if(x<y) alert("原谅我目前还没有写移动端的布局。。暂时使用横屏浏览吧");
    init_layout();
    $(window).scroll(function() {img_transition()});
    $(window).resize(function(){
        init_layout();
        img_transition();
    });
    init();


});
function init() {
    $(".imageView").each(function(i,e) {
        $(e).css({"background-image":"url(/static/img/"+i+".jpg)"});
    });

    $(".show").each(function(i,e) {
        $(e).mousemove(function() {
            $(e).children().eq(0).addClass("bluron");
            $(e).children().eq(1).css({"display":"block"});
        });
        $(e).mouseout(function() {
            $(e).children().eq(0).removeClass("bluron");
            $(e).children().eq(1).css({"display":"none"});
        });
    })

    $(".scrollTip").css({"animation":"pulse 1s infinite"});

    $(".show").each(function(i,e) {
        $(e).click(function() {
            if(link[i]) window.open(link[i]);
            else alert("你可以在网上搜索有关 "+$(e).children().eq(1).text()+" 的内容")
        })
    })



}
function init_layout() {
    aim.length = 0;
    x = window.innerWidth;
    y = window.innerHeight;
    $(".imageBar").each(function(i,e) {
        $(e).width(x);
        $(e).height(y);
    });
    $(".imageBar").css({"transform":"translateY(-100%)"});
    $(".imageBar").eq(0).css({"transform":"translateY(0)"});

    $(".imageTitle").height(y);
    $(".imageTitle").css({"line-height":y+"px"});
    $(".imageTitle").each(function(i,e) {
        aim.push($(e).offset().top-y);
    });
}
function img_transition() {
    var len = $(window).scrollTop();

    $(".imageBar").each(function(i,e) {
        var delta = 0.7,
            offset_val = len>=aim[i]?aim[i]+y-len+"px":"-100%",
            inner_offset = len>=aim[i]?-(aim[i]+y-len)*delta+"px":"-100%"
        $(e).css({"transform":"translateY("+offset_val+")"})
        $(e).children().eq(0).css({"transform":"translateY("+inner_offset+")"})
    });

}
