

function link_post_detail(){
    document.querySelectorAll('.post_box').forEach(
    post_box => {post_box.addEventListener("click" ,function(){
        const postId = this.dataset.id;
        window.location.href= `/posts/${postId}`;
})
});

}


document.addEventListener('DOMContentLoaded',function(){
    link_post_detail()
})