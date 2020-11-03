const count = 8;
var index = 0;

function addPosts(){
    fetch(`/getPosts?start=${index}&end=${index+count}`).then((data) => {
        return data.json();
    }).then((data) => {
        
        data.forEach(post => {
            var postDiv = document.createElement("div");
        postDiv.className ="box2";
        postDiv.innerHTML = `
        <div>
        <img class="piconTortura" src="static/images/Zappa.jpg" alt="zappa">
        Written By: ${post.author}
        </div>
        <div class="pHeader"> ${post.title}</div>
        <hr>
        <p class="pText">${post.text}</p>
        <hr>
        <div class="pReact">
                <a href="#"><div class="react">
                <img src="static/images/like.png" alt="like">
                <p>Like</p></div></a>
                <div class="p-line"></div>
                <a href="#"><div class="react"><img src="static/images/comment.png" alt="comment">
                <p>Comment</p></div></a>
                <div class="p-line"></div>
                <a href="#"><div class="react"><img src="static/images/gift.png" alt="gift">
                <p>Give award</p></div></a>
        </div>
        `;

        document.getElementById("post-container").appendChild(postDiv);

        });
    });    
    index += count;
}

document.onscroll = function(){
    var postCont = document.getElementById("post-container");
    if (document.documentElement.scrollTop >= postCont.scrollHeight-450){
        addPosts();
    }
}