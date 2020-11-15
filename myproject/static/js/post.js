const count = 8;
var index = 0;

function dropdownClick(target, other) {
    if(document.querySelectorAll(other)[0].classList.contains('active')){
      document.querySelectorAll(other)[0].classList.remove('active');
    }
    document.querySelectorAll(target)[0].classList.toggle('active');
  }

function createMenu(menu){
    var menuList = "";
    for(i=0;i<menu.length;i++){
        menuList += `<a href=${menu[i].link}>${menu[i].text}</a>`;
    }
    return menuList;
}

function addPosts(){
    fetch(`/getPosts?start=${index}&end=${index+count}`).then((data) => {
        return data.json();
    }).then((data) => {
        
        data.forEach(post => {
            var postDiv = document.createElement("div");
        postDiv.className ="box2";
        postDiv.innerHTML = `
        <div>
        <a href="${post.profile_link}">
        <img class="piconTortura" src=${post.photo} alt="zappa">
        </a>
        Written By: <a href="${post.profile_link}">${post.author}</a>
            <div class="points3-bar">    
                <nav class="dddnav">
                    <div class="navcontainer">
                        <nav class="navinner">
                            <a class="pprofileddtrigger" onclick="dropdownClick('.postdd${post.id}','.postmobilemenudd')"><img src="static/images/points.svg" /></a>
                            <!-- mobile main menu-->
                            <div class="ppcontainer postmobilemenudd">
                            </div>
                            <div class="ppcontainer postdd${post.id}">
                                <nav class="ddnav">
                                    ${createMenu(post.menu)}
                                </nav>
                            </div>
                        </nav>
                    </div>
                </nav>
            </div>
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