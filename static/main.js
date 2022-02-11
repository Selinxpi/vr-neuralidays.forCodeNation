function mouseOverBe(obj) {
    obj.innerHTML = "Always popular, beach holidays. We have every destinations possible to choose from.";
}

function mouseOutBe(obj){
    obj.innerHTML = "BEACH NEURALIDAYS";
}

function mouseOverCi(obj) {
    obj.innerHTML = "City breaks are perfect for anyone looking to relax and get away from it all.";
}

function mouseOutCi(obj){
    obj.innerHTML = "CITY BREAK NEURALIDAYS";
}

function mouseOverSp(obj) {
    obj.innerHTML = "Space Adventures are for the more adventurous person";
}

function mouseOutSp(obj){
    obj.innerHTML = "SPACE NEURALIDAYS";
}

function mouseOverOt(obj) {
    obj.innerHTML = "We offer more than your standard holiday, lets be creative.";
}

function mouseOutOt(obj){
    obj.innerHTML = "OTHER NEURALIDAYS";
}

function mouseOverRe(obj) {
    obj.innerHTML = "Want to relive a time in your life?.";
}

function mouseOutRe(obj){
    obj.innerHTML = "RECALL NEURALIDAYS";
}

function checkCookies(){
    let response = "";
    if (navigator.cookieEnabled === true){
        response = "cookies are enabled";
    } else {
        response = "cookies are not enabled";
    }
    document.getElementById("cookie").innerHTML = response;
}

// jQuery

$(function() {


    $(document).ready(function() {
    $('.form-box1,.form-box2,.form-box3').hide();
    });


    $("#hide-text").click(function() {
        $(".form-box1").show();
    });

    $("#hide-text2").click(function() {
        $(".form-box2").show();
    });

    $("#hide-text3").click(function() {
        $(".form-box3").show();
    });




});
