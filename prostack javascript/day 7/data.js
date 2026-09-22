function display_ct(){
    alert('Good Afternoon')
    let p_Tag=document.getElementById('abc')
    console.log(p_Tag)
    p_Tag.innerHTML=new Date().toLocaleString()
}