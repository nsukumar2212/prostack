function mouseOver() {
    document.getElementById("btn1").style.backgroundColor = "green";
}

function mouseOut() {
    document.getElementById("btn2").style.backgroundColor = "blue";
}

function clickEvent() {
    document.getElementById("btn3").style.backgroundColor = "orange";
}

function dblClickEvent() {
    document.getElementById("btn4").style.backgroundColor = "purple";
}

function focusEvent() {
    document.getElementById("txt1").style.backgroundColor = "yellow";
}

function blurEvent() {
    let input = document.getElementById("txt2");
    input.value = input.value.toUpperCase();
}