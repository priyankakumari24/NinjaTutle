var i = 0;
var text = 'Go Turn Your Photo To Cartoon Image In Just A Single Click...';
function typing(){
    if (i < text.length) {
        document.getElementById("animated_heading").innerHTML += text.charAt(i);
        i++;
        setTimeout(typing, 100);
        document.getElementById("animated_heading").style.transform = 'scale(1.25)';
        
    }
};
typing();
